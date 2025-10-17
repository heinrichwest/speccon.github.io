import os
import re
from pathlib import Path

def comment_out_request_info_button(file_path):
    """Comment out the Request Information button in a qualification HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already commented out
        if '<!-- <button onclick="openEnquiryModal()"' in content or '<!-- <button onclick="openContactModal()"' in content:
            return False

        # Pattern to match the button with either openEnquiryModal() or openContactModal()
        # This pattern matches the button across multiple lines
        pattern = r'(<button onclick="(?:openEnquiryModal|openContactModal)\(\)" class="block w-full border-2 border-\[#12265E\] text-\[#12265E\] font-bold py-3 px-6 rounded-lg text-center hover:bg-\[#12265E\] hover:text-white transition duration-300">[\s]*Request Information[\s]*</button>)'

        # Check if the button exists
        if re.search(pattern, content, re.MULTILINE):
            # Replace with commented version
            replacement = r'<!-- \1 -->'
            new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

            # Write the updated content back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            return True
        else:
            return False

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def main():
    qualifications_dir = Path('qualifications')

    # Get all HTML files (exclude .backup files)
    html_files = [f for f in qualifications_dir.glob('*.html') if not f.name.endswith('.backup')]

    updated_count = 0
    skipped_count = 0

    print("Commenting out 'Request Information' buttons...\n")

    for html_file in sorted(html_files):
        if comment_out_request_info_button(html_file):
            print(f"[OK] Updated: {html_file.name}")
            updated_count += 1
        else:
            skipped_count += 1

    print(f"\n{'='*60}")
    print(f"Complete! Updated {updated_count} files, skipped {skipped_count} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
