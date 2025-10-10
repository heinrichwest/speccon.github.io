#!/usr/bin/env python3
"""
Script to update credits text color to white where background is #12265E or #92abc4
"""

import re
from pathlib import Path

def fix_credits_color(content):
    """Fix credits text color to white on colored backgrounds"""

    # Pattern 1: Fix "Credits" label in stats boxes with bg-[#12265E]
    # Change text-gray-600 or similar to text-white/80
    pattern1 = r'(<div class="text-center p-4 bg-\[#12265E\] rounded-lg shadow">.*?<div class="text-xl font-bold text-white">\d+</div>\s*<div class="text-sm )text-gray-\d+(">(Credits|Days)</div>)'
    content = re.sub(pattern1, r'\1text-white/80\2', content, flags=re.DOTALL)

    # Pattern 2: Fix number and label in stats boxes with bg-[#92abc4]
    # Change text-[#12265E] to text-white
    pattern2 = r'(<div class="text-center p-4 bg-\[#92abc4\] rounded-lg shadow">.*?<div class="text-xl font-bold )text-\[#12265E\](">\d+</div>\s*<div class="text-sm )text-\[#12265E\]/\d+(">(Credits|Days|Months|Level)</div>)'
    content = re.sub(pattern2, r'\1text-white\2text-white/80\3', content, flags=re.DOTALL)

    # Pattern 3: Alternative - stats boxes with bg-[#92abc4] and different structure
    pattern3 = r'(<div class="text-center p-4 bg-\[#92abc4\] rounded-lg shadow">.*?<div class="text-xl font-bold )text-\[#12265E\](">[^<]+</div>\s*<div class="text-sm )text-\[#12265E\]/\d+(">[^<]+</div>)'
    content = re.sub(pattern3, r'\1text-white\2text-white/80\3', content, flags=re.DOTALL)

    # Pattern 4: Fix text-[#ffa600] to text-white in bg-[#12265E] contexts (SETA pages)
    pattern4 = r'(<div class="text-2xl font-bold )text-\[#ffa600\](">)(\d+)(</div>\s*<div class="text-sm )text-\[#ffffff\](">(Credits|Qualifications)</div>)'
    content = re.sub(pattern4, r'\1text-white\2\3\4text-white\5', content, flags=re.DOTALL)

    # Pattern 5: Fix remaining orange text in blue boxes
    pattern5 = r'(bg-\[#12265E\] rounded-lg shadow">.*?<div class="text-2xl font-bold )text-\[#ffa600\](">)'
    content = re.sub(pattern5, r'\1text-white\2', content, flags=re.DOTALL)

    # Pattern 6: Fix text on blue backgrounds - broader pattern
    pattern6 = r'(<div class="text-center p-4 bg-\[#12265E\] rounded-lg shadow">.*?<div class="text-xl font-bold )text-\[#ffa600\](">)'
    content = re.sub(pattern6, r'\1text-white\2', content, flags=re.DOTALL)

    # Pattern 7: Fix text-[#12265E]/80 to text-white/80 in light blue backgrounds
    pattern7 = r'(bg-\[#92abc4\][^>]*>.*?)text-\[#12265E\]/80'
    content = re.sub(pattern7, r'\1text-white/80', content, flags=re.DOTALL)

    return content

def process_qualification_files():
    """Process all HTML files in the qualifications folder"""

    qualifications_dir = Path('qualifications')

    if not qualifications_dir.exists():
        print(f"Error: {qualifications_dir} directory not found")
        return

    # Get all .html files (excluding .backup files)
    html_files = [f for f in qualifications_dir.glob('*.html') if not f.name.endswith('.backup') and f.name != 'template-qualification.html']

    print(f"Found {len(html_files)} HTML files to process")
    print("="*60)

    processed_count = 0
    error_count = 0

    for html_file in html_files:
        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Fix credits color
            updated_content = fix_credits_color(content)

            if updated_content != original_content:
                # Write back to file
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                processed_count += 1
                print(f"[OK] Updated: {html_file.name}")
            else:
                print(f"[SKIP] No changes: {html_file.name}")

        except Exception as e:
            error_count += 1
            print(f"[ERROR] Error processing {html_file.name}: {str(e)}")

    print("="*60)
    print(f"Processing complete!")
    print(f"Files updated: {processed_count}")
    print(f"Errors: {error_count}")
    print("="*60)

if __name__ == '__main__':
    process_qualification_files()
