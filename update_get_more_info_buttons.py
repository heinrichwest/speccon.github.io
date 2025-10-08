#!/usr/bin/env python3
"""
Update all "Get More Info" and "Get More Information" buttons/links to trigger the enquiry modal
"""

import os
import re
from pathlib import Path

def update_get_more_info_buttons(file_path):
    """Update Get More Info buttons to trigger enquiry modal"""

    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Pattern 1: Links with "Get More Information" that go to contact section
    # Replace with button that opens enquiry modal
    pattern1 = r'<a\s+href="[^"]*#contact"[^>]*>\s*Get More Information\s*</a>'
    if re.search(pattern1, content):
        content = re.sub(pattern1,
            '<button onclick="openEnquiryModal()" class="border-2 border-white text-white px-8 py-4 rounded-lg font-semibold hover:bg-white hover:text-orange-600 transition duration-300">Get More Information</button>',
            content)
        changes_made = True
        print(f"  [OK] Updated 'Get More Information' link to button with modal")

    # Pattern 2: Any remaining anchor tags with "Get More Info" text
    pattern2 = r'<a\s+[^>]*>\s*Get More Info\s*</a>'
    if re.search(pattern2, content):
        # Extract the classes if they exist
        def replace_anchor(match):
            anchor_tag = match.group(0)
            # Try to extract classes
            class_match = re.search(r'class="([^"]*)"', anchor_tag)
            if class_match:
                classes = class_match.group(1)
            else:
                classes = "border-2 border-blue-600 text-[#12265E] font-semibold px-8 py-4 rounded-lg hover:bg-blue-600 hover:text-white transition duration-300"

            return f'<button onclick="openEnquiryModal()" class="{classes}">Get More Info</button>'

        content = re.sub(pattern2, replace_anchor, content)
        changes_made = True
        print(f"  [OK] Updated 'Get More Info' anchor to button with modal")

    # Check if openEnquiryModal function exists in the file
    if 'openEnquiryModal' in content and 'function openEnquiryModal' not in content:
        # The button calls openEnquiryModal but function might not be defined
        # Add the function definition if it's missing
        if '</body>' in content:
            enquiry_modal_script = '''
    <!-- Enquiry Modal Script -->
    <script>
        function openEnquiryModal() {
            const modal = document.getElementById('enquiry-modal');
            if (modal) {
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
            }
        }

        function closeEnquiryModal() {
            const modal = document.getElementById('enquiry-modal');
            if (modal) {
                modal.classList.remove('show');
                document.body.style.overflow = '';
            }
        }
    </script>
'''
            content = content.replace('</body>', enquiry_modal_script + '\n</body>')
            changes_made = True
            print(f"  [OK] Added enquiry modal functions")

    # For short course pages, ensure they have the enquiry modal HTML
    if 'short-courses' in str(file_path) and 'enquiry-modal' not in content:
        # Check if this page needs the enquiry modal HTML
        if 'openEnquiryModal' in content:
            # Add basic enquiry modal HTML before closing body tag
            enquiry_modal_html = '''
    <!-- Enquiry Modal -->
    <div id="enquiry-modal" class="enquiry-modal">
        <div class="enquiry-modal-content">
            <div class="flex justify-between items-center p-6 border-b">
                <h2 class="text-2xl font-bold text-gray-800">Enquire Now</h2>
                <button onclick="closeEnquiryModal()" class="text-gray-400 hover:text-gray-600 text-xl">
                    <span>&times;</span>
                </button>
            </div>
            <div class="p-6">
                <form id="enquiry-form" class="space-y-4">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">First Name *</label>
                            <input type="text" name="firstName" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Last Name *</label>
                            <input type="text" name="lastName" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Email *</label>
                            <input type="email" name="email" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Phone *</label>
                            <input type="tel" name="phone" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Company</label>
                        <input type="text" name="company" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Message</label>
                        <textarea name="message" rows="4" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"></textarea>
                    </div>
                    <div class="flex gap-4 pt-4">
                        <button type="submit" class="flex-1 bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold py-3 px-6 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300">
                            Submit Enquiry
                        </button>
                        <button type="button" onclick="closeEnquiryModal()" class="flex-1 bg-gray-500 text-white font-semibold py-3 px-6 rounded-lg hover:bg-gray-600 transition duration-300">
                            Cancel
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <style>
        .enquiry-modal {
            display: none;
            position: fixed;
            z-index: 9999;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(4px);
        }

        .enquiry-modal.show {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .enquiry-modal-content {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
        }
    </style>
'''
            content = content.replace('</body>', enquiry_modal_html + '\n</body>')
            changes_made = True
            print(f"  [OK] Added enquiry modal HTML for short course page")

    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [DONE] File updated successfully!")
        return True
    else:
        print(f"  [INFO] No changes needed")
        return False

def main():
    base_dir = Path(r'C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master')

    # Files that need updating based on our search
    files_to_update = [
        # Short courses with "Get More Information" links
        'short-courses/fire-fighter-training.html',
        'short-courses/first-aid-training.html',
        'short-courses/forklift-operations.html',
        'short-courses/ohs-training.html',
        'short-courses/popi-act-training.html',
    ]

    total_updated = 0

    print("=" * 60)
    print("Updating 'Get More Info' buttons to trigger enquiry modal")
    print("=" * 60)

    for file_path in files_to_update:
        full_path = base_dir / file_path
        if full_path.exists():
            if update_get_more_info_buttons(full_path):
                total_updated += 1
        else:
            print(f"[WARNING] File not found: {full_path}")

    # Also check qualification and SETA pages to ensure consistency
    print("\n" + "=" * 60)
    print("Verifying qualification pages...")
    print("=" * 60)

    # Check a sample of qualification pages
    qual_pages = [
        'qualifications/agri-animal-production-nqf1.html',
        'qualifications/wr-retail-manager-nqf5.html',
        'setas/teta-seta.html'
    ]

    for file_path in qual_pages:
        full_path = base_dir / file_path
        if full_path.exists():
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if Get More Info buttons already use modal
            if 'Get More Info' in content and 'openEnquiryModal()' in content:
                print(f"[OK] {file_path}: Already configured correctly")
            elif 'Get More Info' in content:
                print(f"[WARNING] {file_path}: May need update")
                if update_get_more_info_buttons(full_path):
                    total_updated += 1

    print("\n" + "=" * 60)
    print(f"Update complete! {total_updated} files were modified.")
    print("=" * 60)

if __name__ == '__main__':
    main()