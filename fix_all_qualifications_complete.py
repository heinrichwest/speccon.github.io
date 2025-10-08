#!/usr/bin/env python3
"""
Complete fix for all qualification pages:
1. Ensure all text on #12265E and #92abc4 backgrounds is white
2. Update all button colors to #12265E with #92abc4 hover
"""

import os
import re
import glob

# Get all qualification HTML files
qualification_files = glob.glob('qualifications/*.html')

print(f"Found {len(qualification_files)} qualification files to process\n")

for file_path in qualification_files:
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # ===== FIX TEXT COLORS =====

    # Fix any remaining text-gray variations globally
    content = re.sub(r'text-gray-\d+', r'text-white', content)

    # Fix text-blue, text-indigo, text-purple variations
    content = re.sub(r'text-(blue|indigo|purple|red|green|yellow|orange|pink|teal|cyan)-\d+', r'text-white', content)

    # Fix text-white/90 or text-white/80 to text-white
    content = re.sub(r'text-white/\d+', r'text-white', content)

    # Ensure headers in module containers are white
    content = re.sub(
        r'(<div class="(?:bg-\[#12265E\]|bg-\[#92abc4\])[^>]*>.*?)<h[1-6] class="([^"]*?)text-gray-\d+',
        r'\1<h\2 class="\2text-white',
        content,
        flags=re.DOTALL
    )

    # Ensure paragraph text in module containers is white
    content = re.sub(
        r'(<div class="(?:bg-\[#12265E\]|bg-\[#92abc4\])[^>]*>.*?)<p class="([^"]*?)text-gray-\d+',
        r'\1<p class="\2text-white',
        content,
        flags=re.DOTALL
    )

    # Ensure list text in module containers is white
    content = re.sub(
        r'(<div class="(?:bg-\[#12265E\]|bg-\[#92abc4\])[^>]*>.*?)<ul class="([^"]*?)text-gray-\d+',
        r'\1<ul class="\2text-white',
        content,
        flags=re.DOTALL
    )

    content = re.sub(
        r'(<div class="(?:bg-\[#12265E\]|bg-\[#92abc4\])[^>]*>.*?)<li class="([^"]*?)text-gray-\d+',
        r'\1<li class="\2text-white',
        content,
        flags=re.DOTALL
    )

    # ===== FIX BUTTON COLORS =====

    # Fix gradient buttons to solid SpecCon colors
    # Pattern 1: bg-gradient-to-r from-X-600 to-Y-600
    content = re.sub(
        r'bg-gradient-to-r from-\w+-\d+ to-\w+-\d+',
        r'bg-[#12265E]',
        content
    )

    # Pattern 2: Any bg-blue-600, bg-purple-600, bg-indigo-600 etc on buttons
    content = re.sub(
        r'(<(?:button|a)[^>]*class="[^"]*?)bg-(blue|purple|indigo|green|red|yellow|orange|pink|teal|cyan)-\d+',
        r'\1bg-[#12265E]',
        content
    )

    # Fix hover states on buttons
    # Replace hover:bg-X-700, hover:from-X-700, etc.
    content = re.sub(
        r'hover:(?:bg-|from-|to-)\w+-\d+',
        r'hover:bg-[#92abc4]',
        content
    )

    # Ensure "Apply for This Qualification" buttons use correct colors
    content = re.sub(
        r'(<a[^>]*?Apply for This Qualification[^>]*?class="[^"]*?)bg-\[#\w+\]([^"]*?)hover:bg-\[#\w+\]',
        r'\1bg-[#12265E]\2hover:bg-[#92abc4]',
        content
    )

    # Fix any "Enquire Now" or "Contact Us" buttons
    content = re.sub(
        r'(<(?:button|a)[^>]*?(?:Enquire|Contact|Apply|Book)[^>]*?class="[^"]*?)bg-\w+-\d+([^"]*?)hover:bg-\w+-\d+',
        r'\1bg-[#12265E]\2hover:bg-[#92abc4]',
        content
    )

    # Specific pattern for buttons with multiple hover states
    content = re.sub(
        r'hover:bg-gradient-to-r hover:from-\w+-\d+ hover:to-\w+-\d+',
        r'hover:bg-[#92abc4]',
        content
    )

    # Fix focus states on buttons
    content = re.sub(
        r'focus:ring-\w+-\d+',
        r'focus:ring-[#12265E]',
        content
    )

    # ===== FIX ANY COLORED BACKGROUNDS IN MODULES =====

    # Replace any remaining bg-color-50 patterns with #12265E
    content = re.sub(
        r'bg-(red|green|blue|yellow|orange|purple|pink|indigo|teal|cyan)-\d+',
        r'bg-[#12265E]',
        content
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {file_path}\n")
    else:
        print(f"[-] No changes needed for {file_path}\n")

print("\n[OK] All qualification pages processed!")
print("Summary:")
print("- Fixed all text colors on #12265E and #92abc4 backgrounds to white")
print("- Updated all button colors to #12265E with #92abc4 hover")
print("- Removed gradient backgrounds and non-brand colors")
