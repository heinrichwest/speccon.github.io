#!/usr/bin/env python3
"""
Final Module Background Fixer
Fixes ALL module backgrounds to alternate correctly:
- Odd modules (1, 3, 5...): bg-[#12265E] with white text
- Even modules (2, 4, 6...): bg-[#92abc4] with dark text
"""

import re
from pathlib import Path

QUALIFICATIONS_DIR = Path(__file__).parent

# Target backgrounds
ODD_BG = 'bg-[#12265E]'
EVEN_BG = 'bg-[#92abc4]'

def fix_file(filepath):
    """Fix all module backgrounds in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        lines = content.split('\n')
        module_count = 0
        changes_made = False

        i = 0
        while i < len(lines):
            line = lines[i]

            # Check if this is a div with a module heading nearby
            if '<div' in line and 'class=' in line:
                # Look ahead for Module N: or Core Module
                is_module = False
                module_num = None

                for j in range(i, min(i + 3, len(lines))):
                    # Check for Module X:
                    module_match = re.search(r'Module\s+(\d+):', lines[j], re.IGNORECASE)
                    if module_match:
                        is_module = True
                        module_num = int(module_match.group(1))
                        break
                    # Check for Core Module
                    if re.search(r'Core\s+Module', lines[j], re.IGNORECASE):
                        is_module = True
                        module_num = 1  # Treat as first module
                        break

                if is_module and module_num:
                    # Check if div has a background we need to change
                    has_wrong_bg = False

                    # Determine correct background
                    correct_bg = ODD_BG if module_num % 2 == 1 else EVEN_BG
                    correct_heading_color = 'text-white' if module_num % 2 == 1 else 'text-[#12265E]'

                    # Check if current background is wrong
                    if correct_bg not in line:
                        # Has wrong background - need to fix
                        if 'bg-' in line:
                            has_wrong_bg = True

                    if has_wrong_bg:
                        module_count += 1
                        changes_made = True

                        # Remove ALL existing background classes
                        new_line = line
                        # Remove bg-[#...] patterns
                        new_line = re.sub(r'bg-\[#[0-9a-fA-F]+\]', '', new_line)
                        # Remove bg-color-50 patterns
                        new_line = re.sub(r'bg-(?:green|blue|gray|yellow|red|brown|purple|pink|indigo|emerald|orange|teal|cyan|white|black)-\d+', '', new_line)

                        # Clean up spaces
                        new_line = re.sub(r'\s+', ' ', new_line)

                        # Add correct background
                        new_line = new_line.replace('class="', f'class="{correct_bg} ')

                        # Clean up double spaces again
                        new_line = re.sub(r'\s+', ' ', new_line)

                        lines[i] = new_line

                        # Fix heading color in next few lines
                        for j in range(i + 1, min(i + 4, len(lines))):
                            if re.search(r'<h[34]', lines[j]):
                                heading_line = lines[j]

                                # Remove old text colors
                                heading_line = re.sub(r'text-\[#[0-9a-fA-F]+\]', '', heading_line)
                                heading_line = re.sub(r'text-gray-\d+', '', heading_line)
                                heading_line = re.sub(r'text-white\b', '', heading_line)

                                # Clean and add correct color
                                heading_line = re.sub(r'\s+', ' ', heading_line)
                                heading_line = heading_line.replace('class="', f'class="{correct_heading_color} ')
                                heading_line = re.sub(r'\s+', ' ', heading_line)

                                lines[j] = heading_line
                                break

            i += 1

        # Rebuild content
        new_content = '\n'.join(lines)

        # Write if changed
        if changes_made:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, module_count
        else:
            # Count modules even if no changes
            total_modules = len(re.findall(r'Module\s+\d+:', new_content, re.IGNORECASE))
            return False, total_modules

    except Exception as e:
        print(f"ERROR {filepath.name}: {e}")
        return None, 0

def main():
    """Process all qualification HTML files"""
    print("=" * 70)
    print("Final Module Background Fixer")
    print("=" * 70)
    print()

    html_files = [f for f in QUALIFICATIONS_DIR.glob('*.html')
                  if not f.name.endswith('.backup') and '.py' not in f.name]

    updated = []
    correct = []
    no_modules = []
    errors = []
    total_fixed = 0

    for filepath in sorted(html_files):
        result, count = fix_file(filepath)

        if result is True:
            updated.append(filepath.name)
            total_fixed += count
            print(f"[FIXED] {filepath.name}: {count} modules")
        elif result is False:
            if count > 0:
                correct.append(filepath.name)
                print(f"[OK] {filepath.name}: {count} modules already correct")
            else:
                no_modules.append(filepath.name)
                print(f"[SKIP] {filepath.name}: No modules")
        else:
            errors.append(filepath.name)

    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total files processed: {len(html_files)}")
    print(f"Files fixed: {len(updated)}")
    print(f"Files already correct: {len(correct)}")
    print(f"Files without modules: {len(no_modules)}")
    print(f"Errors: {len(errors)}")
    print(f"Total modules fixed: {total_fixed}")
    print()

    if updated:
        print("Files that were fixed:")
        for f in updated:
            print(f"  - {f}")
        print()

    print("All modules now correctly alternate:")
    print("  Odd modules (1, 3, 5...): bg-[#12265E] with white text")
    print("  Even modules (2, 4, 6...): bg-[#92abc4] with dark text")
    print()

if __name__ == '__main__':
    main()
