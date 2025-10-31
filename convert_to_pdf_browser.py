#!/usr/bin/env python3
"""
HTML to PDF Converter using Playwright (Browser-based)
This method preserves the exact look and feel of the HTML page
"""

import os
import sys
from pathlib import Path

def install_playwright():
    """Install playwright and its browsers"""
    print("Installing Playwright...")
    os.system("pip install playwright")
    print("\nInstalling Playwright browsers...")
    os.system("playwright install chromium")

def convert_html_to_pdf_playwright(html_file, output_pdf=None):
    """
    Convert HTML to PDF using Playwright (browser rendering)
    This preserves the exact look and feel
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is not installed.")
        response = input("Would you like to install it now? (y/n): ")
        if response.lower() == 'y':
            install_playwright()
            from playwright.sync_api import sync_playwright
        else:
            return False

    try:
        # Set default output path
        if output_pdf is None:
            html_path = Path(html_file)
            output_pdf = html_path.parent / f"{html_path.stem}.pdf"

        print(f"Converting {html_file} to PDF using browser rendering...")
        print(f"Output: {output_pdf}")

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

        print(f"[SUCCESS] PDF created successfully: {output_pdf_abs}")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Main function"""
    html_file = "qualifications/services-bookkeeper-nqf5.html"
    output_pdf = "Qualifications PDF/services-bookkeeper-nqf5.pdf"

    # Check if file exists
    if not os.path.exists(html_file):
        print(f"Error: File not found: {html_file}")
        print("Please run this script from the website root directory.")
        return 1

    print("="*60)
    print("HTML to PDF Converter (Browser-based)")
    print("="*60)
    print("\nThis will create a PDF that looks exactly like the webpage.")

    success = convert_html_to_pdf_playwright(html_file, output_pdf)

    if success:
        print("\n" + "="*60)
        print("PDF CONVERSION COMPLETE")
        print("="*60)
        print(f"PDF Location: {os.path.abspath(output_pdf)}")
        print(f"File size: {os.path.getsize(output_pdf) / 1024:.2f} KB")
        return 0
    else:
        print("\n" + "="*60)
        print("PDF CONVERSION FAILED")
        print("="*60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
