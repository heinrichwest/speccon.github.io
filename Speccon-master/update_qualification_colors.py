#!/usr/bin/env python3
"""
Script to update all qualification HTML files with standardized SpecCon color scheme
Based on services-bookkeeper-nqf5.html reference template
"""

import os
import re
from pathlib import Path

# Define color mappings
COLOR_UPDATES = {
    # Header subtitle patterns
    r'text-sm text-gray-600">Services SETA': r'text-sm text-[#ffa600]">Services SETA',
    r'text-sm text-gray-600">AgriSETA': r'text-sm text-[#ffa600]">AgriSETA',
    r'text-sm text-gray-600">W&R SETA': r'text-sm text-[#ffa600]">W&R SETA',
    r'text-sm text-gray-600">INSETA': r'text-sm text-[#ffa600]">INSETA',
    r'text-sm text-gray-600">MICT SETA': r'text-sm text-[#ffa600]">MICT SETA',
    r'text-sm text-gray-600">ETDP SETA': r'text-sm text-[#ffa600]">ETDP SETA',
    r'text-sm text-gray-600">FASSET': r'text-sm text-[#ffa600]">FASSET',
    r'text-sm text-gray-600">TETA': r'text-sm text-[#ffa600]">TETA',
    r'text-sm text-gray-600">MER SETA': r'text-sm text-[#ffa600]">MER SETA',

    # Hero section - NQF level badge
    r'text-blue-600 font-semibold">NQF': r'text-[#ffa600] font-semibold">NQF',
    r'text-orange-600 font-semibold">NQF': r'text-[#ffa600] font-semibold">NQF',
    r'text-green-600 font-semibold">NQF': r'text-[#ffa600] font-semibold">NQF',

    # Main title in header
    r'text-xl font-bold text-gray-900">SpecCon': r'text-xl font-bold text-[#12265E]">SpecCon',

    # Section titles
    r'text-3xl font-bold text-gray-900 mb-8">Qualification Overview': r'text-3xl font-bold text-[#12265E] mb-8">Qualification Overview',
    r'text-2xl font-bold text-gray-900 mb-4">Learning Outcomes': r'text-2xl font-bold text-[#12265E] mb-4">Learning Outcomes',
    r'text-2xl font-bold text-gray-900 mb-4">Career Opportunities': r'text-2xl font-bold text-[#12265E] mb-4">Career Opportunities',
    r'text-2xl font-bold text-gray-900 mb-4">Entry Requirements': r'text-2xl font-bold text-[#12265E] mb-4">Entry Requirements',
    r'text-2xl font-bold text-gray-900 mb-6">Core Modules': r'text-2xl font-bold text-[#12265E] mb-6">Core Modules',
    r'text-2xl font-bold text-gray-900 mb-6">Workplace Experience': r'text-2xl font-bold text-[#12265E] mb-6">Workplace Experience',
    r'text-3xl font-bold text-gray-900 mb-6">Core Modules': r'text-3xl font-bold text-[#12265E] mb-6">Core Modules',
    r'text-xl font-bold text-gray-900 mb-6">Qualification Details': r'text-xl font-bold text-[#12265E] mb-6">Qualification Details',
    r'text-3xl md:text-4xl font-bold text-gray-900 mb-4">Related': r'text-3xl md:text-4xl font-bold text-[#12265E] mb-4">Related',

    # Hero title
    r'text-4xl md:text-5xl font-bold text-gray-900"': r'text-4xl md:text-5xl font-bold text-[#12265E]"',

    # Icon containers in hero
    r'bg-blue-100 rounded-2xl flex items-center justify-center': r'bg-[#ffffff]/70 rounded-2xl flex items-center justify-center',
    r'bg-green-100 rounded-2xl flex items-center justify-center': r'bg-[#ffffff]/70 rounded-2xl flex items-center justify-center',
    r'bg-orange-100 rounded-2xl flex items-center justify-center': r'bg-[#ffffff]/70 rounded-2xl flex items-center justify-center',

    # Icons in hero
    r'text-blue-600"\s*></i>': r'text-[#ffa600]"></i>',
    r'text-green-600"\s*></i>': r'text-[#ffa600]"></i>',
    r'text-orange-600"\s*></i>': r'text-[#ffa600]"></i>',

    # Stats boxes - need to be more specific
    r'text-xl font-bold text-blue-600">': r'text-xl font-bold text-white">',
    r'text-xl font-bold text-green-600">': r'text-xl font-bold text-[#12265E]">',
    r'text-xl font-bold text-purple-600">': r'text-xl font-bold text-white">',
    r'text-xl font-bold text-orange-600">': r'text-xl font-bold text-white">',

    # Buttons
    r'border-2 border-blue-600 text-blue-600': r'border-2 border-[#12265E] text-[#12265E]',
    r'hover:bg-blue-600 hover:text-white': r'hover:bg-[#12265E] hover:text-white',

    # Breadcrumb
    r'hover:text-blue-600">Home': r'hover:text-[#ffa600]">Home',
    r'hover:text-blue-600">Services SETA': r'hover:text-[#ffa600]">Services SETA',
    r'hover:text-blue-600">AgriSETA': r'hover:text-[#ffa600]">AgriSETA',
    r'hover:text-blue-600">W&R SETA': r'hover:text-[#ffa600]">W&R SETA',
    r'hover:text-blue-600">INSETA': r'hover:text-[#ffa600]">INSETA',
    r'hover:text-blue-600">MICT SETA': r'hover:text-[#ffa600]">MICT SETA',
    r'hover:text-blue-600">ETDP SETA': r'hover:text-[#ffa600]">ETDP SETA',
    r'text-gray-900">([^<]+NQF Level \d+)': r'text-[#12265E] font-semibold">\1',

    # Check icons
    r'text-blue-600 mr-3': r'text-[#ffa600] mr-3',
    r'text-green-600 mr-3': r'text-[#ffa600] mr-3',

    # Career opportunities icons
    r'text-blue-600 mr-3"\s*></i>': r'text-[#ffa600] mr-3"></i>',

    # Related qualifications icon containers
    r'bg-blue-100 rounded-lg flex': r'bg-[#ffffff]/70 rounded-lg flex',
    r'bg-green-100 rounded-lg flex': r'bg-[#ffffff]/70 rounded-lg flex',

    # Related qualifications icons
    r'text-blue-600"\s*></i>\s*</div>\s*<div>\s*<span class="text-sm text-blue-600': r'text-[#ffa600]"></i>\n                        </div>\n                        <div>\n                            <span class="text-sm text-[#ffa600]',
    r'text-green-600"\s*></i>\s*</div>\s*<div>\s*<span class="text-sm text-green-600': r'text-[#ffa600]"></i>\n                        </div>\n                        <div>\n                            <span class="text-sm text-[#ffa600]',

    # Related qualifications titles
    r'font-bold text-lg text-gray-900"': r'font-bold text-lg text-[#12265E]"',

    # Sidebar help section
    r'font-bold text-gray-900 mb-2">Need Help': r'font-bold text-[#12265E] mb-2">Need Help',
    r'hover:text-blue-600 font-medium': r'hover:text-[#ffa600] font-medium',
}

# Module card pattern updates
def update_module_cards(content):
    """Update module card backgrounds with alternating gradient pattern"""

    # Find all module card divs
    module_pattern = r'<div class="([^"]*(?:bg-white|bg-blue-50|bg-gray-50|bg-green-50|bg-orange-50)[^"]*) p-6 rounded-xl">'

    matches = list(re.finditer(module_pattern, content))

    # Replace from end to start to maintain positions
    for idx, match in enumerate(reversed(matches)):
        module_num = len(matches) - idx
        if module_num % 2 == 1:  # Odd modules
            new_class = 'bg-gradient-to-br from-[#12265E] to-[#92abc4] p-6 rounded-xl'
        else:  # Even modules
            new_class = 'bg-gradient-to-br from-[#92abc4] to-[#12265E] p-6 rounded-xl'

        old_div = match.group(0)
        new_div = f'<div class="{new_class}">'
        content = content[:match.start()] + new_div + content[match.end():]

    # Update module titles and text colors
    content = re.sub(r'font-bold text-lg text-gray-900 mb-3">Module', r'font-bold text-lg text-white mb-3">Module', content)
    content = re.sub(r'font-bold text-lg text-blue-600 mb-3">Module', r'font-bold text-lg text-white mb-3">Module', content)
    content = re.sub(r'text-sm text-gray-700">\s*<li>', r'text-sm text-white/90">\n                                <li>', content)
    content = re.sub(r'text-sm text-gray-600">\s*<li>', r'text-sm text-white/90">\n                                <li>', content)

    return content

def update_stats_boxes(content):
    """Update stats boxes with alternating colors"""

    # Pattern for stats boxes in hero section
    stats_pattern = r'<div class="text-center p-4 ([^"]*) rounded-lg shadow">'

    matches = list(re.finditer(stats_pattern, content))

    # Check if we're in the hero stats section (should be 3 boxes)
    if len(matches) >= 3:
        # Replace from end to start
        for idx, match in enumerate(reversed(matches[:3])):
            box_num = 3 - idx
            if box_num in [1, 3]:  # First and third
                new_class = 'text-center p-4 bg-[#12265E] rounded-lg shadow'
            else:  # Second
                new_class = 'text-center p-4 bg-[#92abc4] rounded-lg shadow'

            old_div = match.group(0)
            new_div = new_class + '">'
            content = content[:match.start()] + f'<div class="{new_div}' + content[match.end():]

    return content

def update_sidebar_help(content):
    """Update sidebar help section colors"""

    # Help section background
    content = re.sub(
        r'<div class="mt-8 p-4 ([^"]*bg-(?:blue|green|gray)-[^"]*) rounded-lg">',
        r'<div class="mt-8 p-4 bg-[#92abc4] rounded-lg">',
        content
    )

    return content

def process_file(file_path):
    """Process a single HTML file with color updates"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Apply all regex replacements
        for pattern, replacement in COLOR_UPDATES.items():
            content = re.sub(pattern, replacement, content)

        # Apply module card updates
        content = update_module_cards(content)

        # Apply stats box updates
        content = update_stats_boxes(content)

        # Apply sidebar help updates
        content = update_sidebar_help(content)

        # Write back if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Updated successfully"
        else:
            return False, "No changes needed"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main execution function"""

    # Get qualifications directory
    script_dir = Path(__file__).parent
    qual_dir = script_dir / "qualifications"

    if not qual_dir.exists():
        print(f"Error: Qualifications directory not found at {qual_dir}")
        return

    # Get all HTML files except template
    html_files = [f for f in qual_dir.glob("*.html") if f.name != "template-qualification.html"]

    print(f"Found {len(html_files)} qualification files to process\n")
    print("=" * 80)

    updated_count = 0
    error_count = 0
    skipped_count = 0

    results = []

    for file_path in sorted(html_files):
        file_name = file_path.name
        success, message = process_file(file_path)

        if success:
            updated_count += 1
            status = "[UPDATED]"
        elif "Error" in message:
            error_count += 1
            status = "[ERROR]"
        else:
            skipped_count += 1
            status = "[SKIPPED]"

        results.append({
            'file': file_name,
            'status': status,
            'message': message
        })

        print(f"{status}: {file_name}")
        if "Error" in message:
            print(f"  → {message}")

    print("\n" + "=" * 80)
    print(f"\nSummary:")
    print(f"  Total files processed: {len(html_files)}")
    print(f"  Files updated: {updated_count}")
    print(f"  Files skipped: {skipped_count}")
    print(f"  Errors: {error_count}")

    if error_count > 0:
        print(f"\nFiles with errors:")
        for result in results:
            if "ERROR" in result['status']:
                print(f"  - {result['file']}: {result['message']}")

if __name__ == "__main__":
    main()
