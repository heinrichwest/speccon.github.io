#!/usr/bin/env python3
"""
Update all Services SETA pages to use the same header and logo structure as services-bookkeeper-nqf5.html
"""

import os
import re
import glob

def update_header_structure(content, filename):
    """Update the header structure to match services-bookkeeper-nqf5.html"""

    # Define the standard header structure from services-bookkeeper-nqf5.html
    standard_header = '''    <!-- Header -->
    <header class="bg-white/95 backdrop-blur-md shadow-lg fixed w-full z-50 top-0">
        <div class="container mx-auto px-4 lg:px-6 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center">
                    <a href="../index.html">
                        <img src="../images/Logo.png" alt="SpecCon Holdings Logo" class="h-12">
                    </a>
                    <div class="ml-3">
                        <h1 class="text-xl font-bold text-gray-900">SpecCon Holdings</h1>
                        <p class="text-sm text-gray-600">Services SETA Qualifications</p>
                    </div>
                </div>'''

    # Pattern to match the header section up to the logo and title
    header_pattern = r'(<!-- Header -->.*?<header[^>]*>.*?<div[^>]*>.*?<div[^>]*>.*?<div[^>]*>.*?<a href="../index\.html">.*?</a>.*?<div[^>]*>.*?<h1[^>]*>[^<]*</h1>.*?<p[^>]*>[^<]*</p>.*?</div>.*?</div>)'

    # Replace with standard header structure
    def replace_header(match):
        # Get the current content after the header div
        current_content = content[match.end():]
        # Find where the nav section starts
        nav_start = current_content.find('<nav')
        if nav_start != -1:
            # Return standard header + the rest of the content from nav onwards
            return standard_header + current_content[nav_start-16:]  # -16 to include proper indentation
        return match.group(0)

    # First, try to replace the entire header section
    new_content = re.sub(header_pattern, replace_header, content, flags=re.DOTALL)

    # If no replacement was made, try a simpler approach
    if new_content == content:
        # Replace just the logo image path
        new_content = re.sub(
            r'<img src="[^"]*"([^>]*)alt="[^"]*Logo"',
            '<img src="../images/Logo.png" alt="SpecCon Holdings Logo"',
            content
        )

        # Update the logo link structure
        new_content = re.sub(
            r'<a href="../index\.html"[^>]*>\s*<img src="../images/Logo\.png"[^>]*>\s*</a>',
            '''<a href="../index.html">
                        <img src="../images/Logo.png" alt="SpecCon Holdings Logo" class="h-12">
                    </a>''',
            new_content,
            flags=re.DOTALL
        )

        # Update the title section to be consistent
        new_content = re.sub(
            r'<div[^>]*>\s*<h1[^>]*>[^<]*SpecCon[^<]*</h1>\s*<p[^>]*>[^<]*</p>\s*</div>',
            '''<div class="ml-3">
                        <h1 class="text-xl font-bold text-gray-900">SpecCon Holdings</h1>
                        <p class="text-sm text-gray-600">Services SETA Qualifications</p>
                    </div>''',
            new_content,
            flags=re.DOTALL
        )

        # Update header classes if different
        new_content = re.sub(
            r'<header[^>]*>',
            '<header class="bg-white/95 backdrop-blur-md shadow-lg fixed w-full z-50 top-0">',
            new_content
        )

    return new_content

def update_mobile_menu(content):
    """Ensure mobile menu exists and is properly structured"""

    # Check if mobile menu exists
    if 'id="mobile-menu"' not in content:
        # Find the closing div of the header container
        header_end = content.find('</header>')
        if header_end != -1:
            # Find the last </div> before </header>
            last_div = content.rfind('</div>', 0, header_end)
            if last_div != -1:
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
            </div>'''
                content = content[:last_div] + mobile_menu + '\n        ' + content[last_div:]

    return content

def update_mobile_menu_button(content):
    """Ensure mobile menu button exists"""

    if 'id="mobile-menu-button"' not in content:
        # Find the enquire button div closing tag
        enquire_pattern = r'(</button>\s*</div>)(\s*)(</div>)(\s*)(<!-- Mobile Menu -->|</header>)'

        def add_mobile_button(match):
            mobile_button = '''
                <button id="mobile-menu-button" class="lg:hidden">
                    <i data-lucide="menu" class="w-6 h-6"></i>
                </button>'''
            return match.group(1) + '\n' + mobile_button + '\n            ' + match.group(3) + match.group(4) + match.group(5)

        content = re.sub(enquire_pattern, add_mobile_button, content)

    return content

def process_file(filepath):
    """Process a single Services SETA file"""

    filename = os.path.basename(filepath)

    # Skip services-bookkeeper-nqf5.html as it's our template
    if filename == 'services-bookkeeper-nqf5.html':
        print(f"Skipping {filename} (template file)")
        return True

    print(f"Processing {filename}...")

    try:
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply updates
        original_content = content
        content = update_header_structure(content, filename)
        content = update_mobile_menu(content)
        content = update_mobile_menu_button(content)

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
    print(f"Successfully processed {success_count}/{len(services_files)} files")

if __name__ == "__main__":
    main()