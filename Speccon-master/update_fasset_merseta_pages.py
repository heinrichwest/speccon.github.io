#!/usr/bin/env python3
"""
Update FASSET and MERSETA qualification pages to use enquiry modal
"""

import os
import re
from pathlib import Path

def add_enquiry_modal_to_page(file_path):
    """Add enquiry modal and update buttons to use it"""

    print(f"Processing: {file_path.name}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Replace apply links with modal buttons
    patterns_to_replace = [
        (r'<a href="[^"]*#apply"([^>]*)>([^<]*Apply[^<]*)</a>',
         lambda m: f'<button onclick="openEnquiryModal()"{m.group(1).replace("href=", "data-href=")}>{m.group(2)}</button>'),

        (r'<a href="[^"]*#contact"([^>]*)>([^<]*Contact[^<]*)</a>',
         lambda m: f'<button onclick="openEnquiryModal()"{m.group(1).replace("href=", "data-href=")}>{m.group(2)}</button>'),

        (r'<a href="[^"]*#contact"([^>]*)>([^<]*Get Information[^<]*)</a>',
         lambda m: f'<button onclick="openEnquiryModal()"{m.group(1).replace("href=", "data-href=")}>{m.group(2)}</button>'),
    ]

    for pattern, replacement in patterns_to_replace:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes_made = True
            print(f"  [OK] Updated links to use enquiry modal")

    # Add enquiry modal HTML and JavaScript if not present
    if 'enquiry-modal' not in content and changes_made:
        # Add modal CSS to head
        if '</style>' in content and '.enquiry-modal' not in content:
            modal_css = '''
        /* Enquiry Modal Styles */
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
    </style>'''
            content = content.replace('</style>', modal_css)
            print(f"  [OK] Added modal CSS styles")

        # Add modal HTML and JavaScript before </body>
        if '</body>' in content:
            modal_html = '''
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

        // Handle form submission
        document.getElementById('enquiry-form').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you for your enquiry! We will contact you soon.');
            closeEnquiryModal();
            this.reset();
        });

        // Close modal when clicking outside
        document.getElementById('enquiry-modal').addEventListener('click', function(e) {
            if (e.target === this) {
                closeEnquiryModal();
            }
        });
    </script>
</body>'''
            content = content.replace('</body>', modal_html)
            print(f"  [OK] Added enquiry modal HTML and JavaScript")

    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [DONE] File updated successfully!")
        return True
    else:
        print(f"  [INFO] No changes needed")
        return False

def main():
    base_dir = Path(r'C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master\qualifications')

    # Files to update
    files_to_update = [
        'fasset-computer-technician-nqf5.html',
        'merseta-automotive-sales-advisor-nqf4.html'
    ]

    total_updated = 0

    print("=" * 60)
    print("Updating FASSET and MERSETA pages with enquiry modal")
    print("=" * 60)

    for filename in files_to_update:
        file_path = base_dir / filename
        if file_path.exists():
            if add_enquiry_modal_to_page(file_path):
                total_updated += 1
        else:
            print(f"[WARNING] File not found: {filename}")

    print("\n" + "=" * 60)
    print(f"Update complete! {total_updated} files were modified.")
    print("=" * 60)

if __name__ == '__main__':
    main()