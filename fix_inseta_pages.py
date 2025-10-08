#!/usr/bin/env python3
"""Fix INSETA qualification pages - Core Modules backgrounds and text colors"""

import os
import re
import glob

# Get all INSETA qualification HTML files
inseta_files = glob.glob('qualifications/inseta-*.html')

print(f"Found {len(inseta_files)} INSETA qualification files to process\n")

for file_path in inseta_files:
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix text-gray-500 to text-white globally
    content = re.sub(
        r'text-gray-500',
        r'text-white',
        content
    )

    # Fix any remaining bg-red-50, bg-green-50, bg-blue-50, etc. to bg-[#12265E]
    content = re.sub(
        r'<div class="bg-(red|green|blue|yellow|orange|purple|pink|indigo|teal|cyan)-\d+ p-6 rounded-xl">',
        r'<div class="bg-[#12265E] p-6 rounded-xl">',
        content
    )

    # Fix text-gray-600 to text-white in paragraphs within module containers
    content = re.sub(
        r'(<div class="bg-\[#12265E\] p-6 rounded-xl">.*?)<p class="text-gray-600',
        r'\1<p class="text-white',
        content,
        flags=re.DOTALL
    )

    content = re.sub(
        r'(<div class="bg-\[#92abc4\] p-6 rounded-xl">.*?)<p class="text-gray-600',
        r'\1<p class="text-white',
        content,
        flags=re.DOTALL
    )

    # Fix h4 text colors to ensure they're white
    content = re.sub(
        r'(<div class="bg-\[#12265E\] p-6 rounded-xl">)\s*<h4 class="font-bold text-lg text-gray-900',
        r'\1\n                            <h4 class="font-bold text-lg text-white',
        content
    )

    content = re.sub(
        r'(<div class="bg-\[#92abc4\] p-6 rounded-xl">)\s*<h4 class="font-bold text-lg text-gray-900',
        r'\1\n                            <h4 class="font-bold text-lg text-white',
        content
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {file_path}\n")
    else:
        print(f"[-] No changes needed for {file_path}\n")

print("[OK] All INSETA qualification pages processed!")
