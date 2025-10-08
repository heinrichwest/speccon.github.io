#!/usr/bin/env python3
"""
Fix remaining qualification pages to use openEnquiryModal instead of openApplicationModal
"""

import os
import re
from pathlib import Path

def fix_modal_references(file_path):
    """Replace openApplicationModal with openEnquiryModal and related fixes"""

    print(f"Processing: {file_path.name}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Replace openApplicationModal with openEnquiryModal
    if 'openApplicationModal' in content:
        content = content.replace('openApplicationModal()', 'openEnquiryModal()')
        content = content.replace('closeApplicationModal()', 'closeEnquiryModal()')
        content = content.replace('application-modal', 'enquiry-modal')
        content = content.replace('applicationModal', 'enquiryModal')
        changes_made = True
        print(f"  [OK] Replaced application modal references with enquiry modal")

    # Check if function definitions need updating
    if 'function openApplicationModal' in content:
        content = re.sub(r'function openApplicationModal\(\)', 'function openEnquiryModal()', content)
        content = re.sub(r'function closeApplicationModal\(\)', 'function closeEnquiryModal()', content)
        changes_made = True
        print(f"  [OK] Updated function definitions")

    # Ensure modal ID is correct
    if 'id="application-modal"' in content:
        content = content.replace('id="application-modal"', 'id="enquiry-modal"')
        changes_made = True
        print(f"  [OK] Updated modal ID")

    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [DONE] File updated successfully!")
        return True
    else:
        print(f"  [INFO] No changes needed")
        return False

def main():
    base_dir = Path(r'C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master\qualifications')

    # Files identified as needing fixes
    files_to_fix = [
        'etdp-hr-management-nqf4.html',
        'etdp-training-development-nqf3.html',
        'fasset-computer-technician-nqf5.html',
        'merseta-automotive-sales-advisor-nqf4.html'
    ]

    total_updated = 0

    print("=" * 60)
    print("Fixing remaining qualification modal references")
    print("=" * 60)

    for filename in files_to_fix:
        file_path = base_dir / filename
        if file_path.exists():
            if fix_modal_references(file_path):
                total_updated += 1
        else:
            print(f"[WARNING] File not found: {filename}")

    print("\n" + "=" * 60)
    print(f"Update complete! {total_updated} files were modified.")
    print("=" * 60)

if __name__ == '__main__':
    main()