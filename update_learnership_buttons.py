import os
import re

def update_learnership_buttons():
    """Update Apply for Learnership buttons to link to learnership-application.html"""

    # Directory containing qualification pages
    directory = 'qualifications'

    updated_files = 0
    processed_files = 0

    # Process all HTML files in the qualifications directory
    for filename in os.listdir(directory):
        if filename.endswith('.html') and filename != 'learnership-application.html':
            filepath = os.path.join(directory, filename)
            processed_files += 1

            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            original_content = content

            # Pattern 1: Button with onclick="openEnquiryModal()" that says Apply for Learnership
            pattern1 = r'<button onclick="openEnquiryModal\(\)"([^>]*)>\s*Apply for Learnership\s*</button>'
            replacement1 = r'<a href="../learnership-application.html"\1>\n                                Apply for Learnership\n                            </a>'
            content = re.sub(pattern1, replacement1, content)

            # Pattern 2: Button with data-modal="enquire" that says Apply for Learnership
            pattern2 = r'<button data-modal="enquire"([^>]*)>\s*Apply for Learnership\s*</button>'
            replacement2 = r'<a href="../learnership-application.html"\1>\n                                Apply for Learnership\n                            </a>'
            content = re.sub(pattern2, replacement2, content)

            # Pattern 3: Any other button element with Apply for Learnership
            pattern3 = r'<button([^>]*)>\s*Apply for Learnership\s*</button>'
            # Check if it doesn't already have the link
            if '../learnership-application.html' not in content or pattern3 in content:
                replacement3 = r'<a href="../learnership-application.html"\1>\n                                Apply for Learnership\n                            </a>'
                content = re.sub(pattern3, replacement3, content)

            # Pattern 4: Anchor tags that might already exist but point elsewhere
            pattern4 = r'<a href="[^"]*"([^>]*)>\s*Apply for Learnership\s*</a>'
            replacement4 = r'<a href="../learnership-application.html"\1>\n                                Apply for Learnership\n                            </a>'
            content = re.sub(pattern4, replacement4, content)

            # Only write if changes were made
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                updated_files += 1
                print(f"[OK] Updated {filename}")

    print(f"\nSummary:")
    print(f"- Files checked: {processed_files}")
    print(f"- Files updated: {updated_files}")

if __name__ == "__main__":
    update_learnership_buttons()