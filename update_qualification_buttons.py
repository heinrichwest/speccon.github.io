#!/usr/bin/env python3
"""
Update all qualification pages to have Apply and Get More Info buttons trigger enquiry modal
"""

import os
import re
from pathlib import Path

def update_qualification_buttons(file_path):
    """Update Apply and Get More Info buttons in qualification pages to trigger enquiry modal"""

    print(f"Processing: {file_path.name}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Pattern 1: Replace "Apply for this Qualification" links with buttons that trigger modal
    pattern1 = r'<a\s+href="[^"]*learnership-application\.html"[^>]*>\s*Apply for this Qualification\s*</a>'
    if re.search(pattern1, content):
        def replace_apply_qualification(match):
            anchor_tag = match.group(0)
            # Extract classes if they exist
            class_match = re.search(r'class="([^"]*)"', anchor_tag)
            if class_match:
                classes = class_match.group(1)
            else:
                classes = "bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-8 py-4 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 text-center"

            return f'<button onclick="openEnquiryModal()" class="{classes}">Apply for this Qualification</button>'

        content = re.sub(pattern1, replace_apply_qualification, content)
        changes_made = True
        print(f"  [OK] Updated 'Apply for this Qualification' to trigger modal")

    # Pattern 2: Replace "Apply Now" links with buttons that trigger modal
    pattern2 = r'<a\s+href="[^"]*learnership-application\.html"[^>]*>\s*Apply Now\s*</a>'
    if re.search(pattern2, content):
        def replace_apply_now(match):
            anchor_tag = match.group(0)
            # Extract classes if they exist
            class_match = re.search(r'class="([^"]*)"', anchor_tag)
            if class_match:
                classes = class_match.group(1)
            else:
                classes = "bg-white text-[#12265E] font-semibold px-8 py-4 rounded-lg hover:bg-gray-100 transition duration-300"

            return f'<button onclick="openEnquiryModal()" class="{classes}">Apply Now</button>'

        content = re.sub(pattern2, replace_apply_now, content)
        changes_made = True
        print(f"  [OK] Updated 'Apply Now' to trigger modal")

    # Pattern 3: Replace any "Get More Information" links that go to contact section
    pattern3 = r'<a\s+href="[^"]*#contact"[^>]*>\s*Get More Information\s*</a>'
    if re.search(pattern3, content):
        def replace_get_more_info(match):
            anchor_tag = match.group(0)
            # Extract classes if they exist
            class_match = re.search(r'class="([^"]*)"', anchor_tag)
            if class_match:
                classes = class_match.group(1)
            else:
                classes = "border-2 border-white text-white font-semibold px-8 py-4 rounded-lg hover:bg-white hover:text-[#12265E] transition duration-300"

            return f'<button onclick="openEnquiryModal()" class="{classes}">Get More Information</button>'

        content = re.sub(pattern3, replace_get_more_info, content)
        changes_made = True
        print(f"  [OK] Updated 'Get More Information' to trigger modal")

    # Pattern 4: Check if "Enquire Now" buttons in CTA section link to apply page instead of modal
    pattern4 = r'<a\s+href="[^"]*#apply"[^>]*>\s*Enquire Now\s*</a>'
    if re.search(pattern4, content):
        def replace_enquire_now(match):
            anchor_tag = match.group(0)
            # Extract classes if they exist
            class_match = re.search(r'class="([^"]*)"', anchor_tag)
            if class_match:
                classes = class_match.group(1)
            else:
                classes = "bg-white text-[#12265E] px-8 py-4 rounded-lg font-semibold hover:bg-gray-100 transition duration-300"

            return f'<button onclick="openEnquiryModal()" class="{classes}">Enquire Now</button>'

        content = re.sub(pattern4, replace_enquire_now, content)
        changes_made = True
        print(f"  [OK] Updated 'Enquire Now' to trigger modal")

    # Verify that openEnquiryModal function exists
    if changes_made and 'function openEnquiryModal' not in content:
        print(f"  [WARNING] Missing openEnquiryModal function - may need to add modal code")

    # Verify that enquiry modal HTML exists
    if changes_made and 'enquiry-modal' not in content:
        print(f"  [WARNING] Missing enquiry modal HTML - may need to add modal structure")

    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [DONE] File updated successfully!")
        return True
    else:
        # Check if buttons are already configured correctly
        if 'openEnquiryModal' in content and ('Apply for this Qualification' in content or 'Apply Now' in content):
            print(f"  [INFO] Already configured correctly")
        else:
            print(f"  [INFO] No changes needed")
        return False

def main():
    base_dir = Path(r'C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master\qualifications')

    # Get all HTML files in qualifications directory
    qualification_files = list(base_dir.glob('*.html'))

    # Exclude template file if it exists
    qualification_files = [f for f in qualification_files if 'template' not in f.name.lower()]

    total_files = len(qualification_files)
    total_updated = 0
    files_need_modal = []

    print("=" * 60)
    print("Updating qualification pages - Apply & Get More Info buttons")
    print(f"Found {total_files} qualification HTML files")
    print("=" * 60)

    for file_path in sorted(qualification_files):
        if update_qualification_buttons(file_path):
            total_updated += 1

            # Check if file needs modal code
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'function openEnquiryModal' not in content or 'enquiry-modal' not in content:
                files_need_modal.append(file_path.name)

    print("\n" + "=" * 60)
    print(f"Update complete!")
    print(f"Files updated: {total_updated} / {total_files}")

    if files_need_modal:
        print(f"\n[WARNING] The following files may need modal code added:")
        for filename in files_need_modal:
            print(f"  - {filename}")
        print("\nRun add_modal_to_qualifications.py to add missing modal code")

    print("=" * 60)

if __name__ == '__main__':
    main()