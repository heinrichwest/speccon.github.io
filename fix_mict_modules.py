#!/usr/bin/env python3
"""Fix MICT SETA qualification pages - Core Modules backgrounds and text colors"""

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

    # Fix all module containers with bg-[#12265E]
    # Pattern: bg-[#12265E] bg-gradient-to-r from-*-50 to-*-50
    content = re.sub(
        r'<div class="bg-\[#12265E\] bg-gradient-to-r from-\w+-\d+ to-\w+-\d+ p-6 rounded-xl">',
        r'<div class="bg-[#12265E] p-6 rounded-xl">',
        content
    )

    # Fix all module containers with bg-[#92abc4]
    content = re.sub(
        r'<div class="bg-\[#92abc4\] bg-gradient-to-r from-\w+-\d+ to-\w+-\d+ p-6 rounded-xl">',
        r'<div class="bg-[#92abc4] p-6 rounded-xl">',
        content
    )

    # Fix text colors in modules with bg-[#12265E] - should be white
    # Find all h4 tags with text-white after bg-[#12265E] and ensure they stay white
    # Find all ul tags with text-white/90 after bg-[#12265E] and make them white
    content = re.sub(
        r'(<div class="bg-\[#12265E\] p-6 rounded-xl">)\s*<h4 class="text-\[#12265E\]',
        r'\1\n<h4 class="text-white',
        content
    )

    # Fix ul text colors for bg-[#12265E] containers
    content = re.sub(
        r'(<div class="bg-\[#12265E\] p-6 rounded-xl">.*?<h4 class="text-white.*?</h4>)\s*<ul class="space-y-2 text-sm text-\[#12265E\]',
        r'\1\n                            <ul class="space-y-2 text-sm text-white',
        content,
        flags=re.DOTALL
    )

    # Fix text colors in modules with bg-[#92abc4] - should be white
    content = re.sub(
        r'(<div class="bg-\[#92abc4\] p-6 rounded-xl">)\s*<h4 class="text-\[#12265E\]',
        r'\1\n<h4 class="text-white',
        content
    )

    # Fix ul text colors for bg-[#92abc4] containers
    content = re.sub(
        r'(<div class="bg-\[#92abc4\] p-6 rounded-xl">.*?<h4 class="text-white.*?</h4>)\s*<ul class="space-y-2 text-sm text-white/90',
        r'\1\n                            <ul class="space-y-2 text-sm text-white',
        content,
        flags=re.DOTALL
    )

    # Fix text-white/90 to text-white for better visibility
    content = re.sub(
        r'text-white/90',
        r'text-white',
        content
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {file_path}")
    else:
        print(f"[-] No changes needed for {file_path}")

print("\n[OK] All MICT qualification pages processed!")
