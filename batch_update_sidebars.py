#!/usr/bin/env python3
"""
Batch update all qualification sidebars to standardized format.
Keeps only: SETA, NQF Level, Credits, Duration (if exists), NLRD ID/SAQA Qual ID
"""

import os
import re
from pathlib import Path

# Files to exclude
EXCLUDED_FILES = [
    'skills-conflict-management-nqf5.html',
    'skills-new-venture-creation-nqf2.html',
    'skills-workplace-essential-skills-nqf4.html',
    'template-qualification.html'
]

# Files already processed
PROCESSED_FILES = [
    'agri-farming-nqf1.html',
    'agri-farming-nqf2.html',
    'agri-animal-production-nqf1.html'
]

def standardize_sidebar(content, filename):
    """Standardize the sidebar section in a qualification file."""

    # Pattern to find the sidebar details section
    # Looking for either "Qualification Details" or "Quick Facts"
    pattern = r'((?:Qualification Details|Quick Facts)</h3>\s*<div class="space-y-4[^"]*">)(.*?)(</div>\s*(?:</div>|<!-- Career|<div class="mb-8|<button|<div class="space-y-4">))'

    def process_sidebar(match):
        before = match.group(1)
        fields_html = match.group(2)
        after = match.group(3)

        # Extract all field divs
        field_pattern = r'<div class="flex justify-between[^>]*>\s*<span class="text-gray-600">([^<]+?)(?::)?</span>\s*<span class="font-semibold">([^<]+)</span>\s*</div>'
        fields = re.findall(field_pattern, fields_html, re.DOTALL)

        if not fields:
            return match.group(0)

        # Create field dictionary
        field_dict = {}
        for label, value in fields:
            clean_label = label.strip().rstrip(':')
            field_dict[clean_label] = value.strip()

        # Build standardized field list
        standardized_fields = []

        # Add fields in standard order
        if 'SETA' in field_dict:
            standardized_fields.append(('SETA', field_dict['SETA']))

        # NQF Level (various formats)
        for key in ['NQF Level', 'NQF level']:
            if key in field_dict:
                standardized_fields.append(('NQF Level', field_dict[key]))
                break

        if 'Credits' in field_dict:
            standardized_fields.append(('Credits', field_dict['Credits']))

        if 'Duration' in field_dict:
            standardized_fields.append(('Duration', field_dict['Duration']))

        # NLRD ID or SAQA Qual ID
        for key in ['NLRD ID', 'SAQA Qual ID', 'SAQA ID']:
            if key in field_dict:
                standardized_fields.append((key, field_dict[key]))
                break

        # Rebuild HTML
        new_fields = []
        for label, value in standardized_fields:
            new_fields.append(
                f'                            <div class="flex justify-between items-center py-3 border-b border-gray-100">\n'
                f'                                <span class="text-gray-600">{label}</span>\n'
                f'                                <span class="font-semibold">{value}</span>\n'
                f'                            </div>'
            )

        return before + '\n' + '\n'.join(new_fields) + '\n                        ' + after

    # Apply standardization
    new_content = re.sub(pattern, process_sidebar, content, flags=re.DOTALL)

    return new_content

def main():
    qualifications_dir = Path('qualifications')

    if not qualifications_dir.exists():
        print(f"Error: {qualifications_dir} not found")
        return

    files = sorted(qualifications_dir.glob('*.html'))

    updated = 0
    skipped = 0
    errors = 0

    for filepath in files:
        filename = filepath.name

        # Skip excluded files
        if filename in EXCLUDED_FILES or filename in PROCESSED_FILES:
            print(f"Skipping: {filename}")
            skipped += 1
            continue

        try:
            print(f"Processing: {filename}")

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Standardize the sidebar
            new_content = standardize_sidebar(content, filename)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  [UPDATED]: {filename}")
                updated += 1
            else:
                print(f"  [-] No changes needed: {filename}")

        except Exception as e:
            print(f"  [ERROR]: {filename} - {e}")
            errors += 1

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")
    print(f"  Total files: {len(files)}")

if __name__ == '__main__':
    main()