#!/usr/bin/env python3
"""
Final comprehensive update for all short course pages:
1. Ensure Other Products dropdown works on hover
2. Remove Contact Us from navigation
3. Update Get Training Information buttons to trigger contact modal
4. Fix any close button issues
"""

import os
import re

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

def update_file(filepath):
    """Comprehensive update for a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = []

        # 1. Remove onclick from Other Products dropdown button (should only work on hover)
        if re.search(r'<button onclick="[^"]*" class="[^"]*dropdown', content):
            content = re.sub(
                r'<button onclick="[^"]*"( class="[^"]*dropdown)',
                r'<button\1',
                content
            )
            changes_made.append("Removed onclick from dropdown button")

        # 2. Remove Contact Us links from navigation
        if re.search(r'<a href="[^"]*#contact"[^>]*>Contact Us</a>', content):
            content = re.sub(
                r'\s*<a href="[^"]*#contact"[^>]*>Contact Us</a>\s*',
                '\n',
                content
            )
            changes_made.append("Removed Contact Us from nav")

        # 3. Fix "Get Training Information" to use contact modal
        # Pattern 1: Links with href
        if 'Get Training Information' in content:
            old_pattern1 = r'<a href="[^"]*#contact"([^>]*)>\s*(<i[^>]*></i>\s*)?Get Training Information\s*(</a>)'
            new_pattern1 = r'<button data-modal="contact"\1>\2Get Training Information</button>'
            if re.search(old_pattern1, content, re.DOTALL):
                content = re.sub(old_pattern1, new_pattern1, content, flags=re.DOTALL)
                changes_made.append("Fixed Get Training Information button")

        # 4. Fix "Get More Information" to use booking modal
        if 'Get More Information' in content:
            # Find course name from title or use generic
            course_match = re.search(r'<title>([^|]+)', content)
            course_name = course_match.group(1).strip() if course_match else "Training"

            old_pattern2 = r'<button onclick="openEnquiryModal\(\)"([^>]*)>Get More Information</button>'
            new_pattern2 = f'<button onclick="openBookNowModal()" data-modal="book" data-course="{course_name}"\1>Get More Information</button>'
            if re.search(old_pattern2, content):
                content = re.sub(old_pattern2, new_pattern2, content)
                changes_made.append("Fixed Get More Information button")

        # 5. Fix duplicate onclick on close buttons
        if re.search(r'onclick="openBookNowModal\(\)" onclick="closeBookNowModal\(\)"', content):
            content = re.sub(
                r'onclick="openBookNowModal\(\)" onclick="closeBookNowModal\(\)"',
                r'onclick="closeBookNowModal()"',
                content
            )
            changes_made.append("Fixed duplicate onclick on close button")

        # 6. Ensure dropdown CSS is present
        if 'dropdown-menu' in content and 'dropdown:hover .dropdown-menu' not in content:
            # Find style section and add dropdown CSS
            style_pattern = r'(\.card-hover:hover \{[^}]+\})\s*(</style>)'
            dropdown_css = '''        .dropdown:hover .dropdown-menu {
            display: block;
        }
        .dropdown-menu {
            display: none;
        }'''
            if re.search(style_pattern, content):
                content = re.sub(style_pattern, r'\1\n' + dropdown_css + r'\n    \2', content)
                changes_made.append("Added dropdown hover CSS")

        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[+] Updated {os.path.basename(filepath)}: {', '.join(changes_made)}")
            return True
        else:
            print(f"[=] No changes: {os.path.basename(filepath)}")
            return False

    except Exception as e:
        print(f"[!] Error in {os.path.basename(filepath)}: {str(e)}")
        return False

def main():
    print("Final comprehensive update for short course pages...")
    print("=" * 70)

    updated_count = 0
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            if update_file(filepath):
                updated_count += 1
        else:
            print(f"[!] File not found: {filename}")

    print("=" * 70)
    print(f"Complete! Updated {updated_count} out of {len(files)} files.")

if __name__ == "__main__":
    main()
