#!/usr/bin/env python3
"""
Standardize the Qualification Details sidebar across all qualification HTML files.
Keep only: SETA, NQF Level, Credits, Duration, NLRD ID (or SAQA Qual ID)
Remove: Delivery Mode, Assessment, Status, Expiry Date, Provider, etc.
Keep Career Opportunities section if it exists.
Keep "Need Help?" section if it exists.
"""

import re
import os
from pathlib import Path

# Files to exclude
EXCLUDED_FILES = [
    'skills-conflict-management-nqf5.html',
    'skills-new-venture-creation-nqf2.html',
    'skills-workplace-essential-skills-nqf4.html',
    'template-qualification.html'
]

# Fields to keep (in this order)
KEEP_FIELDS = ['SETA', 'NQF Level', 'Credits', 'Duration', 'NLRD ID', 'SAQA Qual ID']

def process_file(filepath):
    """Process a single HTML file to standardize its sidebar."""
    print(f"Processing: {filepath.name}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the sidebar section with Qualification Details or Quick Facts
    # Pattern 1: Look for the details container
    pattern1 = r'(<div class="space-y-4[^"]*">)(.*?)(</div>\s*(?:</div>|<div class="space-y-4">|<div class="mb-8[^"]*">|<button|<!-- Career Opportunities -->))'

    def replace_sidebar_fields(match):
        opening = match.group(1)
        fields_section = match.group(2)
        closing = match.group(3)

        # Extract all field divs
        field_pattern = r'<div class="flex justify-between[^"]*">\s*<span class="text-gray-600[^"]*">([^<]+)</span>\s*<span class="font-semibold[^"]*">([^<]+)</span>\s*</div>'

        fields = re.findall(field_pattern, fields_section)

        if not fields:
            return match.group(0)  # Return original if no fields found

        # Filter and reorder fields
        kept_fields = []
        field_dict = {label.strip().rstrip(':'): value.strip() for label, value in fields}

        for keep_field in KEEP_FIELDS:
            if keep_field in field_dict:
                kept_fields.append((keep_field, field_dict[keep_field]))

        if not kept_fields:
            return match.group(0)  # Return original if no fields to keep

        # Rebuild the fields HTML
        new_fields = []
        for label, value in kept_fields:
            # Determine if border-b should be included (all except last)
            new_fields.append(
                f'                            <div class="flex justify-between items-center py-3 border-b border-gray-100">\n'
                f'                                <span class="text-gray-600">{label}</span>\n'
                f'                                <span class="font-semibold">{value}</span>\n'
                f'                            </div>'
            )

        return opening + '\n' + '\n'.join(new_fields) + '\n                        ' + closing

    # Apply the replacement
    new_content = re.sub(pattern1, replace_sidebar_fields, content, flags=re.DOTALL)

    # Write back
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  [OK] Updated {filepath.name}")
        return True
    else:
        print(f"  [-] No changes needed for {filepath.name}")
        return False

def main():
    """Main function to process all qualification files."""
    qualifications_dir = Path('qualifications')

    if not qualifications_dir.exists():
        print(f"Error: {qualifications_dir} directory not found!")
        return

    # Get all HTML files
    html_files = sorted(qualifications_dir.glob('*.html'))

    processed = 0
    updated = 0
    skipped = 0

    for filepath in html_files:
        if filepath.name in EXCLUDED_FILES:
            print(f"Skipping (excluded): {filepath.name}")
            skipped += 1
            continue

        try:
            if process_file(filepath):
                updated += 1
            processed += 1
        except Exception as e:
            print(f"  [ERROR] Error processing {filepath.name}: {e}")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Processed: {processed}")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Total files: {len(html_files)}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
