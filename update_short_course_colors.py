#!/usr/bin/env python3
"""
Update short course pages with consistent SpecCon color scheme
- Replace green check marks with orange accent
- Standardize orange color codes
"""

import os
import glob

def update_short_course_colors():
    """Update all short course HTML files with consistent colors"""

    # Get all short course HTML files
    short_course_dir = "short-courses"
    html_files = glob.glob(os.path.join(short_course_dir, "*.html"))

    print(f"Found {len(html_files)} short course files to update")

    updates_count = 0

    for html_file in html_files:
        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Color replacements for consistency
            replacements = {
                'text-green-500': 'text-[#ffa600]',
                'text-orange-600': 'text-[#ffa600]',
                'text-orange-500': 'text-[#ffa600]',
                'text-green-600': 'text-[#ffa600]',
            }

            # Apply replacements
            for old_color, new_color in replacements.items():
                if old_color in content:
                    content = content.replace(old_color, new_color)
                    print(f"  {os.path.basename(html_file)}: Replaced {old_color} with {new_color}")

            # Only write if changes were made
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updates_count += 1
                print(f"[OK] Updated: {os.path.basename(html_file)}")
            else:
                print(f"  No changes needed: {os.path.basename(html_file)}")

        except Exception as e:
            print(f"[ERROR] Error processing {html_file}: {str(e)}")

    print(f"\n{'='*60}")
    print(f"Color update complete!")
    print(f"Total files updated: {updates_count}/{len(html_files)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    update_short_course_colors()
