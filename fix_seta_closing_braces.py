#!/usr/bin/env python3
"""
Fix missing closing braces in submitEnquiry functions
"""

import os
import glob
import re

def fix_seta_closing_braces():
    """Add missing closing braces to submitEnquiry functions"""

    # Get all SETA HTML files
    setas_dir = "setas"
    html_files = glob.glob(os.path.join(setas_dir, "*.html"))

    print(f"Found {len(html_files)} SETA files to fix")
    print("="*60)

    updates_count = 0

    for html_file in html_files:
        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Pattern to find submitEnquiry function missing closing brace
            # Should have the catch block ending with } but missing the function's closing }
            pattern = r'(catch \(error\) \{\s*alert\([^\)]+\);\s*console\.error\([^\)]+\);\s*\}\s*)\n\n(\s*//\s*Set up modal)'

            # Replace with proper closing
            replacement = r'\1        }\n\n\2'

            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                updates_count += 1
                print(f"[OK] Fixed closing brace in: {os.path.basename(html_file)}")

            # Write if changes were made
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                print(f"  No issues found in: {os.path.basename(html_file)}")

        except Exception as e:
            print(f"[ERROR] Error processing {html_file}: {str(e)}")

    print("="*60)
    print(f"Closing brace fix complete!")
    print(f"Total files fixed: {updates_count}/{len(html_files)}")
    print("="*60)

if __name__ == "__main__":
    fix_seta_closing_braces()
