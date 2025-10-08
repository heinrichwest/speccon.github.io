#!/usr/bin/env python3
"""
Final cleanup of all remaining navigation patterns
"""
import os
import re
from pathlib import Path

def update_file(filepath):
    """Update a single HTML file with all remaining navigation patterns"""
    changes = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern 1: Any text-gray-700 hover:text-* in navigation
        pattern1 = r'text-gray-700 hover:text-[^\s"]+(["\s])'
        def replace1(match):
            return f'text-[#12265E] hover:text-[#FFA600]{match.group(1)}'
        content, count1 = re.subn(pattern1, replace1, content)
        if count1 > 0:
            changes.append(f"text-gray-700 patterns: {count1} replacements")

        # Pattern 2: Any text-gray-600 hover:text-blue* in navigation
        pattern2 = r'text-gray-600 hover:text-blue-\d+'
        replacement2 = r'text-[#12265E] hover:text-[#FFA600]'
        content, count2 = re.subn(pattern2, replacement2, content)
        if count2 > 0:
            changes.append(f"text-gray-600 hover:text-blue: {count2} replacements")

        # Pattern 3: hover:bg-[#92ABC4]/20 or hover:bg-[#92abc4]/20
        pattern3 = r'hover:bg-\[#92[Aa][Bb][Cc]4\]/20'
        replacement3 = r'hover:bg-[#12265E]/10'
        content, count3 = re.subn(pattern3, replacement3, content)
        if count3 > 0:
            changes.append(f"hover:bg-[#92ABC4]/20: {count3} replacements")

        # Pattern 4: Ensure hover:text-[#FFA600] follows the dropdown colors
        pattern4 = r'hover:bg-\[#12265E\]/10 hover:text-\[#FFA600\]'
        replacement4 = r'hover:bg-[#12265E]/10 hover:text-[#12265E]'
        content, count4 = re.subn(pattern4, replacement4, content)
        if count4 > 0:
            changes.append(f"Dropdown hover text fix: {count4} replacements")

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

    # Find all remaining files with issues
    problem_files = [
        base_dir / 'short-courses' / 'advanced-ai-training.html',
        base_dir / 'short-courses' / 'intro-to-ai-training.html',
        base_dir / 'short-courses' / 'stress-management-training.html',
        base_dir / 'qualifications' / 'etdp-training-development-nqf3.html',
    ]

    total_updated = 0
    all_changes = []

    for filepath in problem_files:
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
    print("FINAL NAVIGATION CLEANUP SUMMARY")
    print("="*80 + "\n")

    if all_changes:
        for item in all_changes:
            print(f"Updated: {item['file']}")
            for change in item['changes']:
                print(f"  - {change}")
            print()
        print(f"TOTAL: {total_updated} files updated\n")
    else:
        print("No files needed updating.\n")

    print("="*80)

if __name__ == '__main__':
    main()
