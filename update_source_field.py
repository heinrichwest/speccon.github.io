#!/usr/bin/env python3
"""
Update all qualification pages to add Source field with the actual page filename.
The Source field should reflect the page name (e.g., 'agri-animal-production')
instead of being hardcoded as 'contactus'.
"""

import os
import re
from pathlib import Path

def update_source_field(content, filename):
    """
    Add or update the Source field in enquiryData to use the actual filename.
    """

    # Extract filename without extension (e.g., 'agri-animal-production-nqf1' from 'agri-animal-production-nqf1.html')
    page_source = filename.replace('.html', '')

    # Pattern 1: Find enquiryData object that has 'qualification' but no 'Source'
    # This pattern looks for the closing brace of enquiryData before localStorage
    pattern1 = r"(const enquiryData = \{[^}]*qualification: '[^']*'\s*)\};"

    # Check if Source field already exists
    if re.search(r"[Ss]ource:\s*['\"]", content):
        # Source field exists, update it
        pattern_update = r"([Ss]ource:\s*['\"])[^'\"]*(['\"])"
        replacement = rf"\1{page_source}\2"
        updated_content = re.sub(pattern_update, replacement, content)
        return updated_content, "updated"
    else:
        # Source field doesn't exist, add it
        replacement1 = rf"\1,\n                source: '{page_source}'\n            }};"
        updated_content = re.sub(pattern1, replacement1, content)

        # Check if update was successful
        if updated_content != content:
            return updated_content, "added"
        else:
            # Try alternative pattern for different formatting
            pattern2 = r"(const enquiryData = \{[^}]*qualification: '[^']*')\s*\};"
            replacement2 = rf"\1,\n                source: '{page_source}'\n            }};"
            updated_content = re.sub(pattern2, replacement2, content)

            if updated_content != content:
                return updated_content, "added"
            else:
                return content, "no_change"

def update_all_qualification_files():
    """Update all qualification HTML files to add proper Source field."""

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

    added_count = 0
    updated_count = 0
    no_change_count = 0
    error_count = 0

    for html_file in sorted(html_files):
        try:
            # Read file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if file has enquiryData
            if 'const enquiryData' not in content:
                no_change_count += 1
                continue

            # Update content
            updated_content, status = update_source_field(content, html_file.name)

            if status in ['added', 'updated']:
                # Write updated content back to file
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                if status == 'added':
                    print(f"[+] Added Source field: {html_file.name}")
                    added_count += 1
                else:
                    print(f"[*] Updated Source field: {html_file.name}")
                    updated_count += 1
            else:
                print(f"[-] No change needed: {html_file.name}")
                no_change_count += 1

        except Exception as e:
            print(f"[!] Error processing {html_file.name}: {str(e)}")
            error_count += 1

    # Summary
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Source field added: {added_count}")
    print(f"  Source field updated: {updated_count}")
    print(f"  No change needed: {no_change_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total processed: {len(html_files)}")
    print(f"{'='*60}")

    if added_count > 0 or updated_count > 0:
        print(f"\n[SUCCESS] Modified {added_count + updated_count} qualification page(s)")
        print(f"  All forms now use actual page filename for Source field")
    else:
        print("\nNo files needed updating")

if __name__ == '__main__':
    update_all_qualification_files()
