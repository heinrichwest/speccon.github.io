#!/usr/bin/env python3
"""
Script to update all "Get More Info" buttons/links in qualification files
to use openContactModal() instead of openEnquiryModal()
Also converts anchor tags to buttons with openContactModal()
"""

import os
import re
from pathlib import Path

def update_file(filepath):
    """Update a single file to change openEnquiryModal to openContactModal for Get More Info buttons"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = []

        # Pattern 1: Match button tags with openEnquiryModal and "Get More Info" text
        button_pattern = r'(<button\s+onclick="open)Enquiry(Modal\(\)"[^>]*>[\s\S]{0,200}?Get More Info[\s\S]{0,50}?</button>)'
        if re.search(button_pattern, content):
            content = re.sub(button_pattern, r'\1Contact\2', content, flags=re.MULTILINE)
            changes_made.append("Updated button with openEnquiryModal")

        # Pattern 2: Convert anchor tags linking to contact section with "Get More Info" to buttons with openContactModal
        # Match anchor tags that point to #contact or ../index.html#contact and contain "Get More Info"
        anchor_pattern = r'<a\s+href="[^"]*#contact"([^>]*)>\s*Get More Info\s*</a>'
        anchor_matches = re.findall(anchor_pattern, content)
        if anchor_matches:
            def replace_anchor(match):
                # Extract the class attribute if it exists
                attrs = match.group(1)
                class_match = re.search(r'class="([^"]*)"', attrs)
                if class_match:
                    classes = class_match.group(1)
                else:
                    classes = "border-2 border-green-600 text-[#12265E] font-semibold px-8 py-4 rounded-lg hover:bg-green-600 hover:text-white transition duration-300 text-center"
                
                return f'<button onclick="openContactModal()" class="{classes}">\n                            Get More Info\n                        </button>'
            
            content = re.sub(anchor_pattern, replace_anchor, content)
            changes_made.append("Converted anchor to button with openContactModal")

        # Pattern 3: Fix the typo opencontactModal (lowercase c) to openContactModal
        if 'opencontactModal()' in content:
            content = content.replace('opencontactModal()', 'openContactModal()')
            changes_made.append("Fixed lowercase typo opencontactModal")

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        return False, []
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False, []

def main():
    # Directory containing qualification files
    qual_dir = Path(r"C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master\qualifications")

    if not qual_dir.exists():
        print(f"Directory not found: {qual_dir}")
        return

    # Get all HTML files
    html_files = list(qual_dir.glob("*.html"))

    print(f"Found {len(html_files)} HTML files in qualifications folder")
    print("Updating files...\n")

    updated_count = 0
    updated_files = []

    for html_file in html_files:
        updated, changes = update_file(html_file)
        if updated:
            updated_count += 1
            updated_files.append((html_file.name, changes))
            print(f"[OK] Updated: {html_file.name}")
            for change in changes:
                print(f"     - {change}")

    print(f"\n{'='*60}")
    print(f"Update Complete!")
    print(f"{'='*60}")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files updated: {updated_count}")
    print(f"Files unchanged: {len(html_files) - updated_count}")

    if updated_files:
        print(f"\n{'='*60}")
        print("Updated files:")
        print(f"{'='*60}")
        for filename, changes in sorted(updated_files):
            print(f"  - {filename}")

if __name__ == "__main__":
    main()
