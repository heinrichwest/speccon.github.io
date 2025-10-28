#!/usr/bin/env python3
"""
Export all qualification page links and details to CSV
"""

import os
import csv
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_qualification_info(html_file):
    """Extract qualification information from HTML file"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')

        # Extract title from <title> tag or h1
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else ''

        # Try to get qualification name from h1 or h2
        h1_tag = soup.find('h1')
        if h1_tag:
            qual_name = h1_tag.text.strip()
        else:
            h2_tag = soup.find('h2')
            qual_name = h2_tag.text.strip() if h2_tag else title

        # Extract SETA from class or content
        seta = ''
        seta_badge = soup.find('span', class_=lambda x: x and 'badge' in x.lower())
        if seta_badge:
            seta = seta_badge.text.strip()

        # Try to find SETA in title or filename
        if not seta:
            filename = os.path.basename(html_file)
            if 'services' in filename:
                seta = 'Services SETA'
            elif 'agri' in filename:
                seta = 'AgriSETA'
            elif 'wr-' in filename:
                seta = 'W&R SETA'
            elif 'inseta' in filename:
                seta = 'INSETA'
            elif 'etdp' in filename:
                seta = 'ETDP SETA'
            elif 'mict' in filename:
                seta = 'MICT SETA'
            elif 'fasset' in filename:
                seta = 'FASSET'
            elif 'teta' in filename:
                seta = 'TETA'
            elif 'mer' in filename:
                seta = 'MER SETA'

        # Extract NQF Level from filename or content
        nqf_match = re.search(r'nqf(\d+)', html_file.lower())
        nqf_level = f"NQF {nqf_match.group(1)}" if nqf_match else ''

        # Extract NLRD/SAQA ID if available
        nlrd_id = ''
        nlrd_match = soup.find(string=re.compile(r'(NLRD|SAQA)\s*ID', re.I))
        if nlrd_match:
            parent = nlrd_match.find_parent()
            if parent:
                nlrd_text = parent.text
                id_match = re.search(r'\d{5,}', nlrd_text)
                if id_match:
                    nlrd_id = id_match.group()

        # Get relative path for URL
        filename = os.path.basename(html_file)
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

    # Get all HTML files
    html_files = sorted(qual_dir.glob('*.html'))

    # Extract information from each file
    qualifications = []
    for html_file in html_files:
        # Skip template file
        if 'template' in html_file.name.lower():
            continue

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

    print(f"✓ Exported {len(qualifications)} qualifications to {csv_file}")
    print(f"\nSummary by SETA:")

    # Count by SETA
    seta_counts = {}
    for qual in qualifications:
        seta = qual['seta'] or 'Unknown'
        seta_counts[seta] = seta_counts.get(seta, 0) + 1

    for seta, count in sorted(seta_counts.items()):
        print(f"  {seta}: {count} qualifications")

if __name__ == '__main__':
    main()
