#!/usr/bin/env python3
"""
Update all Services SETA pages with correct enquiry modal and learnership application link
"""

import os
import re
import glob

def update_enquiry_modal_link(content, filename):
    """Update the enquiry modal with correct learnership application link"""

    # Fix the learnership application link in the enquiry modal
    content = re.sub(
        r'<a href="apply-btn-hero"([^>]*)>click here</a>',
        '<a href="../learnership-application.html"\\1>click here</a>',
        content,
        flags=re.IGNORECASE
    )

    # Also check for any variations of the incorrect link
    content = re.sub(
        r'href="apply-btn-hero"',
        'href="../learnership-application.html"',
        content
    )

    return content

def update_header_navigation(content, filename):
    """Update the header navigation to match services-bookkeeper-nqf5.html"""

    # Pattern for the header nav section
    nav_pattern = r'(<nav class="hidden lg:flex[^>]*>)(.*?)(</nav>)'

    # New navigation HTML (from services-bookkeeper-nqf5.html)
    new_nav_content = '''
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
                '''

    # Replace the navigation content
    def replace_nav(match):
        return match.group(1) + new_nav_content + match.group(3)

    content = re.sub(nav_pattern, replace_nav, content, flags=re.DOTALL)

    return content

def update_enquiry_button(content, filename):
    """Ensure the enquiry button is properly configured"""

    # Pattern for the desktop enquiry button
    desktop_button_pattern = r'<div class="hidden lg:block">\s*<button[^>]*>(.*?)</button>\s*</div>'

    # New enquiry button HTML
    new_button = '''<div class="hidden lg:block">
                    <button onclick="openEnquiryModal()" class="bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg">
                        Enquire Now
                    </button>
                </div>'''

    # Check if the button already has the correct onclick
    if 'onclick="openEnquiryModal()"' not in content:
        content = re.sub(desktop_button_pattern, new_button, content, flags=re.DOTALL)

    # Also update mobile menu enquiry button
    mobile_button_pattern = r'<button[^>]*onclick="[^"]*"[^>]*class="[^"]*mt-2 w-full bg-gradient[^>]*>.*?Enquire Now.*?</button>'

    new_mobile_button = '''<button onclick="openEnquiryModal()" class="mt-2 w-full bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-5 py-2 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg text-center block">
                    Enquire Now
                </button>'''

    content = re.sub(mobile_button_pattern, new_mobile_button, content, flags=re.DOTALL | re.IGNORECASE)

    return content

def process_file(filepath):
    """Process a single Services SETA file"""

    filename = os.path.basename(filepath)
    print(f"Processing {filename}...")

    try:
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply updates
        original_content = content
        content = update_header_navigation(content, filename)
        content = update_enquiry_button(content, filename)
        content = update_enquiry_modal_link(content, filename)

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
    """Main function to update all Services SETA pages"""

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