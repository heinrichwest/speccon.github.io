#!/usr/bin/env python3
"""
Fix broken links in qualification pages by replacing them with valid alternatives
"""

import os
import re
from pathlib import Path

def replace_broken_links(filepath, replacements):
    """Replace broken links in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = False
        for old_link, new_link in replacements.items():
            if old_link in content:
                content = content.replace(f'href="{old_link}"', f'href="{new_link}"')
                modified = True

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function to fix broken links"""
    qualifications_dir = Path('qualifications')

    # Define link replacements
    replacements = {
        # Replace non-existent services-retail-operations-nqf3.html with services-management-nqf3.html
        'services-retail-operations-nqf3.html': 'services-management-nqf3.html',

        # Replace non-existent services-business-administration-nqf5.html with services-office-supervision-nqf5.html
        'services-business-administration-nqf5.html': 'services-office-supervision-nqf5.html',

        # MICT SETA broken links
        'mict-systems-development-nqf5.html': 'mict-system-support-nqf5.html',
        'mict-database-development-nqf5.html': 'mict-software-tester-nqf5.html',
        'mict-systems-support-nqf5.html': 'mict-system-support-nqf5.html',
        'mict-database-administrator-nqf5.html': 'mict-software-tester-nqf5.html'
    }

    print("Fixing broken qualification links...")
    print("=" * 60)

    # Process Services SETA files
    services_files = [
        'services-business-administration-nqf3.html',
        'services-business-administration-nqf4.html',
        'services-business-process-outsourcing-nqf3.html',
        'services-contact-centre-manager-nqf5.html',
        'services-customer-service-nqf2.html',
        'services-generic-management-nqf4.html',
        'services-management-nqf3.html',
        'services-marketing-coordinator-nqf5.html',
        'services-new-venture-creation-nqf4.html',
        'services-new-venture-creation-smme-nqf2.html',
        'services-office-supervision-nqf5.html',
        'services-project-manager-nqf5.html',
        'services-quality-manager-nqf6.html'
    ]

    # Process MICT SETA files
    mict_files = [
        'mict-end-user-computing-nqf3.html',
        'mict-software-tester-nqf5.html',
        'mict-system-support-nqf5.html'
    ]

    all_files = services_files + mict_files
    success_count = 0

    for filename in all_files:
        filepath = qualifications_dir / filename
        if filepath.exists():
            if replace_broken_links(filepath, replacements):
                print(f"[FIXED] {filename}")
                success_count += 1
            else:
                print(f"[UNCHANGED] {filename}")
        else:
            print(f"[WARNING] {filename}: File not found")

    print("=" * 60)
    print(f"Fixed {success_count} files")

    # Also update the "Retail Operations" text to match the new link
    print("\nUpdating link text to match new destinations...")
    print("=" * 60)

    for filename in services_files:
        filepath = qualifications_dir / filename
        if filepath.exists():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Update the text for retail operations link
                if 'services-management-nqf3.html' in content and 'Retail Operations' in content:
                    # Find and replace the entire block for retail operations
                    pattern = r'(<a href="services-management-nqf3\.html"[^>]*>.*?)<h3[^>]*>Retail Operations</h3>'
                    replacement = r'\1<h3 class="font-bold text-lg text-gray-900">Management</h3>'
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

                    # Also update the description
                    pattern = r'(href="services-management-nqf3\.html".*?)Advanced retail skills and operations management\.'
                    replacement = r'\1Management fundamentals and team leadership skills.'
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

                # Update the text for business administration NQF5 link
                if 'services-office-supervision-nqf5.html' in content and 'Business Administration' in content and 'NQF Level 5' in content:
                    # Find and replace the title in the related qualifications
                    pattern = r'(<a href="services-office-supervision-nqf5\.html"[^>]*>.*?)<h3[^>]*>Business Administration</h3>'
                    replacement = r'\1<h3 class="font-bold text-lg text-gray-900">Office Supervision</h3>'
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

                    # Update the description
                    pattern = r'(href="services-office-supervision-nqf5\.html".*?)Advanced business and administrative skills\.'
                    replacement = r'\1Office management and supervisory skills.'
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"[TEXT UPDATED] {filename}")

            except Exception as e:
                print(f"[ERROR] {filename}: {e}")

    print("=" * 60)
    print("Link fixing complete!")

if __name__ == "__main__":
    main()