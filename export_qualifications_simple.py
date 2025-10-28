#!/usr/bin/env python3
"""
Export all qualification page links and details to CSV (simple version without external dependencies)
"""

import os
import csv
import re
from pathlib import Path

def extract_qualification_info(html_file):
    """Extract qualification information from HTML file using regex"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title from <title> tag
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else ''

        # Try to get qualification name from h1
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        if h1_match:
            qual_name = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        else:
            qual_name = title

        # Clean up qualification name
        qual_name = re.sub(r'\s+', ' ', qual_name)
        qual_name = re.sub(r'[|•].*$', '', qual_name).strip()

        # Extract SETA from filename
        filename = os.path.basename(html_file)
        seta = ''

        if filename.startswith('services-'):
            seta = 'Services SETA'
        elif filename.startswith('agri-'):
            seta = 'AgriSETA'
        elif filename.startswith('wr-'):
            seta = 'W&R SETA'
        elif filename.startswith('inseta-'):
            seta = 'INSETA'
        elif filename.startswith('etdp-'):
            seta = 'ETDP SETA'
        elif filename.startswith('mict-'):
            seta = 'MICT SETA'
        elif filename.startswith('fasset-'):
            seta = 'FASSET'
        elif filename.startswith('teta-'):
            seta = 'TETA'
        elif filename.startswith('mer-') or filename.startswith('merseta-'):
            seta = 'MER SETA'
        elif filename.startswith('skills-'):
            seta = 'Skills'

        # Extract NQF Level from filename
        nqf_match = re.search(r'nqf(\d+)', filename.lower())
        nqf_level = f"NQF {nqf_match.group(1)}" if nqf_match else ''

        # Extract NLRD/SAQA ID if available
        nlrd_id = ''
        nlrd_match = re.search(r'(NLRD|SAQA)\s*ID[:\s]*(\d{5,})', content, re.I)
        if nlrd_match:
            nlrd_id = nlrd_match.group(2)

        # Get relative path for URL
        relative_path = f"qualifications/{filename}"

        return {
            'filename': filename,
            'qualification_name': qual_name,
            'seta': seta,
            'nqf_level': nqf_level,
            'nlrd_id': nlrd_id,
            'relative_url': relative_path,
            'full_url': f"https://speccon.co.za/{relative_path}"
        }

    except Exception as e:
        print(f"Error processing {html_file}: {e}")
        return None

def main():
    # Get the qualifications directory
    qual_dir = Path('qualifications')

    if not qual_dir.exists():
        print(f"Error: {qual_dir} directory not found!")
        return

    # Get all HTML files
    html_files = sorted(qual_dir.glob('*.html'))

    # Extract information from each file
    qualifications = []
    for html_file in html_files:
        # Skip template file
        if 'template' in html_file.name.lower():
            continue

        print(f"Processing: {html_file.name}")
        info = extract_qualification_info(html_file)
        if info:
            qualifications.append(info)

    # Write to CSV
    csv_file = 'qualifications_export.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['filename', 'qualification_name', 'seta', 'nqf_level', 'nlrd_id', 'relative_url', 'full_url']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(qualifications)

    print(f"\n✓ Exported {len(qualifications)} qualifications to {csv_file}")
    print(f"\nSummary by SETA:")

    # Count by SETA
    seta_counts = {}
    for qual in qualifications:
        seta = qual['seta'] or 'Unknown'
        seta_counts[seta] = seta_counts.get(seta, 0) + 1

    for seta, count in sorted(seta_counts.items()):
        print(f"  {seta}: {count} qualifications")

    print(f"\nCSV file created: {os.path.abspath(csv_file)}")

if __name__ == '__main__':
    main()
