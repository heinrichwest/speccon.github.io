#!/usr/bin/env python3
"""
Update all short course HTML files to use standardized SpecCon color scheme
"""
import os
import re
from pathlib import Path

# Color mappings from old colors to new SpecCon standard colors
COLOR_REPLACEMENTS = [
    # Header subtitle colors
    (r'text-gray-600">(Services SETA|[^<]*)</p>', r'text-[#ffa600]\1</p>'),
    (r'text-sm text-gray-600">Services SETA', r'text-sm text-[#ffa600]">Services SETA'),

    # Main title colors in headers
    (r'text-gray-900">SpecCon Holdings', r'text-[#12265E]">SpecCon Holdings'),
    (r'text-gray-800">([^<]+)</h1>', r'text-[#12265E]">\1</h1>'),

    # Section titles
    (r'text-3xl.*?font-bold text-gray-[89]00', r'text-3xl md:text-4xl font-bold text-[#12265E]'),
    (r'text-2xl.*?font-bold text-gray-900', r'text-2xl font-bold text-[#12265E]'),
    (r'text-xl.*?font-bold text-gray-900', r'text-xl font-bold text-[#12265E]'),
    (r'text-lg font-bold text-gray-900', r'text-lg font-bold text-[#12265E]'),
    (r'text-lg font-semibold text-gray-900', r'text-lg font-semibold text-[#12265E]'),
    (r'font-semibold text-gray-900', r'font-semibold text-[#12265E]'),

    # Subtitle/secondary text colors
    (r'text-xl text-gray-600', r'text-xl text-[#ffa600]'),

    # Stats boxes - emerald/green to SpecCon colors
    (r'bg-emerald-[56]00/20', r'bg-[#ffa600]/20'),
    (r'text-emerald-1', r'text-white'),
    (r'bg-purple-[56]00/20', r'bg-[#ffa600]/20'),
    (r'text-purple-1', r'text-white'),
    (r'bg-cyan-[56]00/20', r'bg-[#ffa600]/20'),
    (r'text-cyan-1', r'text-white'),

    # Button gradients - convert all to SpecCon gradient
    (r'bg-gradient-to-r from-emerald-[56]00 to-emerald-[67]00', r'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
    (r'hover:from-emerald-[67]00 hover:to-emerald-[78]00', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]'),
    (r'bg-gradient-to-r from-purple-[56]00 to-purple-[67]00', r'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
    (r'hover:from-purple-[67]00 hover:to-purple-[78]00', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]'),
    (r'bg-gradient-to-r from-cyan-[56]00 to-cyan-[67]00', r'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
    (r'hover:from-cyan-[67]00 hover:to-cyan-[78]00', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]'),
    (r'bg-gradient-to-r from-cyan-600 to-indigo-700', r'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),

    # Hero section backgrounds
    (r'bg-gradient-to-br from-emerald-600 via-emerald-700 to-emerald-800', r'bg-gradient-to-br from-[#12265E] via-[#92abc4] to-[#12265E]'),
    (r'bg-gradient-to-br from-purple-600 via-purple-700 to-purple-800', r'bg-gradient-to-br from-[#12265E] via-[#92abc4] to-[#12265E]'),
    (r'bg-gradient-to-br from-cyan-600 via-cyan-700 to-indigo-800', r'bg-gradient-to-br from-[#12265E] via-[#92abc4] to-[#12265E]'),

    # Icon backgrounds - convert to white/70 with orange icons
    (r'bg-emerald-100 rounded-2xl flex items-center justify-center.*?\n.*?<i data-lucide="([^"]+)" class="w-8 h-8 text-emerald-600"',
     r'bg-[#ffffff]/70 rounded-2xl flex items-center justify-center\n                        <i data-lucide="\1" class="w-8 h-8 text-[#ffa600]"'),
    (r'bg-purple-100 rounded-2xl flex items-center justify-center.*?\n.*?<i data-lucide="([^"]+)" class="w-8 h-8 text-purple-600"',
     r'bg-[#ffffff]/70 rounded-2xl flex items-center justify-center\n                        <i data-lucide="\1" class="w-8 h-8 text-[#ffa600]"'),
    (r'bg-cyan-100 rounded-2xl flex items-center justify-center.*?\n.*?<i data-lucide="([^"]+)" class="w-8 h-8 text-cyan-600"',
     r'bg-[#ffffff]/70 rounded-2xl flex items-center justify-center\n                        <i data-lucide="\1" class="w-8 h-8 text-[#ffa600]"'),
    (r'bg-indigo-100 rounded-2xl flex items-center justify-center.*?\n.*?<i data-lucide="([^"]+)" class="w-8 h-8 text-indigo-600"',
     r'bg-[#ffffff]/70 rounded-2xl flex items-center justify-center\n                        <i data-lucide="\1" class="w-8 h-8 text-[#ffa600]"'),

    # Icon colors in smaller contexts
    (r'text-emerald-600"', r'text-[#ffa600]"'),
    (r'text-purple-600"', r'text-[#ffa600]"'),
    (r'text-cyan-600"', r'text-[#ffa600]"'),
    (r'text-indigo-600"', r'text-[#ffa600]"'),

    # Button text colors
    (r'text-emerald-600 font-bold', r'text-[#ffa600] font-bold'),
    (r'text-purple-600 font-bold', r'text-[#ffa600] font-bold'),
    (r'text-cyan-600 font-bold', r'text-[#ffa600] font-bold'),
    (r'hover:text-emerald-600', r'hover:text-[#ffa600]'),
    (r'hover:text-purple-600', r'hover:text-[#ffa600]'),
    (r'hover:text-cyan-600', r'hover:text-[#ffa600]'),

    # Background colors for icon containers (rounded-full)
    (r'bg-emerald-100 rounded-full', r'bg-[#ffffff]/70 rounded-full'),
    (r'bg-purple-100 rounded-full', r'bg-[#ffffff]/70 rounded-full'),
    (r'bg-cyan-100 rounded-full', r'bg-[#ffffff]/70 rounded-full'),
    (r'bg-indigo-100 rounded-full', r'bg-[#ffffff]/70 rounded-full'),
    (r'bg-blue-100 rounded-full', r'bg-[#ffffff]/70 rounded-full'),
    (r'bg-green-100 rounded-full', r'bg-[#ffffff]/70 rounded-full'),
    (r'bg-orange-100 rounded-full', r'bg-[#ffffff]/70 rounded-full'),

    # Border color for special cards
    (r'border-2 border-emerald-500', r'border-2 border-[#12265E]'),
    (r'border-2 border-purple-500', r'border-2 border-[#12265E]'),
    (r'border-2 border-indigo-500', r'border-2 border-[#12265E]'),

    # Badge colors
    (r'bg-emerald-500 text-white', r'bg-[#ffa600] text-white'),
    (r'bg-indigo-500 text-white', r'bg-[#ffa600] text-white'),

    # Duration/stat text colors
    (r'text-sm text-emerald-600', r'text-sm text-[#ffa600]'),
    (r'text-sm text-purple-600', r'text-sm text-[#ffa600]'),
    (r'text-sm text-cyan-600', r'text-sm text-[#ffa600]'),
    (r'text-sm text-indigo-600', r'text-sm text-[#ffa600]'),

    # CTA section backgrounds
    (r'bg-gradient-to-r from-emerald-600 to-emerald-700', r'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
    (r'bg-gradient-to-r from-purple-600 to-purple-700', r'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),
    (r'bg-gradient-to-r from-cyan-600 to-indigo-700', r'bg-gradient-to-r from-[#12265E] to-[#92ABC4]'),

    # Text colors in hero sections
    (r'text-emerald-100', r'text-[#ffa600]'),
    (r'text-purple-100', r'text-[#ffa600]'),
    (r'text-cyan-100', r'text-[#ffa600]'),

    # Icon backgrounds with specific patterns
    (r'bg-white/20', r'bg-[#ffffff]/70'),
]

def update_file(file_path):
    """Update a single HTML file with color replacements"""
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = 0

    # Apply all color replacements
    for pattern, replacement in COLOR_REPLACEMENTS:
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            changes_made += 1
        content = new_content

    # Only write if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] Updated with {changes_made} pattern(s) modified")
        return True
    else:
        print(f"  [SKIP] No changes needed")
        return False

def main():
    """Main function to update all short course files"""
    script_dir = Path(__file__).parent
    short_courses_dir = script_dir / "short-courses"

    if not short_courses_dir.exists():
        print(f"Error: Directory not found: {short_courses_dir}")
        return

    print("=== Updating Short Course HTML Files with SpecCon Color Scheme ===\n")

    # Get all HTML files in short-courses directory
    html_files = list(short_courses_dir.glob("*.html"))

    if not html_files:
        print("No HTML files found in short-courses directory")
        return

    updated_count = 0
    skipped_count = 0

    for html_file in sorted(html_files):
        if update_file(html_file):
            updated_count += 1
        else:
            skipped_count += 1

    print(f"\n=== Summary ===")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files updated: {updated_count}")
    print(f"Files skipped (no changes): {skipped_count}")
    print(f"\n[SUCCESS] Color standardization complete!")

if __name__ == "__main__":
    main()
