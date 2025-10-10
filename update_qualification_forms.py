#!/usr/bin/env python3
"""
Update all qualification page forms to save data to localStorage like index.html does.
This script adds localStorage.setItem() functionality to save enquiry form data.
"""

import os
import re
from pathlib import Path

def update_form_submission(content):
    """
    Add localStorage saving to the submitEnquiry function.
    Adds localStorage.setItem after enquiryData is created and before the alert.
    """

    # Pattern to find the submitEnquiry function with enquiryData object
    # We want to add localStorage saving after the enquiryData object is created
    pattern = r"(function submitEnquiry\(event\) \{[\s\S]*?const enquiryData = \{[\s\S]*?\};)\s*(\n\s*// For now, just show success message)"

    # Check if localStorage saving already exists
    if 'localStorage.setItem' in content:
        return content, False

    # Replacement adds localStorage saving
    replacement = r'''\1

            // Save to localStorage for reference (matching index.html behavior)
            localStorage.setItem('lastEnquiryData', JSON.stringify(enquiryData));
\2'''

    updated_content = re.sub(pattern, replacement, content)

    # Check if update was made
    was_updated = updated_content != content

    return updated_content, was_updated

def update_qualification_files():
    """Update all qualification HTML files to add localStorage saving."""

    qualifications_dir = Path('qualifications')

    if not qualifications_dir.exists():
        print(f"Error: {qualifications_dir} directory not found")
        return

    # Get all HTML files
    html_files = list(qualifications_dir.glob('*.html'))

    if not html_files:
        print(f"No HTML files found in {qualifications_dir}")
        return

    print(f"Found {len(html_files)} HTML files in qualifications folder\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0

    for html_file in sorted(html_files):
        try:
            # Read file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if file has submitEnquiry function
            if 'function submitEnquiry' not in content:
                skipped_count += 1
                continue

            # Update content
            updated_content, was_updated = update_form_submission(content)

            if was_updated:
                # Write updated content back to file
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                print(f"[+] Updated: {html_file.name}")
                updated_count += 1
            else:
                print(f"[-] Already has localStorage: {html_file.name}")
                skipped_count += 1

        except Exception as e:
            print(f"[!] Error processing {html_file.name}: {str(e)}")
            error_count += 1

    # Summary
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files updated: {updated_count}")
    print(f"  Files skipped: {skipped_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total processed: {len(html_files)}")
    print(f"{'='*60}")

    if updated_count > 0:
        print(f"\n[SUCCESS] Updated {updated_count} qualification page(s)")
        print(f"  All enquiry forms now save to localStorage like index.html")
    else:
        print("\nNo files needed updating (all already have localStorage saving)")

if __name__ == '__main__':
    update_qualification_files()
