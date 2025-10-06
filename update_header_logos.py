#!/usr/bin/env python3
"""
Script to update header logos across all HTML files to use:
- Root level files: <img src="images/Logo.png" alt="SpecCon Holdings Logo" class="h-12">
- Subfolder files: <img src="../images/Logo.png" alt="SpecCon Holdings Logo" class="h-12">
"""

import os
import re

def update_header_logo(file_path):
    """Update header logo in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Determine the correct path based on file location
        # If file is in a subdirectory, use ../images/Logo.png
        # If file is in root, use images/Logo.png
        file_dir = os.path.dirname(file_path)
        if file_dir and file_dir != '.':
            # File is in a subdirectory
            new_logo = '<img src="../images/Logo.png" alt="SpecCon Holdings Logo" class="h-12">'
        else:
            # File is in root directory
            new_logo = '<img src="images/Logo.png" alt="SpecCon Holdings Logo" class="h-12">'

        # Find header section (typically within first 500 lines)
        # Look for header tag and the logo within it
        header_match = re.search(r'<header[^>]*>(.*?)</header>', content[:50000], re.DOTALL | re.IGNORECASE)

        if header_match:
            header_content = header_match.group(0)
            original_header = header_content

            # Pattern to match header logo images with various variations
            patterns = [
                # Match images with SpecCon in the name and h-12 class
                r'<img\s+src="[^"]*[Ss]pec[Cc]on[^"]*\.png"\s+alt="[^"]*"\s+class="h-12[^"]*"[^>]*>',
                r'<img\s+src="[^"]*[Ll]ogo[^"]*\.png"\s+alt="[^"]*"\s+class="h-12[^"]*"[^>]*>',
                # Match with attributes in different order
                r'<img\s+[^>]*class="h-12[^"]*"[^>]*src="[^"]*[Ll]ogo[^"]*\.png"[^>]*>',
                r'<img\s+[^>]*alt="[^"]*[Ss]pec[Cc]on[^"]*"[^>]*class="h-12[^"]*"[^>]*>',
                # More flexible pattern for any logo in header
                r'<img\s+[^>]*class="h-12"[^>]*>',
            ]

            logo_replaced = False
            for pattern in patterns:
                if re.search(pattern, header_content):
                    # Found a matching logo, replace it
                    header_content = re.sub(pattern, new_logo, header_content, count=1)
                    logo_replaced = True
                    break

            if logo_replaced and header_content != original_header:
                # Replace the header in the content
                content = content.replace(original_header, header_content)
        else:
            # No header tag found, look for logo in nav or first part of body
            # Search in first 1000 lines for a logo
            lines = content.split('\n')
            for i in range(min(300, len(lines))):
                line = lines[i]
                # Check if this line contains a logo image
                if 'class="h-12"' in line and '<img' in line:
                    # Found potential header logo
                    patterns = [
                        r'<img\s+src="[^"]*\.png"\s+alt="[^"]*"\s+class="h-12[^"]*"[^>]*>',
                        r'<img\s+[^>]*class="h-12[^"]*"[^>]*src="[^"]*\.png"[^>]*>',
                        r'<img\s+[^>]*class="h-12"[^>]*>',
                    ]

                    for pattern in patterns:
                        if re.search(pattern, line):
                            lines[i] = re.sub(pattern, new_logo, line, count=1)
                            content = '\n'.join(lines)
                            break
                    break

        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated: {file_path}")
            return True
        else:
            print(f"[SKIP] No changes needed: {file_path}")
            return False

    except Exception as e:
        print(f"[ERROR] Error updating {file_path}: {e}")
        return False

def main():
    # Start from current directory
    root_dir = '.'

    # Find all HTML files
    html_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]

        for filename in filenames:
            if filename.endswith('.html'):
                file_path = os.path.join(dirpath, filename)
                # Normalize path
                file_path = file_path.replace('\\', '/').replace('./', '')
                html_files.append(file_path)

    if not html_files:
        print("No HTML files found")
        return

    print(f"Found {len(html_files)} HTML files to process\n")

    # Group files by directory for better reporting
    root_files = []
    setas_files = []
    qualifications_files = []
    short_courses_files = []
    other_files = []

    for file_path in html_files:
        if '/' not in file_path:
            root_files.append(file_path)
        elif file_path.startswith('setas/'):
            setas_files.append(file_path)
        elif file_path.startswith('qualifications/'):
            qualifications_files.append(file_path)
        elif file_path.startswith('short-courses/'):
            short_courses_files.append(file_path)
        else:
            other_files.append(file_path)

    success_count = 0

    # Process root files
    if root_files:
        print(f"\nProcessing {len(root_files)} root directory files...")
        for file_path in root_files:
            if update_header_logo(file_path):
                success_count += 1

    # Process setas files
    if setas_files:
        print(f"\nProcessing {len(setas_files)} setas folder files...")
        for file_path in setas_files:
            if update_header_logo(file_path):
                success_count += 1

    # Process qualifications files
    if qualifications_files:
        print(f"\nProcessing {len(qualifications_files)} qualifications folder files...")
        for file_path in qualifications_files:
            if update_header_logo(file_path):
                success_count += 1

    # Process short-courses files
    if short_courses_files:
        print(f"\nProcessing {len(short_courses_files)} short-courses folder files...")
        for file_path in short_courses_files:
            if update_header_logo(file_path):
                success_count += 1

    # Process other files
    if other_files:
        print(f"\nProcessing {len(other_files)} other files...")
        for file_path in other_files:
            if update_header_logo(file_path):
                success_count += 1

    print(f"\n[DONE] Successfully updated {success_count}/{len(html_files)} files")

if __name__ == "__main__":
    main()