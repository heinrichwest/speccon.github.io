#!/usr/bin/env python3
"""
Fix all qualification sidebar issues comprehensively.
This script ensures:
1. All sidebar content stays in one container
2. No sticky positioning
3. Proper structure for all elements
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

def fix_sidebar_comprehensive(content, filename):
    """Fix all sidebar issues in a qualification file."""

    # Pattern to find common broken structures with extra closing divs after qualification details
    # This happens when there's </div>\n</div> after the space-y-4 mb-8 section

    # Fix pattern 1: Extra closing div after qualification details fields
    pattern1 = r'(</div>\s*</div>\s*</div>\s*<div class="space-y-4)'
    content = re.sub(pattern1, r'</div>\n\n                        <div class="space-y-4', content, flags=re.DOTALL)

    # Fix pattern 2: Extra closing div between sections
    pattern2 = r'(</div>\s*</div>\s*<div class="mb-8 pb-8 border-b border-gray-100">)'
    content = re.sub(pattern2, r'</div>\n\n                        <div class="mb-8 pb-8 border-b border-gray-100">', content, flags=re.DOTALL)

    # Fix pattern 3: Career Opportunities outside container
    pattern3 = r'(</div>\s*</div>\s*</div>\s*<!-- Career Opportunities -->)'
    content = re.sub(pattern3, r'</div>\n\n                    <!-- Career Opportunities -->', content, flags=re.DOTALL)

    # Fix pattern 4: Fix broken structure after qualification details
    pattern4 = r'(</div>\s*</div>\s*<div class="space-y-4 mb-8">)'
    content = re.sub(pattern4, r'</div>\n\n                        <div class="space-y-4 mb-8">', content, flags=re.DOTALL)

    # Remove sticky positioning if present
    pattern_sticky = r'(<div class="bg-white border border-gray-200 rounded-2xl[^"]*p-8)(\s+sticky top-\d+)([^>]*>)'
    content = re.sub(pattern_sticky, r'\1\3', content)

    # Alternative sticky removal
    pattern_sticky2 = r'sticky top-24'
    content = re.sub(pattern_sticky2, '', content)

    return content

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
            print(f"Processing: {filename}")

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Apply comprehensive fixes
            new_content = fix_sidebar_comprehensive(content, filename)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  [FIXED]: {filename}")
                fixed += 1
            else:
                print(f"  [-] No changes needed: {filename}")

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