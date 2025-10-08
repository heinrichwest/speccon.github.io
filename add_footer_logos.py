#!/usr/bin/env python3
"""
Add footer logos to HTML files that don't have them
"""

import os
import re
from pathlib import Path

def get_correct_logo_path(file_path):
    """
    Determine the correct relative path to images/SpecCon-LOGO.png based on file location
    """
    # Convert to Path object
    file_path = Path(file_path)

    # Get the relative path from the file to the base directory
    base_dir = Path(r'C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master')

    # Get the file's parent directory relative to base
    try:
        relative_dir = file_path.parent.relative_to(base_dir)
    except ValueError:
        # If file is in base directory
        return 'images/SpecCon-LOGO.png'

    # Calculate how many directories deep we are
    depth = len(relative_dir.parts) if str(relative_dir) != '.' else 0

    # Build the correct path
    if depth == 0:
        # Files in root directory
        return 'images/SpecCon-LOGO.png'
    else:
        # Files in subdirectories need ../
        return '../' * depth + 'images/SpecCon-LOGO.png'

def add_footer_logo(file_path):
    """Add footer logo to HTML file if it doesn't have one"""

    print(f"Processing: {file_path.name}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Get the correct path for this file
    correct_path = get_correct_logo_path(file_path)

    # Find footer section
    footer_pattern = r'(<footer[^>]*>.*?</footer>)'
    footer_match = re.search(footer_pattern, content, re.DOTALL | re.IGNORECASE)

    if footer_match:
        footer_content = footer_match.group(1)
        original_footer = footer_content

        # Check if footer already has a logo image
        if 'img src' in footer_content and 'SpecCon' in footer_content:
            # Update existing logo path if needed
            if correct_path not in footer_content:
                # Pattern to match SpecCon logo img tags
                img_patterns = [
                    r'<img\s+src="[^"]*"([^>]*alt="SpecCon[^"]*"[^>]*)>',
                    r'<img([^>]*alt="SpecCon[^"]*"[^>]*)src="[^"]*"([^>]*)>',
                ]

                for pattern in img_patterns:
                    if re.search(pattern, footer_content, re.IGNORECASE):
                        # Replace the src attribute
                        footer_content = re.sub(
                            r'src="[^"]*"',
                            f'src="{correct_path}"',
                            footer_content
                        )
                        changes_made = True
                        print(f"  [OK] Updated existing footer logo to: {correct_path}")
                        break
        else:
            # No logo in footer - need to add one
            # Look for the pattern where we need to add the logo
            # Pattern 1: Look for SpecCon Holdings text without logo
            pattern1 = r'(<div[^>]*>)\s*(<h3[^>]*>SpecCon Holdings</h3>)'
            match1 = re.search(pattern1, footer_content, re.IGNORECASE)

            if match1:
                # Add logo with flex container
                replacement = f'''{match1.group(1)}
                    <div class="flex items-center mb-4">
                        <img src="{correct_path}" alt="SpecCon Holdings Logo" class="h-12 mr-3">
                        <div>
                            {match1.group(2)}'''

                footer_content = re.sub(pattern1, replacement, footer_content, count=1)
                # Close the extra div
                footer_content = re.sub(
                    r'(</h3>)\s*(<p[^>]*>[^<]*</p>)',
                    r'\1\n                            <p class="text-white/80">Professional Training & Development</p>\n                        </div>\n                    </div>\n                    \2',
                    footer_content,
                    count=1
                )
                changes_made = True
                print(f"  [OK] Added footer logo: {correct_path}")
            else:
                # Pattern 2: Look for container div without logo
                pattern2 = r'(<div class="md:col-span-2">)\s*(<h3[^>]*>SpecCon[^<]*</h3>)'
                match2 = re.search(pattern2, footer_content, re.IGNORECASE)

                if match2:
                    replacement = f'''{match2.group(1)}
                    <div class="flex items-center mb-4">
                        <img src="{correct_path}" alt="SpecCon Holdings Logo" class="h-12 mr-3">
                        <div>
                            {match2.group(2)}
                            <p class="text-white/80">Professional Training & Development</p>
                        </div>
                    </div>'''

                    footer_content = re.sub(pattern2, replacement, footer_content, count=1)
                    changes_made = True
                    print(f"  [OK] Added footer logo structure: {correct_path}")

        # Replace the footer in the content if changes were made
        if changes_made:
            content = content.replace(original_footer, footer_content)

    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [DONE] File updated successfully!")
        return True
    else:
        # Check if it already has the correct logo
        if correct_path in content:
            print(f"  [INFO] Footer logo already correct")
        else:
            print(f"  [INFO] No footer found or unable to add logo")
        return False

def main():
    base_dir = Path(r'C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master')

    # Get all HTML files
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(Path(root) / file)

    # Sort files for consistent output
    html_files.sort()

    total_files = len(html_files)
    total_updated = 0

    print("=" * 60)
    print("Adding footer logos to HTML files")
    print(f"Found {total_files} HTML files")
    print("=" * 60)

    for file_path in html_files:
        if add_footer_logo(file_path):
            total_updated += 1

    print("\n" + "=" * 60)
    print(f"Update complete!")
    print(f"Files updated: {total_updated} / {total_files}")
    print("All footer logos now use: images/SpecCon-LOGO.png")
    print("=" * 60)

if __name__ == '__main__':
    main()