#!/usr/bin/env python3
"""
Fix W&R SETA qualification pages - Replace red and orange colors with #ffa600
"""

import os
import re
import glob

# Get all W&R SETA qualification HTML files (excluding the one we already fixed)
wr_files = [f for f in glob.glob('qualifications/wr-*.html') if 'wr-store-person-nqf2.html' not in f]

print(f"Found {len(wr_files)} W&R SETA qualification files to process\n")

for file_path in wr_files:
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # ===== FIX BACKGROUND COLORS =====

    # Hero section: from-orange-50 to from-[#ffa600]/10
    content = re.sub(r'from-orange-50', r'from-[#ffa600]/10', content)

    # Sidebar: bg-orange-50 to bg-[#ffa600]/10
    content = re.sub(r'bg-orange-50', r'bg-[#ffa600]/10', content)

    # ===== FIX BUTTON COLORS =====

    # Apply button: from-orange-600 to-red-600 gradient to solid #ffa600
    content = re.sub(
        r'bg-gradient-to-r from-orange-600 to-red-600',
        r'bg-[#ffa600]',
        content
    )

    # Apply button hover: hover:from-orange-700 hover:to-red-700
    content = re.sub(
        r'hover:from-orange-700 hover:to-red-700',
        r'hover:bg-[#ffa600]/90',
        content
    )

    # Get More Info button border: border-orange-600 to border-[#ffa600]
    content = re.sub(r'border-orange-600', r'border-[#ffa600]', content)

    # Get More Info button text: text-orange-600 to text-[#ffa600]
    content = re.sub(r'text-orange-600', r'text-[#ffa600]', content)

    # Get More Info button hover bg: hover:bg-orange-600
    content = re.sub(r'hover:bg-orange-600', r'hover:bg-[#ffa600]', content)

    # ===== FIX ICON AND TEXT COLORS =====

    # Checkmark icons: text-orange-500 to text-[#ffa600]
    content = re.sub(r'text-orange-500', r'text-[#ffa600]', content)

    # Other orange text variations
    content = re.sub(r'text-orange-400', r'text-[#ffa600]', content)
    content = re.sub(r'text-orange-700', r'text-[#ffa600]', content)

    # ===== FIX HOVER STATES =====

    # Hover border: hover:border-orange-300 to hover:border-[#ffa600]
    content = re.sub(r'hover:border-orange-300', r'hover:border-[#ffa600]', content)
    content = re.sub(r'hover:border-orange-200', r'hover:border-[#ffa600]', content)

    # Hover background: hover:bg-orange-50 to hover:bg-[#ffa600]/10
    content = re.sub(r'hover:bg-orange-50', r'hover:bg-[#ffa600]/10', content)

    # Hover text: hover:text-orange to hover:text-[#ffa600]
    content = re.sub(r'hover:text-orange(["\s])', r'hover:text-[#ffa600]\1', content)

    # ===== FIX CTA SECTION =====

    # CTA section gradient: from-orange-600 to-red-600 to from-[#12265E] to-[#92abc4]
    content = re.sub(
        r'bg-gradient-to-r from-orange-600 to-red-600',
        r'bg-gradient-to-r from-[#12265E] to-[#92abc4]',
        content
    )

    # ===== FIX RED COLORS =====

    # Replace any remaining red colors
    content = re.sub(r'text-red-600', r'text-[#ffa600]', content)
    content = re.sub(r'text-red-500', r'text-[#ffa600]', content)
    content = re.sub(r'border-red-600', r'border-[#ffa600]', content)
    content = re.sub(r'bg-red-600', r'bg-[#ffa600]', content)
    content = re.sub(r'from-red-600', r'from-[#ffa600]', content)
    content = re.sub(r'to-red-600', r'to-[#ffa600]', content)
    content = re.sub(r'hover:bg-red-700', r'hover:bg-[#ffa600]/90', content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {file_path}\n")
    else:
        print(f"[-] No changes needed for {file_path}\n")

print("\n[OK] All W&R SETA qualification pages processed!")
print("Summary:")
print("- Replaced all orange and red colors with #ffa600")
print("- Updated CTA sections to use #12265E to #92abc4 gradient")
print("- Fixed all buttons, icons, and hover states")
