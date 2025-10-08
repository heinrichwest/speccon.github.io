#!/usr/bin/env python3
"""
Fix Book Training buttons on all short course pages - Apply SpecCon brand colors
"""

import os
import re
import glob

# Get all short course HTML files
short_course_files = glob.glob('short-courses/*.html')

print(f"Found {len(short_course_files)} short course files to process\n")

for file_path in short_course_files:
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # ===== FIX BOOK TRAINING BUTTONS =====

    # Pattern 1: Various color gradients in Book Training buttons
    patterns = [
        # Green variations
        (r'(Book Training.*?(?:class=|onclick=)[^>]*?)bg-gradient-to-r from-green-500 to-green-600', r'\1bg-gradient-to-r from-[#12265E] to-[#92abc4]'),
        (r'(Book Training.*?)hover:from-green-600 hover:to-green-700', r'\1hover:from-[#0d1a47] hover:to-[#3a7bc8]'),

        # Blue variations
        (r'(Book Training.*?(?:class=|onclick=)[^>]*?)bg-gradient-to-r from-blue-500 to-blue-600', r'\1bg-gradient-to-r from-[#12265E] to-[#92abc4]'),
        (r'(Book Training.*?)hover:from-blue-600 hover:to-blue-700', r'\1hover:from-[#0d1a47] hover:to-[#3a7bc8]'),

        # Orange/Red variations
        (r'(Book Training.*?(?:class=|onclick=)[^>]*?)bg-gradient-to-r from-orange-500 to-orange-600', r'\1bg-gradient-to-r from-[#12265E] to-[#92abc4]'),
        (r'(Book Training.*?)hover:from-orange-600 hover:to-orange-700', r'\1hover:from-[#0d1a47] hover:to-[#3a7bc8]'),
        (r'(Book Training.*?(?:class=|onclick=)[^>]*?)bg-gradient-to-r from-red-500 to-red-600', r'\1bg-gradient-to-r from-[#12265E] to-[#92abc4]'),
        (r'(Book Training.*?)hover:from-red-600 hover:to-red-700', r'\1hover:from-[#0d1a47] hover:to-[#3a7bc8]'),

        # Purple variations
        (r'(Book Training.*?(?:class=|onclick=)[^>]*?)bg-gradient-to-r from-purple-500 to-purple-600', r'\1bg-gradient-to-r from-[#12265E] to-[#92abc4]'),
        (r'(Book Training.*?)hover:from-purple-600 hover:to-purple-700', r'\1hover:from-[#0d1a47] hover:to-[#3a7bc8]'),

        # Teal variations
        (r'(Book Training.*?(?:class=|onclick=)[^>]*?)bg-gradient-to-r from-teal-500 to-teal-600', r'\1bg-gradient-to-r from-[#12265E] to-[#92abc4]'),
        (r'(Book Training.*?)hover:from-teal-600 hover:to-teal-700', r'\1hover:from-[#0d1a47] hover:to-[#3a7bc8]'),

        # Yellow variations
        (r'(Book Training.*?(?:class=|onclick=)[^>]*?)bg-gradient-to-r from-yellow-500 to-yellow-600', r'\1bg-gradient-to-r from-[#12265E] to-[#92abc4]'),
        (r'(Book Training.*?)hover:from-yellow-600 hover:to-yellow-700', r'\1hover:from-[#0d1a47] hover:to-[#3a7bc8]'),
    ]

    # Apply all patterns
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Alternative approach: Find button elements with "Book Training" text and update their colors
    # This handles buttons that might be formatted differently

    # Find all occurrences of Book Training buttons and fix gradient colors
    content = re.sub(
        r'(<button[^>]*Book Training[^>]*class="[^"]*?)bg-gradient-to-r from-(?:green|blue|orange|red|purple|teal|yellow|indigo|pink)-\d+ to-(?:green|blue|orange|red|purple|teal|yellow|indigo|pink)-\d+',
        r'\1bg-gradient-to-r from-[#12265E] to-[#92abc4]',
        content,
        flags=re.IGNORECASE
    )

    # Fix hover states for Book Training buttons
    content = re.sub(
        r'(Book Training[^>]*?class="[^"]*?)hover:from-(?:green|blue|orange|red|purple|teal|yellow|indigo|pink)-\d+ hover:to-(?:green|blue|orange|red|purple|teal|yellow|indigo|pink)-\d+',
        r'\1hover:from-[#0d1a47] hover:to-[#3a7bc8]',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Also fix solid color Book Training buttons
    content = re.sub(
        r'(<button[^>]*Book Training[^>]*class="[^"]*?)bg-(?:green|blue|orange|red|purple|teal|yellow|indigo|pink)-(?:500|600)',
        r'\1bg-[#12265E]',
        content,
        flags=re.IGNORECASE
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {file_path}\n")
    else:
        print(f"[-] No changes needed for {file_path}\n")

print("\n[OK] All short course Book Training buttons processed!")
print("Summary:")
print("- Updated all Book Training buttons to use #12265E to #92abc4 gradient")
print("- Fixed hover states to use #0d1a47 to #3a7bc8")
print("- Standardized button colors across all short course pages")
