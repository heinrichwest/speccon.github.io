#!/usr/bin/env python3
"""
Update all SETA qualification pages to match services-bookkeeper format
Includes: W&R SETA, INSETA, MICT SETA, AgriSETA, and TETA
"""

import os
import re
import glob

def get_seta_name(filename):
    """Get the appropriate SETA name based on filename"""
    if filename.startswith('wr-'):
        return 'W&R SETA Qualifications'
    elif filename.startswith('inseta-'):
        return 'INSETA Qualifications'
    elif filename.startswith('mict-'):
        return 'MICT SETA Qualifications'
    elif filename.startswith('agri-'):
        return 'AgriSETA Qualifications'
    elif filename.startswith('teta-'):
        return 'TETA Qualifications'
    else:
        return 'SETA Qualifications'

def get_qualification_name(filename):
    """Extract qualification name from filename"""
    # Remove prefix and extension
    name = filename.replace('.html', '')

    # Remove SETA prefix
    for prefix in ['wr-', 'inseta-', 'mict-', 'agri-', 'teta-']:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break

    # Convert to title case and replace hyphens
    name = name.replace('-', ' ').title()

    # Fix common abbreviations
    name = name.replace('Nqf', 'NQF')
    name = name.replace('It ', 'IT ')

    return name

def add_modal_styles(content):
    """Add enquiry modal CSS if not present"""

    # Check if modal styles already exist
    if 'enquiry-modal' in content:
        return content

    # Find the closing style tag
    style_end = content.find('</style>')

    if style_end == -1:
        # No style tag, need to add one before </head>
        head_end = content.find('</head>')
        if head_end != -1:
            style_section = '''
    <style>
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
    </style>'''
            content = content[:head_end] + style_section + '\n' + content[head_end:]
    else:
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
        }'''

        # Insert modal styles before the closing style tag
        content = content[:style_end] + modal_styles + '\n    ' + content[style_end:]

    return content

def update_header_structure(content, filename):
    """Update the header to match services-bookkeeper format"""

    seta_name = get_seta_name(filename)

    # Update logo path
    content = re.sub(
        r'<img src="[^"]*" alt="[^"]*Logo"',
        '<img src="../images/Logo.png" alt="SpecCon Holdings Logo"',
        content
    )

    # Update logo class
    content = re.sub(
        r'(<img src="../images/Logo.png"[^>]*class=")[^"]*"',
        r'\1h-12"',
        content
    )

    # Check if the header has the title structure
    if 'SpecCon Holdings</h1>' not in content:
        # Add the title structure after the logo
        pattern = r'(<a href="../index.html">\s*<img src="../images/Logo.png"[^>]*>\s*</a>)'
        replacement = rf'''\1
                    <div class="ml-3">
                        <h1 class="text-xl font-bold text-gray-900">SpecCon Holdings</h1>
                        <p class="text-sm text-gray-600">{seta_name}</p>
                    </div>'''

        # First, ensure the logo is wrapped in a flex container
        if '<div class="flex items-center">' not in content:
            content = re.sub(
                r'(<div class="flex items-center justify-between">)\s*(<a href="../index.html">)',
                r'\1\n                <div class="flex items-center">\n                    \2',
                content
            )
            content = re.sub(
                r'(</a>)(\s*<nav)',
                r'\1\n                </div>\2',
                content
            )

        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Update navigation menu
    nav_pattern = r'<nav class="hidden lg:flex[^>]*>.*?</nav>'

    new_nav = '''<nav class="hidden lg:flex items-center space-x-8">
                    <a href="../index.html#about" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">Why Choose Us</a>
                    <a href="../index.html#qualifications" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">Qualifications</a>
                    <a href="../index.html#accreditations" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">Accreditations</a>
                    <a href="../index.html#classroom-training" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">Classroom Training</a>
                    <div class="relative dropdown">
                        <button class="text-gray-700 hover:text-blue-600 font-medium transition duration-300 inline-flex items-center">
                            Other Products <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i>
                        </button>
                        <div class="dropdown-menu absolute left-0 w-64 bg-white rounded-lg shadow-xl py-2 z-20 border">
                            <a href="https://elearning.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="monitor" class="w-4 h-4 inline mr-2"></i>Online Training
                            </a>
                            <a href="https://employmentequityact.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="shield-check" class="w-4 h-4 inline mr-2"></i>Employment Equity
                            </a>
                            <a href="https://learningmanagementsystem.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="graduation-cap" class="w-4 h-4 inline mr-2"></i>Learning Management System
                            </a>
                            <a href="https://skillsdevelopment.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="trending-up" class="w-4 h-4 inline mr-2"></i>Skills Development
                            </a>
                            <a href="https://www.specconacademy.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="school" class="w-4 h-4 inline mr-2"></i>SpecCon Academy
                            </a>
                            <a href="https://bbbee.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="award" class="w-4 h-4 inline mr-2"></i>BBBEE Consulting
                            </a>
                        </div>
                    </div>
                </nav>'''

    content = re.sub(nav_pattern, new_nav, content, flags=re.DOTALL)

    return content

def update_enquire_button(content):
    """Update or add the enquire button"""

    # Pattern for existing button area
    button_pattern = r'<div class="hidden lg:block">.*?</div>'

    new_button = '''<div class="hidden lg:block">
                    <button onclick="openEnquiryModal()" class="bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg">
                        Enquire Now
                    </button>
                </div>'''

    # Check if button exists
    if 'onclick="openEnquiryModal()"' not in content:
        content = re.sub(button_pattern, new_button, content, flags=re.DOTALL)

    return content

def add_mobile_menu(content):
    """Add or update mobile menu"""

    if 'id="mobile-menu"' not in content:
        # Find the header closing div
        header_pattern = r'(</div>\s*</header>)'

        mobile_menu = '''
            <!-- Mobile Menu -->
            <div id="mobile-menu" class="hidden lg:hidden mt-4">
                <a href="../index.html#about" class="block py-2 text-gray-600 hover:text-blue-600">About Us</a>
                <a href="../index.html#qualifications" class="block py-2 text-gray-600 hover:text-blue-600">Qualifications</a>
                <a href="../index.html#accreditations" class="block py-2 text-gray-600 hover:text-blue-600">Accreditations</a>
                <a href="../index.html#classroom-training" class="block py-2 text-gray-600 hover:text-blue-600">Classroom Training</a>
                <button onclick="openEnquiryModal()" class="mt-2 w-full bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-5 py-2 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg text-center block">
                    Enquire Now
                </button>
            </div>
        </div>
    </header>'''

        content = re.sub(header_pattern, mobile_menu, content, flags=re.DOTALL)

    return content

def add_enquiry_modal(content, filename):
    """Add the enquiry modal HTML"""

    if 'id="enquiryModal"' in content:
        # Just update the learnership link
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
    </div>'''

    # Find footer and insert modal before it
    footer_pos = content.find('<!-- Footer -->')
    if footer_pos == -1:
        footer_pos = content.find('<footer')

    if footer_pos != -1:
        content = content[:footer_pos] + modal_html + '\n\n    ' + content[footer_pos:]

    return content

def add_modal_javascript(content, filename):
    """Add or update modal JavaScript"""

    if 'function openEnquiryModal()' in content:
        return content

    qual_name = get_qualification_name(filename)

    # Find script section
    script_start = content.rfind('<script>')

    if script_start == -1:
        # No script tag, add one before </body>
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

        document.addEventListener('DOMContentLoaded', function() {{
            if (typeof lucide !== 'undefined') {{
                lucide.createIcons();
            }}

            const enquiryModal = document.getElementById('enquiryModal');
            if (enquiryModal) {{
                enquiryModal.addEventListener('click', function(e) {{
                    if (e.target === this) {{
                        closeEnquiryModal();
                    }}
                }});
            }}

            document.addEventListener('keydown', function(e) {{
                if (e.key === 'Escape') {{
                    closeEnquiryModal();
                }}
            }});

            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');
            if (mobileMenuButton && mobileMenu) {{
                mobileMenuButton.addEventListener('click', () => {{
                    mobileMenu.classList.toggle('hidden');
                }});
            }}
        }});
    </script>'''
            content = content[:body_end] + script_section + '\n' + content[body_end:]
    else:
        # Add functions after existing script tag
        insert_pos = script_start + len('<script>')

        modal_functions = f'''
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
'''
        content = content[:insert_pos] + '\n' + modal_functions + content[insert_pos:]

    return content

def process_file(filepath):
    """Process a single qualification file"""

    filename = os.path.basename(filepath)
    print(f"Processing {filename}...")

    try:
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply all updates
        original_content = content
        content = add_modal_styles(content)
        content = update_header_structure(content, filename)
        content = update_enquire_button(content)
        content = add_mobile_menu(content)
        content = add_enquiry_modal(content, filename)
        content = add_modal_javascript(content, filename)

        # Write back if changes were made
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
    """Main function to update all SETA qualification pages"""

    # Get all qualification files
    patterns = [
        'qualifications/wr-*.html',
        'qualifications/inseta-*.html',
        'qualifications/mict-*.html',
        'qualifications/agri-*.html',
        'qualifications/teta-*.html'
    ]

    all_files = []
    for pattern in patterns:
        files = glob.glob(pattern)
        # Exclude backup files
        files = [f for f in files if not f.endswith('.backup')]
        all_files.extend(files)

    if not all_files:
        print("No qualification files found!")
        return

    print(f"Found {len(all_files)} qualification files to update")
    print("-" * 50)

    success_count = 0
    for filepath in all_files:
        if process_file(filepath):
            success_count += 1

    print("-" * 50)
    print(f"Successfully updated {success_count}/{len(all_files)} files")

if __name__ == "__main__":
    main()