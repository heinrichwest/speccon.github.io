#!/usr/bin/env python3
"""
Update all footer logos in HTML files to use the correct path: images/SpecCon-LOGO.png
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
    relative_dir = file_path.parent.relative_to(base_dir)

    # Calculate how many directories deep we are
    depth = len(relative_dir.parts) if str(relative_dir) != '.' else 0

    # Build the correct path
    if depth == 0:
        # Files in root directory
        return 'images/SpecCon-LOGO.png'
    else:
        # Files in subdirectories need ../
        return '../' * depth + 'images/SpecCon-LOGO.png'

def update_footer_logos(file_path):
    """Update footer logo paths in HTML file"""

    print(f"Processing: {file_path.name}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Get the correct path for this file
    correct_path = get_correct_logo_path(file_path)

    # Find footer section
    footer_match = re.search(r'<footer[^>]*>.*?</footer>', content, re.DOTALL | re.IGNORECASE)

    if footer_match:
        footer_content = footer_match.group(0)
        original_footer = footer_content

        # Pattern to match SpecCon logo img tags in footer
        # Match various possible paths for SpecCon logo
        patterns = [
            r'<img\s+src="[^"]*(?:Logo\.png|SpecCon2\.png|SpecCon-LOGO\.png|LOGO\.png|logo\.png)"[^>]*alt="SpecCon[^"]*"[^>]*>',
            r'<img\s+src="[^"]*(?:Logo\.png|SpecCon2\.png|SpecCon-LOGO\.png|LOGO\.png|logo\.png)"[^>]*>',
            # Also match if alt comes before src
            r'<img[^>]*alt="SpecCon[^"]*"[^>]*src="[^"]*(?:Logo\.png|SpecCon2\.png|SpecCon-LOGO\.png|LOGO\.png|logo\.png)"[^>]*>',
        ]

        for pattern in patterns:
            matches = re.finditer(pattern, footer_content, re.IGNORECASE)
            for match in matches:
                old_img_tag = match.group(0)

                # Extract existing classes if any
                class_match = re.search(r'class="([^"]*)"', old_img_tag)
                if class_match:
                    classes = class_match.group(1)
                    # Make sure it has the required classes
                    if 'h-12' not in classes:
                        classes = 'h-12 mr-3'
                else:
                    classes = 'h-12 mr-3'

                # Create new img tag with correct path
                new_img_tag = f'<img src="{correct_path}" alt="SpecCon Holdings Logo" class="{classes}">'

                footer_content = footer_content.replace(old_img_tag, new_img_tag)

                if footer_content != original_footer:
                    changes_made = True
                    print(f"  [OK] Updated footer logo to: {correct_path}")

        # Replace the footer in the content if changes were made
        if changes_made:
            content = content.replace(original_footer, footer_content)

    # Also check for any SpecCon logos outside footer that might need updating
    # (in case there are logos in other sections that should be updated)
    if not changes_made:
        # Check if there's any SpecCon logo reference that needs updating
        logo_patterns = [
            (r'src="[^"]*Logo\.png"', f'src="{correct_path}"'),
            (r'src="[^"]*SpecCon2\.png"', f'src="{correct_path}"'),
            (r'src="[^"]*SpecCon-Logo\.png"', f'src="{correct_path}"'),
            (r'src="[^"]*LOGO\.png"', f'src="{correct_path}"'),
        ]

        for old_pattern, new_value in logo_patterns:
            if re.search(old_pattern, content) and 'SpecCon' in content[max(0, content.find(old_pattern) - 100):content.find(old_pattern) + 100]:
                content = re.sub(old_pattern, new_value, content)
                changes_made = True
                print(f"  [OK] Updated logo reference to: {correct_path}")
                break

    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [DONE] File updated successfully!")
        return True
    else:
        print(f"  [INFO] No footer logo found or already correct")
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
    print("Updating footer logos in all HTML files")
    print(f"Found {total_files} HTML files")
    print("=" * 60)

    for file_path in html_files:
        if update_footer_logos(file_path):
            total_updated += 1

    print("\n" + "=" * 60)
    print(f"Update complete!")
    print(f"Files updated: {total_updated} / {total_files}")
    print("All footer logos now use: images/SpecCon-LOGO.png")
    print("=" * 60)

if __name__ == '__main__':
    main()