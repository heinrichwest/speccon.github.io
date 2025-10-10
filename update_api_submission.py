#!/usr/bin/env python3
"""
Update all qualification pages to submit data to the actual API endpoint.
Replaces the alert/console.log with actual fetch POST to:
https://enquiry.speccon.co.za/api/enquiry/submit
"""

import os
import re
from pathlib import Path

def update_api_submission(content):
    """
    Update the submitEnquiry function to POST to the actual API.
    """

    # Pattern to find the section after localStorage.setItem and before closeEnquiryModal
    # We want to replace the alert and add actual API submission

    # Pattern 1: For files with localStorage (most files)
    pattern1 = r"(localStorage\.setItem\('lastEnquiryData', JSON\.stringify\(enquiryData\)\);)\s*\n\s*// For now, just show success message and close modal\s*\n\s*alert\('Thank you for your enquiry! We will get back to you soon\.'\);\s*\n\s*closeEnquiryModal\(\);"

    replacement1 = r'''\1

            // Submit to API
            try {
                const response = await fetch('https://enquiry.speccon.co.za/api/enquiry/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(enquiryData)
                });

                if (response.ok) {
                    alert('Thank you for your enquiry! We will get back to you soon.');
                    closeEnquiryModal();
                    event.target.reset();
                } else {
                    const errorData = await response.json();
                    alert('There was an error submitting your enquiry. Please try again or contact us directly.');
                    console.error('API Error:', errorData);
                }
            } catch (error) {
                alert('There was an error submitting your enquiry. Please try again or contact us directly.');
                console.error('Network Error:', error);
            }'''

    # Pattern 2: For files with console.log before alert
    pattern2 = r"(const enquiryData = \{[\s\S]*?\};)\s*\n\s*console\.log\('Enquiry submitted:', enquiryData\);\s*\n\s*alert\('Thank you for your enquiry! We will get back to you soon\.'\);\s*\n\s*closeEnquiryModal\(\);\s*\n\s*event\.target\.reset\(\);"

    replacement2 = r'''\1

            // Save to localStorage for reference
            localStorage.setItem('lastEnquiryData', JSON.stringify(enquiryData));

            // Submit to API
            try {
                const response = await fetch('https://enquiry.speccon.co.za/api/enquiry/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(enquiryData)
                });

                if (response.ok) {
                    alert('Thank you for your enquiry! We will get back to you soon.');
                    closeEnquiryModal();
                    event.target.reset();
                } else {
                    const errorData = await response.json();
                    alert('There was an error submitting your enquiry. Please try again or contact us directly.');
                    console.error('API Error:', errorData);
                }
            } catch (error) {
                alert('There was an error submitting your enquiry. Please try again or contact us directly.');
                console.error('Network Error:', error);
            }'''

    # Pattern 3: For files without localStorage and different order
    pattern3 = r"(const enquiryData = \{[\s\S]*?\};)\s*\n\s*alert\('Thank you for your enquiry! We will get back to you soon\.'\);\s*\n\s*closeEnquiryModal\(\);\s*\n\s*event\.target\.reset\(\);\s*\n\s*console\.log\('Enquiry submitted:', enquiryData\);"

    replacement3 = r'''\1

            // Save to localStorage for reference
            localStorage.setItem('lastEnquiryData', JSON.stringify(enquiryData));

            // Submit to API
            try {
                const response = await fetch('https://enquiry.speccon.co.za/api/enquiry/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(enquiryData)
                });

                if (response.ok) {
                    alert('Thank you for your enquiry! We will get back to you soon.');
                    closeEnquiryModal();
                    event.target.reset();
                } else {
                    const errorData = await response.json();
                    alert('There was an error submitting your enquiry. Please try again or contact us directly.');
                    console.error('API Error:', errorData);
                }
            } catch (error) {
                alert('There was an error submitting your enquiry. Please try again or contact us directly.');
                console.error('Network Error:', error);
            }'''

    # Also need to make submitEnquiry an async function
    content = content.replace('function submitEnquiry(event) {', 'async function submitEnquiry(event) {')

    # Try pattern 1 first (with localStorage)
    updated_content = re.sub(pattern1, replacement1, content)

    if updated_content == content:
        # Try pattern 2 (console.log before alert)
        updated_content = re.sub(pattern2, replacement2, content)

    if updated_content == content:
        # Try pattern 3 (alert before console.log)
        updated_content = re.sub(pattern3, replacement3, content)

    return updated_content, updated_content != content

def update_all_qualification_files():
    """Update all qualification HTML files to submit to API."""

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

            # Check if already has API submission
            if 'https://enquiry.speccon.co.za/api/enquiry/submit' in content:
                print(f"[-] Already has API submission: {html_file.name}")
                no_change_count += 1
                continue

            # Update content
            updated_content, was_updated = update_api_submission(content)

            if was_updated:
                # Write updated content back to file
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                print(f"[+] Added API submission: {html_file.name}")
                updated_count += 1
            else:
                print(f"[-] No pattern match: {html_file.name}")
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
        print(f"  All forms now submit to: https://enquiry.speccon.co.za/api/enquiry/submit")
        print(f"  - Async/await for proper error handling")
        print(f"  - JSON POST request")
        print(f"  - User-friendly error messages")
    else:
        print("\nNo files needed updating")

if __name__ == '__main__':
    update_all_qualification_files()
