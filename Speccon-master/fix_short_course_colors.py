#!/usr/bin/env python3
"""
Fix remaining color issues from the automated update
"""
import os
import re
from pathlib import Path

def fix_file(file_path):
    """Fix specific issues in a single HTML file"""
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    fixes_made = []

    # Fix "text-white00" (should be "text-[#ffa600]")
    if 'text-white00' in content:
        content = content.replace('text-white00', 'text-[#ffa600]')
        fixes_made.append('Fixed text-white00')

    # Fix missing closing bracket in subtitle color
    pattern = r'text-\[#ffa600\](Services SETA|[^<]*)</p>'
    if re.search(pattern, content):
        content = re.sub(pattern, r'text-[#ffa600]">\1</p>', content)
        fixes_made.append('Fixed missing quote in subtitle')

    # Fix broken icon container divs (missing closing >)
    pattern = r'bg-\[#ffffff\]/70 rounded-2xl flex items-center justify-center\s*\n\s*<i data-lucide'
    if re.search(pattern, content):
        content = re.sub(pattern, r'bg-[#ffffff]/70 rounded-2xl flex items-center justify-center mx-auto mb-6>\n                        <i data-lucide', content)
        fixes_made.append('Fixed icon container')

    # Fix broken icon container divs (rounded-full variant)
    pattern = r'bg-\[#ffffff\]/70 rounded-full flex items-center justify-center\s*\n\s*<i data-lucide'
    if re.search(pattern, content):
        content = re.sub(pattern, r'bg-[#ffffff]/70 rounded-full flex items-center justify-center mx-auto mb-4>\n                            <i data-lucide', content)
        fixes_made.append('Fixed rounded-full icon container')

    # Fix missing > in p tags with text-xl text-[#ffa600]
    pattern = r'text-xl text-\[#ffa600\]([^<]+)</p>'
    if re.search(pattern, content):
        content = re.sub(pattern, r'text-xl text-[#ffa600]">\1</p>', content)
        fixes_made.append('Fixed missing quote in xl text')

    # Fix modal title colors
    if 'text-2xl font-bold text-gray-900">Book This Training' in content:
        content = content.replace('text-2xl font-bold text-gray-900">Book This Training', 'text-2xl font-bold text-[#12265E]">Book This Training')
        fixes_made.append('Fixed modal title color')

    # Fix any remaining purple-600 in icon contexts (small icons in cards)
    content = re.sub(r'text-purple-600">', r'text-[#ffa600]">', content)

    # Only write if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [FIXED] {', '.join(fixes_made)}")
        return True
    else:
        print(f"  [OK] No issues found")
        return False

def main():
    """Main function to fix all short course files"""
    script_dir = Path(__file__).parent
    short_courses_dir = script_dir / "short-courses"

    if not short_courses_dir.exists():
        print(f"Error: Directory not found: {short_courses_dir}")
        return

    print("=== Fixing Remaining Color Issues in Short Course HTML Files ===\n")

    # Get all HTML files in short-courses directory
    html_files = list(short_courses_dir.glob("*.html"))

    if not html_files:
        print("No HTML files found in short-courses directory")
        return

    fixed_count = 0
    ok_count = 0

    for html_file in sorted(html_files):
        if fix_file(html_file):
            fixed_count += 1
        else:
            ok_count += 1

    print(f"\n=== Summary ===")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files fixed: {fixed_count}")
    print(f"Files already OK: {ok_count}")
    print(f"\n[SUCCESS] Cleanup complete!")

if __name__ == "__main__":
    main()
