#!/usr/bin/env python3
"""
Secondary refinement script for qualification HTML files
Handles additional color pattern updates missed in the first pass
"""

import os
import re
from pathlib import Path

# Additional refinements
REFINEMENT_UPDATES = {
    # Module card text colors that might have been missed
    r'font-bold text-lg text-gray-900 mb-3">': r'font-bold text-lg text-white mb-3">',
    r'text-sm text-gray-600">\s*<li>': r'text-sm text-white/90">\n                                <li>',

    # Check icons that might be green-500
    r'text-green-500 mr-3': r'text-[#ffa600] mr-3',

    # Related qualifications sections with various color schemes
    r'text-sm text-green-600 font-medium">NQF': r'text-sm text-[#ffa600] font-medium">NQF',
    r'text-sm text-indigo-600 font-medium">NQF': r'text-sm text-[#ffa600] font-medium">NQF',
    r'text-sm text-purple-600 font-medium">NQF': r'text-sm text-[#ffa600] font-medium">NQF',

    # Icon containers that might be various colors
    r'bg-indigo-100 rounded-lg flex': r'bg-[#ffffff]/70 rounded-lg flex',
    r'bg-purple-100 rounded-lg flex': r'bg-[#ffffff]/70 rounded-lg flex',
    r'bg-pink-100 rounded-lg flex': r'bg-[#ffffff]/70 rounded-lg flex',
    r'bg-teal-100 rounded-lg flex': r'bg-[#ffffff]/70 rounded-lg flex',

    # Icon colors in related sections
    r'text-indigo-600"\s*></i>': r'text-[#ffa600]"></i>',
    r'text-purple-600"\s*></i>': r'text-[#ffa600]"></i>',
    r'text-pink-600"\s*></i>': r'text-[#ffa600]"></i>',
    r'text-teal-600"\s*></i>': r'text-[#ffa600]"></i>',

    # Sidebar help section text colors
    r'text-blue-600 hover:text-blue-700 font-medium': r'text-[#ffa600] hover:text-[#ffa600] font-medium',

    # Sidebar "Apply for Learnership" button
    r'from-blue-600 to-purple-600 text-white font-bold py-3 px-6 rounded-lg text-center hover:from-blue-700 hover:to-purple-700': r'from-[#12265E] to-[#92ABC4] text-white font-bold py-3 px-6 rounded-lg text-center hover:from-[#0d1a47] hover:to-[#7a95af]',

    # Hero icon colors that might have been missed
    r'text-[#12265E]"></i>\s*</div>\s*<div>\s*<span class="text-[#12265E] font-semibold">NQF': r'text-[#ffa600]"></i>\n                        </div>\n                        <div>\n                            <span class="text-[#ffa600] font-semibold">NQF',

    # Stats box text colors
    r'<div class="text-xl font-bold text-\[#12265E\]">(\d+)</div>\s*<div class="text-sm text-gray-600">Credits</div>': r'<div class="text-xl font-bold text-white">\1</div>\n                            <div class="text-sm text-white/80">Credits</div>',
    r'<div class="text-xl font-bold text-\[#12265E\]">(\d+)</div>\s*<div class="text-sm text-gray-600">Months</div>': r'<div class="text-xl font-bold text-[#12265E]">\1</div>\n                            <div class="text-sm text-[#12265E]/80">Months</div>',
    r'<div class="text-xl font-bold text-white">(NQF \d+)</div>\s*<div class="text-sm text-gray-600">Level</div>': r'<div class="text-xl font-bold text-white">\1</div>\n                            <div class="text-sm text-white/80">Level</div>',
}

def refine_file(file_path):
    """Apply refinement updates to a single file"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = 0

        # Apply all refinement replacements
        for pattern, replacement in REFINEMENT_UPDATES.items():
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, replacement, content)
                changes_made += len(matches)

        # Write back if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        else:
            return False, 0

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

    print(f"Refining {len(html_files)} qualification files")
    print("=" * 80)

    refined_count = 0
    total_changes = 0

    for file_path in sorted(html_files):
        file_name = file_path.name
        success, changes = refine_file(file_path)

        if success:
            refined_count += 1
            if isinstance(changes, int):
                total_changes += changes
                print(f"[REFINED]: {file_name} ({changes} patterns updated)")
            else:
                print(f"[REFINED]: {file_name}")
        elif isinstance(changes, str) and "Error" in changes:
            print(f"[ERROR]: {file_name} - {changes}")

    print("\n" + "=" * 80)
    print(f"\nRefinement Summary:")
    print(f"  Files refined: {refined_count}")
    print(f"  Total pattern updates: {total_changes}")
    print(f"  Files unchanged: {len(html_files) - refined_count}")

if __name__ == "__main__":
    main()
