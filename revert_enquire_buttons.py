#!/usr/bin/env python3
"""
Revert "Enquire Now" buttons in header back to openEnquiryModal()
Keep "Get More Info" buttons as openContactModal()
"""

import os
import re
import glob

def revert_enquire_buttons(file_path):
    """Revert Enquire Now buttons in header to openEnquiryModal()."""
    print(f"Processing: {os.path.basename(file_path)}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = []

        # Find the header section (from <header> to </header>)
        header_pattern = r'(<header[^>]*>.*?</header>)'
        header_match = re.search(header_pattern, content, re.DOTALL)

        if header_match:
            header_content = header_match.group(1)

            # In the header section, change openContactModal back to openEnquiryModal
            # for buttons with "Enquire Now" text
            updated_header = header_content.replace('onclick="openContactModal()"', 'onclick="openEnquiryModal()"')

            if updated_header != header_content:
                content = content.replace(header_content, updated_header)
                changes_made.append("Reverted Enquire Now buttons in header to openEnquiryModal()")

        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [+] Reverted: {', '.join(changes_made)}")
            return True
        else:
            print(f"  [-] No changes needed")
            return False

    except Exception as e:
        print(f"  [!] Error: {e}")
        return False

def main():
    """Main function to revert all qualification pages."""
    # Get all HTML files in qualifications directory
    qualifications_dir = os.path.join(os.path.dirname(__file__), 'qualifications')
    html_files = glob.glob(os.path.join(qualifications_dir, '*.html'))

    print(f"Found {len(html_files)} qualification pages to check\n")
    print("=" * 70)

    updated_count = 0

    for file_path in sorted(html_files):
        # Skip template files
        if 'template' in os.path.basename(file_path).lower():
            print(f"Skipping template: {os.path.basename(file_path)}")
            continue

        if revert_enquire_buttons(file_path):
            updated_count += 1
        print()

    print("=" * 70)
    print(f"\nSummary:")
    print(f"  Total files processed: {len(html_files)}")
    print(f"  Files reverted: {updated_count}")
    print(f"  Files unchanged: {len(html_files) - updated_count}")
    print("\nEnquire Now buttons have been reverted successfully!")
    print("Get More Info buttons still use openContactModal() as intended.")

if __name__ == '__main__':
    main()
