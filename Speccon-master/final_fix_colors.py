#!/usr/bin/env python3
"""
Final cleanup to fix double quotes and other issues
"""
import os
import re
from pathlib import Path

def final_fix(file_path):
    """Final fixes for a single HTML file"""
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    fixes_made = []

    # Fix double quotes like text-[#ffa600]">">
    content = content.replace('text-[#ffa600]">">', 'text-[#ffa600]">')
    if original_content != content:
        fixes_made.append('Fixed double quotes')

    # Fix malformed div tags like: >"\n or >">
    content = re.sub(r'>\s*"\s*>\s*', '>', content)
    content = re.sub(r'>\s*"\s*', '>', content)

    # Fix broken div closings with missing >
    content = re.sub(r'(bg-\[#ffffff\]/70 rounded-2xl flex items-center justify-center mx-auto mb-6)>\s*\n', r'\1">\n', content)

    # Fix text-[#ffa600]"> mb-8"> patterns
    content = re.sub(r'text-\[#ffa600\]"\s*>\s*"\s*([^>]+)>', r'text-[#ffa600]" \1>', content)

    # Fix text-[#ffa600]"> max-w-3xl patterns
    content = re.sub(r'text-\[#ffa600\]"\s*>\s*([a-z-]+)>', r'text-[#ffa600]" \1>', content)

    # Only write if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [FIXED]")
        return True
    else:
        print(f"  [OK]")
        return False

def main():
    """Main function to fix all short course files"""
    script_dir = Path(__file__).parent
    short_courses_dir = script_dir / "short-courses"

    if not short_courses_dir.exists():
        print(f"Error: Directory not found: {short_courses_dir}")
        return

    print("=== Final Cleanup of Short Course HTML Files ===\n")

    # Get all HTML files in short-courses directory
    html_files = list(short_courses_dir.glob("*.html"))

    if not html_files:
        print("No HTML files found in short-courses directory")
        return

    fixed_count = 0

    for html_file in sorted(html_files):
        if final_fix(html_file):
            fixed_count += 1

    print(f"\n=== Summary ===")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files needing final fixes: {fixed_count}")
    print(f"\n[SUCCESS] All fixes complete!")

if __name__ == "__main__":
    main()
