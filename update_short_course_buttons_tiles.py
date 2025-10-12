#!/usr/bin/env python3
"""
Update short course pages with consistent SpecCon button and tile colors
- Replace hero section gradients with SpecCon gradient
- Replace CTA section gradients with SpecCon gradient
- Replace button colors with SpecCon gradient
- Replace badge/tag colors with SpecCon orange
"""

import os
import glob
import re

def update_short_course_buttons_tiles():
    """Update all short course HTML files with consistent button and tile colors"""

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

            # Hero section gradient replacements
            hero_gradients = [
                ('bg-gradient-to-br from-green-600 via-green-700 to-green-800', 'bg-gradient-to-br from-[#12265E] via-[#92abc4] to-[#12265E]'),
                ('bg-gradient-to-br from-blue-600 via-blue-700 to-blue-800', 'bg-gradient-to-br from-[#12265E] via-[#92abc4] to-[#12265E]'),
                ('bg-gradient-to-br from-purple-600 via-purple-700 to-purple-800', 'bg-gradient-to-br from-[#12265E] via-[#92abc4] to-[#12265E]'),
                ('bg-gradient-to-br from-orange-600 via-orange-700 to-orange-800', 'bg-gradient-to-br from-[#12265E] via-[#92abc4] to-[#12265E]'),
                ('bg-gradient-to-br from-indigo-600 via-indigo-700 to-indigo-800', 'bg-gradient-to-br from-[#12265E] via-[#92abc4] to-[#12265E]'),
            ]

            # CTA section gradient replacements
            cta_gradients = [
                ('bg-gradient-to-r from-green-600 to-green-800', 'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
                ('bg-gradient-to-r from-blue-600 to-blue-800', 'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
                ('bg-gradient-to-r from-purple-600 to-purple-800', 'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
                ('bg-gradient-to-r from-orange-600 to-orange-800', 'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
                ('bg-gradient-to-r from-indigo-600 to-indigo-800', 'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
            ]

            # Badge/tag color replacements
            badge_colors = [
                ('bg-green-500/20 text-green-100', 'bg-[#ffa600]/20 text-[#ffa600]'),
                ('bg-blue-500/20 text-blue-100', 'bg-[#ffa600]/20 text-[#ffa600]'),
                ('bg-purple-500/20 text-purple-100', 'bg-[#ffa600]/20 text-[#ffa600]'),
                ('bg-orange-500/20 text-orange-100', 'bg-[#ffa600]/20 text-[#ffa600]'),
                ('bg-indigo-500/20 text-indigo-100', 'bg-[#ffa600]/20 text-[#ffa600]'),
            ]

            # Text color replacements in hero/CTA sections
            text_colors = [
                ('text-green-100', 'text-white'),
                ('text-blue-100', 'text-white'),
                ('text-purple-100', 'text-white'),
                ('text-orange-100', 'text-white'),
                ('text-indigo-100', 'text-white'),
            ]

            # Button color replacements
            button_colors = [
                ('bg-blue-600 text-white font-semibold px-5 py-2 rounded-lg hover:bg-blue-700',
                 'bg-gradient-to-r from-[#12265E] to-[#92ABC4] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8]'),
                ('bg-green-600 text-white font-semibold px-5 py-2 rounded-lg hover:bg-green-700',
                 'bg-gradient-to-r from-[#12265E] to-[#92ABC4] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8]'),
            ]

            # Apply all replacements
            changes_made = []

            for old_color, new_color in hero_gradients + cta_gradients + badge_colors + text_colors + button_colors:
                if old_color in content:
                    content = content.replace(old_color, new_color)
                    changes_made.append(f"Replaced {old_color[:50]}...")

            # Only write if changes were made
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updates_count += 1
                print(f"[OK] Updated: {os.path.basename(html_file)}")
                for change in changes_made:
                    print(f"  - {change}")
            else:
                print(f"  No changes needed: {os.path.basename(html_file)}")

        except Exception as e:
            print(f"[ERROR] Error processing {html_file}: {str(e)}")

    print(f"\n{'='*60}")
    print(f"Button and tile color update complete!")
    print(f"Total files updated: {updates_count}/{len(html_files)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    update_short_course_buttons_tiles()
