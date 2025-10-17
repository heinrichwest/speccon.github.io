#!/usr/bin/env python3
"""
Remove sticky positioning from all qualification sidebars.
Changes 'sticky top-24' to just normal positioning so sidebars scroll with the page.
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

def remove_sticky(content, filename):
    """Remove sticky positioning from sidebar containers."""

    # Pattern to find sidebar container with sticky positioning
    # Looking for the sidebar div with sticky top-24
    pattern = r'(<div class="bg-white border border-gray-200 rounded-2xl shadow-lg p-8) sticky top-24(")'

    # Replace with non-sticky version
    new_content = re.sub(pattern, r'\1\2', content)

    # Alternative pattern for any variations
    pattern2 = r'(<div class="[^"]*rounded-2xl[^"]*p-8[^"]*) sticky top-\d+(")'
    new_content = re.sub(pattern2, r'\1\2', new_content)

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

            # Check if the file has sticky positioning
            if 'sticky top-' in content:
                # Remove sticky positioning
                new_content = remove_sticky(content, filename)

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  [FIXED]: {filename} - Removed sticky positioning")
                    fixed += 1
                else:
                    print(f"  [-] Could not remove sticky: {filename}")
            else:
                print(f"  [-] No sticky positioning found: {filename}")

        except Exception as e:
            print(f"  [ERROR]: {filename} - {e}")
            errors += 1

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Fixed: {fixed} files")
    print(f"  Skipped: {skipped} files")
    print(f"  Errors: {errors} files")
    print(f"  Total files: {len(files)}")

if __name__ == '__main__':
    main()