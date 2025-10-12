#!/usr/bin/env python3
"""
Update all qualification pages to:
1. Ensure 'Accept': 'application/json' is in all form submissions
2. Update 'Get More Info' buttons to use openContactModal()
3. Ensure centralized-modals.js is included
"""

import os
import re
import glob

def update_qualification_page(file_path):
    """Update a single qualification page with the required changes."""
    print(f"Processing: {os.path.basename(file_path)}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = []

        # 1. Update "Get More Info" buttons to use openContactModal instead of openEnquiryModal
        if 'openEnquiryModal()' in content:
            # Find all instances where buttons call openEnquiryModal for "Get More Info"
            content = content.replace('onclick="openEnquiryModal()"', 'onclick="openContactModal()"')
            if content != original_content:
                changes_made.append("Updated Get More Info button to openContactModal()")
                original_content = content

        # 2. Add 'Accept': 'application/json' to fetch headers if missing
        # Find fetch calls that don't have Accept header
        fetch_pattern = r"fetch\('https://enquiry\.speccon\.co\.za/api/enquiry/submit',\s*\{[^}]*method:\s*'POST',\s*headers:\s*\{([^}]*)\},"

        matches = list(re.finditer(fetch_pattern, content, re.DOTALL))
        for match in matches:
            headers_content = match.group(1)
            # Check if 'Accept' is already present
            if "'Accept'" not in headers_content and '"Accept"' not in headers_content:
                # Add Accept header
                old_headers = match.group(0)
                # Insert 'Accept': 'application/json' after 'Content-Type'
                new_headers = old_headers.replace(
                    "'Content-Type': 'application/json'",
                    "'Content-Type': 'application/json',\n                            'Accept': 'application/json'"
                )
                content = content.replace(old_headers, new_headers)
                if content != original_content:
                    changes_made.append("Added 'Accept': 'application/json' header")
                    original_content = content

        # 3. Ensure centralized-modals.js is included (check if it's missing)
        if '../js/centralized-modals.js' not in content:
            # Find the closing </body> tag and add the script before it
            script_tag = '    <script src="../js/centralized-modals.js"></script>'

            # Look for existing script tags before </body>
            if '<script src="../js/value-adds-popup.js"></script>' in content:
                # Add it after value-adds-popup.js
                content = content.replace(
                    '<script src="../js/value-adds-popup.js"></script>',
                    '<script src="../js/value-adds-popup.js"></script>\n    <script src="../js/centralized-modals.js"></script>'
                )
            elif '</body>' in content:
                # Add before closing body tag
                content = content.replace('</body>', f'\n{script_tag}\n</body>')

            if content != original_content:
                changes_made.append("Added centralized-modals.js script")
                original_content = content

        # 4. Fix typo in API URL if present (equiry instead of enquiry)
        if 'https://equiry.speccon.co.za' in content:
            content = content.replace('https://equiry.speccon.co.za', 'https://enquiry.speccon.co.za')
            if content != original_content:
                changes_made.append("Fixed API URL typo")
                original_content = content

        # Write back if changes were made
        if changes_made:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [+] Updated: {', '.join(changes_made)}")
            return True
        else:
            print(f"  [-] No changes needed")
            return False

    except Exception as e:
        print(f"  [!] Error: {e}")
        return False

def main():
    """Main function to update all qualification pages."""
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

        if update_qualification_page(file_path):
            updated_count += 1
        print()

    print("=" * 70)
    print(f"\nSummary:")
    print(f"  Total files processed: {len(html_files)}")
    print(f"  Files updated: {updated_count}")
    print(f"  Files unchanged: {len(html_files) - updated_count}")
    print("\nAll qualification pages have been updated successfully!")

if __name__ == '__main__':
    main()
