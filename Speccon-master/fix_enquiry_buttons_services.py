#!/usr/bin/env python3
"""
Fix all enquiry buttons to use onclick instead of href in Services SETA pages
"""

import os
import re
import glob

def fix_enquiry_buttons(content):
    """Fix enquiry buttons to use onclick instead of href"""

    # Fix desktop enquiry button
    pattern1 = r'<a href="[^"]*"([^>]*)class="([^"]*bg-gradient[^"]*)"[^>]*>\s*Enquire Now\s*</a>'
    replacement1 = r'<button onclick="openEnquiryModal()" class="\2">Enquire Now</button>'
    content = re.sub(pattern1, replacement1, content, flags=re.IGNORECASE)

    # Fix mobile menu enquiry button - first remove contact us link if it exists
    pattern2 = r'<a href="[^"]*#contact"[^>]*>Contact Us</a>\s*'
    content = re.sub(pattern2, '', content)

    # Then fix the mobile enquiry button
    pattern3 = r'<a href="[^"]*"([^>]*)class="([^"]*mt-2 w-full bg-gradient[^"]*)"[^>]*>\s*Enquire Now\s*</a>'
    replacement3 = r'<button onclick="openEnquiryModal()" class="\2">Enquire Now</button>'
    content = re.sub(pattern3, replacement3, content, flags=re.IGNORECASE)

    # Alternative pattern for desktop button if it's structured differently
    pattern4 = r'<div class="hidden lg:block">\s*<a href="[^"]*"[^>]*>\s*Enquire Now\s*</a>\s*</div>'
    replacement4 = '''<div class="hidden lg:block">
                    <button onclick="openEnquiryModal()" class="bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg">
                        Enquire Now
                    </button>
                </div>'''
    content = re.sub(pattern4, replacement4, content, flags=re.DOTALL | re.IGNORECASE)

    return content

def process_file(filepath):
    """Process a single Services SETA file"""

    filename = os.path.basename(filepath)
    print(f"Processing {filename}...")

    try:
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply fixes
        original_content = content
        content = fix_enquiry_buttons(content)

        # Write the updated content back if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [UPDATED] {filename}")
        else:
            print(f"  [NO CHANGES] {filename}")

        return True

    except Exception as e:
        print(f"  [ERROR] {filename}: {str(e)}")
        return False

def main():
    """Main function to fix enquiry buttons in all Services SETA pages"""

    # Get all Services SETA qualification files
    services_files = glob.glob('qualifications/services-*.html')

    if not services_files:
        print("No Services SETA qualification files found!")
        return

    print(f"Found {len(services_files)} Services SETA qualification files")
    print("-" * 50)

    success_count = 0
    for filepath in services_files:
        if process_file(filepath):
            success_count += 1

    print("-" * 50)
    print(f"Successfully updated {success_count}/{len(services_files)} files")

if __name__ == "__main__":
    main()