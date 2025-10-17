#!/usr/bin/env python3
"""
Fix sidebar structure issues in qualification files.
The problem: Extra closing div tags are breaking the sticky sidebar container.
"""

import re
import os
from pathlib import Path

# Files to exclude
EXCLUDED_FILES = [
    'skills-conflict-management-nqf5.html',
    'skills-new-venture-creation-nqf2.html',
    'skills-workplace-essential-skills-nqf4.html',
    'template-qualification.html'
]

def fix_sidebar_structure(content, filename):
    """Fix the broken sidebar structure caused by extra closing divs."""

    # Pattern to find the problematic structure with extra closing div
    # Looking for the qualification details section with the extra </div> after the fields
    pattern = r'(<div class="space-y-4 mb-8">.*?</div>\s*</div>\s*</div>\s*<div class="space-y-4[^>]*>)'

    # Simpler approach - look for double closing divs after the space-y-4 mb-8 section
    pattern = r'(</div>\s*</div>\s*</div>\s*<div class="space-y-4)'

    # Replace with single closing div
    new_content = re.sub(pattern, r'</div>\n\n                        <div class="space-y-4', content, flags=re.DOTALL)

    # Alternative pattern for files that have different structure
    # Look for closing div followed immediately by opening div for button section
    pattern2 = r'(</div>\s*</div>\s*<div class="space-y-4 mb-8">)'
    new_content = re.sub(pattern2, r'</div>\n\n                        <div class="space-y-4 mb-8">', new_content, flags=re.DOTALL)

    # Fix the specific issue where there's an orphaned closing div after the details section
    # Look for pattern where qualification details ends and then there's extra closing div
    pattern3 = r'(<div class="flex justify-between items-center py-3 border-b border-gray-100">.*?</span>\s*</div>\s*</div>\s*</div>)(\s*</div>\s*<div class="space-y-4)'
    new_content = re.sub(pattern3, r'\1\n\n                        <div class="space-y-4', new_content, flags=re.DOTALL)

    return new_content

def main():
    qualifications_dir = Path('qualifications')

    if not qualifications_dir.exists():
        print(f"Error: {qualifications_dir} not found")
        return

    files = sorted(qualifications_dir.glob('*.html'))

    fixed = 0
    skipped = 0
    errors = 0

    for filepath in files:
        filename = filepath.name

        # Skip excluded files
        if filename in EXCLUDED_FILES:
            print(f"Skipping: {filename}")
            skipped += 1
            continue

        try:
            print(f"Checking: {filename}")

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if the file has the problematic pattern
            if '</div>\s*</div>\s*</div>\s*<div class="space-y-4' in content or \
               '</div>\s*</div>\s*<div class="space-y-4 mb-8">' in content:

                # Fix the sidebar structure
                new_content = fix_sidebar_structure(content, filename)

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  [FIXED]: {filename}")
                    fixed += 1
                else:
                    print(f"  [-] No fix needed: {filename}")
            else:
                print(f"  [-] No issue found: {filename}")

        except Exception as e:
            print(f"  [ERROR]: {filename} - {e}")
            errors += 1

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Fixed: {fixed}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")
    print(f"  Total files: {len(files)}")

if __name__ == '__main__':
    main()