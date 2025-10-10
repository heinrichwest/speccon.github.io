#!/usr/bin/env python3
"""
Script to remove all Apply buttons from qualification pages.
Removes: Apply for This Qualification, Apply for Learnership, Apply Now buttons
"""

import os
import re
from pathlib import Path

def remove_apply_buttons(content):
    """Remove all apply button variations from HTML content"""

    # Pattern 1: Remove "Apply for This Qualification" button (any onclick handler)
    # This handles: <button onclick="..." ...>Apply for This Qualification</button>
    pattern1 = r'<button\s+onclick="[^"]*"\s+class="[^"]*"[^>]*>\s*Apply for This Qualification\s*</button>'
    content = re.sub(pattern1, '', content, flags=re.IGNORECASE | re.DOTALL)

    # Pattern 2: Remove "Apply Now" button (any onclick handler)
    # This handles: <button onclick="..." ...>Apply Now</button>
    pattern2 = r'<button\s+onclick="[^"]*"\s+class="[^"]*"[^>]*>\s*Apply Now\s*</button>'
    content = re.sub(pattern2, '', content, flags=re.IGNORECASE | re.DOTALL)

    # Pattern 3: Remove "Apply for Learnership" link
    # This handles: <a href="../learnership-application.html" ...>Apply for Learnership</a>
    pattern3 = r'<a\s+href="\.\.\/learnership-application\.html"[^>]*>\s*Apply for Learnership\s*</a>'
    content = re.sub(pattern3, '', content, flags=re.IGNORECASE | re.DOTALL)

    # Pattern 4: Alternative button format with text on new line
    pattern4 = r'<button[^>]+>\s*Apply for This Qualification\s*</button>'
    content = re.sub(pattern4, '', content, flags=re.IGNORECASE | re.DOTALL)

    pattern5 = r'<button[^>]+>\s*Apply Now\s*</button>'
    content = re.sub(pattern5, '', content, flags=re.IGNORECASE | re.DOTALL)

    # Pattern 6: Remove Apply Now as link
    pattern6 = r'<a\s+href="[^"]*"[^>]*>\s*Apply Now\s*</a>'
    content = re.sub(pattern6, '', content, flags=re.IGNORECASE | re.DOTALL)

    # Pattern 7: Remove Apply for This Qualification as link
    pattern7 = r'<a\s+href="[^"]*"[^>]*>\s*Apply for This Qualification\s*</a>'
    content = re.sub(pattern7, '', content, flags=re.IGNORECASE | re.DOTALL)

    # Clean up empty flex containers that might remain
    # Remove divs with only whitespace between tags
    content = re.sub(r'<div class="flex flex-col sm:flex-row gap-4[^"]*">\s*</div>', '', content)
    content = re.sub(r'<div class="space-y-4">\s*</div>', '', content)

    # Clean up multiple consecutive blank lines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    return content

def process_qualification_files():
    """Process all HTML files in the qualifications folder"""

    qualifications_dir = Path('qualifications')

    if not qualifications_dir.exists():
        print(f"Error: {qualifications_dir} directory not found")
        return

    # Get all .html files (excluding .backup files)
    html_files = [f for f in qualifications_dir.glob('*.html') if not f.name.endswith('.backup')]

    print(f"Found {len(html_files)} HTML files to process")

    processed_count = 0
    error_count = 0

    for html_file in html_files:
        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if file has any apply buttons
            has_apply = any(pattern in content for pattern in [
                'Apply for This Qualification',
                'Apply for Learnership',
                'Apply Now'
            ])

            if has_apply:
                # Remove apply buttons
                updated_content = remove_apply_buttons(content)

                # Write back to file
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                processed_count += 1
                print(f"[OK] Processed: {html_file.name}")
            else:
                print(f"[SKIP] No apply buttons: {html_file.name}")

        except Exception as e:
            error_count += 1
            print(f"[ERROR] Error processing {html_file.name}: {str(e)}")

    print(f"\n{'='*60}")
    print(f"Processing complete!")
    print(f"Files processed: {processed_count}")
    print(f"Errors: {error_count}")
    print(f"{'='*60}")

if __name__ == '__main__':
    process_qualification_files()
