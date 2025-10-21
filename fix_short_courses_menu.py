#!/usr/bin/env python3
"""
Fix navigation menus in all short-course HTML files
"""

import os
import re
import sys

# Ensure UTF-8 encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = r'C:\Users\Speccon\Documents\Websites\Speccon-master\short-courses'

# Correct navigation HTML according to CLAUDE.md guidelines
CORRECT_NAV = '''                <nav class="hidden lg:flex items-center space-x-8">
                    <a href="../index.html#about" class="text-[#12265E] hover:text-[#FFA600] font-medium transition duration-300">Why Choose Us</a>
                    <a href="../index.html#qualifications" class="text-[#12265E] hover:text-[#FFA600] font-medium transition duration-300">Qualifications</a>
                    <a href="../index.html#accreditations" class="text-[#12265E] hover:text-[#FFA600] font-medium transition duration-300">Accreditations</a>
                    <a href="../index.html#classroom-training" class="text-[#12265E] hover:text-[#FFA600] font-medium transition duration-300">Classroom Training</a>
                    <div class="relative dropdown">
                        <button class="text-[#12265E] hover:text-[#FFA600] font-medium transition duration-300 inline-flex items-center">
                            Other Products <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i>
                        </button>
                        <div class="dropdown-menu absolute left-0 w-64 bg-white rounded-lg shadow-xl py-2 z-20 border">
                            <a href="https://elearning.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-[#12265E]/10 hover:text-[#12265E] transition duration-200">
                                <i data-lucide="monitor" class="w-4 h-4 inline mr-2"></i>Online Training
                            </a>
                            <a href="https://employmentequityact.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-[#12265E]/10 hover:text-[#12265E] transition duration-200">
                                <i data-lucide="shield-check" class="w-4 h-4 inline mr-2"></i>Employment Equity
                            </a>
                            <a href="https://learningmanagementsystem.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-[#12265E]/10 hover:text-[#12265E] transition duration-200">
                                <i data-lucide="graduation-cap" class="w-4 h-4 inline mr-2"></i>Learning Management System
                            </a>
                            <a href="https://skillsdevelopment.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-[#12265E]/10 hover:text-[#12265E] transition duration-200">
                                <i data-lucide="trending-up" class="w-4 h-4 inline mr-2"></i>Skills Development
                            </a>
                            <a href="https://www.specconacademy.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-[#12265E]/10 hover:text-[#12265E] transition duration-200">
                                <i data-lucide="school" class="w-4 h-4 inline mr-2"></i>SpecCon Academy
                            </a>
                            <a href="https://bbbee.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-[#12265E]/10 hover:text-[#12265E] transition duration-200">
                                <i data-lucide="award" class="w-4 h-4 inline mr-2"></i>BBBEE Consulting
                            </a>
                        </div>
                    </div>
                </nav>'''

def fix_navigation(content):
    """Fix navigation menu in HTML content"""

    # Fix subtitle from "Services SETA Qualifications" to "Classroom Training"
    content = re.sub(
        r'<p class="text-sm text-\[#ffa600\]">Services SETA Qualifications</p>',
        '<p class="text-sm text-[#ffa600]">Classroom Training</p>',
        content
    )

    # Fix navigation section - match from <nav to </nav> including nested elements
    nav_pattern = r'<nav class="hidden lg:flex[^>]*>.*?</nav>'
    content = re.sub(nav_pattern, CORRECT_NAV, content, flags=re.DOTALL)

    return content

def process_file(filepath):
    """Process a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file needs fixing
        if '../home.html' in content or 'Services SETA Qualifications' in content or 'employmentequityact.za' in content:
            original_content = content
            content = fix_navigation(content)

            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
    except Exception as e:
        print(f"❌ Error processing {os.path.basename(filepath)}: {e}")
        return False

    return False

def main():
    """Main function to process all short-course files"""
    print("🔧 Fixing navigation menus in short-courses directory...\n")

    # Get all HTML files
    html_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]

    if not html_files:
        print("❌ No HTML files found in short-courses directory")
        return

    print(f"📁 Found {len(html_files)} HTML files\n")

    fixed_count = 0
    for filename in sorted(html_files):
        filepath = os.path.join(BASE_DIR, filename)
        if process_file(filepath):
            print(f"✅ Fixed: {filename}")
            fixed_count += 1
        else:
            print(f"⏭️  Skipped: {filename} (no changes needed)")

    print(f"\n✨ Complete! Fixed {fixed_count}/{len(html_files)} files")

if __name__ == '__main__':
    main()
