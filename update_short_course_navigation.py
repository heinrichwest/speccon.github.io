#!/usr/bin/env python3
"""
Update navigation in all short course HTML files:
- Add "Other Products" dropdown menu
- Remove "Contact Us" link from navigation
"""

import os
import re

# List of all short course files
files = [
    "advanced-ai-training.html",
    "ai-training.html",
    "b-bbee-training.html",
    "compliance-courses.html",
    "computer-courses.html",
    "cyber-security-training.html",
    "disciplinary-procedures-training.html",
    "employment-equity-training.html",
    "excel-training.html",
    "finance-for-non-financial-managers.html",
    "fire-fighter-training.html",
    "first-aid-training.html",
    "forklift-operations.html",
    "intro-to-ai-training.html",
    "ohs-training.html",
    "personal-finance-management.html",
    "popi-act-training.html",
    "power-bi-training.html",
    "professional-development.html",
    "sales-training.html",
    "stress-management-training.html",
    "time-management-training.html",
]

base_dir = "short-courses"

# Navigation template with Other Products dropdown
other_products_dropdown = '''                    <div class="relative dropdown">
                        <button class="text-gray-700 hover:text-[#12265E] font-medium transition duration-300 flex items-center">
                            Other Products <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i>
                        </button>
                        <div class="dropdown-menu absolute -left-16 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-20">
                            <a href="professional-development.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Professional Development</a>
                            <a href="intro-to-ai-training.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">AI Training Courses</a>
                            <a href="cyber-security-training.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Cyber Security Training</a>
                            <a href="compliance-courses.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Compliance Training</a>
                        </div>
                    </div>'''

# Add dropdown CSS if not present
dropdown_css = '''        .dropdown:hover .dropdown-menu {
            display: block;
        }
        .dropdown-menu {
            display: none;
        }'''

def update_navigation(filepath):
    """Update navigation in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Check if Other Products dropdown already exists
        if 'Other Products' in content:
            print(f"[=] Already has Other Products: {os.path.basename(filepath)}")
            return False

        # Remove Contact Us link from navigation
        # Pattern matches various forms of Contact Us link in nav
        content = re.sub(
            r'\s*<a href="[^"]*#contact"[^>]*>Contact Us</a>\s*',
            '\n',
            content,
            flags=re.IGNORECASE
        )

        # Find the nav section and add Other Products dropdown before closing </nav>
        # Look for the pattern: Classroom Training link followed by closing nav or other content
        nav_pattern = r'(<a href="[^"]*#classroom-training"[^>]*>Classroom Training</a>)\s*(</nav>)'

        if re.search(nav_pattern, content):
            replacement = r'\1\n' + other_products_dropdown + r'\n                \2'
            content = re.sub(nav_pattern, replacement, content)
        else:
            # Alternative pattern: find last nav link before </nav>
            nav_pattern2 = r'(<a href="[^"]*"[^>]*>[^<]+</a>)\s*(</nav>)'
            if re.search(nav_pattern2, content):
                replacement = r'\1\n' + other_products_dropdown + r'\n                \2'
                content = re.sub(nav_pattern2, replacement, content)

        # Add dropdown CSS if not present
        if 'dropdown-menu' not in content and 'Other Products' in content:
            # Find the style section and add dropdown CSS before closing </style>
            style_pattern = r'(\.card-hover:hover \{[^}]+\})\s*(</style>)'
            if re.search(style_pattern, content):
                replacement = r'\1\n' + dropdown_css + r'\n    \2'
                content = re.sub(style_pattern, replacement, content)

        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[+] Updated: {os.path.basename(filepath)}")
            return True
        else:
            print(f"[=] No changes needed: {os.path.basename(filepath)}")
            return False

    except Exception as e:
        print(f"[!] Error in {os.path.basename(filepath)}: {str(e)}")
        return False

def main():
    print("Updating navigation in short course files...")
    print("=" * 60)

    updated_count = 0
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            if update_navigation(filepath):
                updated_count += 1
        else:
            print(f"[!] File not found: {filename}")

    print("=" * 60)
    print(f"Complete! Updated {updated_count} out of {len(files)} files.")

if __name__ == "__main__":
    main()
