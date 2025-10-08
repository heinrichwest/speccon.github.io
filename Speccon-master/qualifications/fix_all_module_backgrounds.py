#!/usr/bin/env python3
"""
Comprehensive Module Background Fixer
Handles two scenarios:
1. Files with bg-*-50 colors -> Replace with alternating #12265E and #92abc4
2. Files with existing #12265E and #92abc4 -> Ensure correct alternation (odd=dark, even=light)
"""

import re
from pathlib import Path

QUALIFICATIONS_DIR = Path(__file__).parent

def fix_file(filepath):
    """Fix module backgrounds comprehensively"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = False

        # Find all module divs with their backgrounds
        # Pattern: div with background followed by module heading
        pattern = r'(<div\s+class="[^"]*)(bg-\[#(?:12265E|92abc4)\]|bg-(?:green|blue|gray|yellow|red|brown|purple|pink|indigo|emerald|orange|teal|cyan)-50)([^"]*"\s*[^>]*>)\s*<h[34]\s+class="([^"]*)"([^>]*>)\s*(Module\s+(\d+)|Core\s+Module)'

        def replace_background(match):
            nonlocal changes_made

            div_prefix = match.group(1)
            old_bg = match.group(2)
            div_suffix = match.group(3)
            heading_classes = match.group(4)
            heading_suffix = match.group(5)
            module_text = match.group(6)
            module_num_str = match.group(7)

            # Extract module number
            if module_num_str:
                module_num = int(module_num_str)
            else:
                # For "Core Module", treat as module 1
                module_num = 1

            # Determine correct colors based on module number
            if module_num % 2 == 1:  # Odd
                correct_bg = 'bg-[#12265E]'
                correct_heading_color = 'text-white'
            else:  # Even
                correct_bg = 'bg-[#92abc4]'
                correct_heading_color = 'text-[#12265E]'

            # Check if change is needed
            if old_bg != correct_bg:
                changes_made = True

                # Remove old background from div classes
                new_div_prefix = div_prefix
                new_div_prefix = re.sub(r'bg-\[#[0-9a-fA-F]+\]', '', new_div_prefix)
                new_div_prefix = re.sub(r'bg-(?:green|blue|gray|yellow|red|brown|purple|pink|indigo|emerald|orange|teal|cyan)-50', '', new_div_prefix)
                new_div_prefix = re.sub(r'\s+', ' ', new_div_prefix).strip()

                # Add correct background
                new_div = f'{new_div_prefix} {correct_bg}{div_suffix}'

                # Fix heading color
                new_heading = heading_classes
                new_heading = re.sub(r'text-\[#[0-9a-fA-F]+\]', correct_heading_color, new_heading)
                new_heading = re.sub(r'text-gray-\d+', correct_heading_color, new_heading)
                new_heading = re.sub(r'text-white', correct_heading_color, new_heading)

                # If no text color present, add it
                if 'text-' not in new_heading:
                    new_heading = f'{correct_heading_color} {new_heading}'.strip()

                # Reconstruct the match
                result = f'{new_div}<h{heading_suffix[0] if heading_suffix else "4"} class="{new_heading}"{heading_suffix}{module_text}'
                return result

            return match.group(0)

        # Apply the replacements
        new_content = re.sub(pattern, replace_background, content, flags=re.IGNORECASE)

        # Count modules
        module_count = len(re.findall(r'Module\s+\d+:|Core\s+Module', new_content, re.IGNORECASE))

        # Write back if changes were made
        if changes_made and new_content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, module_count
        else:
            return False, module_count

    except Exception as e:
        print(f"ERROR: {filepath.name}: {e}")
        import traceback
        traceback.print_exc()
        return None, 0

def main():
    """Process all HTML files"""
    print("=" * 70)
    print("Comprehensive Module Background Fixer")
    print("=" * 70)
    print()

    html_files = [f for f in QUALIFICATIONS_DIR.glob('*.html')
                  if not f.name.endswith('.backup') and
                  not f.name.endswith('_backgrounds.py')]

    updated = []
    unchanged = []
    errors = []
    total_modules = 0

    for filepath in sorted(html_files):
        result, count = fix_file(filepath)

        if result is True:
            updated.append(filepath.name)
            total_modules += count
            print(f"[OK] {filepath.name}: Fixed {count} modules")
        elif result is False:
            if count > 0:
                unchanged.append(filepath.name)
                print(f"  {filepath.name}: Already correct ({count} modules)")
            else:
                print(f"  {filepath.name}: No modules found")
        else:
            errors.append(filepath.name)

    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total files: {len(html_files)}")
    print(f"Fixed: {len(updated)}")
    print(f"Already correct: {len(unchanged)}")
    print(f"Errors: {len(errors)}")
    print(f"Total modules processed: {total_modules}")
    print()

    if updated:
        print("Files fixed:")
        for filename in updated:
            print(f"  - {filename}")
        print()

    if errors:
        print("Files with errors:")
        for filename in errors:
            print(f"  - {filename}")
        print()

    print("Module colors correctly alternate:")
    print("  Odd modules (1, 3, 5...): bg-[#12265E] with white text")
    print("  Even modules (2, 4, 6...): bg-[#92abc4] with dark text")
    print()

if __name__ == '__main__':
    main()
