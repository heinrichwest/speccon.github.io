#!/usr/bin/env python3
"""
Script to update all "Get More Info" buttons in qualification files
to use openContactModal() instead of openEnquiryModal()
"""

import os
import re
from pathlib import Path

def update_file(filepath):
    """Update a single file to change openEnquiryModal to openContactModal for Get More Info buttons"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern to match button with openEnquiryModal followed by Get More Info text within ~200 characters
        # This ensures we only change the "Get More Info" buttons, not "Apply" or "Enquire Now" buttons
        pattern = r'(<button\s+onclick="open)Enquiry(Modal\(\)"[^>]*>[\s\S]{0,200}?Get More Info[\s\S]{0,50}?</button>)'

        # Replace openEnquiryModal with openContactModal for buttons containing "Get More Info"
        updated_content = re.sub(pattern, r'\1Contact\2', content, flags=re.MULTILINE)

        # Also fix the typo opencontactModal (lowercase c) to openContactModal
        updated_content = updated_content.replace('opencontactModal()', 'openContactModal()')

        if updated_content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    # Directory containing qualification files
    qual_dir = Path(r"C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master\qualifications")

    if not qual_dir.exists():
        print(f"Directory not found: {qual_dir}")
        return

    # Get all HTML files
    html_files = list(qual_dir.glob("*.html"))

    print(f"Found {len(html_files)} HTML files in qualifications folder")
    print("Updating files...\n")

    updated_count = 0
    updated_files = []

    for html_file in html_files:
        if update_file(html_file):
            updated_count += 1
            updated_files.append(html_file.name)
            print(f"[OK] Updated: {html_file.name}")

    print(f"\n{'='*60}")
    print(f"Update Complete!")
    print(f"{'='*60}")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files updated: {updated_count}")
    print(f"Files unchanged: {len(html_files) - updated_count}")

    if updated_files:
        print(f"\n{'='*60}")
        print("Updated files:")
        print(f"{'='*60}")
        for filename in sorted(updated_files):
            print(f"  - {filename}")

if __name__ == "__main__":
    main()
