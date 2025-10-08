#!/usr/bin/env python3
"""
Finish updating Services SETA pages headers and logos
"""

import os
import re
import glob

def update_logo_and_title(content):
    """Update logo path and title structure"""

    # Update logo image source
    content = re.sub(
        r'<img src="[^"]*" alt="[^"]*Logo"',
        '<img src="../images/Logo.png" alt="SpecCon Holdings Logo"',
        content
    )

    # Update logo class to h-12
    content = re.sub(
        r'(<img src="../images/Logo.png"[^>]*class=")[^"]*"',
        r'\1h-12"',
        content
    )

    # Update the title div to match services-bookkeeper-nqf5.html
    content = re.sub(
        r'(<div class="ml-3">.*?<h1[^>]*>)[^<]*(</h1>.*?<p[^>]*>)[^<]*(</p>.*?</div>)',
        r'\1SpecCon Holdings\2Services SETA Qualifications\3',
        content,
        flags=re.DOTALL
    )

    return content

def process_file(filepath):
    """Process a single file"""

    filename = os.path.basename(filepath)

    # Skip the template file
    if filename == 'services-bookkeeper-nqf5.html':
        return True

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already updated
        if 'Services SETA Qualifications' in content and 'src="../images/Logo.png"' in content:
            print(f"  [ALREADY UPDATED] {filename}")
            return True

        # Apply updates
        original_content = content
        content = update_logo_and_title(content)

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
    # Get all Services SETA files
    services_files = glob.glob('qualifications/services-*.html')

    print(f"Found {len(services_files)} Services SETA qualification files")
    print("-" * 50)

    success_count = 0
    for filepath in services_files:
        if process_file(filepath):
            success_count += 1

    print("-" * 50)
    print(f"Successfully processed {success_count}/{len(services_files)} files")

if __name__ == "__main__":
    main()