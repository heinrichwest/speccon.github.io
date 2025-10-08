#!/usr/bin/env python3
"""
Script to update all qualification pages to match the reference layout
with dropdown navigation and sticky banner functionality.
"""

import os
import re
from pathlib import Path

# Define the qualification files that need to be updated
qualification_files = [
    "agri-animal-production-nqf1.html",
    "agri-animal-production-nqf2.html",
    "agri-animal-production-nqf4.html",
    "agri-farming-nqf1.html",
    "agri-farming-nqf2.html",
    "agri-fruit-packaging-nqf3.html",
    "agri-mixed-farming-nqf1.html",
    "agri-mixed-farming-nqf2.html",
    "agri-plant-production-nqf1.html",
    "agri-plant-production-nqf2.html",
    "agri-plant-production-nqf3.html",
    "agri-plant-production-nqf4.html",
    "etdp-education-training-nqf5.html",
    "fasset-computer-technician-nqf5.html",
    "inseta-financial-advisor-nqf6.html",
    "inseta-health-care-benefits-advisor-nqf5.html",
    "inseta-insurance-claims-administrator-assessor-nqf4.html",
    "inseta-insurance-underwriter-nqf5.html",
    "inseta-long-term-insurance-advisor-nqf4.html",
    "mer-automotive-sales-advisor-nqf4.html",
    "mict-systems-development-nqf4.html",
    "mict-business-analysis-nqf6.html",
    "mict-end-user-computing-nqf3.html",
    "mict-design-thinking-nqf4.html",
    "mict-software-engineer-nqf6.html",
    "mict-software-tester-nqf5.html",
    "services-business-administration-nqf4.html",
    "services-new-venture-creation-nqf4.html",
    "services-business-administration-nqf3.html",
    "services-business-process-outsourcing-nqf3.html",
    "services-generic-management-nqf5.html",
    "services-generic-management-nqf4.html",
    "services-new-venture-creation-smme-nqf2.html",
    "services-management-nqf3.html",
    "services-quality-manager-nqf6.html",
    "services-marketing-coordinator-nqf5.html",
    "services-contact-centre-manager-nqf5.html",
    "services-office-supervision-nqf5.html",
    "services-project-manager-nqf5.html",
    "services-quality-assurer-nqf5.html",
    "teta-transport-clerk-nqf4.html",
    "wr-planner-nqf5.html",
    "wr-retail-buyer-nqf5.html",
    "wr-retail-manager-nqf5.html",
    "wr-retail-supervisor-nqf4.html",
    "wr-sales-assistant-nqf3.html",
    "wr-service-station-assistant-nqf2.html",
    "wr-store-person-nqf2.html",
    "wr-visual-merchandiser-nqf3.html"
]

# CSS styles to add
additional_css = """
        .dropdown:hover .dropdown-menu {
            display: block;
        }
        .dropdown-menu {
            display: none;
        }
        /* Dropdown styling for better hover stability and alignment */
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
        }
        /* Sticky Banner Styles */
        .sticky-banner {
            position: fixed;
            top: 100px;
            right: 20px;
            background: linear-gradient(135deg, #12265E 0%, #FF9C2A 100%);
            color: white;
            padding: 12px 20px;
            border-radius: 50px;
            cursor: pointer;
            z-index: 1000;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            font-weight: 600;
            font-size: 14px;
            backdrop-filter: blur(10px);
        }
        .sticky-banner:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            background: linear-gradient(135deg, #0d1a47 0%, #e8891f 100%);
        }
        .banner-popup {
            position: fixed;
            top: 160px;
            right: 20px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            z-index: 999;
            overflow: hidden;
            transform: translateY(-20px);
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s ease;
            max-width: 420px;
            width: 90vw;
        }
        .banner-popup.show {
            transform: translateY(0);
            opacity: 1;
            pointer-events: all;
        }
        .animate-scroll {
            animation: scroll 30s linear infinite;
        }
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-100%); }
        }"""

# Navigation section to replace basic nav
navigation_html = """                <nav class="hidden lg:flex items-center space-x-8">
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
                    <a href="../index.html#contact" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">Contact Us</a>
                </nav>"""

# Apply button update
apply_button_html = """                <div class="hidden lg:block">
                    <a href="../index.html#apply" class="bg-gradient-to-r from-[#12265E] to-[#FF9C2A] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#e8891f] transition duration-300 shadow-lg">
                        Apply for a Learnership
                    </a>
                </div>"""

# Mobile menu update
mobile_menu_html = """            <!-- Mobile Menu -->
            <div id="mobile-menu" class="hidden lg:hidden mt-4">
                <a href="../index.html#about" class="block py-2 text-gray-600 hover:text-blue-600">About Us</a>
                <a href="../index.html#qualifications" class="block py-2 text-gray-600 hover:text-blue-600">Qualifications</a>
                <a href="../index.html#accreditations" class="block py-2 text-gray-600 hover:text-blue-600">Accreditations</a>
                <a href="../index.html#classroom-training" class="block py-2 text-gray-600 hover:text-blue-600">Classroom Training</a>
                <a href="../index.html#contact" class="block py-2 text-gray-600 hover:text-blue-600">Contact Us</a>
                <a href="../index.html#apply" class="mt-2 w-full bg-gradient-to-r from-[#12265E] to-[#FF9C2A] text-white font-semibold px-5 py-2 rounded-lg hover:from-[#0d1a47] hover:to-[#e8891f] transition duration-300 shadow-lg text-center block">
                    Apply for a Learnership
                </a>
            </div>"""

# Sticky banner and popup HTML to add before footer
sticky_banner_html = """
    <!-- Sticky Banner -->
    <div id="stickyBanner" class="sticky-banner">
        <i data-lucide="gift" class="w-4 h-4 inline mr-2"></i>
        Our Free Value Adds
    </div>

    <!-- Banner Popup -->
    <div id="bannerPopup" class="banner-popup">
        <div class="p-6">
            <div class="flex items-center justify-between mb-4">
                <h3 class="text-xl font-bold text-gray-900">Value-Added Benefits</h3>
                <button id="closePopup" class="text-gray-400 hover:text-gray-600">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>
            <p class="text-gray-600 text-sm mb-6">You can get these value adds for free when you do learnerships with SpecCon</p>
            <!-- Value Adds Grid -->
            <div class="grid grid-cols-1 gap-4 mb-6">
                <div class="flex items-center p-3 bg-blue-50 rounded-lg">
                    <div class="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center mr-3">
                        <i data-lucide="layout-template" class="w-4 h-4 text-white"></i>
                    </div>
                    <div>
                        <h4 class="font-semibold text-sm text-gray-900">White Labelled LMS</h4>
                        <p class="text-xs text-gray-600">Complete Learning Management System</p>
                    </div>
                </div>
                <div class="flex items-center p-3 bg-green-50 rounded-lg">
                    <div class="w-8 h-8 bg-green-500 rounded-lg flex items-center justify-center mr-3">
                        <i data-lucide="book-open" class="w-4 h-4 text-white"></i>
                    </div>
                    <div>
                        <h4 class="font-semibold text-sm text-gray-900">300+ Online Courses</h4>
                        <p class="text-xs text-gray-600">Comprehensive course library</p>
                    </div>
                </div>
                <div class="flex items-center p-3 bg-purple-50 rounded-lg">
                    <div class="w-8 h-8 bg-purple-500 rounded-lg flex items-center justify-center mr-3">
                        <i data-lucide="users" class="w-4 h-4 text-white"></i>
                    </div>
                    <div>
                        <h4 class="font-semibold text-sm text-gray-900">Employment Equity System</h4>
                        <p class="text-xs text-gray-600">Compliance and reporting</p>
                    </div>
                </div>
                <div class="flex items-center p-3 bg-orange-50 rounded-lg">
                    <div class="w-8 h-8 bg-orange-500 rounded-lg flex items-center justify-center mr-3">
                        <i data-lucide="clipboard-check" class="w-4 h-4 text-white"></i>
                    </div>
                    <div>
                        <h4 class="font-semibold text-sm text-gray-900">10+ Work Assessments</h4>
                        <p class="text-xs text-gray-600">Excel & workplace skills tests</p>
                    </div>
                </div>
                <div class="flex items-center p-3 bg-red-50 rounded-lg">
                    <div class="w-8 h-8 bg-red-500 rounded-lg flex items-center justify-center mr-3">
                        <i data-lucide="shield-check" class="w-4 h-4 text-white"></i>
                    </div>
                    <div>
                        <h4 class="font-semibold text-sm text-gray-900">Compliance Training</h4>
                        <p class="text-xs text-gray-600">First Aid, Fire Fighter, OHS</p>
                    </div>
                </div>
                <div class="flex items-center p-3 bg-teal-50 rounded-lg">
                    <div class="w-8 h-8 bg-teal-500 rounded-lg flex items-center justify-center mr-3">
                        <i data-lucide="graduation-cap" class="w-4 h-4 text-white"></i>
                    </div>
                    <div>
                        <h4 class="font-semibold text-sm text-gray-900">Academy Access</h4>
                        <p class="text-xs text-gray-600">Resources for staff children</p>
                    </div>
                </div>
            </div>
            <!-- Client Testimonials -->
            <div class="border-t pt-4">
                <h4 class="font-bold text-gray-900 mb-3 text-sm">What Our Clients Say</h4>
                <div class="space-y-3">
                    <div class="flex items-start space-x-3">
                        <img src="../Client Logos/AVI.PNG" alt="AVI" class="w-8 h-8 object-contain">
                        <div>
                            <p class="text-xs text-gray-700 italic">"SpecCon is knowledgeable, passionate and always goes the extra mile..."</p>
                            <p class="text-xs text-gray-500 mt-1">- Neteske Gerber, AVI</p>
                        </div>
                    </div>
                    <div class="flex items-start space-x-3">
                        <img src="../Client Logos/isuzu.PNG" alt="Isuzu" class="w-8 h-8 object-contain">
                        <div>
                            <p class="text-xs text-gray-700 italic">"The SpecCon LMS has transformed our training approach..."</p>
                            <p class="text-xs text-gray-500 mt-1">- Lisa van Aswegen, Isuzu</p>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Client Logos Scrolling Bar -->
            <div class="border-t pt-4 mt-4">
                <p class="text-xs text-gray-500 text-center mb-2">Trusted by Leading Companies</p>
                <div class="overflow-hidden">
                    <div class="flex animate-scroll">
                        <div class="flex space-x-4 min-w-max">
                            <img src="../Client Logos/AVI.PNG" alt="AVI" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/isuzu.PNG" alt="Isuzu" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/afgri.PNG" alt="Afgri" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/engen.PNG" alt="Engen" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/capitec.PNG" alt="Capitec" class="h-6 object-contain grayscale">
                        </div>
                    </div>
                </div>
            </div>
            <!-- Enquiry Button -->
            <div class="border-t pt-4 mt-4 text-center">
                <a href="../index.html#contact" class="bg-gradient-to-r from-[#12265E] to-[#FF9C2A] text-white px-6 py-3 rounded-lg font-semibold hover:from-[#0d1a47] hover:to-[#e8891f] transition duration-300 shadow-lg inline-block">
                    Enquiry Now
                </a>
            </div>
        </div>
    </div>"""

# JavaScript to add before closing body tag
additional_javascript = """
        // Mobile menu toggle
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');

        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });

        // Sticky banner functionality
        const stickyBanner = document.getElementById('stickyBanner');
        const bannerPopup = document.getElementById('bannerPopup');
        const closePopup = document.getElementById('closePopup');
        let isPopupOpen = false;

        // Show banner immediately when page loads
        stickyBanner.style.display = 'block';

        // Toggle popup on banner hover/click
        stickyBanner.addEventListener('mouseenter', function() {
            if (!isPopupOpen) {
                bannerPopup.classList.add('show');
                isPopupOpen = true;
            }
        });

        stickyBanner.addEventListener('click', function() {
            bannerPopup.classList.toggle('show');
            isPopupOpen = !isPopupOpen;
        });

        // Close popup
        closePopup.addEventListener('click', function() {
            bannerPopup.classList.remove('show');
            isPopupOpen = false;
        });

        // Close popup when clicking outside
        document.addEventListener('click', function(e) {
            if (!stickyBanner.contains(e.target) && !bannerPopup.contains(e.target)) {
                bannerPopup.classList.remove('show');
                isPopupOpen = false;
            }
        });"""

def update_qualification_file(file_path):
    """Update a single qualification file with the new features."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add additional CSS styles
        if additional_css not in content:
            # Find the closing </style> tag and add new CSS before it
            style_end = content.find('</style>')
            if style_end != -1:
                content = content[:style_end] + additional_css + '\n    ' + content[style_end:]

        # Update navigation - find the nav section and replace it
        nav_pattern = r'<nav class="hidden lg:flex[^>]*">.*?</nav>'
        content = re.sub(nav_pattern, navigation_html, content, flags=re.DOTALL)

        # Update apply button
        apply_pattern = r'<div class="hidden lg:block">.*?</div>(?=\s*<button)'
        content = re.sub(apply_pattern, apply_button_html, content, flags=re.DOTALL)

        # Add mobile menu if it doesn't exist
        if 'mobile-menu' not in content:
            # Find the closing div of the header flex container
            header_end = content.find('</div>\n        </div>\n    </header>')
            if header_end != -1:
                insert_pos = content.rfind('</div>', 0, header_end)
                if insert_pos != -1:
                    content = content[:insert_pos + 6] + '\n\n' + mobile_menu_html + '\n        ' + content[insert_pos + 6:]

        # Add mobile menu button if it doesn't exist
        if 'mobile-menu-button' not in content:
            # Find where to add the mobile menu button (usually after the apply button div)
            apply_div_end = content.find('</div>\n\n                <button')
            if apply_div_end == -1:
                apply_div_end = content.find('</div>\n            </div>\n        </div>\n    </header>')
                if apply_div_end != -1:
                    mobile_button = '\n\n                <button id="mobile-menu-button" class="lg:hidden">\n                    <i data-lucide="menu" class="w-6 h-6"></i>\n                </button>'
                    content = content[:apply_div_end] + mobile_button + content[apply_div_end:]

        # Add sticky banner and popup before footer
        if 'sticky-banner' not in content:
            footer_start = content.find('    <!-- Footer -->')
            if footer_start != -1:
                content = content[:footer_start] + sticky_banner_html + '\n\n    ' + content[footer_start:]

        # Add JavaScript functionality
        if 'stickyBanner' not in content:
            # Find the lucide.createIcons() call and add our JS after it
            lucide_call = content.find('lucide.createIcons();')
            if lucide_call != -1:
                script_end = content.find('</script>', lucide_call)
                if script_end != -1:
                    content = content[:script_end] + '\n\n' + additional_javascript + '\n\n    ' + content[script_end:]

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Updated: {file_path}")
        return True

    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all qualification files."""
    base_dir = Path("C:/Users/Asus/OneDrive - Speccon Holdings (Pty) Ltd/Websites/Speccon/qualifications")

    if not base_dir.exists():
        print(f"❌ Directory not found: {base_dir}")
        return

    updated_count = 0
    skipped_count = 0

    for file_name in qualification_files:
        file_path = base_dir / file_name

        if file_path.exists():
            if update_qualification_file(file_path):
                updated_count += 1
            else:
                skipped_count += 1
        else:
            print(f"⚠️  File not found: {file_path}")
            skipped_count += 1

    print(f"\n📊 Summary:")
    print(f"   ✅ Updated: {updated_count} files")
    print(f"   ⚠️  Skipped: {skipped_count} files")
    print(f"   📁 Total: {len(qualification_files)} files")

if __name__ == "__main__":
    main()