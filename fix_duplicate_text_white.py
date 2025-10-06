#!/usr/bin/env python3
"""
Fix duplicate text-white classes in footer tags
"""

import os
import re
from pathlib import Path

def fix_duplicate_classes(content):
    """Remove duplicate text-white classes."""
    # Fix duplicate text-white in footer tag
    content = re.sub(r'text-white text-white', 'text-white', content)
    return content

def process_file(file_path):
    """Process a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix duplicates
        updated_content = fix_duplicate_classes(content)

        # Write back only if changed
        if content != updated_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all HTML files."""
    base_dir = Path(r"C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master")
    html_files = list(base_dir.glob("**/*.html"))

    fixed = 0
    for file_path in html_files:
        if process_file(file_path):
            fixed += 1

    print(f"Fixed {fixed} files with duplicate text-white classes")

if __name__ == "__main__":
    main()