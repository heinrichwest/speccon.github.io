#!/usr/bin/env python3
"""Fix Services SETA qualification pages - Core Modules backgrounds and text colors"""

import os
import re

# List of files to fix
files_to_fix = [
    'qualifications/services-business-process-outsourcing-nqf3.html',
    'qualifications/services-contact-centre-manager-nqf5.html',
    'qualifications/services-management-nqf3.html',
    'qualifications/services-generic-management-nqf4.html',
    'qualifications/services-generic-management-nqf5.html',
    'qualifications/services-new-venture-creation-smme-nqf2.html',
    'qualifications/services-new-venture-creation-nqf4.html'
]

print(f"Found {len(files_to_fix)} Services SETA qualification files to fix\n")

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        print(f"[SKIP] File not found: {file_path}")
        continue

    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix all module containers with bg-[#12265E] and gradients
    # Pattern: bg-[#12265E] bg-gradient-to-r from-*-50 to-*-50
    content = re.sub(
        r'<div class="bg-\[#12265E\] bg-gradient-to-r from-\w+-\d+ to-\w+-\d+ p-6 rounded-xl">',
        r'<div class="bg-[#12265E] p-6 rounded-xl">',
        content
    )

    # Also handle bg-gradient-to-br variants
    content = re.sub(
        r'<div class="bg-gradient-to-br from-\[#12265E\] to-\[#92abc4\] p-6 rounded-xl">',
        r'<div class="bg-[#12265E] p-6 rounded-xl">',
        content
    )

    # Fix all module containers with bg-[#92abc4] and gradients
    content = re.sub(
        r'<div class="bg-\[#92abc4\] bg-gradient-to-r from-\w+-\d+ to-\w+-\d+ p-6 rounded-xl">',
        r'<div class="bg-[#92abc4] p-6 rounded-xl">',
        content
    )

    # Also handle bg-gradient-to-br variants
    content = re.sub(
        r'<div class="bg-gradient-to-br from-\[#92abc4\] to-\[#12265E\] p-6 rounded-xl">',
        r'<div class="bg-[#92abc4] p-6 rounded-xl">',
        content
    )

    # Fix text colors - change text-[#12265E] to text-white in module h4 tags
    content = re.sub(
        r'(<div class="bg-\[#12265E\] p-6 rounded-xl">)\s*<h4 class="text-\[#12265E\]',
        r'\1\n                            <h4 class="text-white',
        content
    )

    content = re.sub(
        r'(<div class="bg-\[#92abc4\] p-6 rounded-xl">)\s*<h4 class="text-\[#12265E\]',
        r'\1\n                            <h4 class="text-white',
        content
    )

    # Fix text colors - change text-gray-600 to text-white in module paragraphs/lists
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

    # Fix ul text colors - change text-white/90 to text-white
    content = re.sub(
        r'text-white/90',
        r'text-white',
        content
    )

    # Fix additional spacing issues - remove extra line breaks before <h4> tags
    content = re.sub(
        r'<div class="bg-\[#(12265E|92abc4)\] p-6 rounded-xl">\s+<h4',
        r'<div class="bg-[#\1] p-6 rounded-xl">\n                            <h4',
        content
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {file_path}\n")
    else:
        print(f"[-] No changes needed for {file_path}\n")

print("[OK] All Services SETA qualification pages processed!")
