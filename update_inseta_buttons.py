import os
import re

def update_inseta_buttons():
    """Update Apply for This Qualification buttons in INSETA pages to use enquiry modal"""

    # Directory containing qualification pages
    directory = 'qualifications'

    # INSETA files
    inseta_files = [
        'inseta-financial-advisor-nqf6.html',
        'inseta-health-care-benefits-advisor-nqf5.html',
        'inseta-insurance-claims-administrator-assessor-nqf4.html',
        'inseta-insurance-underwriter-nqf5.html',
        'inseta-long-term-insurance-advisor-nqf4.html'
    ]

    updated_files = 0

    for filename in inseta_files:
        filepath = os.path.join(directory, filename)

        if not os.path.exists(filepath):
            print(f"[ERROR] File not found: {filename}")
            continue

        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        original_content = content

        # Pattern to find the Apply for This Qualification button (as anchor tag)
        # This pattern matches the anchor tag with href to ../index.html#apply
        pattern = r'<a href="[^"]*#apply"([^>]*)>\s*Apply for This Qualification\s*</a>'

        # Check if enquiryModal function already exists
        has_enquiry_function = 'function openEnquiryModal()' in content or 'onclick="openEnquiryModal()"' in content

        # Replace with button that triggers enquiry modal
        if has_enquiry_function:
            # If enquiryModal exists, use it
            replacement = r'<button onclick="openEnquiryModal()"\1>\n                        Apply for This Qualification\n                    </button>'
        else:
            # Otherwise use data-modal attribute for centralized modal system
            replacement = r'<button data-modal="enquire"\1>\n                        Apply for This Qualification\n                    </button>'

        content = re.sub(pattern, replacement, content)

        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            updated_files += 1
            print(f"[OK] Updated {filename}")
        else:
            print(f"[SKIP] No changes needed in {filename}")

    print(f"\nSummary:")
    print(f"- Files checked: {len(inseta_files)}")
    print(f"- Files updated: {updated_files}")

if __name__ == "__main__":
    update_inseta_buttons()