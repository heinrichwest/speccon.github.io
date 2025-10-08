#!/usr/bin/env python3
"""
Script to systematically fix all qualification pages to match the reference layout
"""

import os
import re

# List of files to fix based on user request
FILES_TO_FIX = [
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

# Base directory for qualification files
BASE_DIR = r"C:\Users\Asus\OneDrive - Speccon Holdings (Pty) Ltd\Websites\Speccon\qualifications"

# Sticky banner CSS to add
STICKY_BANNER_CSS = '''        .dropdown:hover .dropdown-menu {
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
        }'''

def check_file_status(filepath):
    """Check what components are missing from a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        missing = []

        # Check for correct header navigation
        if 'Why Choose Us' not in content:
            missing.append("Header navigation")

        # Check for Other Products dropdown
        if 'Other Products' not in content:
            missing.append("Other Products dropdown")

        # Check for mobile menu
        if 'mobile-menu' not in content:
            missing.append("Mobile menu")

        # Check for sticky banner CSS
        if '.sticky-banner {' not in content:
            missing.append("Sticky banner CSS")

        # Check for sticky banner HTML
        if 'Our Free Value Adds' not in content:
            missing.append("Sticky banner HTML")

        # Check for correct subtitle
        if any(x in content for x in ["Animal Production Qualification", "Plant Production Qualification", "Mixed Farming Qualification"]) and "SETA Qualifications" not in content:
            missing.append("Header subtitle correction")

        return missing

    except Exception as e:
        return [f"Error reading file: {e}"]

def main():
    """Main function to check all files"""
    print("Checking qualification pages for missing components...\n")

    for filename in FILES_TO_FIX:
        filepath = os.path.join(BASE_DIR, filename)

        if os.path.exists(filepath):
            missing = check_file_status(filepath)

            if missing:
                print(f"❌ {filename}:")
                for item in missing:
                    print(f"   - Missing: {item}")
            else:
                print(f"✅ {filename}: All components present")
        else:
            print(f"⚠️  {filename}: File not found")

        print()

if __name__ == "__main__":
    main()