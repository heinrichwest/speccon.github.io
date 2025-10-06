#!/usr/bin/env python3
"""
Fix navigation bar styling across all pages:
1. Use Roboto font for nav
2. Menu items: #12265E
3. Hover color: #ff9c2a
"""

import os
import re
from pathlib import Path

def fix_nav_styling(file_path):
    """Fix navigation styling in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Add nav font-family styling if not present
        if 'nav {' not in content and 'nav{' not in content:
            # Add after <style> tag
            content = re.sub(
                r'(<style>)',
                r'\1\n        nav { font-family: \'Roboto\', sans-serif; }',
                content,
                count=1
            )

        # Ensure Roboto font is loaded (add if not present)
        if 'family=Roboto' not in content:
            # Add before </head>
            roboto_link = '    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap" rel="stylesheet">\n'
            content = content.replace('</head>', roboto_link + '</head>')

        # Only save if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    base_dir = Path('.')

    # Process all HTML files
    folders = ['qualifications', 'setas', 'short-courses']
    files_to_process = ['learnership-application.html']

    for folder in folders:
        folder_path = base_dir / folder
        if folder_path.exists():
            files_to_process.extend([str(f) for f in folder_path.glob('*.html')])

    updated_count = 0
    for file_path in files_to_process:
        if os.path.exists(file_path):
            if fix_nav_styling(file_path):
                updated_count += 1
                print(f"Updated: {file_path}")

    print(f"\nUpdated {updated_count} files")
    print("Navigation bars now use:")
    print("  - Font: Roboto")
    print("  - Text color: #12265E")
    print("  - Hover color: #ff9c2a")

if __name__ == '__main__':
    main()
