#!/usr/bin/env python3
"""
Fix Module Container Backgrounds
Updates module containers to use alternating solid backgrounds:
- Odd modules (1, 3, 5...): bg-[#12265E] with white text
- Even modules (2, 4, 6...): bg-[#92abc4] with dark text
"""

import re
from pathlib import Path

QUALIFICATIONS_DIR = Path(__file__).parent

# Background color patterns to remove
BG_COLORS_TO_REMOVE = [
    r'bg-green-50',
    r'bg-blue-50',
    r'bg-gray-50',
    r'bg-yellow-50',
    r'bg-red-50',
    r'bg-brown-50',
    r'bg-purple-50',
    r'bg-pink-50',
    r'bg-indigo-50',
    r'bg-emerald-50',
    r'bg-orange-50',
    r'bg-teal-50',
    r'bg-cyan-50',
]

def fix_file(filepath):
    """Fix module backgrounds in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        module_count = 0

        # Split content into lines for easier processing
        lines = content.split('\n')
        result_lines = []
        i = 0

        while i < len(lines):
            line = lines[i]

            # Check if this line contains a module div
            # Look for: <div class="...bg-XXX-50..."> followed soon by Module N:
            if '<div' in line and 'class=' in line:
                # Check next few lines for Module heading
                is_module = False
                for j in range(i, min(i + 3, len(lines))):
                    if re.search(r'Module\s+\d+:', lines[j], re.IGNORECASE):
                        is_module = True
                        break
                    if re.search(r'Core\s+Module', lines[j], re.IGNORECASE):
                        is_module = True
                        break

                if is_module:
                    # Check if line has a background color to replace
                    has_bg = False
                    for bg_pattern in BG_COLORS_TO_REMOVE:
                        if re.search(bg_pattern, line):
                            has_bg = True
                            break

                    if has_bg:
                        module_count += 1

                        # Remove all old background colors
                        new_line = line
                        for bg_pattern in BG_COLORS_TO_REMOVE:
                            new_line = re.sub(bg_pattern, '', new_line)

                        # Clean up extra spaces
                        new_line = re.sub(r'\s+', ' ', new_line)
                        new_line = re.sub(r'\s+"', '"', new_line)

                        # Add new background color
                        if module_count % 2 == 1:  # Odd module
                            new_bg = 'bg-[#12265E]'
                        else:  # Even module
                            new_bg = 'bg-[#92abc4]'

                        # Insert new background before closing quote of class attribute
                        new_line = re.sub(r'class="([^"]*)"', rf'class="\1 {new_bg}"', new_line)
                        # Clean up potential double spaces
                        new_line = re.sub(r'\s+', ' ', new_line)
                        new_line = re.sub(r'"\s+', '"', new_line)

                        # Fix the heading color on the next line(s)
                        result_lines.append(new_line)
                        i += 1

                        # Look ahead for the h3/h4 heading and fix its color
                        for j in range(i, min(i + 3, len(lines))):
                            heading_line = lines[j]
                            if re.search(r'<h[34]', heading_line):
                                # Update text color
                                if module_count % 2 == 1:  # Odd module
                                    heading_line = re.sub(r'text-gray-\d+', 'text-white', heading_line)
                                    heading_line = re.sub(r'text-\[[#0-9a-fA-F]+\]', 'text-white', heading_line)
                                    # Add text-white if not present
                                    if 'text-white' not in heading_line and 'class="' in heading_line:
                                        heading_line = re.sub(r'class="', 'class="text-white ', heading_line)
                                else:  # Even module
                                    heading_line = re.sub(r'text-gray-\d+', 'text-[#12265E]', heading_line)
                                    heading_line = re.sub(r'text-white', 'text-[#12265E]', heading_line)
                                    # Add text-[#12265E] if not present
                                    if 'text-[#12265E]' not in heading_line and 'class="' in heading_line:
                                        heading_line = re.sub(r'class="', 'class="text-[#12265E] ', heading_line)

                                lines[j] = heading_line
                                break

                        continue

            result_lines.append(line)
            i += 1

        # Rebuild content
        content = '\n'.join(result_lines)

        # Write back if changed
        if content != original_content and module_count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, module_count
        else:
            return False, module_count

    except Exception as e:
        print(f"ERROR: {filepath.name}: {e}")
        import traceback
        traceback.print_exc()
        return None, 0

def main():
    """Process all HTML files in qualifications directory"""
    print("=" * 70)
    print("Fixing Module Container Backgrounds")
    print("=" * 70)
    print()

    html_files = [f for f in QUALIFICATIONS_DIR.glob('*.html')
                  if not f.name.endswith('.backup') and f.name != 'fix_module_backgrounds.html']

    updated = []
    unchanged = []
    errors = []
    total_modules = 0

    for filepath in sorted(html_files):
        result, count = fix_file(filepath)

        if result is True:
            updated.append(filepath.name)
            total_modules += count
            print(f"[OK] {filepath.name}: Updated {count} modules")
        elif result is False:
            if count > 0:
                unchanged.append(filepath.name)
                print(f"  {filepath.name}: No changes needed ({count} modules already correct)")
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
    print(f"Updated: {len(updated)}")
    print(f"Unchanged: {len(unchanged)}")
    print(f"Errors: {len(errors)}")
    print(f"Total modules fixed: {total_modules}")
    print()

    if updated:
        print("Files updated:")
        for filename in updated:
            print(f"  - {filename}")
        print()

    if errors:
        print("Files with errors:")
        for filename in errors:
            print(f"  - {filename}")
        print()

    print("Module colors now alternate:")
    print("  Odd modules (1, 3, 5...): bg-[#12265E] with white text")
    print("  Even modules (2, 4, 6...): bg-[#92abc4] with dark text")
    print()

if __name__ == '__main__':
    main()
