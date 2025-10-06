#!/usr/bin/env python3
"""
Script to update all SETA pages to:
1. Remove 'What Our Clients Say' section
2. Remove 'Trusted by Leading Companies' section
3. Update footer logo to use SpecCon-LOGO.png
"""

import os
import re

def update_seta_page(file_path):
    """Update a single SETA HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Remove "What Our Clients Say" section
        # This section starts with <!-- Client Testimonials --> and includes the testimonial content
        pattern1 = r'<!-- Client Testimonials -->.*?<h4[^>]*>What Our Clients Say</h4>.*?(?=<!-- Client Logos|<!-- Add this new section|</div>\s*</div>\s*</div>\s*</section>)'
        content = re.sub(pattern1, '', content, flags=re.DOTALL)

        # Remove "Trusted by Leading Companies" section
        # This section starts with <!-- Client Logos Scrolling Bar -->
        pattern2 = r'<!-- Client Logos Scrolling Bar -->.*?<p[^>]*>Trusted by Leading Companies</p>.*?(?=<!-- Add this new section|</div>\s*</div>\s*</div>\s*</section>)'
        content = re.sub(pattern2, '', content, flags=re.DOTALL)

        # Alternative patterns for variations in HTML structure
        # Remove entire client testimonials div block
        pattern3 = r'<div class="border-t pt-4">\s*<h4[^>]*>What Our Clients Say</h4>.*?</div>\s*</div>\s*(?=<div class="border-t pt-4 mt-4">|<!-- Add this new section|</div>)'
        content = re.sub(pattern3, '', content, flags=re.DOTALL)

        # Remove entire trusted companies div block
        pattern4 = r'<div class="border-t pt-4 mt-4">\s*<p[^>]*>Trusted by Leading Companies</p>.*?</div>\s*</div>\s*</div>\s*(?=<!-- Add this new section|</div>)'
        content = re.sub(pattern4, '', content, flags=re.DOTALL)

        # Update footer logo - look for existing logo in footer and replace
        # Common footer logo patterns
        footer_patterns = [
            r'<img src="[^"]*" alt="[^"]*SpecCon[^"]*" class="h-12[^"]*">',
            r'<img src="[^"]*SpecCon[^"]*\.png" alt="[^"]*" class="h-12[^"]*">',
            r'<img src="../[^"]*logo[^"]*\.png" alt="[^"]*" class="h-12[^"]*">'
        ]

        new_logo = '<img src="../images/SpecCon-LOGO.png" alt="SpecCon Holdings Logo" class="h-12 mr-3">'

        for pattern in footer_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                content = re.sub(pattern, new_logo, content, flags=re.IGNORECASE)
                break

        # Additional check - if no logo was replaced, look for footer section and update
        if 'src="../images/SpecCon-LOGO.png"' not in content:
            # Look for footer tag and find first img tag within it
            footer_match = re.search(r'<footer[^>]*>(.*?)</footer>', content, re.DOTALL)
            if footer_match:
                footer_content = footer_match.group(1)
                # Find and replace first logo-like image in footer
                img_pattern = r'<img src="[^"]*" alt="[^"]*" class="h-12[^"]*">'
                if re.search(img_pattern, footer_content):
                    updated_footer = re.sub(img_pattern, new_logo, footer_content, count=1)
                    content = content.replace(footer_content, updated_footer)

        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated: {os.path.basename(file_path)}")
            return True
        else:
            print(f"[SKIP] No changes needed: {os.path.basename(file_path)}")
            return False

    except Exception as e:
        print(f"[ERROR] Error updating {os.path.basename(file_path)}: {e}")
        return False

def main():
    setas_dir = 'setas'

    if not os.path.exists(setas_dir):
        print(f"Error: {setas_dir} directory not found")
        return

    # Get all HTML files in setas directory
    html_files = [f for f in os.listdir(setas_dir) if f.endswith('.html')]

    if not html_files:
        print("No HTML files found in setas directory")
        return

    print(f"Found {len(html_files)} HTML files to update\n")

    success_count = 0
    for file_name in html_files:
        file_path = os.path.join(setas_dir, file_name)
        if update_seta_page(file_path):
            success_count += 1

    print(f"\n[DONE] Successfully updated {success_count}/{len(html_files)} files")

if __name__ == "__main__":
    main()