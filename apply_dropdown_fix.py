#!/usr/bin/env python3
"""
Apply dropdown menu fixes to all HTML files that have the Other Products dropdown
"""

import os
import re
from pathlib import Path

def fix_dropdown_in_file(filepath):
    """Apply dropdown fixes to a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file has dropdown menu
        if 'Other Products' not in content or 'dropdown' not in content:
            return False, "No dropdown menu found"

        modified = False

        # Fix CSS if old dropdown styles exist
        if '.dropdown:hover .dropdown-menu' in content and '/* Enhanced Dropdown Menu Styles */' not in content:
            # Replace old dropdown CSS with enhanced version
            old_css_pattern = r'\.dropdown:hover \.dropdown-menu \{[^}]*\}.*?\.dropdown-menu \{[^}]*\}.*?(?:/\*.*?Dropdown.*?\*/.*?)?\.dropdown \{[^}]*\}.*?\.dropdown button \{[^}]*\}.*?\.dropdown-menu \{[^}]*\}'

            enhanced_css = """/* Enhanced Dropdown Menu Styles */
        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropdown-menu {
            display: none;
            position: absolute;
            top: calc(100% + 8px);
            left: 0;
            min-width: 16rem;
            background: white;
            border-radius: 0.5rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            border: 1px solid #e5e7eb;
            z-index: 1000;
            opacity: 0;
            transform: translateY(-10px);
            transition: opacity 0.2s ease, transform 0.2s ease;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
            opacity: 1;
            transform: translateY(0);
        }

        /* Invisible bridge to prevent menu closing when moving cursor */
        .dropdown::before {
            content: '';
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            height: 12px;
            z-index: 999;
        }

        .dropdown button {
            background: transparent;
            border: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            padding: 0;
            font-size: inherit;
            font-family: inherit;
            color: inherit;
        }"""

            # Try to replace in style section
            if re.search(old_css_pattern, content, re.DOTALL):
                content = re.sub(old_css_pattern, enhanced_css, content, flags=re.DOTALL)
                modified = True

        # Add JavaScript if not present
        if '<!-- Enhanced Dropdown Menu JavaScript -->' not in content:
            js_code = """
    <!-- Enhanced Dropdown Menu JavaScript -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const dropdown = document.querySelector('.dropdown');
            const dropdownButton = document.querySelector('.dropdown button');
            const dropdownMenu = document.querySelector('.dropdown-menu');

            if (dropdown && dropdownButton) {
                // Handle click to toggle dropdown
                dropdownButton.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
                    if (dropdownMenu.style.display === 'block') {
                        dropdownMenu.style.opacity = '1';
                        dropdownMenu.style.transform = 'translateY(0)';
                    }
                });

                // Close dropdown when clicking outside
                document.addEventListener('click', function(e) {
                    if (!dropdown.contains(e.target)) {
                        dropdownMenu.style.display = 'none';
                    }
                });

                // Ensure dropdown works on touch devices
                dropdownButton.addEventListener('touchstart', function(e) {
                    e.preventDefault();
                    dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
                });
            }
        });
    </script>"""

            # Add before closing body tag
            if '</body>' in content:
                content = content.replace('</body>', js_code + '\n</body>')
                modified = True

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Dropdown fixed"
        else:
            return False, "Already up to date"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Process all HTML files"""
    base_dir = Path('Speccon-master')
    if not base_dir.exists():
        base_dir = Path('.')

    print("Applying dropdown fixes to all HTML files...")
    print("=" * 60)

    # Find all HTML files
    html_files = []
    for pattern in ['*.html', 'qualifications/*.html', 'short-courses/*.html', 'setas/*.html']:
        html_files.extend(base_dir.glob(pattern))

    fixed_count = 0
    for filepath in html_files:
        success, message = fix_dropdown_in_file(filepath)
        if success:
            print(f"[FIXED] {filepath.name}: {message}")
            fixed_count += 1
        elif "No dropdown menu found" not in message and "Already up to date" not in message:
            print(f"[INFO] {filepath.name}: {message}")

    print("=" * 60)
    print(f"Fixed {fixed_count} files")
    print("\nDropdown menus should now work with both hover and click!")

if __name__ == "__main__":
    main()