#!/usr/bin/env python3
"""Fix W&R SETA qualification pages - Core Modules backgrounds, text colors, and button colors"""

import os
import re

# List of files to fix
files_to_fix = [
    'qualifications/wr-service-station-assistant-nqf2.html',
    'qualifications/wr-store-person-nqf2.html',
    'qualifications/wr-retail-operations-nqf2.html',
    'qualifications/wr-sales-assistant-nqf3.html',
    'qualifications/wr-sales-marketing-nqf3.html',
    'qualifications/wr-retail-buyer-nqf5.html'
]

print(f"Found {len(files_to_fix)} W&R SETA qualification files to fix\n")

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        print(f"[SKIP] File not found: {file_path}")
        continue

    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix all module containers with bg-[#12265E] and gradients
    content = re.sub(
        r'<div class="bg-\[#12265E\] bg-gradient-to-r from-\w+-\d+ to-\w+-\d+ p-6 rounded-xl">',
        r'<div class="bg-[#12265E] p-6 rounded-xl">',
        content
    )

    # Handle bg-gradient-to-br variants
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

    # Handle bg-gradient-to-br variants
    content = re.sub(
        r'<div class="bg-gradient-to-br from-\[#92abc4\] to-\[#12265E\] p-6 rounded-xl">',
        r'<div class="bg-[#92abc4] p-6 rounded-xl">',
        content
    )

    # Fix text colors - change text-[#12265E] to text-white in module h4 tags
    content = re.sub(
        r'(<div class="bg-\[#12265E\] p-6 rounded-xl">)\s*<h4 class="(font-bold text-lg text-\[#12265E\]|text-\[#12265E\] font-bold text-lg)',
        r'\1\n                            <h4 class="text-white font-bold text-lg',
        content
    )

    content = re.sub(
        r'(<div class="bg-\[#92abc4\] p-6 rounded-xl">)\s*<h4 class="(font-bold text-lg text-\[#12265E\]|text-\[#12265E\] font-bold text-lg)',
        r'\1\n                            <h4 class="text-white font-bold text-lg',
        content
    )

    # Fix text colors - change text-gray-600 to text-white in module paragraphs
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

    # Fix ul text colors - change text-gray-700 to text-white in module lists
    content = re.sub(
        r'(<div class="rounded-xl p-6 bg-\[#12265E\]">.*?)<ul class="space-y-2 text-gray-700">',
        r'\1<ul class="space-y-2 text-white">',
        content,
        flags=re.DOTALL
    )

    content = re.sub(
        r'(<div class="rounded-xl p-6 bg-\[#92abc4\]">.*?)<ul class="space-y-2 text-gray-700">',
        r'\1<ul class="space-y-2 text-white">',
        content,
        flags=re.DOTALL
    )

    # Fix h3 text colors in Learning Modules sections
    content = re.sub(
        r'(<div class="rounded-xl p-6 bg-\[#92abc4\]">)\s*<h3 class="text-xl font-semibold text-\[#12265E\]',
        r'\1\n                                <h3 class="text-xl font-semibold text-white',
        content
    )

    # Fix "Apply for This Qualification" button colors
    # Pattern: bg-gradient-to-r from-blue-600 to-purple-600 ... hover:from-blue-700 hover:to-purple-700
    content = re.sub(
        r'<button onclick="openEnquiryModal\(\)" class="bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold py-3 px-8 rounded-lg hover:from-blue-700 hover:to-purple-700 transition duration-300 shadow-lg">\s*Apply for This Qualification\s*</button>',
        r'<button onclick="openEnquiryModal()" class="bg-[#12265E] text-white font-bold py-3 px-8 rounded-lg hover:bg-[#92abc4] transition duration-300 shadow-lg">\n                            Apply for This Qualification\n                        </button>',
        content,
        flags=re.DOTALL
    )

    # Also handle variations with different spacing
    content = re.sub(
        r'<button onclick="openEnquiryModal\(\)" class="bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold py-4 px-8 rounded-lg hover:from-blue-700 hover:to-purple-700 transition duration-300 shadow-lg">\s*Apply for This Qualification\s*</button>',
        r'<button onclick="openEnquiryModal()" class="bg-[#12265E] text-white font-bold py-4 px-8 rounded-lg hover:bg-[#92abc4] transition duration-300 shadow-lg">\n                            Apply for This Qualification\n                        </button>',
        content,
        flags=re.DOTALL
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {file_path}\n")
    else:
        print(f"[-] No changes needed for {file_path}\n")

print("[OK] All W&R SETA qualification pages processed!")
