#!/usr/bin/env python3
"""
Final cleanup for short course tile and icon background colors
- Replace light background colors (bg-green-100, bg-blue-100, etc.) with SpecCon colors
- Replace remaining button colors
- Replace section gradient backgrounds
"""

import os
import glob

def update_short_course_tiles_final():
    """Final cleanup of tile and background colors"""

    # Get all short course HTML files
    short_course_dir = "short-courses"
    html_files = glob.glob(os.path.join(short_course_dir, "*.html"))

    print(f"Found {len(html_files)} short course files for final cleanup")

    updates_count = 0

    for html_file in html_files:
        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Light background color replacements for icon tiles
            replacements = {
                'bg-green-100': 'bg-[#ffa600]/20',
                'bg-blue-100': 'bg-[#12265E]/20',
                'bg-purple-100': 'bg-[#92abc4]/30',
                'bg-indigo-100': 'bg-[#12265E]/20',
                'bg-orange-100': 'bg-[#ffa600]/20',

                # Section backgrounds
                'bg-gradient-to-br from-purple-50 to-blue-50': 'bg-gradient-to-br from-blue-50 to-white',
                'bg-purple-50': 'bg-blue-50',
                'border-purple-200': 'border-blue-200',
                'bg-green-50': 'bg-blue-50',
                'border-green-200': 'border-blue-200',

                # Remaining button colors
                'bg-purple-600 text-white font-semibold px-5 py-2 rounded-lg hover:bg-blue-700':
                    'bg-gradient-to-r from-[#12265E] to-[#92ABC4] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8]',
                'bg-green-600 text-white font-semibold px-5 py-2 rounded-lg hover:bg-blue-700':
                    'bg-gradient-to-r from-[#12265E] to-[#92ABC4] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8]',
            }

            # Apply replacements
            changes_made = []
            for old_color, new_color in replacements.items():
                if old_color in content:
                    content = content.replace(old_color, new_color)
                    changes_made.append(f"{old_color[:40]}")

            # Only write if changes were made
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updates_count += 1
                print(f"[OK] Updated: {os.path.basename(html_file)}")
                for change in changes_made:
                    print(f"  - Fixed: {change}")
            else:
                print(f"  No changes needed: {os.path.basename(html_file)}")

        except Exception as e:
            print(f"[ERROR] Error processing {html_file}: {str(e)}")

    print(f"\n{'='*60}")
    print(f"Final tile color cleanup complete!")
    print(f"Total files updated: {updates_count}/{len(html_files)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    update_short_course_tiles_final()
