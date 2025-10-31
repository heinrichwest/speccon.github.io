#!/usr/bin/env python3
"""
Batch convert all Services SETA qualification pages to PDF
"""

import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

def convert_html_to_pdf(html_file, output_pdf, p):
    """
    Convert a single HTML file to PDF using Playwright
    """
    try:
        print(f"\nConverting: {html_file}")

        # Get absolute paths
        html_file_abs = Path(html_file).resolve()
        output_pdf_abs = Path(output_pdf).resolve()

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

    # List of all Services SETA qualification files
    services_seta_files = [
        "services-customer-service-nqf2.html",
        "services-business-administration-nqf3.html",
        "services-business-administration-nqf4.html",
        "services-business-process-outsourcing-nqf3.html",
        "services-contact-centre-manager-nqf5.html",
        "services-generic-management-nqf4.html",
        "services-generic-management-nqf5.html",
        "services-management-nqf3.html",
        "services-marketing-coordinator-nqf5.html",
        "services-new-venture-creation-nqf4.html",
        "services-new-venture-creation-smme-nqf2.html",
        "services-office-supervision-nqf5.html",
        "services-project-manager-nqf5.html",
        "services-quality-assurer-nqf5.html",
        "services-quality-manager-nqf6.html",
        "services-bookkeeper-nqf5.html"
    ]

    # Ensure output directory exists
    output_dir = Path("Qualifications PDF")
    output_dir.mkdir(exist_ok=True)

    print("="*70)
    print("BATCH PDF CONVERTER - Services SETA Qualifications")
    print("="*70)
    print(f"\nTotal files to convert: {len(services_seta_files)}")
    print(f"Output directory: {output_dir.resolve()}")

    successful = 0
    failed = 0

    with sync_playwright() as p:
        for filename in services_seta_files:
            html_path = f"qualifications/{filename}"
            pdf_path = output_dir / filename.replace('.html', '.pdf')

            if not os.path.exists(html_path):
                print(f"\n[ERROR] File not found: {html_path}")
                failed += 1
                continue

            if convert_html_to_pdf(html_path, pdf_path, p):
                successful += 1
            else:
                failed += 1

    print("\n" + "="*70)
    print("BATCH CONVERSION COMPLETE")
    print("="*70)
    print(f"Successful: {successful}/{len(services_seta_files)}")
    print(f"Failed: {failed}/{len(services_seta_files)}")
    print(f"\nAll PDFs saved to: {output_dir.resolve()}")

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    try:
        from playwright.sync_api import sync_playwright
        sys.exit(main())
    except ImportError:
        print("Error: Playwright is not installed.")
        print("Please run: pip install playwright")
        print("Then run: playwright install chromium")
        sys.exit(1)
