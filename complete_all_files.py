#!/usr/bin/env python3
"""
Complete script to update ALL qualification files with sticky banner and JavaScript functionality
"""

import os
import re
from pathlib import Path

# List of all qualification files
FILES = [
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

# Sticky banner HTML
STICKY_BANNER_HTML = '''    <!-- Sticky Banner -->
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
    </div>

'''

# JavaScript for sticky banner
STICKY_BANNER_JS = '''
        // Sticky banner functionality
        const stickyBanner = document.getElementById('stickyBanner');
        const bannerPopup = document.getElementById('bannerPopup');
        const closePopup = document.getElementById('closePopup');
        let isPopupOpen = false;

        // Show banner immediately when page loads
        if (stickyBanner) {
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
        }

        // Close popup
        if (closePopup) {
            closePopup.addEventListener('click', function() {
                bannerPopup.classList.remove('show');
                isPopupOpen = false;
            });
        }

        // Close popup when clicking outside
        document.addEventListener('click', function(e) {
            if (stickyBanner && bannerPopup && !stickyBanner.contains(e.target) && !bannerPopup.contains(e.target)) {
                bannerPopup.classList.remove('show');
                isPopupOpen = false;
            }
        });
'''

def process_file(file_path):
    """Process a single qualification file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if sticky banner HTML already exists
        if 'id="stickyBanner"' in content:
            print(f"⏭️  Skipping {file_path.name} - already has sticky banner")
            return True

        # Add sticky banner HTML before footer
        if '<!-- Footer -->' in content:
            content = content.replace('    <!-- Footer -->', STICKY_BANNER_HTML + '    <!-- Footer -->')
        elif '<footer' in content:
            footer_pos = content.find('<footer')
            content = content[:footer_pos] + STICKY_BANNER_HTML + '\n    ' + content[footer_pos:]
        else:
            print(f"⚠️  No footer found in {file_path.name}")
            return False

        # Add sticky banner JavaScript
        if 'lucide.createIcons();' in content and 'stickyBanner' not in content:
            # Find the script section and add our JS
            lucide_pos = content.find('lucide.createIcons();')
            script_end = content.find('</script>', lucide_pos)

            if script_end != -1:
                content = content[:script_end] + STICKY_BANNER_JS + '\n    ' + content[script_end:]

        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Updated: {file_path.name}")
        return True

    except Exception as e:
        print(f"❌ Error processing {file_path.name}: {e}")
        return False

def main():
    """Main function to process all files"""
    base_dir = Path("qualifications")

    if not base_dir.exists():
        print(f"❌ Directory not found: {base_dir}")
        return

    updated_count = 0
    skipped_count = 0
    error_count = 0

    print("🚀 Starting batch update of all qualification files...")
    print(f"📁 Processing {len(FILES)} files...")
    print()

    for filename in FILES:
        file_path = base_dir / filename

        if not file_path.exists():
            print(f"❌ File not found: {filename}")
            error_count += 1
            continue

        if process_file(file_path):
            updated_count += 1
        else:
            error_count += 1

    print()
    print("📊 Final Summary:")
    print(f"   ✅ Successfully updated: {updated_count} files")
    print(f"   ⚠️  Errors: {error_count} files")
    print(f"   📁 Total processed: {len(FILES)} files")
    print()
    print("🎉 All qualification pages now have the sticky banner functionality!")

if __name__ == "__main__":
    main()