#!/usr/bin/env python3
"""
Fix remaining navigation styling patterns
"""
import os
import re
from pathlib import Path

def update_file(filepath):
    """Update a single HTML file with remaining navigation styling fixes"""
    changes = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern 1: text-gray-700 hover:text-[#FFA600] (SETA files mainly)
        pattern1 = r'class="text-gray-700 hover:text-\[#FFA600\]'
        replacement1 = r'class="text-[#12265E] hover:text-[#FFA600]'
        content, count1 = re.subn(pattern1, replacement1, content)
        if count1 > 0:
            changes.append(f"Nav links text-gray-700: {count1} replacements")

        # Pattern 2: text-gray-600 hover:text-blue (mobile menus in short courses)
        pattern2 = r'class="block py-2 text-gray-600 hover:text-blue-\d+'
        def replace2(match):
            return r'class="block py-2 text-[#12265E] hover:text-[#FFA600]'
        content, count2 = re.subn(pattern2, replace2, content)
        if count2 > 0:
            changes.append(f"Mobile menu text-gray-600: {count2} replacements")

        # Pattern 3: Any remaining hover:text-blue-600 in navigation context
        pattern3 = r'(class="[^"]*(?:nav|menu)[^"]*)\bhover:text-blue-600\b'
        replacement3 = r'\1hover:text-[#FFA600]'
        content, count3 = re.subn(pattern3, replacement3, content, flags=re.IGNORECASE)
        if count3 > 0:
            changes.append(f"Remaining hover:text-blue-600: {count3} replacements")

        # Pattern 4: text-gray-600 in general navigation links
        pattern4 = r'<a href="[^"]*" class="block py-2 text-gray-600 hover:'
        replacement4 = r'<a href="\g<0>" class="block py-2 text-[#12265E] hover:'
        # More precise replacement
        content = re.sub(
            r'(<a href="[^"]*" class=")text-gray-600 hover:text-blue-\d+(")',
            r'\1text-[#12265E] hover:text-[#FFA600]\2',
            content
        )

        # Pattern 5: Button with text-gray-700
        pattern5 = r'<button class="text-gray-700 hover:'
        if pattern5 in content:
            content = re.sub(
                r'(<button class=")text-gray-700 hover:',
                r'\1text-[#12265E] hover:',
                content
            )
            changes.append("Button text-gray-700: updated")

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

    # Target specific files that still need updates
    files_to_check = [
        # SETA files
        base_dir / 'setas' / 'agriseta.html',
        base_dir / 'setas' / 'etdp-seta.html',
        base_dir / 'setas' / 'fasset.html',
        base_dir / 'setas' / 'inseta.html',
        base_dir / 'setas' / 'mer-seta.html',
        base_dir / 'setas' / 'mict-seta.html',
        base_dir / 'setas' / 'services-seta.html',
        base_dir / 'setas' / 'teta-seta.html',
        base_dir / 'setas' / 'wr-seta.html',
        # Short course files
        base_dir / 'short-courses' / 'advanced-ai-training.html',
        base_dir / 'short-courses' / 'intro-to-ai-training.html',
        base_dir / 'short-courses' / 'stress-management-training.html',
        base_dir / 'short-courses' / 'ai-training.html',
        # Qualification files
        base_dir / 'qualifications' / 'etdp-training-development-nqf3.html',
    ]

    total_updated = 0
    all_changes = []

    for filepath in files_to_check:
        if not filepath.exists():
            continue

        updated, changes = update_file(filepath)
        if updated:
            total_updated += 1
            all_changes.append({
                'file': str(filepath.relative_to(base_dir)),
                'changes': changes
            })

    # Print summary
    print("\n" + "="*80)
    print("REMAINING NAVIGATION FIXES SUMMARY")
    print("="*80 + "\n")

    for item in all_changes:
        print(f"Updated: {item['file']}")
        for change in item['changes']:
            print(f"  - {change}")
        print()

    print(f"TOTAL: {total_updated} files updated\n")
    print("="*80)

if __name__ == '__main__':
    main()
