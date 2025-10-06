#!/usr/bin/env python3
"""
Fix remaining title updates in Services SETA pages
"""

import os
import re
import glob

def fix_title_section(content):
    """Fix the title section to match services-bookkeeper-nqf5.html"""

    # Pattern to find any title section with SpecCon
    patterns = [
        # Pattern for title and subtitle in the header
        r'(<div class="ml-3">.*?<h1[^>]*>)[^<]*(SpecCon[^<]*)(</h1>.*?<p[^>]*>)[^<]*(</p>)',
        # Alternative pattern
        r'(<h1[^>]*text-xl[^>]*>)[^<]*(SpecCon[^<]*)(</h1>.*?<p[^>]*text-sm[^>]*>)[^<]*(</p>)',
    ]

    for pattern in patterns:
        content = re.sub(
            pattern,
            r'\1SpecCon Holdings\3Services SETA Qualifications\4',
            content,
            flags=re.DOTALL
        )

    return content

def process_file(filepath):
    """Process a single file"""

    filename = os.path.basename(filepath)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has correct title
        if 'Services SETA Qualifications' in content:
            print(f"  [ALREADY UPDATED] {filename}")
            return True

        # Apply fix
        original_content = content
        content = fix_title_section(content)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [UPDATED] {filename}")
        else:
            print(f"  [NO CHANGES] {filename}")

        return True

    except Exception as e:
        print(f"  [ERROR] {filename}: {str(e)}")
        return False

def main():
    # List of files that need fixing
    files_to_fix = [
        'qualifications/services-customer-service-nqf2.html',
        'qualifications/services-marketing-coordinator-nqf5.html',
        'qualifications/services-new-venture-creation-nqf4.html',
        'qualifications/services-new-venture-creation-smme-nqf2.html',
        'qualifications/services-office-supervision-nqf5.html',
        'qualifications/services-project-manager-nqf5.html',
        'qualifications/services-quality-assurer-nqf5.html',
        'qualifications/services-quality-manager-nqf6.html'
    ]

    print(f"Processing {len(files_to_fix)} files...")
    print("-" * 50)

    success_count = 0
    for filepath in files_to_fix:
        if process_file(filepath):
            success_count += 1

    print("-" * 50)
    print(f"Successfully processed {success_count}/{len(files_to_fix)} files")

if __name__ == "__main__":
    main()