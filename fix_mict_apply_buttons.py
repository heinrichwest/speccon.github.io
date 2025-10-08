#!/usr/bin/env python3
"""Fix MICT SETA qualification pages - Apply for This Qualification button colors"""

import os
import re
import glob

# Get all MICT qualification files
mict_files = glob.glob('qualifications/mict-*.html')

print(f"Found {len(mict_files)} MICT qualification files")

for file_path in mict_files:
    print(f"\nProcessing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix "Apply for This Qualification" button colors
    # Pattern: bg-gradient-to-r from-blue-600 to-purple-600 ... hover:from-blue-700 hover:to-purple-700
    content = re.sub(
        r'<button onclick="openEnquiryModal\(\)" class="bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold py-3 px-8 rounded-lg hover:from-blue-700 hover:to-purple-700 transition duration-300 shadow-lg">\s*Apply for This Qualification\s*</button>',
        r'<button onclick="openEnquiryModal()" class="bg-[#12265E] text-white font-bold py-3 px-8 rounded-lg hover:bg-[#92abc4] transition duration-300 shadow-lg">\n                            Apply for This Qualification\n                        </button>',
        content,
        flags=re.DOTALL
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {file_path}")
    else:
        print(f"[-] No changes needed for {file_path}")

print("\n[OK] All MICT qualification pages processed!")
