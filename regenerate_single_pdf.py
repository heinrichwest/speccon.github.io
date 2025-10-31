#!/usr/bin/env python3
"""
Regenerate a single PDF
"""

import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

def convert_html_to_pdf(html_file, output_pdf):
    """
    Convert a single HTML file to PDF using Playwright
    """
    try:
        print(f"\nConverting: {html_file}")

        # Get absolute paths
        html_file_abs = Path(html_file).resolve()
        output_pdf_abs = Path(output_pdf).resolve()

        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch()
            page = browser.new_page()

            # Navigate to the HTML file
            page.goto(f'file:///{html_file_abs}')

            # Wait for page to fully load including external resources
            page.wait_for_load_state('networkidle')
            page.wait_for_timeout(2000)  # Additional wait for animations/scripts

            # Inject CSS to hide header/logo on pages after the first page
            page.add_style_tag(content="""
                @media print {
                    /* Convert fixed header to static for PDF */
                    header {
                        position: static !important;
                        display: block !important;
                    }

                    /* Remove top padding from breadcrumb section */
                    section.pt-24 {
                        padding-top: 1rem !important;
                    }

                    /* Ensure proper page breaks */
                    @page {
                        margin: 0.5cm;
                    }

                    /* Prevent header from repeating on subsequent pages */
                    body > header {
                        page-break-after: avoid;
                    }

                    /* Add small margin after header */
                    header + section {
                        margin-top: 0 !important;
                        padding-top: 0.5rem !important;
                    }
                }
            """)

            # Generate PDF with optimal settings
            page.pdf(
                path=str(output_pdf_abs),
                format='A4',
                print_background=True,  # Include background colors and images
                margin={
                    'top': '0.5cm',
                    'right': '0.5cm',
                    'bottom': '0.5cm',
                    'left': '0.5cm'
                },
                prefer_css_page_size=False,
                display_header_footer=False
            )

            browser.close()

            file_size = os.path.getsize(output_pdf_abs) / 1024
            print(f"[SUCCESS] Created: {output_pdf} ({file_size:.2f} KB)")
            return True

    except Exception as e:
        print(f"[ERROR] Error converting {html_file}: {e}")
        return False

def main():
    """Main function"""
    html_file = "qualifications/services-business-administration-nqf4.html"
    output_pdf = "Qualifications PDF/services-business-administration-nqf4.pdf"

    if not os.path.exists(html_file):
        print(f"[ERROR] File not found: {html_file}")
        return 1

    print("="*70)
    print("Regenerating PDF - Business Administration NQF4")
    print("="*70)

    if convert_html_to_pdf(html_file, output_pdf):
        print("\n" + "="*70)
        print("PDF REGENERATION COMPLETE")
        print("="*70)
        print(f"PDF Location: {os.path.abspath(output_pdf)}")
        return 0
    else:
        print("\n[ERROR] PDF regeneration failed")
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except ImportError:
        print("Error: Playwright is not installed.")
        sys.exit(1)
