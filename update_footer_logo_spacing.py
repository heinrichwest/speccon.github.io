#!/usr/bin/env python3
"""
Update footer logo spacing to match header spacing across all HTML files
Adds mr-3 (margin-right) to footer logo images for consistent spacing
"""

import os
import glob
import re

def update_footer_logo_spacing():
    """Add consistent spacing to footer logos"""

    # Get all HTML files
    html_files = []
    html_files.extend(glob.glob("*.html"))
    html_files.extend(glob.glob("qualifications/*.html"))
    html_files.extend(glob.glob("setas/*.html"))
    html_files.extend(glob.glob("short-courses/*.html"))

    print(f"Found {len(html_files)} HTML files to check")
    print("="*60)

    updates_count = 0

    for html_file in html_files:
        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Pattern to find footer logo without mr-3 spacing
            # Match: <img src="..." alt="SpecCon Holdings Logo" class="h-12">
            # Replace with: <img src="..." alt="SpecCon Holdings Logo" class="h-12 mr-3">

            # Only update if it doesn't already have mr-3
            pattern1 = r'(<img\s+src="[^"]*SpecCon-LOGO\.png"\s+alt="SpecCon Holdings Logo"\s+class="h-12)">'
            replacement1 = r'\1 mr-3">'

            if re.search(pattern1, content):
                content = re.sub(pattern1, replacement1, content)
                updates_count += 1
                print(f"[OK] Added spacing to: {os.path.basename(html_file)}")
            else:
                # Check if it already has mr-3
                if 'SpecCon-LOGO.png' in content:
                    if 'class="h-12 mr-3"' in content:
                        print(f"  Already has spacing: {os.path.basename(html_file)}")
                    else:
                        print(f"  No standard footer found: {os.path.basename(html_file)}")

            # Write if changes were made
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)

        except Exception as e:
            print(f"[ERROR] Error processing {html_file}: {str(e)}")

    print("="*60)
    print(f"Footer logo spacing update complete!")
    print(f"Total files updated: {updates_count}/{len(html_files)}")
    print("="*60)

if __name__ == "__main__":
    update_footer_logo_spacing()
