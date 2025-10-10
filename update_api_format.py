#!/usr/bin/env python3
"""
Update all qualification pages to use the exact API format.
Converts enquiryData to match API expectations:
{
  "Name": "",
  "Surname": "",
  "Email": "",
  "MobileNumber": "",
  "JobTitle": "",
  "CompanyName": "",
  "NumEmployees": 0,
  "Course": "",
  "NumAttendees": 0,
  "Location": "",
  "Reason": "",
  "Source": "",
  "TrainingBookingDate": ""
}
"""

import os
import re
from pathlib import Path

def extract_qualification_name(content):
    """Extract qualification name from the title or heading."""
    # Try to find in title tag
    title_match = re.search(r'<title>([^|]+)', content)
    if title_match:
        return title_match.group(1).strip()

    # Fallback to h1 tag
    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if h1_match:
        return h1_match.group(1).strip()

    return "Qualification"

def update_enquiry_data_format(content, filename):
    """
    Update the enquiryData object to match exact API format.
    Also fixes formData.getElementById bug to formData.get
    """

    page_source = filename.replace('.html', '')
    qualification_name = extract_qualification_name(content)

    # Find the start of enquiryData
    start_pattern = r'const enquiryData = \{'
    start_match = re.search(start_pattern, content)
    if not start_match:
        return content, False

    start_pos = start_match.start()

    # Find the closing brace and semicolon by counting braces
    brace_count = 0
    in_enquiry_data = False
    end_pos = None

    for i in range(start_pos, len(content)):
        if content[i] == '{':
            brace_count += 1
            in_enquiry_data = True
        elif content[i] == '}':
            brace_count -= 1
            if in_enquiry_data and brace_count == 0:
                # Find the semicolon after this closing brace
                if i + 1 < len(content) and content[i + 1] == ';':
                    end_pos = i + 2
                    break

    if end_pos is None:
        return content, False

    # Extract the old enquiryData
    old_enquiry_data = content[start_pos:end_pos]

    # Build the new enquiryData object with exact API format
    new_enquiry_data = f'''const enquiryData = {{
                Name: formData.get('firstName') || '',
                Surname: formData.get('surname') || '',
                Email: formData.get('email') || '',
                MobileNumber: formData.get('phone') || '',
                JobTitle: '',
                CompanyName: formData.get('company') || '',
                NumEmployees: 0,
                Course: '{qualification_name}',
                NumAttendees: 0,
                Location: '',
                Reason: formData.get('reason') || '',
                Source: '{page_source}',
                TrainingBookingDate: ''
            }};'''

    # Replace the old enquiryData with new format
    updated_content = content.replace(old_enquiry_data, new_enquiry_data)

    return updated_content, updated_content != content

def update_all_qualification_files():
    """Update all qualification HTML files to use exact API format."""

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
    no_change_count = 0
    error_count = 0

    for html_file in sorted(html_files):
        try:
            # Read file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if file has submitEnquiry function
            if 'function submitEnquiry' not in content:
                no_change_count += 1
                continue

            # Update content
            updated_content, was_updated = update_enquiry_data_format(content, html_file.name)

            if was_updated:
                # Write updated content back to file
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                print(f"[+] Updated API format: {html_file.name}")
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
    print(f"  Files updated: {updated_count}")
    print(f"  No change needed: {no_change_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total processed: {len(html_files)}")
    print(f"{'='*60}")

    if updated_count > 0:
        print(f"\n[SUCCESS] Updated {updated_count} qualification page(s)")
        print(f"  All forms now use exact API format:")
        print(f"  - Fixed formData.getElementById bug")
        print(f"  - Proper field names (Name, Surname, Email, MobileNumber, etc.)")
        print(f"  - Added missing fields (JobTitle, NumEmployees, Location, etc.)")
    else:
        print("\nNo files needed updating")

if __name__ == '__main__':
    update_all_qualification_files()
