#!/usr/bin/env python3
"""
Remove TrainingBookingDate field from qualification enquiry forms.
This field is not needed in qualification enquiry forms (only in training booking forms).
"""

import os
import re
import glob

def remove_training_date_field(file_path):
    """Remove TrainingBookingDate: '' from qualification page forms."""
    print(f"Processing: {os.path.basename(file_path)}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = []

        # Remove the TrainingBookingDate line (including the comma before it and newline)
        # Pattern matches variations like:
        # ,\n                TrainingBookingDate: ''
        # ,\n                TrainingBookingDate: ""
        pattern = r",\s*\n\s*TrainingBookingDate:\s*['\"][\w\s\-]*['\"]"

        if re.search(pattern, content):
            content = re.sub(pattern, '', content)
            changes_made.append("Removed TrainingBookingDate field")

        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [+] Updated: {', '.join(changes_made)}")
            return True
        else:
            print(f"  [-] No TrainingBookingDate field found")
            return False

    except Exception as e:
        print(f"  [!] Error: {e}")
        return False

def main():
    """Main function to update all qualification pages."""
    # Get all HTML files in qualifications directory
    qualifications_dir = os.path.join(os.path.dirname(__file__), 'qualifications')
    html_files = glob.glob(os.path.join(qualifications_dir, '*.html'))

    print(f"Found {len(html_files)} qualification pages to check\n")
    print("=" * 70)

    updated_count = 0

    for file_path in sorted(html_files):
        # Skip template files
        if 'template' in os.path.basename(file_path).lower():
            print(f"Skipping template: {os.path.basename(file_path)}")
            continue

        if remove_training_date_field(file_path):
            updated_count += 1
        print()

    print("=" * 70)
    print(f"\nSummary:")
    print(f"  Total files processed: {len(html_files)}")
    print(f"  Files updated: {updated_count}")
    print(f"  Files unchanged: {len(html_files) - updated_count}")
    print("\nTrainingBookingDate field has been removed from all qualification forms!")

if __name__ == '__main__':
    main()
