#!/usr/bin/env python3
"""
Add mobile menu to all SETA pages
"""

import os
import re
from pathlib import Path

# Mobile menu HTML to add after the "Enquire Now" button div
MOBILE_MENU_HTML = '''
                <!-- Mobile Menu Button -->
                <button id="mobileMenuBtn" class="lg:hidden text-[#12265E] focus:outline-none">
                    <i data-lucide="menu" class="w-6 h-6"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div id="mobileMenu" class="hidden lg:hidden bg-white border-t border-gray-200">
            <div class="container mx-auto px-4 py-4">
                <nav class="flex flex-col space-y-3">
                    <a href="../index.html#about" class="text-[#12265E] hover:text-[#ff9c2a] font-medium py-2 transition duration-300">Why Choose Us</a>
                    <a href="../index.html#qualifications" class="text-[#12265E] hover:text-[#ff9c2a] font-medium py-2 transition duration-300">Qualifications</a>
                    <a href="../index.html#accreditations" class="text-[#12265E] hover:text-[#ff9c2a] font-medium py-2 transition duration-300">Accreditations</a>
                    <a href="../index.html#classroom-training" class="text-[#12265E] hover:text-[#ff9c2a] font-medium py-2 transition duration-300">Classroom Training</a>

                    <!-- Mobile Dropdown -->
                    <div class="border-t border-gray-200 pt-3">
                        <p class="text-sm font-semibold text-gray-500 mb-2">Other Products</p>
                        <a href="https://elearning.co.za/" target="_blank" class="block text-[#12265E] hover:text-[#ff9c2a] py-2 pl-4 transition duration-300">
                            <i data-lucide="monitor" class="w-4 h-4 inline mr-2"></i>Online Training
                        </a>
                        <a href="https://employmentequityact.co.za/" target="_blank" class="block text-[#12265E] hover:text-[#ff9c2a] py-2 pl-4 transition duration-300">
                            <i data-lucide="shield-check" class="w-4 h-4 inline mr-2"></i>Employment Equity
                        </a>
                        <a href="https://learningmanagementsystem.co.za/" target="_blank" class="block text-[#12265E] hover:text-[#ff9c2a] py-2 pl-4 transition duration-300">
                            <i data-lucide="graduation-cap" class="w-4 h-4 inline mr-2"></i>Learning Management System
                        </a>
                        <a href="https://skillsdevelopment.co.za/" target="_blank" class="block text-[#12265E] hover:text-[#ff9c2a] py-2 pl-4 transition duration-300">
                            <i data-lucide="trending-up" class="w-4 h-4 inline mr-2"></i>Skills Development
                        </a>
                        <a href="https://www.specconacademy.co.za/" target="_blank" class="block text-[#12265E] hover:text-[#ff9c2a] py-2 pl-4 transition duration-300">
                            <i data-lucide="school" class="w-4 h-4 inline mr-2"></i>SpecCon Academy
                        </a>
                        <a href="https://bbbee.co.za/" target="_blank" class="block text-[#12265E] hover:text-[#ff9c2a] py-2 pl-4 transition duration-300">
                            <i data-lucide="award" class="w-4 h-4 inline mr-2"></i>BBBEE Consulting
                        </a>
                    </div>

                    <button onclick="openEnquiryModal()" class="bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg mt-4">
                        Enquire Now
                    </button>
                </nav>
            </div>
        </div>
    </header>'''

# Mobile menu JavaScript
MOBILE_MENU_JS = '''
    <!-- Mobile Menu Toggle JavaScript -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenuBtn = document.getElementById('mobileMenuBtn');
            const mobileMenu = document.getElementById('mobileMenu');

            if (mobileMenuBtn && mobileMenu) {
                mobileMenuBtn.addEventListener('click', function() {
                    mobileMenu.classList.toggle('hidden');
                });
            }
        });
    </script>
</body>
</html>'''

def add_mobile_menu(file_path):
    """Add mobile menu to a SETA HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Check if mobile menu already exists
        if 'id="mobileMenuBtn"' in content:
            print(f"Mobile menu already exists in {file_path}")
            return False

        # Pattern to find the closing of the header div structure
        # Look for the "Enquire Now" button block followed by closing divs and header
        pattern = r'(                <div class="hidden lg:block">\s+<button onclick="openEnquiryModal\(\)"[^>]*>.*?</button>\s+</div>\s+</div>\s+</div>\s+</header>)'

        if re.search(pattern, content, re.DOTALL):
            # Replace with mobile menu added
            content = re.sub(
                pattern,
                lambda m: m.group(0).replace('</div>\n            </div>\n        </div>\n    </header>', MOBILE_MENU_HTML),
                content,
                flags=re.DOTALL
            )
        else:
            print(f"Pattern not found in {file_path}")
            return False

        # Add mobile menu JavaScript before closing body tag
        if '</body>\n</html>' in content and 'Mobile Menu Toggle JavaScript' not in content:
            content = content.replace('</body>\n</html>', MOBILE_MENU_JS)

        # Only save if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    base_dir = Path('Speccon-master/setas')

    # Process remaining SETA files (excluding services-seta.html and agriseta.html which are already done)
    files_to_process = [
        'etdp-seta.html',
        'fasset.html',
        'inseta.html',
        'mer-seta.html',
        'mict-seta.html',
        'teta-seta.html',
        'wr-seta.html'
    ]

    updated_count = 0
    for filename in files_to_process:
        file_path = base_dir / filename
        if file_path.exists():
            if add_mobile_menu(str(file_path)):
                updated_count += 1
                print(f"Updated: {file_path}")

    print(f"\nUpdated {updated_count} files with mobile menus")

if __name__ == '__main__':
    main()
