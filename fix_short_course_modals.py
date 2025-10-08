#!/usr/bin/env python3
"""
Fix modal close functionality in all short course HTML files.
Removes 'flex' class from modal div and updates open/close functions.
"""

import os
import re

# List of all short course files
files = [
    "b-bbee-training.html",
    "personal-finance-management.html",
    "ohs-training.html",
    "fire-fighter-training.html",
    "cyber-security-training.html",
    "ai-training.html",
    "excel-training.html",
    "time-management-training.html",
    "stress-management-training.html",
    "sales-training.html",
    "professional-development.html",
    "power-bi-training.html",
    "popi-act-training.html",
    "intro-to-ai-training.html",
    "forklift-operations.html",
    "first-aid-training.html",
    "finance-for-non-financial-managers.html",
    "employment-equity-training.html",
    "disciplinary-procedures-training.html",
    "computer-courses.html",
    "compliance-courses.html",
]

base_dir = "short-courses"

def fix_modal_in_file(filepath):
    """Fix modal close functionality in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Fix 1: Remove 'flex' from modal div, keeping other classes
        content = re.sub(
            r'(<div id="bookNowModal" class="[^"]*)\s+flex\s+([^"]*">)',
            r'\1 \2',
            content
        )

        # Fix 2: Update openBookNowModal function to add 'flex' class
        old_open_function = r'''function openBookNowModal\(\) \{
            const modal = document\.getElementById\('bookNowModal'\);
            if \(modal\) \{
                modal\.classList\.remove\('hidden'\);
                document\.body\.style\.overflow = 'hidden';
            \}
        \}'''

        new_open_function = '''function openBookNowModal() {
            const modal = document.getElementById('bookNowModal');
            if (modal) {
                modal.classList.remove('hidden');
                modal.classList.add('flex');
                document.body.style.overflow = 'hidden';
            }
        }'''

        content = re.sub(old_open_function, new_open_function, content, flags=re.MULTILINE)

        # Fix 3: Update closeBookNowModal function to remove 'flex' class
        old_close_function = r'''function closeBookNowModal\(\) \{
            const modal = document\.getElementById\('bookNowModal'\);
            if \(modal\) \{
                modal\.classList\.add\('hidden'\);
                document\.body\.style\.overflow = 'auto';
            \}
        \}'''

        new_close_function = '''function closeBookNowModal() {
            const modal = document.getElementById('bookNowModal');
            if (modal) {
                modal.classList.add('hidden');
                modal.classList.remove('flex');
                document.body.style.overflow = 'auto';
            }
        }'''

        content = re.sub(old_close_function, new_close_function, content, flags=re.MULTILINE)

        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[+] Fixed: {os.path.basename(filepath)}")
            return True
        else:
            print(f"[=] No changes needed: {os.path.basename(filepath)}")
            return False

    except Exception as e:
        print(f"[!] Error in {os.path.basename(filepath)}: {str(e)}")
        return False

def main():
    print("Fixing modal close functionality in short course files...")
    print("=" * 60)

    fixed_count = 0
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            if fix_modal_in_file(filepath):
                fixed_count += 1
        else:
            print(f"[!] File not found: {filename}")

    print("=" * 60)
    print(f"Complete! Fixed {fixed_count} out of {len(files)} files.")

if __name__ == "__main__":
    main()
