#!/usr/bin/env python3
"""
Fix duplicate button issues in qualification HTML files.
Removes buttons that are incorrectly placed INSIDE the stats grid.
"""

import os
import re
from pathlib import Path

# Files to skip (already fixed)
SKIP_FILES = {
    'agri-plant-production-nqf1.html',
    'wr-planner-nqf5.html',
    'wr-retail-buyer-nqf5.html',
    'wr-store-person-nqf2.html',
    'wr-retail-operations-nqf2.html',
    'wr-retail-supervisor-nqf4.html',
    'wr-retail-manager-nqf5.html',
    'wr-service-station-assistant-nqf2.html',
}

# All files found with the duplicate button pattern
FILES_TO_FIX = [
    'agri-plant-production-nqf1.html',  # Skip - already fixed
    'agri-animal-production-nqf1.html',
    'services-quality-manager-nqf6.html',
    'services-quality-assurer-nqf5.html',
    'services-project-manager-nqf5.html',
    'agri-farming-nqf1.html',
    'services-office-supervision-nqf5.html',
    'services-new-venture-creation-smme-nqf2.html',
    'services-new-venture-creation-nqf4.html',
    'services-marketing-coordinator-nqf5.html',
    'services-management-nqf3.html',
    'services-generic-management-nqf4.html',
    'agri-animal-production-nqf2.html',
    'services-customer-service-nqf2.html',
    'services-contact-centre-manager-nqf5.html',
    'services-bookkeeper-nqf5.html',
    'services-business-process-outsourcing-nqf3.html',
    'services-business-administration-nqf4.html',
    'services-business-administration-nqf3.html',
    'wr-retail-manager-nqf5.html',  # Skip - already fixed
    'wr-planner-nqf5.html',  # Skip - already fixed
    'wr-retail-buyer-nqf5.html',  # Skip - already fixed
    'wr-retail-supervisor-nqf4.html',  # Skip - already fixed
    'wr-store-person-nqf2.html',  # Skip - already fixed
    'wr-service-station-assistant-nqf2.html',  # Skip - already fixed
    'wr-visual-merchandiser-nqf3.html',
    'wr-sales-assistant-nqf3.html',
    'inseta-financial-advisor-nqf6.html',
    'etdp-education-training-nqf5.html',
    'agri-plant-production-nqf4.html',
    'agri-plant-production-nqf3.html',
    'agri-plant-production-nqf2.html',
    'agri-mixed-farming-nqf2.html',
    'agri-mixed-farming-nqf1.html',
    'agri-fruit-packaging-nqf3.html',
    'agri-farming-nqf2.html',
    'agri-animal-production-nqf4.html',
]

def fix_duplicate_buttons(file_path):
    """
    Fix duplicate button issue in a single HTML file.

    The issue: Buttons are placed INSIDE the stats grid between stat boxes.
    The fix: Remove the button section that's inside the grid, keeping only
    the button section that appears AFTER the grid closes.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern to match: stats grid start -> first stat -> WRONG buttons -> other stats -> grid end -> CORRECT buttons
    # We want to remove the WRONG buttons section

    # The problematic pattern is:
    # <div class="grid grid-cols-3 gap-4 mb-8">
    #     <div class="text-center p-4 bg-white rounded-lg shadow">...</div>
    #     <div class="flex flex-col sm:flex-row gap-4">  <!-- WRONG - inside grid! -->
    #         [buttons]
    #     </div>
    #     <div class="text-center p-4 bg-white rounded-lg shadow">...</div>
    #     <div class="text-center p-4 bg-white rounded-lg shadow">...</div>
    # </div>
    # <div class="flex flex-col sm:flex-row gap-4">  <!-- CORRECT - after grid -->

    # Strategy: Find the button div that appears INSIDE the grid (after first stat, before second stat)
    # and remove it, keeping the one that appears after the grid closes

    # Match pattern: credits stat box, then button section, then months stat box
    pattern = re.compile(
        r'(<div class="text-center p-4 bg-white rounded-lg shadow">\s*'
        r'<div class="text-xl font-bold[^>]*>[\d]+</div>\s*'
        r'<div class="text-sm text-gray-600">Credits</div>\s*'
        r'</div>)\s*'
        r'(<div class="flex flex-col sm:flex-row gap-4">.*?</div>)\s*'
        r'(<div class="text-center p-4 bg-white rounded-lg shadow">\s*'
        r'<div class="text-xl font-bold[^>]*>[\d\-]+</div>\s*'
        r'<div class="text-sm text-gray-600">Months</div>)',
        re.DOTALL
    )

    # Replace: keep credits stat, remove buttons, keep months stat
    content = pattern.sub(r'\1\n                        \3', content)

    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Main function to process all files."""
    base_dir = Path(r'C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master\qualifications')

    files_checked = 0
    files_fixed = 0
    files_skipped = 0
    errors = []

    print("Starting duplicate button fix process...\n")

    for filename in FILES_TO_FIX:
        files_checked += 1

        # Skip already-fixed files
        if filename in SKIP_FILES:
            print(f"SKIPPED (already fixed): {filename}")
            files_skipped += 1
            continue

        file_path = base_dir / filename

        if not file_path.exists():
            error_msg = f"File not found: {filename}"
            print(f"ERROR: {error_msg}")
            errors.append(error_msg)
            continue

        try:
            was_fixed = fix_duplicate_buttons(file_path)
            if was_fixed:
                print(f"FIXED: {filename}")
                files_fixed += 1
            else:
                print(f"NO CHANGE: {filename} (pattern not found or already correct)")
        except Exception as e:
            error_msg = f"Error processing {filename}: {str(e)}"
            print(f"ERROR: {error_msg}")
            errors.append(error_msg)

    # Print summary
    print("\n" + "="*70)
    print("SUMMARY REPORT")
    print("="*70)
    print(f"Total files checked: {files_checked}")
    print(f"Files skipped (already fixed): {files_skipped}")
    print(f"Files successfully fixed: {files_fixed}")
    print(f"Files with no changes: {files_checked - files_skipped - files_fixed - len(errors)}")
    print(f"Errors encountered: {len(errors)}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")

    print("\nDuplicate button fix process complete!")

if __name__ == '__main__':
    main()
