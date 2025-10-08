#!/usr/bin/env python3
"""
Comprehensive script to systematically update ALL remaining qualification pages
with complete header, navigation, sticky banner, and JavaScript functionality
"""

import os
import re
import shutil
from pathlib import Path

def get_seta_info(filename):
    """Get SETA information based on filename"""
    seta_mapping = {
        'agri-': 'AgriSETA',
        'etdp-': 'ETDP SETA',
        'fasset-': 'FASSET',
        'inseta-': 'INSETA',
        'mer-': 'merSETA',
        'mict-': 'MICT SETA',
        'services-': 'Services SETA',
        'teta-': 'TETA',
        'wr-': 'W&R SETA'
    }

    for prefix, seta in seta_mapping.items():
        if filename.startswith(prefix):
            return seta
    return 'Services SETA'  # Default

def get_complete_html_template():
    """Get the complete HTML template with all required components"""
    return '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {seta_name} | SpecCon Holdings</title>
    <meta name="description" content="{description}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>

    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .card-hover:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 10px 10px -5px rgb(0 0 0 / 0.04);
        }
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
        }
    </style>
</head>

<body class="bg-white text-gray-900">
    <!-- Header -->
    <header class="bg-white/95 backdrop-blur-md shadow-lg fixed w-full z-50 top-0">
        <div class="container mx-auto px-4 lg:px-6 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center">
                    <a href="../index.html">
                        <img src="../images/Logo.png" alt="SpecCon Holdings Logo" class="h-12">
                    </a>
                    <div class="ml-3">
                        <h1 class="text-xl font-bold text-gray-900">SpecCon Holdings</h1>
                        <p class="text-sm text-gray-600">{seta_name} Qualifications</p>
                    </div>
                </div>

                <nav class="hidden lg:flex items-center space-x-8">
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
                </nav>

                <div class="hidden lg:block">
                    <a href="../index.html#apply" class="bg-gradient-to-r from-[#12265E] to-[#FF9C2A] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#e8891f] transition duration-300 shadow-lg">
                        Apply for a Learnership
                    </a>
                </div>

                <button id="mobile-menu-button" class="lg:hidden">
                    <i data-lucide="menu" class="w-6 h-6"></i>
                </button>
            </div>

            <!-- Mobile Menu -->
            <div id="mobile-menu" class="hidden lg:hidden mt-4">
                <a href="../index.html#about" class="block py-2 text-gray-600 hover:text-blue-600">About Us</a>
                <a href="../index.html#qualifications" class="block py-2 text-gray-600 hover:text-blue-600">Qualifications</a>
                <a href="../index.html#accreditations" class="block py-2 text-gray-600 hover:text-blue-600">Accreditations</a>
                <a href="../index.html#classroom-training" class="block py-2 text-gray-600 hover:text-blue-600">Classroom Training</a>
                <a href="../index.html#contact" class="block py-2 text-gray-600 hover:text-blue-600">Contact Us</a>
                <a href="../index.html#apply" class="mt-2 w-full bg-gradient-to-r from-[#12265E] to-[#FF9C2A] text-white font-semibold px-5 py-2 rounded-lg hover:from-[#0d1a47] hover:to-[#e8891f] transition duration-300 shadow-lg text-center block">
                    Apply for a Learnership
                </a>
            </div>
        </div>
    </header>


    <!-- Breadcrumb -->
    <section class="pt-24 pb-8 bg-gray-50">
        <div class="container mx-auto px-6">
            <nav class="text-sm text-gray-600">
                <a href="../index.html" class="hover:text-blue-600">Home</a>
                <span class="mx-2">/</span>
                <a href="../setas/{seta_link}.html" class="hover:text-blue-600">{seta_name}</a>
                <span class="mx-2">/</span>
                <span class="text-gray-900">{breadcrumb_title}</span>
            </nav>
        </div>
    </section>

    {main_content}

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
    </div>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12">
        <div class="container mx-auto px-6">
            <div class="grid md:grid-cols-4 gap-8">
                <div class="md:col-span-2">
                    <div class="flex items-center mb-4">
                        <img src="../images/Logo.png" alt="SpecCon Holdings Logo" class="h-12 mr-3">
                        <div>
                            <h3 class="text-xl font-bold">SpecCon Holdings</h3>
                            <p class="text-gray-400">{title} Qualification</p>
                        </div>
                    </div>
                    <p class="text-gray-400 mb-4">Building expertise through comprehensive training.</p>
                </div>

                <div>
                    <h4 class="text-lg font-semibold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="../index.html" class="text-gray-400 hover:text-white transition duration-200">Home</a></li>
                        <li><a href="../setas/{seta_link}.html" class="text-gray-400 hover:text-white transition duration-200">{seta_name}</a></li>
                        <li><a href="../index.html#qualifications" class="text-gray-400 hover:text-white transition duration-200">All Qualifications</a></li>
                        <li><a href="../index.html#contact" class="text-gray-400 hover:text-white transition duration-200">Contact</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-semibold mb-4">Get Started</h4>
                    <ul class="space-y-2">
                        <li><a href="../index.html#contact" class="text-gray-400 hover:text-white transition duration-200">Get Information</a></li>
                        <li><a href="mailto:help@speccon.co.za" class="text-gray-400 hover:text-white transition duration-200">Email Us</a></li>
                    </ul>
                </div>
            </div>

            <div class="border-t border-gray-800 mt-8 pt-8 text-center">
                <p class="text-gray-400">&copy; 2025 SpecCon Holdings. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        lucide.createIcons();

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
        });

    </script>
</body>
</html>'''

def get_seta_link(seta_name):
    """Get SETA link for breadcrumb"""
    seta_links = {
        'AgriSETA': 'agriseta',
        'ETDP SETA': 'etdp-seta',
        'FASSET': 'fasset',
        'INSETA': 'inseta',
        'merSETA': 'merseta',
        'MICT SETA': 'mict-seta',
        'Services SETA': 'services-seta',
        'TETA': 'teta',
        'W&R SETA': 'wr-seta'
    }
    return seta_links.get(seta_name, 'services-seta')

def extract_main_content(html_content):
    """Extract main content sections from existing HTML"""
    try:
        # Extract from hero section to before footer
        hero_start = html_content.find('<!-- Hero Section -->')
        if hero_start == -1:
            hero_start = html_content.find('<section class="py-16')

        footer_start = html_content.find('<!-- Footer -->')
        if footer_start == -1:
            footer_start = html_content.find('<footer')

        if hero_start != -1 and footer_start != -1:
            return html_content[hero_start:footer_start].strip()
        else:
            # Fallback: extract between body tag and footer
            body_start = html_content.find('<body')
            if body_start != -1:
                body_start = html_content.find('>', body_start) + 1
                if footer_start != -1:
                    content = html_content[body_start:footer_start].strip()
                    # Remove any existing header/nav content
                    content = re.sub(r'<header.*?</header>', '', content, flags=re.DOTALL)
                    content = re.sub(r'<nav.*?</nav>', '', content, flags=re.DOTALL)
                    return content

            return html_content
    except Exception as e:
        print(f"Error extracting main content: {e}")
        return html_content

def extract_title_and_description(html_content):
    """Extract title and description from existing HTML"""
    title = "Qualification"
    description = "Professional qualification accredited by SETA."

    try:
        # Extract title
        title_match = re.search(r'<title>(.*?)\|', html_content)
        if title_match:
            title = title_match.group(1).strip()
        else:
            # Try to extract from h1
            h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.DOTALL)
            if h1_match:
                title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()

        # Extract description
        desc_match = re.search(r'<meta name="description" content="(.*?)"', html_content)
        if desc_match:
            description = desc_match.group(1)
        else:
            # Try to extract from first paragraph
            p_match = re.search(r'<p[^>]*class="[^"]*text-lg[^"]*"[^>]*>(.*?)</p>', html_content, re.DOTALL)
            if p_match:
                description = re.sub(r'<[^>]+>', '', p_match.group(1)).strip()[:150] + "..."

    except Exception as e:
        print(f"Error extracting title/description: {e}")

    return title, description

def update_qualification_file(filepath):
    """Update a single qualification file with complete template"""
    try:
        # Create backup
        backup_path = f"{filepath}.backup"
        if not os.path.exists(backup_path):
            shutil.copy2(filepath, backup_path)
            print(f"Created backup: {backup_path}")

        # Read existing content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = os.path.basename(filepath)
        seta_name = get_seta_info(filename)
        seta_link = get_seta_link(seta_name)

        # Extract title, description, and main content
        title, description = extract_title_and_description(content)
        main_content = extract_main_content(content)

        # Create breadcrumb title
        breadcrumb_title = title

        # Get complete template
        template = get_complete_html_template()

        # Fill in the template
        updated_content = template.format(
            title=title,
            seta_name=seta_name,
            seta_link=seta_link,
            description=description,
            breadcrumb_title=breadcrumb_title,
            main_content=main_content
        )

        # Write updated content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"✅ Updated: {filename}")
        return True

    except Exception as e:
        print(f"❌ Error updating {filepath}: {e}")
        return False

def main():
    """Main function to update all qualification files"""

    # Define all file batches
    batches = {
        "BATCH 1 - AgriSETA": [
            "agri-animal-production-nqf4.html",
            "agri-farming-nqf1.html",
            "agri-farming-nqf2.html",
            "agri-fruit-packaging-nqf3.html",
            "agri-mixed-farming-nqf1.html",
            "agri-mixed-farming-nqf2.html",
            "agri-plant-production-nqf1.html",
            "agri-plant-production-nqf2.html",
            "agri-plant-production-nqf3.html",
            "agri-plant-production-nqf4.html"
        ],
        "BATCH 2 - ETDP & FASSET": [
            "etdp-education-training-nqf5.html",
            "fasset-computer-technician-nqf5.html"
        ],
        "BATCH 3 - INSETA": [
            "inseta-financial-advisor-nqf6.html",
            "inseta-health-care-benefits-advisor-nqf5.html",
            "inseta-insurance-claims-administrator-assessor-nqf4.html",
            "inseta-insurance-underwriter-nqf5.html",
            "inseta-long-term-insurance-advisor-nqf4.html"
        ],
        "BATCH 4 - MER & MICT": [
            "mer-automotive-sales-advisor-nqf4.html",
            "mict-systems-development-nqf4.html",
            "mict-business-analysis-nqf6.html",
            "mict-end-user-computing-nqf3.html",
            "mict-design-thinking-nqf4.html",
            "mict-software-engineer-nqf6.html",
            "mict-software-tester-nqf5.html"
        ],
        "BATCH 5 - Services SETA": [
            "services-new-venture-creation-nqf4.html",
            "services-generic-management-nqf5.html",
            "services-generic-management-nqf4.html",
            "services-new-venture-creation-smme-nqf2.html",
            "services-management-nqf3.html",
            "services-quality-manager-nqf6.html",
            "services-marketing-coordinator-nqf5.html",
            "services-contact-centre-manager-nqf5.html",
            "services-office-supervision-nqf5.html",
            "services-project-manager-nqf5.html",
            "services-quality-assurer-nqf5.html"
        ],
        "BATCH 6 - TETA & W&R SETA": [
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
    }

    # Base directory for qualifications
    qual_dir = Path("qualifications")

    if not qual_dir.exists():
        print(f"❌ Qualifications directory not found: {qual_dir}")
        return

    total_files = sum(len(files) for files in batches.values())
    updated_count = 0
    failed_count = 0

    print(f"🚀 Starting systematic update of {total_files} qualification files...")
    print("=" * 60)

    # Process each batch
    for batch_name, files in batches.items():
        print(f"\n📁 Processing {batch_name} ({len(files)} files)")
        print("-" * 40)

        for filename in files:
            filepath = qual_dir / filename

            if filepath.exists():
                if update_qualification_file(filepath):
                    updated_count += 1
                else:
                    failed_count += 1
            else:
                print(f"⚠️  File not found: {filename}")
                failed_count += 1

    # Final summary
    print("\n" + "=" * 60)
    print("📊 FINAL SUMMARY")
    print("=" * 60)
    print(f"✅ Successfully updated: {updated_count}/{total_files}")
    print(f"❌ Failed/Missing: {failed_count}/{total_files}")

    if updated_count == total_files:
        print("\n🎉 ALL QUALIFICATION PAGES SUCCESSFULLY UPDATED!")
        print("All files now have:")
        print("  ✓ Complete header with enhanced navigation")
        print("  ✓ Sticky banner with value-adds popup")
        print("  ✓ Proper breadcrumbs with SETA links")
        print("  ✓ Mobile-responsive JavaScript functionality")
        print("  ✓ Consistent branding and styling")
    else:
        print(f"\n⚠️  {failed_count} files need attention")

    print("\n🔄 All updates completed!")

if __name__ == "__main__":
    main()