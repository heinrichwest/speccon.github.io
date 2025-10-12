#!/usr/bin/env python3
"""
Clean up duplicate/orphaned code in SETA files after API integration
Removes old submitEnquiry implementation leftovers
"""

import os
import glob
import re

def cleanup_seta_duplicate_code():
    """Remove duplicate code blocks in SETA files"""

    # Get all SETA HTML files
    setas_dir = "setas"
    html_files = glob.glob(os.path.join(setas_dir, "*.html"))

    print(f"Found {len(html_files)} SETA files to clean up")
    print("="*60)

    updates_count = 0

    for html_file in html_files:
        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Pattern to find the orphaned code block after the async submitEnquiry function
            # This is the leftover code from the old implementation
            orphaned_pattern = r'\s*\};\s*//\s*For now, just show success message.*?console\.log\([\'"]Enquiry submitted:[\'"],\s*enquiryData\);\s*\}'

            # Remove the orphaned code
            if re.search(orphaned_pattern, content, re.DOTALL):
                content = re.sub(orphaned_pattern, '', content, flags=re.DOTALL)
                print(f"[OK] Removed orphaned code from: {os.path.basename(html_file)}")
                updates_count += 1

            # Also look for and remove duplicate alert/close calls after the closing brace
            duplicate_pattern = r'(\}\s*\}\s*catch.*?\}\s*\})(;\s*//\s*For now.*?console\.log\([\'"]Enquiry submitted.*?\})'
            if re.search(duplicate_pattern, content, re.DOTALL):
                content = re.sub(duplicate_pattern, r'\1', content, flags=re.DOTALL)
                print(f"[OK] Cleaned duplicate code from: {os.path.basename(html_file)}")
                updates_count += 1

            # Write if changes were made
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                print(f"  No duplicate code found in: {os.path.basename(html_file)}")

        except Exception as e:
            print(f"[ERROR] Error processing {html_file}: {str(e)}")

    print("="*60)
    print(f"Code cleanup complete!")
    print(f"Total files cleaned: {updates_count}/{len(html_files)}")
    print("="*60)

if __name__ == "__main__":
    cleanup_seta_duplicate_code()
