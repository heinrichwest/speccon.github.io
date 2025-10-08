#!/usr/bin/env python3
"""
Add title sections to remaining Services SETA pages
"""

import os
import re

def add_title_section(content):
    """Add the title section if missing"""

    # Check if title section already exists
    if 'Services SETA Qualifications' in content:
        return content

    # Pattern to find the logo without title section
    pattern = r'(<div class="flex items-center justify-between">)\s*(<a href="[^"]*">\s*<img src="../images/Logo.png"[^>]*>\s*</a>)'

    replacement = r'''\1
                <div class="flex items-center">
                    \2
                    <div class="ml-3">
                        <h1 class="text-xl font-bold text-gray-900">SpecCon Holdings</h1>
                        <p class="text-sm text-gray-600">Services SETA Qualifications</p>
                    </div>
                </div>'''

    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Also update the home.html references to index.html
    content = content.replace('href="../home.html"', 'href="../index.html"')

    return content

def process_files():
    files_to_fix = [
        'qualifications/services-marketing-coordinator-nqf5.html',
        'qualifications/services-new-venture-creation-nqf4.html',
        'qualifications/services-new-venture-creation-smme-nqf2.html',
        'qualifications/services-office-supervision-nqf5.html',
        'qualifications/services-project-manager-nqf5.html',
        'qualifications/services-quality-assurer-nqf5.html',
        'qualifications/services-quality-manager-nqf6.html'
    ]

    for filepath in files_to_fix:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            updated_content = add_title_section(content)

            if updated_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"[UPDATED] {os.path.basename(filepath)}")
            else:
                print(f"[NO CHANGES] {os.path.basename(filepath)}")
        except Exception as e:
            print(f"[ERROR] {filepath}: {e}")

if __name__ == "__main__":
    process_files()