#!/usr/bin/env python3
"""
Script to add Google Analytics tracking code to all HTML files
"""
import os
import glob
import re

# Google Analytics tracking code to insert
GA_CODE = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-C0EW343WC5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-C0EW343WC5');
</script>
"""

def add_ga_to_file(filepath):
    """Add Google Analytics code to a single HTML file if not already present"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if GA code is already present
        if 'G-C0EW343WC5' in content or 'gtag.js' in content:
            print(f"[SKIP] {filepath} - GA code already present")
            return False

        # Find the <head> tag and insert GA code after it
        if '<head>' in content:
            # Insert after <head> tag
            content = content.replace('<head>', '<head>\n' + GA_CODE, 1)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated {filepath}")
            return True
        else:
            print(f"[WARN] No <head> tag found in {filepath}")
            return False

    except Exception as e:
        print(f"[ERROR] Error processing {filepath}: {str(e)}")
        return False

def main():
    """Main function to process all HTML files"""
    # Get all HTML files recursively
    html_files = glob.glob('**/*.html', recursive=True)

    print(f"Found {len(html_files)} HTML files\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0

    for html_file in sorted(html_files):
        result = add_ga_to_file(html_file)
        if result is True:
            updated_count += 1
        elif result is False and 'already present' in str(result):
            skipped_count += 1
        else:
            error_count += 1

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  [OK] Updated: {updated_count} files")
    print(f"  [SKIP] Skipped: {skipped_count} files (already had GA)")
    print(f"  [ERROR] Errors: {error_count} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
