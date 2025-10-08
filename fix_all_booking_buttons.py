#!/usr/bin/env python3
"""
Script to ensure ALL booking buttons in short-courses pages use openBookNowModal()
This includes: Book This Training, Schedule Training, Book Training, Get Training Information
"""

import os
import re

def update_booking_buttons(file_path):
    """Update all booking-related buttons to use openBookNowModal"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = False

        # Pattern to find various booking button texts
        booking_texts = [
            'Book This Training',
            'Schedule Training',
            'Book Training',
            'Get Training Information',
            'Book Training Now',
            'Schedule Your Training',
            'Register for Training',
            'Enroll Now'
        ]

        for text in booking_texts:
            # Pattern 1: Find buttons that already have onclick but might not be correct
            pattern1 = rf'<button[^>]*>(?:[^<]*<[^>]+>)*[^<]*{re.escape(text)}[^<]*(?:</[^>]+>[^<]*)*</button>'
            matches = re.finditer(pattern1, content, re.IGNORECASE)

            for match in matches:
                old_button = match.group(0)
                # Check if it already has openBookNowModal
                if 'openBookNowModal' not in old_button:
                    # Add or update onclick
                    if 'onclick=' in old_button:
                        # Replace existing onclick
                        new_button = re.sub(r'onclick="[^"]*"', 'onclick="openBookNowModal()"', old_button)
                    else:
                        # Add onclick after <button
                        new_button = old_button.replace('<button', '<button onclick="openBookNowModal()"')

                    content = content.replace(old_button, new_button)
                    changes_made = True
                    print(f"  Updated button: {text}")

            # Pattern 2: Find anchor tags that look like buttons with these texts
            pattern2 = rf'<a[^>]*class="[^"]*(?:btn|button)[^"]*"[^>]*>(?:[^<]*<[^>]+>)*[^<]*{re.escape(text)}[^<]*(?:</[^>]+>[^<]*)*</a>'
            matches = re.finditer(pattern2, content, re.IGNORECASE)

            for match in matches:
                old_link = match.group(0)
                # Convert to button with onclick
                new_button = old_link
                # Replace <a with <button
                new_button = re.sub(r'<a\s+', '<button onclick="openBookNowModal()" ', new_button)
                # Replace </a> with </button>
                new_button = re.sub(r'</a>', '</button>', new_button)
                # Remove href attribute
                new_button = re.sub(r'href="[^"]*"', '', new_button)

                content = content.replace(old_link, new_button)
                changes_made = True
                print(f"  Converted link to button: {text}")

        # Special case: Ensure all buttons in hero sections, CTA sections have onclick
        # Pattern for buttons without onclick that contain booking-related text
        pattern3 = r'<button(?![^>]*onclick)[^>]*>(.*?(?:Book|Schedule|Training|Register|Enroll).*?)</button>'
        matches = re.finditer(pattern3, content, re.IGNORECASE | re.DOTALL)

        for match in matches:
            old_button = match.group(0)
            button_text = match.group(1)
            # Clean the text to check if it's booking-related
            clean_text = re.sub(r'<[^>]+>', '', button_text).strip()

            if any(keyword in clean_text.lower() for keyword in ['book', 'schedule', 'training', 'register', 'enroll']):
                # Don't update if it's a navigation or back button
                if not any(skip in clean_text.lower() for skip in ['back to', 'view', 'learn more', 'details']):
                    new_button = old_button.replace('<button', '<button onclick="openBookNowModal()"')
                    content = content.replace(old_button, new_button)
                    changes_made = True
                    print(f"  Added onclick to button: {clean_text[:50]}...")

        # Only write if changes were made
        if changes_made:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"[ERROR] Error updating {os.path.basename(file_path)}: {e}")
        return False

def main():
    short_courses_dir = 'short-courses'

    if not os.path.exists(short_courses_dir):
        print(f"Error: {short_courses_dir} directory not found")
        return

    # Get all HTML files in short-courses directory
    html_files = [f for f in os.listdir(short_courses_dir) if f.endswith('.html')]

    if not html_files:
        print("No HTML files found in short-courses directory")
        return

    print(f"Checking {len(html_files)} HTML files for booking buttons...\n")

    success_count = 0
    for file_name in html_files:
        file_path = os.path.join(short_courses_dir, file_name)
        print(f"Processing: {file_name}")
        if update_booking_buttons(file_path):
            success_count += 1
            print(f"  [OK] Updated")
        else:
            print(f"  [SKIP] No changes needed")

    print(f"\n[DONE] Updated {success_count}/{len(html_files)} files")

if __name__ == "__main__":
    main()