#!/usr/bin/env python3
"""
Script to add or update "Apply for This Qualification" buttons in all qualification pages.
This script ensures all qualification pages have the correct button with proper styling and function calls.
"""

import os
import re
from pathlib import Path

# Configuration
QUALIFICATIONS_DIR = r"C:\Users\Speccon\Documents\Websites\Speccon-master\Speccon-master\qualifications"

# Statistics
stats = {
    'total_files': 0,
    'button_added': [],
    'button_updated': [],
    'already_correct': [],
    'errors': []
}

def detect_seta_colors(content):
    """Detect SETA type and return appropriate button colors."""
    if 'W&R SETA' in content or 'wr-' in content:
        return 'from-orange-600 to-red-600', 'from-orange-700 to-red-700'
    elif 'AgriSETA' in content or 'agri-' in content:
        return 'from-[#12265E] to-[#4A90E2]', 'from-[#0d1a47] to-[#3a7bc8]'
    elif 'MICT SETA' in content or 'mict-' in content:
        return 'from-blue-600 to-indigo-600', 'from-blue-700 to-indigo-700'
    elif 'INSETA' in content or 'inseta-' in content:
        return 'from-teal-600 to-cyan-600', 'from-teal-700 to-cyan-700'
    elif 'ETDP SETA' in content or 'etdp-' in content:
        return 'from-purple-600 to-indigo-600', 'from-purple-700 to-indigo-700'
    elif 'Services SETA' in content or 'services-' in content:
        return 'from-[#12265E] to-[#4A90E2]', 'from-[#0d1a47] to-[#3a7bc8]'
    else:
        # Default colors
        return 'from-[#12265E] to-[#4A90E2]', 'from-[#0d1a47] to-[#3a7bc8]'

def create_apply_button(base_color, hover_color):
    """Create the apply button HTML."""
    return f'''<button onclick="openEnquireModal()" class="bg-gradient-to-r {base_color} text-white font-semibold px-8 py-4 rounded-lg hover:{hover_color} transition duration-300 text-center">
                        Apply for This Qualification
                    </button>'''

def process_file(filepath):
    """Process a single qualification file."""
    filename = os.path.basename(filepath)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Detect SETA colors
        base_color, hover_color = detect_seta_colors(content)
        correct_button = create_apply_button(base_color, hover_color)

        # Check if file already has the correct button
        if 'Apply for This Qualification' in content and 'openEnquireModal()' in content:
            # Check if it's in the hero section (before "Qualification Details" or similar)
            hero_section_match = re.search(r'<!-- Hero Section -->.*?(?=<!-- [A-Z]|<section class="py-16 bg-white">|<section class="py-20">)', content, re.DOTALL)
            if hero_section_match and 'Apply for This Qualification' in hero_section_match.group():
                stats['already_correct'].append(filename)
                return False

        # Fix incorrect function names (openEnquireModal with typo)
        if 'openEnquireModal()' in content:
            content = content.replace('openEnquireModal()', 'openEnquireModal()')
            stats['button_updated'].append(f"{filename} - Fixed typo in function name")

        # Pattern to find the stats/credits section in hero
        stats_section_pattern = r'(<div class="grid grid-cols-[23] gap-[46] mb-8">.*?</div>)\s*</div>'

        # Check if there's already an Apply button in hero section
        hero_button_patterns = [
            r'<button[^>]*onclick="[^"]*"[^>]*>\s*Apply[^<]*</button>',
            r'<button[^>]*>\s*Apply[^<]*</button>',
            r'<a[^>]*>\s*Apply[^<]*</a>'
        ]

        has_apply_button = False
        for pattern in hero_button_patterns:
            if re.search(pattern, content[:10000]):  # Check first 10k chars (hero section)
                has_apply_button = True
                break

        if not has_apply_button:
            # Need to add button after stats section
            match = re.search(stats_section_pattern, content, re.DOTALL)
            if match:
                # Insert button container after stats
                button_html = f'''
                    <div class="flex flex-col sm:flex-row gap-4">
                        {correct_button}
                        <button onclick="openContactModal()" class="border-2 border-blue-600 text-blue-600 font-semibold px-8 py-4 rounded-lg hover:bg-blue-600 hover:text-white transition duration-300 text-center">
                            Get More Info
                        </button>
                    </div>'''

                insert_pos = match.end()
                content = content[:insert_pos] + button_html + content[insert_pos:]
                stats['button_added'].append(filename)
            else:
                # Fallback: Try to find after the description paragraph in hero
                hero_match = re.search(r'<!-- Hero Section -->.*?<p class="text-[^"]*">(.*?)</p>', content, re.DOTALL)
                if hero_match:
                    insert_pos = hero_match.end()
                    button_html = f'''
                    <div class="flex flex-col sm:flex-row gap-4 mb-8">
                        {correct_button}
                        <button onclick="openContactModal()" class="border-2 border-blue-600 text-blue-600 font-semibold px-8 py-4 rounded-lg hover:bg-blue-600 hover:text-white transition duration-300 text-center">
                            Get More Info
                        </button>
                    </div>'''
                    content = content[:insert_pos] + button_html + content[insert_pos:]
                    stats['button_added'].append(filename)
        else:
            # Update existing button text and function
            # Pattern to find Apply buttons with wrong text or function
            old_patterns = [
                (r'<button[^>]*onclick="openEnquiry\(\)"[^>]*>\s*Apply Now\s*</button>', 'Apply Now'),
                (r'<button[^>]*onclick="openEnquiry\(\)"[^>]*>\s*Apply for Qualification\s*</button>', 'Apply for Qualification'),
                (r'<button[^>]*onclick="openEnquiryModal\(\)"[^>]*>\s*Apply for this Qualification\s*</button>', 'Apply for this Qualification'),
                (r'<button[^>]*>\s*Apply for this Qualification\s*</button>', 'Apply for this Qualification (lowercase)'),
            ]

            for pattern, desc in old_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    # Extract and preserve the button classes if they exist
                    old_button_match = re.search(pattern, content, re.IGNORECASE)
                    if old_button_match:
                        content = re.sub(pattern, correct_button, content, flags=re.IGNORECASE)
                        stats['button_updated'].append(f"{filename} - Updated '{desc}' to 'Apply for This Qualification'")
                        break

        # Write back if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        stats['errors'].append(f"{filename}: {str(e)}")
        return False

def main():
    """Main function to process all qualification files."""
    print("=" * 80)
    print("Adding/Updating 'Apply for This Qualification' Buttons")
    print("=" * 80)
    print()

    # Get all HTML files in qualifications directory
    html_files = list(Path(QUALIFICATIONS_DIR).glob('*.html'))
    stats['total_files'] = len(html_files)

    print(f"Found {stats['total_files']} HTML files in qualifications directory")
    print()

    # Process each file
    for filepath in sorted(html_files):
        if filepath.name == 'template-qualification.html':
            continue  # Skip template

        process_file(filepath)

    # Print summary
    print()
    print("=" * 80)
    print("SUMMARY REPORT")
    print("=" * 80)
    print()
    print(f"Total files checked: {stats['total_files'] - 1}")  # -1 for template
    print(f"Buttons added: {len(stats['button_added'])}")
    print(f"Buttons updated: {len(stats['button_updated'])}")
    print(f"Already correct: {len(stats['already_correct'])}")
    print(f"Errors: {len(stats['errors'])}")
    print()

    if stats['button_added']:
        print("FILES WHERE BUTTON WAS ADDED:")
        for filename in sorted(stats['button_added']):
            print(f"  ✓ {filename}")
        print()

    if stats['button_updated']:
        print("FILES WHERE BUTTON WAS UPDATED:")
        for update in sorted(stats['button_updated']):
            print(f"  ✓ {update}")
        print()

    if stats['already_correct']:
        print(f"FILES THAT ALREADY HAD CORRECT BUTTON: {len(stats['already_correct'])}")
        print()

    if stats['errors']:
        print("ERRORS:")
        for error in stats['errors']:
            print(f"  ✗ {error}")
        print()

    # List all modified files
    all_modified = stats['button_added'] + [u.split(' - ')[0] for u in stats['button_updated']]
    if all_modified:
        print("=" * 80)
        print("ALL MODIFIED FILES:")
        print("=" * 80)
        for filename in sorted(set(all_modified)):
            print(f"  {os.path.join(QUALIFICATIONS_DIR, filename)}")
        print()

if __name__ == "__main__":
    main()
