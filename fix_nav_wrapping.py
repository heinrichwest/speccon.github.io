#!/usr/bin/env python3
"""
Fix navigation menu wrapping by adjusting spacing and font sizes.
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

def fix_navigation_wrapping(filepath):
    """Fix navigation menu wrapping issues."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Find and replace navigation with tighter spacing
        # Change space-x-8 to space-x-4 for tighter spacing
        content = re.sub(
            r'(<nav class="hidden lg:flex items-center )space-x-8(">)',
            r'\1space-x-4\2',
            content
        )

        # Make nav links slightly smaller and use white-space: nowrap
        # Pattern 1: Standard nav links
        old_link_pattern = r'<a href="([^"]*)" class="text-gray-700 hover:text-\[#12265E\] font-medium transition duration-300">'
        new_link_pattern = r'<a href="\1" class="text-gray-700 hover:text-[#12265E] font-medium transition duration-300 text-sm whitespace-nowrap">'
        content = re.sub(old_link_pattern, new_link_pattern, content)

        # Pattern 2: Blue hover links
        old_link_pattern2 = r'<a href="([^"]*)" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">'
        new_link_pattern2 = r'<a href="\1" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300 text-sm whitespace-nowrap">'
        content = re.sub(old_link_pattern2, new_link_pattern2, content)

        # Pattern 3: Cyan hover links
        old_link_pattern3 = r'<a href="([^"]*)" class="text-gray-700 hover:text-cyan-600 font-medium transition duration-300">'
        new_link_pattern3 = r'<a href="\1" class="text-gray-700 hover:text-cyan-600 font-medium transition duration-300 text-sm whitespace-nowrap">'
        content = re.sub(old_link_pattern3, new_link_pattern3, content)

        # Update dropdown button to be smaller
        old_dropdown_button = r'<button class="text-gray-700 hover:text-\[#12265E\] font-medium transition duration-300 flex items-center">'
        new_dropdown_button = r'<button class="text-gray-700 hover:text-[#12265E] font-medium transition duration-300 flex items-center text-sm whitespace-nowrap">'
        content = re.sub(old_dropdown_button, new_dropdown_button, content)

        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[+] Fixed: {os.path.basename(filepath)}")
            return True
        else:
            print(f"[=] No changes: {os.path.basename(filepath)}")
            return False

    except Exception as e:
        print(f"[!] Error in {os.path.basename(filepath)}: {str(e)}")
        return False

def main():
    print("Fixing navigation menu wrapping...")
    print("=" * 60)

    fixed_count = 0
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            if fix_navigation_wrapping(filepath):
                fixed_count += 1
        else:
            print(f"[!] File not found: {filename}")

    print("=" * 60)
    print(f"Complete! Fixed {fixed_count} out of {len(files)} files.")

if __name__ == "__main__":
    main()
