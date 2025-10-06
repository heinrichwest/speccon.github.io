#!/usr/bin/env python3
"""
Update all W&R SETA qualification pages with:
1. Enquiry modal buttons (Apply for this Qualification, Get More Info, Apply Now, Contact Us)
2. Fixed footer logo path
3. Fixed modal JavaScript
"""

import os
import re

# Define the files to update
WR_SETA_FILES = [
    "qualifications/wr-planner-nqf5.html",
    "qualifications/wr-retail-buyer-nqf5.html",
    "qualifications/wr-retail-manager-nqf5.html",
    "qualifications/wr-retail-supervisor-nqf4.html",
    "qualifications/wr-sales-assistant-nqf3.html",
    "qualifications/wr-store-person-nqf2.html",
    "qualifications/wr-visual-merchandiser-nqf3.html",
    "qualifications/wr-retail-operations-nqf2.html",
    "qualifications/wr-sales-marketing-nqf3.html",
]

def update_hero_buttons(content):
    """Update hero section buttons to trigger openEnquiryModal()"""
    # Pattern 1: <a href="../index.html#apply" ...>Apply for this Qualification</a>
    pattern1 = r'<a\s+href="\.\.\/index\.html#apply"\s+([^>]*?)>\s*Apply for this Qualification\s*<\/a>'
    replacement1 = r'<button onclick="openEnquiryModal()" \1>\n                            Apply for this Qualification\n                        </button>'
    content = re.sub(pattern1, replacement1, content)

    # Pattern 2: <a href="../index.html#contact" ...>Get More Info</a>
    pattern2 = r'<a\s+href="\.\.\/index\.html#contact"\s+([^>]*?)>\s*Get More Info\s*<\/a>'
    replacement2 = r'<button onclick="openEnquiryModal()" \1>\n                            Get More Info\n                        </button>'
    content = re.sub(pattern2, replacement2, content)

    return content

def update_cta_buttons(content):
    """Update CTA section buttons to trigger openEnquiryModal()"""
    # Pattern 1: <a href="../index.html#apply" ...>Apply Now</a>
    pattern1 = r'<a\s+href="\.\.\/index\.html#apply"\s+([^>]*?)>\s*Apply Now\s*<\/a>'
    replacement1 = r'<button onclick="openEnquiryModal()" \1>\n                    Apply Now\n                </button>'
    content = re.sub(pattern1, replacement1, content)

    # Pattern 2: <a href="../index.html#contact" ...>Contact Us</a>
    pattern2 = r'<a\s+href="\.\.\/index\.html#contact"\s+([^>]*?)>\s*Contact Us\s*<\/a>'
    replacement2 = r'<button onclick="openEnquiryModal()" \1>\n                    Contact Us\n                </button>'
    content = re.sub(pattern2, replacement2, content)

    return content

def fix_footer_logo(content):
    """Fix footer logo path from images/ to ../images/"""
    pattern = r'<img\s+src="images\/SpecCon-LOGO\.png"'
    replacement = r'<img src="../images/SpecCon-LOGO.png"'
    content = re.sub(pattern, replacement, content)
    return content

def fix_modal_javascript(content):
    """Fix modal JavaScript to use classList and proper event listeners"""
    # Fix openEnquiryModal function
    old_open = r'function openEnquiryModal\(\) \{[^}]*document\.getElementById\(\'enquiryModal\'\)\.style\.display\s*=\s*[\'"]flex[\'"];[^}]*\}'
    new_open = '''function openEnquiryModal() {
            const modal = document.getElementById('enquiryModal');
            if (modal) {
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
            }
        }'''
    content = re.sub(old_open, new_open, content, flags=re.DOTALL)

    # Fix closeEnquiryModal function
    old_close = r'function closeEnquiryModal\(\) \{[^}]*document\.getElementById\(\'enquiryModal\'\)\.style\.display\s*=\s*[\'"]none[\'"];[^}]*\}'
    new_close = '''function closeEnquiryModal() {
            const modal = document.getElementById('enquiryModal');
            if (modal) {
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
            }
        }'''
    content = re.sub(old_close, new_close, content, flags=re.DOTALL)

    # Remove broken stickyBanner code if present
    broken_code_pattern = r'stickyBanner\.addEventListener\([^)]*\)[^}]*\}[^}]*\);[^}]*closePopup\.addEventListener[^}]*\}[^}]*\);[^}]*document\.addEventListener\("click"[^}]*\}[^}]*\);'
    if re.search(broken_code_pattern, content, re.DOTALL):
        content = re.sub(broken_code_pattern, '', content, flags=re.DOTALL)

        # Add proper event listeners
        proper_listeners = '''
        // Set up modal event listeners after DOM is ready
        document.addEventListener('DOMContentLoaded', function() {
            // Close modal when clicking outside
            const enquiryModal = document.getElementById('enquiryModal');
            if (enquiryModal) {
                enquiryModal.addEventListener('click', function(e) {
                    if (e.target === this) {
                        closeEnquiryModal();
                    }
                });
            }

            // Close modal with Escape key
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    closeEnquiryModal();
                }
            });
        });'''

        # Insert before closing script tag
        content = re.sub(r'(\s*)<\/script>(\s*<script src="\.\.\/js\/centralized-modals\.js"><\/script>)',
                        proper_listeners + r'\n\1</script>\2', content)

    return content

def update_file(filepath):
    """Update a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Apply updates
        content = update_hero_buttons(content)
        content = update_cta_buttons(content)
        content = fix_footer_logo(content)
        content = fix_modal_javascript(content)

        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated: {filepath}")
            return True
        else:
            print(f"[-] No changes needed: {filepath}")
            return False

    except Exception as e:
        print(f"[ERROR] Error updating {filepath}: {str(e)}")
        return False

def main():
    """Main function to update all W&R SETA files"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    updated_count = 0

    print("Updating W&R SETA qualification pages...\n")

    for file in WR_SETA_FILES:
        filepath = os.path.join(base_dir, file)
        if os.path.exists(filepath):
            if update_file(filepath):
                updated_count += 1
        else:
            print(f"[ERROR] File not found: {filepath}")

    print(f"\n[OK] Update complete! {updated_count} file(s) updated.")

if __name__ == "__main__":
    main()