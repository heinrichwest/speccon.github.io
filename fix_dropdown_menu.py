#!/usr/bin/env python3
"""
Fix the Other Products dropdown menu functionality across all pages
"""

import os
import re
from pathlib import Path

def fix_dropdown_styles(content):
    """Fix dropdown CSS styles to ensure proper hover functionality"""

    # Find the style section
    style_pattern = r'(<style>.*?</style>)'
    style_match = re.search(style_pattern, content, re.DOTALL)

    if not style_match:
        return content

    style_content = style_match.group(1)

    # Remove any existing dropdown styles to avoid conflicts
    style_content = re.sub(r'/\*.*?Dropdown.*?\*/.*?\.dropdown-menu\s*\{[^}]*\}', '', style_content, flags=re.DOTALL)
    style_content = re.sub(r'\.dropdown:hover\s+\.dropdown-menu\s*\{[^}]*\}', '', style_content, flags=re.DOTALL)
    style_content = re.sub(r'\.dropdown-menu\s*\{[^}]*\}', '', style_content, flags=re.DOTALL)
    style_content = re.sub(r'\.dropdown\s*\{[^}]*\}', '', style_content, flags=re.DOTALL)
    style_content = re.sub(r'\.dropdown\s+button\s*\{[^}]*\}', '', style_content, flags=re.DOTALL)

    # Add comprehensive dropdown styles before the closing </style> tag
    dropdown_styles = """
        /* Enhanced Dropdown Menu Styles */
        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            margin-top: 0.5rem;
            min-width: 16rem;
            background: white;
            border-radius: 0.5rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            border: 1px solid #e5e7eb;
            z-index: 1000;
            opacity: 0;
            transform: translateY(-10px);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }

        .dropdown:hover .dropdown-menu,
        .dropdown:focus-within .dropdown-menu,
        .dropdown.active .dropdown-menu {
            display: block;
            opacity: 1;
            transform: translateY(0);
        }

        .dropdown button {
            background: transparent;
            border: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            padding: 0.5rem 0;
            font-size: inherit;
            font-family: inherit;
            color: inherit;
        }

        .dropdown button:focus {
            outline: none;
        }

        /* Add invisible bridge to prevent menu from closing when moving mouse */
        .dropdown::before {
            content: '';
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            height: 0.5rem;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.75rem 1rem;
            text-decoration: none;
            transition: all 0.2s ease;
        }

        .dropdown-menu a:hover {
            background-color: rgba(18, 38, 94, 0.05);
        }
    </style>"""

    # Insert the new styles before the closing </style> tag
    style_content = style_content.replace('</style>', dropdown_styles)

    # Replace the old style section with the updated one
    content = content.replace(style_match.group(1), style_content)

    return content

def add_dropdown_javascript(content):
    """Add JavaScript to handle dropdown click events"""

    # Check if the JavaScript already exists
    if 'dropdownClickHandler' in content:
        return content

    # JavaScript to handle dropdown functionality
    dropdown_js = """
    <!-- Dropdown Menu JavaScript -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Handle dropdown click toggle
            const dropdownButtons = document.querySelectorAll('.dropdown button');

            dropdownButtons.forEach(button => {
                button.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();

                    const dropdown = this.closest('.dropdown');
                    const isActive = dropdown.classList.contains('active');

                    // Close all other dropdowns
                    document.querySelectorAll('.dropdown.active').forEach(d => {
                        d.classList.remove('active');
                    });

                    // Toggle current dropdown
                    if (!isActive) {
                        dropdown.classList.add('active');
                    }
                });
            });

            // Close dropdown when clicking outside
            document.addEventListener('click', function(e) {
                if (!e.target.closest('.dropdown')) {
                    document.querySelectorAll('.dropdown.active').forEach(d => {
                        d.classList.remove('active');
                    });
                }
            });

            // Ensure dropdown stays open when hovering
            const dropdowns = document.querySelectorAll('.dropdown');
            dropdowns.forEach(dropdown => {
                let hoverTimeout;

                dropdown.addEventListener('mouseenter', function() {
                    clearTimeout(hoverTimeout);
                });

                dropdown.addEventListener('mouseleave', function() {
                    const self = this;
                    hoverTimeout = setTimeout(function() {
                        self.classList.remove('active');
                    }, 300);
                });
            });
        });
    </script>
"""

    # Add the JavaScript before the closing </body> tag
    content = content.replace('</body>', dropdown_js + '\n</body>')

    return content

def fix_dropdown_html(content):
    """Ensure the dropdown HTML structure is correct"""

    # Fix the dropdown button to ensure proper structure
    dropdown_pattern = r'(<div class="[^"]*dropdown[^"]*">.*?</div>)'

    # Make sure the dropdown button doesn't have conflicting attributes
    content = re.sub(
        r'<button class="([^"]*)".*?>\s*Other Products\s*<i data-lucide="chevron-down"[^>]*></i>\s*</button>',
        r'<button class="\1" aria-haspopup="true" aria-expanded="false">Other Products <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i></button>',
        content
    )

    return content

def process_file(filepath):
    """Process a single HTML file to fix dropdown functionality"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if the file has a dropdown menu
        if 'Other Products' not in content or 'dropdown' not in content:
            return False, "No dropdown menu found"

        # Apply fixes
        original_content = content
        content = fix_dropdown_styles(content)
        content = fix_dropdown_html(content)
        content = add_dropdown_javascript(content)

        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Dropdown menu fixed"
        else:
            return False, "No changes needed"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main function to fix dropdown menus across all HTML files"""

    # Define paths to search
    paths_to_check = [
        Path('Speccon-master'),
        Path('Speccon-master/qualifications'),
        Path('Speccon-master/short-courses'),
        Path('Speccon-master/setas')
    ]

    print("Fixing dropdown menu functionality...")
    print("=" * 60)

    files_processed = 0
    files_fixed = 0

    for base_path in paths_to_check:
        if not base_path.exists():
            # Try without Speccon-master prefix
            base_path = Path(str(base_path).replace('Speccon-master/', ''))
            if not base_path.exists():
                continue

        # Find all HTML files
        html_files = list(base_path.glob('*.html'))

        for filepath in html_files:
            success, message = process_file(filepath)
            files_processed += 1

            if success:
                files_fixed += 1
                print(f"✓ {filepath.name}: {message}")
            elif "No dropdown menu found" not in message:
                print(f"→ {filepath.name}: {message}")

    print("=" * 60)
    print(f"Processed {files_processed} files, fixed {files_fixed} files")
    print("\nDropdown menus should now work with both hover and click!")

if __name__ == "__main__":
    main()