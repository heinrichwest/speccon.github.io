#!/usr/bin/env python3
"""
Add complete enquiry modal to all Services SETA pages
"""

import os
import re
import glob

def get_qualification_name(filename):
    """Extract qualification name from filename"""

    # Map filenames to proper qualification names
    name_map = {
        'services-bookkeeper-nqf5.html': 'Bookkeeper NQF5',
        'services-business-administration-nqf3.html': 'Business Administration NQF3',
        'services-business-administration-nqf4.html': 'Business Administration NQF4',
        'services-business-process-outsourcing-nqf3.html': 'Business Process Outsourcing NQF3',
        'services-contact-centre-manager-nqf5.html': 'Contact Centre Manager NQF5',
        'services-customer-service-nqf2.html': 'Customer Service NQF2',
        'services-generic-management-nqf4.html': 'Generic Management NQF4',
        'services-generic-management-nqf5.html': 'Generic Management NQF5',
        'services-management-nqf3.html': 'Management NQF3',
        'services-marketing-coordinator-nqf5.html': 'Marketing Coordinator NQF5',
        'services-new-venture-creation-nqf4.html': 'New Venture Creation NQF4',
        'services-new-venture-creation-smme-nqf2.html': 'New Venture Creation SMME NQF2',
        'services-office-supervision-nqf5.html': 'Office Supervision NQF5',
        'services-project-manager-nqf5.html': 'Project Manager NQF5',
        'services-quality-assurer-nqf5.html': 'Quality Assurer NQF5',
        'services-quality-manager-nqf6.html': 'Quality Manager NQF6'
    }

    return name_map.get(filename, 'Services SETA Qualification')

def add_modal_styles(content):
    """Add enquiry modal CSS if not present"""

    # Check if modal styles already exist
    if 'enquiry-modal' in content:
        return content

    # Find the closing style tag
    style_end = content.find('</style>')

    if style_end == -1:
        return content

    modal_styles = '''
        /* Enquiry Popup Modal Styles */
        .enquiry-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 2000;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
        }
        .enquiry-modal.show {
            opacity: 1;
            visibility: visible;
        }
        .enquiry-modal-content {
            background: white;
            border-radius: 20px;
            max-width: 500px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
            transform: translateY(20px);
            transition: transform 0.3s ease;
        }
        .enquiry-modal.show .enquiry-modal-content {
            transform: translateY(0);
        }
    '''

    # Insert modal styles before the closing style tag
    content = content[:style_end] + modal_styles + '\n    ' + content[style_end:]

    return content

def add_modal_html(content, filename):
    """Add the enquiry modal HTML before the footer"""

    # Check if modal already exists
    if 'id="enquiryModal"' in content:
        # Just update the learnership link if needed
        content = re.sub(
            r'href="[^"]*"([^>]*>click here</a>)',
            r'href="../learnership-application.html"\1',
            content
        )
        return content

    qual_name = get_qualification_name(filename)

    modal_html = f'''
    <!-- Enquiry Modal -->
    <div id="enquiryModal" class="enquiry-modal">
        <div class="enquiry-modal-content">
            <div class="p-8">
                <div class="flex items-center justify-between mb-6">
                    <h2 class="text-2xl font-bold text-gray-900">Enquire About {qual_name}</h2>
                    <button onclick="closeEnquiryModal()" class="text-gray-400 hover:text-gray-600 text-xl">
                        <i data-lucide="x" class="w-6 h-6"></i>
                    </button>
                </div>

                <div class="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <p class="text-blue-700 text-sm">
                        <i data-lucide="info" class="w-4 h-4 inline mr-2"></i>
                        If you are applying for a learnership, please <a href="../learnership-application.html" class="font-semibold underline hover:text-blue-800">click here</a>.
                    </p>
                </div>

                <form id="enquiryForm" onsubmit="submitEnquiry(event)">
                    <div class="grid md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <label for="firstName" class="block text-sm font-medium text-gray-700 mb-2">Name *</label>
                            <input type="text" id="firstName" name="firstName" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                        <div>
                            <label for="surname" class="block text-sm font-medium text-gray-700 mb-2">Surname *</label>
                            <input type="text" id="surname" name="surname" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                    </div>

                    <div class="grid md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <label for="email" class="block text-sm font-medium text-gray-700 mb-2">Email *</label>
                            <input type="email" id="email" name="email" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                        <div>
                            <label for="phone" class="block text-sm font-medium text-gray-700 mb-2">Phone Number *</label>
                            <input type="tel" id="phone" name="phone" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                    </div>

                    <div class="mb-4">
                        <label for="company" class="block text-sm font-medium text-gray-700 mb-2">Company *</label>
                        <input type="text" id="company" name="company" required
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                    </div>

                    <div class="mb-6">
                        <label for="reason" class="block text-sm font-medium text-gray-700 mb-2">Reason for Enquiry *</label>
                        <textarea id="reason" name="reason" rows="4" required
                                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                                  placeholder="Please tell us about your enquiry and how we can help you..."></textarea>
                    </div>

                    <div class="flex flex-col sm:flex-row gap-3">
                        <button type="submit" class="flex-1 bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold py-3 px-6 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300">
                            <i data-lucide="send" class="w-4 h-4 inline mr-2"></i>
                            Send Enquiry
                        </button>
                        <button type="button" onclick="closeEnquiryModal()" class="flex-1 bg-gray-500 text-white font-semibold py-3 px-6 rounded-lg hover:bg-gray-600 transition duration-300">
                            Cancel
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
'''

    # Find the footer and insert modal before it
    footer_pos = content.find('<!-- Footer -->')
    if footer_pos == -1:
        footer_pos = content.find('<footer')

    if footer_pos != -1:
        content = content[:footer_pos] + modal_html + '\n\n    ' + content[footer_pos:]

    return content

def add_modal_javascript(content, filename):
    """Add or update the enquiry modal JavaScript functions"""

    # Check if the functions already exist
    if 'function openEnquiryModal()' in content:
        return content

    qual_name = get_qualification_name(filename)

    # Find the script section
    script_start = content.rfind('<script>')

    if script_start == -1:
        # No script tag, need to add one before </body>
        body_end = content.rfind('</body>')
        if body_end != -1:
            script_section = f'''
    <script>
        // Enquiry Modal Functions
        function openEnquiryModal() {{
            const modal = document.getElementById('enquiryModal');
            if (modal) {{
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
            }}
        }}

        function closeEnquiryModal() {{
            const modal = document.getElementById('enquiryModal');
            if (modal) {{
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
            }}
        }}

        function submitEnquiry(event) {{
            event.preventDefault();

            const formData = new FormData(event.target);
            const enquiryData = {{
                firstName: formData.get('firstName'),
                surname: formData.get('surname'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                company: formData.get('company'),
                reason: formData.get('reason'),
                qualification: '{qual_name}'
            }};

            alert('Thank you for your enquiry! We will get back to you soon.');
            closeEnquiryModal();
            event.target.reset();

            console.log('Enquiry submitted:', enquiryData);
        }}

        // Initialize when DOM is ready
        document.addEventListener('DOMContentLoaded', function() {{
            lucide.createIcons();

            // Close modal when clicking outside
            const enquiryModal = document.getElementById('enquiryModal');
            if (enquiryModal) {{
                enquiryModal.addEventListener('click', function(e) {{
                    if (e.target === this) {{
                        closeEnquiryModal();
                    }}
                }});
            }}

            // Close modal with Escape key
            document.addEventListener('keydown', function(e) {{
                if (e.key === 'Escape') {{
                    closeEnquiryModal();
                }}
            }});
        }});
    </script>
'''
            content = content[:body_end] + script_section + '\n' + content[body_end:]
    else:
        # Add functions after the script tag
        insert_pos = script_start + len('<script>')

        modal_functions = f'''
        // Enquiry Modal Functions (defined first to be available immediately)
        function openEnquiryModal() {{
            const modal = document.getElementById('enquiryModal');
            if (modal) {{
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
            }}
        }}

        function closeEnquiryModal() {{
            const modal = document.getElementById('enquiryModal');
            if (modal) {{
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
            }}
        }}

        function submitEnquiry(event) {{
            event.preventDefault();

            const formData = new FormData(event.target);
            const enquiryData = {{
                firstName: formData.get('firstName'),
                surname: formData.get('surname'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                company: formData.get('company'),
                reason: formData.get('reason'),
                qualification: '{qual_name}'
            }};

            alert('Thank you for your enquiry! We will get back to you soon.');
            closeEnquiryModal();
            event.target.reset();

            console.log('Enquiry submitted:', enquiryData);
        }}

'''
        content = content[:insert_pos] + '\n' + modal_functions + content[insert_pos:]

    return content

def process_file(filepath):
    """Process a single Services SETA file to add complete enquiry modal"""

    filename = os.path.basename(filepath)
    print(f"Processing {filename}...")

    try:
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply all updates
        original_content = content
        content = add_modal_styles(content)
        content = add_modal_html(content, filename)
        content = add_modal_javascript(content, filename)

        # Write the updated content back if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [UPDATED] {filename}")
        else:
            print(f"  [NO CHANGES] {filename}")

        return True

    except Exception as e:
        print(f"  [ERROR] {filename}: {str(e)}")
        return False

def main():
    """Main function to add enquiry modal to all Services SETA pages"""

    # Get all Services SETA qualification files
    services_files = glob.glob('qualifications/services-*.html')

    if not services_files:
        print("No Services SETA qualification files found!")
        return

    print(f"Found {len(services_files)} Services SETA qualification files")
    print("-" * 50)

    success_count = 0
    for filepath in services_files:
        if process_file(filepath):
            success_count += 1

    print("-" * 50)
    print(f"Successfully updated {success_count}/{len(services_files)} files")

if __name__ == "__main__":
    main()