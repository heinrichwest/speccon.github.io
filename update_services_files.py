#!/usr/bin/env python3
"""
Script to update all Services SETA qualification HTML files with the requested changes.
"""

import os
import re
from pathlib import Path

def update_services_files():
    # Define the base path
    base_path = Path(r"C:\Users\Asus\OneDrive - Speccon Holdings (Pty) Ltd\Websites\Speccon\qualifications")

    # List of Services SETA files to update
    services_files = [
        "services-bookkeeper-nqf5.html",
        "services-customer-service-nqf2.html",
        "services-new-venture-creation-smme-nqf2.html",
        "services-management-nqf3.html",
        "services-business-administration-nqf3.html",
        "services-business-process-outsourcing-nqf3.html",
        "services-quality-manager-nqf6.html",
        "services-generic-management-nqf4.html",
        "services-marketing-coordinator-nqf5.html",
        "services-quality-assurer-nqf5.html",
        "services-contact-centre-manager-nqf5.html",
        "services-new-venture-creation-nqf4.html",
        "services-office-supervision-nqf5.html",
        "services-project-manager-nqf5.html",
        "services-business-administration-nqf4.html"
    ]

    # New header content
    new_header = '''<!-- Header -->
<header class="bg-white/90 backdrop-blur-md shadow-sm fixed w-full z-50 top-0">
    <div class="container mx-auto px-6 py-3">
        <div class="flex items-center justify-between">
            <a href="../home.html">
                <img src="../SpecCon2.png" alt="SpecCon Holdings Logo" class="h-12">
            </a>

            <nav class="hidden lg:flex items-center space-x-8">
                <a href="../home.html#about" class="text-gray-600 hover:text-blue-600 transition duration-300">About Us</a>
                <a href="../home.html#qualifications" class="text-gray-600 hover:text-blue-600 transition duration-300">Qualifications</a>
                <a href="../home.html#accreditations" class="text-gray-600 hover:text-blue-600 transition duration-300">Accreditations</a>
                <div class="relative dropdown">
                    <button class="text-gray-600 hover:text-blue-600 transition duration-300 flex items-center">
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
                <a href="../home.html#contact" class="text-gray-600 hover:text-blue-600 transition duration-300">Contact Us</a>
            </nav>

            <div class="hidden lg:block">
                <button onclick="window.location.href='../home.html#contact'" class="bg-blue-600 text-white font-semibold px-5 py-2 rounded-lg hover:bg-blue-700 transition duration-300 shadow">Apply for a Learnership</button>
            </div>

            <button id="mobile-menu-button" class="lg:hidden">
                <i data-lucide="menu" class="w-6 h-6"></i>
            </button>
        </div>

        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden lg:hidden mt-4">
            <a href="../home.html#about" class="block py-2 text-gray-600 hover:text-blue-600">About Us</a>
            <a href="../home.html#qualifications" class="block py-2 text-gray-600 hover:text-blue-600">Qualifications</a>
            <a href="../home.html#accreditations" class="block py-2 text-gray-600 hover:text-blue-600">Accreditations</a>
            <a href="../home.html#classroom-training" class="block py-2 text-gray-600 hover:text-blue-600">Classroom Training</a>
            <a href="../home.html#contact" class="block py-2 text-gray-600 hover:text-blue-600">Contact Us</a>
            <button onclick="window.location.href='../home.html#contact'" class="mt-2 w-full bg-blue-600 text-white font-semibold px-5 py-2 rounded-lg hover:bg-blue-700 transition duration-300">Apply for a Learnership</button>
        </div>
    </div>
</header>'''

    # New CSS to add
    new_css = '''        /* Dropdown styling for better hover stability and alignment */
        .dropdown {
            padding-bottom: 8px;
            display: flex;
            align-items: center;
        }
        .dropdown button {
            display: flex;
            align-items: center;
        }
        .dropdown-menu {
            top: 100%;
            margin-top: 0;
            padding-top: 8px;
        }
        .dropdown:hover .dropdown-menu {
            display: block;
        }
        .dropdown-menu {
            display: none;
        }'''

    # Track changes for each file
    changes_report = {}

    for filename in services_files:
        file_path = base_path / filename

        if not file_path.exists():
            print(f"Warning: {filename} not found")
            continue

        print(f"Processing {filename}...")
        changes_report[filename] = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # 1. Update CSS section
            css_pattern = r'(\.dropdown:hover \.dropdown-menu \{\s*display: block;\s*\}\s*\.dropdown-menu \{\s*display: none;\s*\})'
            if re.search(css_pattern, content):
                content = re.sub(css_pattern, new_css, content)
                changes_report[filename].append("Updated CSS with improved dropdown styling")

            # 2. Update header section
            header_pattern = r'<!-- Header -->.*?</header>'
            if re.search(header_pattern, content, re.DOTALL):
                content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
                changes_report[filename].append("Updated header to new format with improved dropdown menu")

            # 3. Remove "Request Information" button
            request_info_pattern = r'\s*<div class="space-y-4">\s*<a href="[^"]*" class="block w-full border-2 border-blue-600 text-blue-600 font-bold py-3 px-6 rounded-lg text-center hover:bg-blue-600 hover:text-white transition duration-300">\s*Request Information\s*</a>\s*</div>'
            if re.search(request_info_pattern, content, re.DOTALL):
                content = re.sub(request_info_pattern, '', content, flags=re.DOTALL)
                changes_report[filename].append("Removed 'Request Information' button")

            # 4. Remove "Need Help?" block
            need_help_pattern = r'\s*<div class="mt-8 p-4 bg-blue-50 rounded-lg">\s*<h4 class="font-bold text-gray-900 mb-2">Need Help\?</h4>.*?</div>'
            if re.search(need_help_pattern, content, re.DOTALL):
                content = re.sub(need_help_pattern, '', content, flags=re.DOTALL)
                changes_report[filename].append("Removed 'Need Help?' block")

            # 5. Remove any remaining "Apply for this qualification" buttons
            apply_qual_pattern = r'\s*<[^>]*>.*?Apply for this qualification.*?</[^>]*>'
            if re.search(apply_qual_pattern, content, re.DOTALL | re.IGNORECASE):
                content = re.sub(apply_qual_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
                changes_report[filename].append("Removed 'Apply for this qualification' button")

            # 6. Remove "Apply for Learnership" buttons in sidebar (if any exist separately from header)
            apply_learnership_sidebar_pattern = r'\s*<a[^>]*class="[^"]*"[^>]*>\s*Apply for Learnership\s*</a>'
            if re.search(apply_learnership_sidebar_pattern, content):
                # Only remove if it's not in the header section
                if '<nav class="hidden lg:flex' not in content[content.find('Apply for Learnership'):content.find('Apply for Learnership')+200]:
                    content = re.sub(apply_learnership_sidebar_pattern, '', content)
                    changes_report[filename].append("Removed sidebar 'Apply for Learnership' button")

            # Write updated content back to file
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Updated {filename}")
            else:
                print(f"No changes needed for {filename}")
                changes_report[filename].append("No changes needed")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            changes_report[filename].append(f"Error: {e}")

    return changes_report

if __name__ == "__main__":
    changes = update_services_files()

    print("\n" + "="*80)
    print("SUMMARY REPORT OF CHANGES")
    print("="*80)

    for filename, file_changes in changes.items():
        print(f"\n{filename}:")
        for change in file_changes:
            print(f"  • {change}")