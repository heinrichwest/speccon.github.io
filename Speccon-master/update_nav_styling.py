#!/usr/bin/env python3
"""
Update navigation menu styling across all HTML files to match index.html
"""
import os
import re
from pathlib import Path

def update_file(filepath):
    """Update a single HTML file with new navigation styling"""
    changes = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. Update desktop navigation links - text-gray-700 to text-[#12265E]
        pattern1 = r'class="text-gray-700 hover:text-blue-600 font-medium'
        replacement1 = r'class="text-[#12265E] hover:text-[#FFA600] font-medium'
        content, count1 = re.subn(pattern1, replacement1, content)
        if count1 > 0:
            changes.append(f"Desktop nav links: {count1} replacements")

        # 2. Update dropdown button - text-gray-700 to text-[#12265E]
        pattern2 = r'<button class="text-gray-700 hover:text-blue-600 font-medium'
        replacement2 = r'<button class="text-[#12265E] hover:text-[#FFA600] font-medium'
        content, count2 = re.subn(pattern2, replacement2, content)
        if count2 > 0:
            changes.append(f"Dropdown button: {count2} replacements")

        # 3. Update dropdown menu items - hover:bg-blue-50 hover:text-blue-600
        pattern3 = r'hover:bg-blue-50 hover:text-blue-600'
        replacement3 = r'hover:bg-[#12265E]/10 hover:text-[#12265E]'
        content, count3 = re.subn(pattern3, replacement3, content)
        if count3 > 0:
            changes.append(f"Dropdown items (blue): {count3} replacements")

        # 4. Update dropdown menu items - hover:bg-[#92ABC4]/20 hover:text-[#FFA600]
        pattern4 = r'hover:bg-\[#92ABC4\]/20 hover:text-\[#FFA600\]'
        replacement4 = r'hover:bg-[#12265E]/10 hover:text-[#12265E]'
        content, count4 = re.subn(pattern4, replacement4, content)
        if count4 > 0:
            changes.append(f"Dropdown items (92ABC4): {count4} replacements")

        # 5. Update dropdown menu items - case insensitive variant
        pattern5 = r'hover:bg-\[#92abc4\]/20 hover:text-\[#FFA600\]'
        replacement5 = r'hover:bg-[#12265E]/10 hover:text-[#12265E]'
        content, count5 = re.subn(pattern5, replacement5, content)
        if count5 > 0:
            changes.append(f"Dropdown items (92abc4): {count5} replacements")

        # 6. Update mobile menu links - text-gray-600 to text-[#12265E]
        pattern6 = r'class="block py-2 text-gray-600 hover:text-blue-600"'
        replacement6 = r'class="block py-2 text-[#12265E] hover:text-[#FFA600]"'
        content, count6 = re.subn(pattern6, replacement6, content)
        if count6 > 0:
            changes.append(f"Mobile menu links: {count6} replacements")

        # 7. Update body font-family from Inter to Roboto
        pattern7 = r"body\s*{\s*font-family:\s*'Inter',\s*sans-serif;"
        replacement7 = r"body {\n            font-family: 'Roboto', sans-serif;"
        content, count7 = re.subn(pattern7, replacement7, content)
        if count7 > 0:
            changes.append(f"Body font: {count7} replacements")

        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes
        else:
            return False, []

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False, []

def main():
    base_dir = Path(__file__).parent

    # Define file patterns to update
    file_groups = {
        'qualifications': list((base_dir / 'qualifications').glob('*.html')),
        'setas': list((base_dir / 'setas').glob('*.html')),
        'short-courses': list((base_dir / 'short-courses').glob('*.html')),
        'root': [base_dir / 'learnership-application.html']
    }

    # Exclude patterns
    exclude_patterns = ['.backup', '.tmp', 'template-qualification.html']

    total_updated = 0
    summary = {}

    for group_name, files in file_groups.items():
        updated_count = 0
        group_changes = []

        for filepath in files:
            # Skip excluded files
            if any(pattern in str(filepath) for pattern in exclude_patterns):
                continue

            # Skip if file doesn't exist
            if not filepath.exists():
                continue

            updated, changes = update_file(filepath)
            if updated:
                updated_count += 1
                total_updated += 1
                group_changes.append({
                    'file': filepath.name,
                    'changes': changes
                })

        summary[group_name] = {
            'count': updated_count,
            'files': group_changes
        }

    # Print summary
    print("\n" + "="*80)
    print("NAVIGATION STYLING UPDATE SUMMARY")
    print("="*80 + "\n")

    for group_name, data in summary.items():
        print(f"{group_name.upper()}: {data['count']} files updated")
        for file_info in data['files']:
            print(f"  - {file_info['file']}")
            for change in file_info['changes']:
                print(f"    * {change}")
        print()

    print(f"TOTAL: {total_updated} files updated\n")
    print("="*80)

if __name__ == '__main__':
    main()
