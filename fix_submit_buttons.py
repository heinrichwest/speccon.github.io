import os
import re

def fix_submit_buttons():
    """Remove onclick handlers from submit buttons within forms"""

    # Directory containing short-courses pages
    directory = 'short-courses'

    # Counter for processed files
    updated_files = 0
    fixed_buttons = 0

    # Process all HTML files in the short-courses directory
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            original_content = content

            # Pattern to find submit buttons within forms that have onclick="openBookNowModal()"
            # This will match submit buttons that incorrectly have the onclick handler
            pattern = r'(<button[^>]*type="submit"[^>]*?)(\s+onclick="openBookNowModal\(\)")?([^>]*>)'

            def fix_submit_button(match):
                before = match.group(1)
                onclick = match.group(2) if match.group(2) else ''
                after = match.group(3)

                # If this submit button has the onclick handler, remove it
                if onclick:
                    nonlocal fixed_buttons
                    fixed_buttons += 1
                    return before + after
                else:
                    return match.group(0)

            # Fix submit buttons
            content = re.sub(pattern, fix_submit_button, content)

            # Also check for submit buttons where type="submit" comes after onclick
            pattern2 = r'(<button[^>]*?)(\s+onclick="openBookNowModal\(\)")([^>]*type="submit"[^>]*>)'

            def fix_submit_button2(match):
                before = match.group(1)
                onclick = match.group(2)
                after = match.group(3)
                nonlocal fixed_buttons
                fixed_buttons += 1
                return before + after

            content = re.sub(pattern2, fix_submit_button2, content)

            # Only write if changes were made
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                updated_files += 1
                print(f"[OK] Fixed submit buttons in {filename}")
            else:
                print(f"[SKIP] No submit button fixes needed in {filename}")

    print(f"\nSummary:")
    print(f"- Files checked: {len([f for f in os.listdir(directory) if f.endswith('.html')])}")
    print(f"- Files updated: {updated_files}")
    print(f"- Submit buttons fixed: {fixed_buttons}")

if __name__ == "__main__":
    fix_submit_buttons()
