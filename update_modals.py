#!/usr/bin/env python3
"""
Centralized Modal System Implementation Script
This script updates all HTML pages to use the new centralized modal system
"""

import os
import re
from pathlib import Path

def update_index_page():
    """Update the main index.html page"""
    index_path = Path('index.html')

    if not index_path.exists():
        print("❌ index.html not found")
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add the centralized modals script
    if 'centralized-modals.js' not in content:
        # Add script before closing head tag
        content = content.replace(
            '</head>',
            '    <script src="js/centralized-modals.js"></script>\n</head>'
        )

    # Update Contact Us links to use centralized modal
    content = re.sub(
        r'<a[^>]*onclick="openContactPopup\(\)"[^>]*>([^<]*)</a>',
        r'<a href="#" data-modal="contact" class="contact-trigger">\1</a>',
        content
    )

    # Update navigation Contact Us links
    content = re.sub(
        r'<a[^>]*href="[^"]*#contact[^"]*"[^>]*>(Contact Us)</a>',
        r'<a href="#" data-modal="contact" class="contact-trigger">\1</a>',
        content
    )

    # Update Enquire Now / Apply buttons
    content = re.sub(
        r'<a[^>]*href="[^"]*#apply[^"]*"[^>]*>([^<]*(?:Enquire Now|Apply|APPLY FOR LEARNERSHIP)[^<]*)</a>',
        r'<a href="#" data-modal="enquire" class="enquire-trigger">\1</a>',
        content
    )

    # Remove old contact modal HTML (keep learnership modal for now)
    # Remove old contact modal CSS and JavaScript

    # Save the updated content
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Updated index.html")

def update_seta_pages():
    """Update all SETA pages"""
    setas_dir = Path('setas')

    if not setas_dir.exists():
        print("❌ setas directory not found")
        return

    for seta_file in setas_dir.glob('*.html'):
        with open(seta_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add the centralized modals script
        if 'centralized-modals.js' not in content:
            content = content.replace(
                '</head>',
                '    <script src="../js/centralized-modals.js"></script>\n</head>'
            )

        # Update Enquire Now buttons in qualification cards
        content = re.sub(
            r'<a[^>]*href="[^"]*#[^"]*"[^>]*class="[^"]*(?:bg-blue|bg-gradient)[^"]*"[^>]*>([^<]*(?:Enquire|Apply)[^<]*)</a>',
            r'<a href="#" data-modal="enquire" class="enquire-trigger bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors">\1</a>',
            content
        )

        # Update navigation Enquire Now links
        content = re.sub(
            r'<a[^>]*href="[^"]*index\.html#apply[^"]*"[^>]*>([^<]*(?:Enquire Now)[^<]*)</a>',
            r'<a href="#" data-modal="enquire" class="enquire-trigger">\1</a>',
            content
        )

        # Remove old enquiry modal CSS and JavaScript if present
        # Remove enquiry-modal classes and related styles

        with open(seta_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Updated {seta_file.name}")

def update_qualification_pages():
    """Update all qualification pages"""
    qualifications_dir = Path('qualifications')

    if not qualifications_dir.exists():
        print("❌ qualifications directory not found")
        return

    for qual_file in qualifications_dir.glob('*.html'):
        with open(qual_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add the centralized modals script
        if 'centralized-modals.js' not in content:
            content = content.replace(
                '</head>',
                '    <script src="../js/centralized-modals.js"></script>\n</head>'
            )

        # Update Enquire Now buttons in navigation and content
        content = re.sub(
            r'<a[^>]*href="[^"]*index\.html#apply[^"]*"[^>]*class="[^"]*(?:bg-gradient|bg-blue)[^"]*"[^>]*>([^<]*(?:Enquire Now)[^<]*)</a>',
            r'<a href="#" data-modal="enquire" class="enquire-trigger bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg">\1</a>',
            content
        )

        # Update mobile Enquire Now buttons
        content = re.sub(
            r'<a[^>]*href="[^"]*index\.html#apply[^"]*"[^>]*class="[^"]*(?:mt-2|w-full)[^"]*bg-gradient[^"]*"[^>]*>([^<]*(?:Enquire Now)[^<]*)</a>',
            r'<a href="#" data-modal="enquire" class="enquire-trigger mt-2 w-full bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-5 py-2 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg text-center block">\1</a>',
            content
        )

        # Update Contact Us links
        content = re.sub(
            r'<a[^>]*href="[^"]*index\.html#contact[^"]*"[^>]*>([^<]*(?:Contact Us)[^<]*)</a>',
            r'<a href="#" data-modal="contact" class="contact-trigger">\1</a>',
            content
        )

        with open(qual_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Updated {qual_file.name}")

def update_short_course_pages():
    """Update all short course pages"""
    short_courses_dir = Path('short-courses')

    if not short_courses_dir.exists():
        print("❌ short-courses directory not found")
        return

    for course_file in short_courses_dir.glob('*.html'):
        with open(course_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract course title from the page title or filename
        title_match = re.search(r'<title>([^<]+)</title>', content)
        if title_match:
            course_title = title_match.group(1).replace(' | SpecCon Holdings', '').strip()
        else:
            course_title = course_file.stem.replace('-', ' ').title()

        # Add the centralized modals script
        if 'centralized-modals.js' not in content:
            content = content.replace(
                '</head>',
                '    <script src="../js/centralized-modals.js"></script>\n</head>'
            )

        # Update Book Now buttons
        content = re.sub(
            r'<button[^>]*onclick="openApplicationModal\(\)"[^>]*>([^<]*(?:Book|Apply)[^<]*)</button>',
            f'<button data-modal="book" data-course="{course_title}" class="book-trigger bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700 transition-colors">\\1</button>',
            content
        )

        # Update Contact Us links
        content = re.sub(
            r'<a[^>]*href="[^"]*index\.html#contact[^"]*"[^>]*>([^<]*(?:Contact Us)[^<]*)</a>',
            r'<a href="#" data-modal="contact" class="contact-trigger">\1</a>',
            content
        )

        # Remove old application modal JavaScript
        content = re.sub(
            r'function openApplicationModal\(\)\s*\{[^}]*\}',
            '',
            content,
            flags=re.DOTALL
        )

        with open(course_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Updated {course_file.name}")

def create_backup():
    """Create backup of important files before modification"""
    backup_dir = Path('modal_backup')
    backup_dir.mkdir(exist_ok=True)

    # Backup index.html
    if Path('index.html').exists():
        Path('index.html').copy(backup_dir / 'index.html.backup')

    # Backup a few key qualification pages
    qual_dir = Path('qualifications')
    if qual_dir.exists():
        for qual_file in list(qual_dir.glob('*.html'))[:3]:  # Just backup first 3
            qual_file.copy(backup_dir / f"{qual_file.name}.backup")

    print("✅ Created backups in modal_backup directory")

def main():
    """Main execution function"""
    print("🚀 Starting Centralized Modal System Implementation")
    print("=" * 60)

    # Create backups first
    create_backup()

    # Update different page types
    print("\n📄 Updating main page...")
    update_index_page()

    print("\n🏢 Updating SETA pages...")
    update_seta_pages()

    print("\n🎓 Updating qualification pages...")
    update_qualification_pages()

    print("\n📚 Updating short course pages...")
    update_short_course_pages()

    print("\n" + "=" * 60)
    print("✅ Centralized Modal System Implementation Complete!")
    print("\n📋 Next Steps:")
    print("1. Test all modal functionality on different page types")
    print("2. Verify mobile responsiveness")
    print("3. Check that all 'Contact Us', 'Enquire Now', and 'Book Now' buttons work")
    print("4. Remove any remaining old modal code manually if needed")
    print("5. Update CLAUDE.md with modal implementation details")

    print("\n🔧 If you encounter issues:")
    print("- Check the console for JavaScript errors")
    print("- Verify script paths are correct for subdirectories")
    print("- Ensure Lucide icons are loaded before centralized-modals.js")
    print("- Review MODAL_IMPLEMENTATION_GUIDE.md for troubleshooting")

if __name__ == "__main__":
    main()