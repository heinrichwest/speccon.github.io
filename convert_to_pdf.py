#!/usr/bin/env python3
"""
HTML to PDF Converter for SpecCon Landing Pages
Converts HTML pages to PDF while maintaining the exact look and feel
"""

import os
import sys
from pathlib import Path

def convert_html_to_pdf(html_file, output_pdf=None):
    """
    Convert HTML file to PDF using weasyprint

    Args:
        html_file: Path to the HTML file
        output_pdf: Output PDF path (optional, defaults to same name with .pdf extension)
    """
    try:
        # Try importing weasyprint
        try:
            from weasyprint import HTML, CSS
            from weasyprint.text.fonts import FontConfiguration
        except ImportError:
            print("Error: weasyprint is not installed.")
            print("Please install it using: pip install weasyprint")
            print("\nAlternatively, you can use pdfkit:")
            print("pip install pdfkit")
            return False

        # Set default output path
        if output_pdf is None:
            html_path = Path(html_file)
            output_pdf = html_path.parent / f"{html_path.stem}.pdf"

        print(f"Converting {html_file} to PDF...")
        print(f"Output: {output_pdf}")

        # Read the HTML file
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Create font configuration for better text rendering
        font_config = FontConfiguration()

        # Additional CSS for PDF rendering to prevent cutoffs
        pdf_css = CSS(string='''
            @page {
                size: A4;
                margin: 1cm;
            }
            body {
                font-family: 'Roboto', Arial, sans-serif;
            }
            /* Hide elements that shouldn't be in PDF */
            header {
                display: none !important;
            }
            footer {
                page-break-inside: avoid;
            }
            .enquiry-modal,
            #enquiryModal,
            #bannerPopup,
            #stickyBanner,
            button[onclick*="Modal"],
            .mobile-menu-button,
            #mobile-menu-button,
            #mobile-menu {
                display: none !important;
            }
            /* Ensure sections don't break awkwardly */
            section {
                page-break-inside: avoid;
            }
            .card-hover {
                page-break-inside: avoid;
            }
            /* Fix gradient backgrounds for PDF */
            .bg-gradient-to-br,
            .bg-gradient-to-b,
            .bg-gradient-to-r {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            img {
                max-width: 100%;
                page-break-inside: avoid;
            }
            /* Ensure content visibility */
            * {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
        ''', font_config=font_config)

        # Convert HTML to PDF
        html_doc = HTML(string=html_content, base_url=str(Path(html_file).parent))
        html_doc.write_pdf(
            output_pdf,
            stylesheets=[pdf_css],
            font_config=font_config
        )

        print(f"✓ PDF created successfully: {output_pdf}")
        return True

    except Exception as e:
        print(f"Error converting HTML to PDF: {e}")
        print("\nTrying alternative method with pdfkit...")
        return convert_with_pdfkit(html_file, output_pdf)

def convert_with_pdfkit(html_file, output_pdf):
    """
    Alternative conversion method using pdfkit (requires wkhtmltopdf)
    """
    try:
        import pdfkit

        # pdfkit options for better rendering
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'enable-local-file-access': None,
            'no-stop-slow-scripts': None,
            'javascript-delay': 1000,
            'print-media-type': None,
            'disable-smart-shrinking': None,
            'zoom': 1.0
        }

        pdfkit.from_file(html_file, output_pdf, options=options)
        print(f"✓ PDF created successfully using pdfkit: {output_pdf}")
        return True

    except ImportError:
        print("Error: pdfkit is not installed.")
        print("Please install it using: pip install pdfkit")
        print("You also need to install wkhtmltopdf:")
        print("  - Windows: Download from https://wkhtmltopdf.org/downloads.html")
        print("  - Linux: sudo apt-get install wkhtmltopdf")
        print("  - Mac: brew install wkhtmltopdf")
        return False
    except Exception as e:
        print(f"Error with pdfkit: {e}")
        return False

def main():
    """Main function to convert bookkeeper page to PDF"""

    # Path to the bookkeeper HTML file
    html_file = "qualifications/services-bookkeeper-nqf5.html"
    output_pdf = "qualifications/services-bookkeeper-nqf5.pdf"

    # Check if file exists
    if not os.path.exists(html_file):
        print(f"Error: File not found: {html_file}")
        print("Please run this script from the website root directory.")
        return 1

    # Convert to PDF
    success = convert_html_to_pdf(html_file, output_pdf)

    if success:
        print("\n" + "="*50)
        print("PDF CONVERSION COMPLETE")
        print("="*50)
        print(f"PDF Location: {os.path.abspath(output_pdf)}")
        return 0
    else:
        print("\n" + "="*50)
        print("PDF CONVERSION FAILED")
        print("="*50)
        print("\nPlease install one of the following:")
        print("1. weasyprint (recommended): pip install weasyprint")
        print("2. pdfkit: pip install pdfkit + wkhtmltopdf binary")
        return 1

if __name__ == "__main__":
    sys.exit(main())
