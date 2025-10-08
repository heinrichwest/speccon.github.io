#!/usr/bin/env python3
"""
Verify all related qualification links in the qualifications folder
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_links_from_file(filepath):
    """Extract all qualification links from a file"""
    links = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all href links to qualification HTML files
        pattern = r'href="([^"]+\.html)"'
        matches = re.findall(pattern, content)

        # Filter for qualification links (exclude external links and non-qualification pages)
        for link in matches:
            # Skip external links and parent directory references
            if link.startswith('http') or link.startswith('../'):
                continue
            # Only include HTML files that look like qualification pages
            if '.html' in link and not link.startswith('#'):
                links.append(link)

    except Exception as e:
        print(f"Error reading {filepath}: {e}")

    return links

def verify_links(qualifications_dir):
    """Verify all qualification links in the directory"""
    broken_links = defaultdict(list)
    valid_links = defaultdict(list)
    all_files = set()

    # Get all HTML files in the qualifications directory
    for file in qualifications_dir.glob('*.html'):
        if not file.name.endswith('.backup'):
            all_files.add(file.name)

    print(f"Found {len(all_files)} qualification files")
    print("=" * 60)

    # Check each file for links
    for filepath in qualifications_dir.glob('*.html'):
        if filepath.name.endswith('.backup'):
            continue

        links = extract_links_from_file(filepath)

        for link in links:
            # Clean the link (remove anchors)
            clean_link = link.split('#')[0]

            # Check if the linked file exists
            linked_file = qualifications_dir / clean_link

            if linked_file.exists():
                valid_links[filepath.name].append(clean_link)
            else:
                broken_links[filepath.name].append(clean_link)

    # Report findings
    if broken_links:
        print("\nBROKEN LINKS FOUND:")
        print("-" * 60)
        for file, links in sorted(broken_links.items()):
            print(f"\n{file}:")
            for link in sorted(set(links)):
                print(f"  [BROKEN] {link} (file does not exist)")
    else:
        print("\n[SUCCESS] No broken links found!")

    # Summary of most referenced files
    print("\n" + "=" * 60)
    print("MOST REFERENCED QUALIFICATION FILES:")
    print("-" * 60)

    reference_count = defaultdict(int)
    for file_links in valid_links.values():
        for link in file_links:
            reference_count[link] += 1

    # Sort by count
    sorted_refs = sorted(reference_count.items(), key=lambda x: x[1], reverse=True)

    for link, count in sorted_refs[:10]:
        exists = "[EXISTS]" if link in all_files else "[MISSING]"
        print(f"{exists} {link}: referenced {count} times")

    # Find orphaned files (not referenced by any other file)
    all_referenced = set()
    for file_links in valid_links.values():
        all_referenced.update(file_links)

    orphaned = all_files - all_referenced - {'template-qualification.html'}

    if orphaned:
        print("\n" + "=" * 60)
        print("ORPHANED FILES (not referenced by other qualification pages):")
        print("-" * 60)
        for file in sorted(orphaned):
            print(f"  ? {file}")

    return len(broken_links) == 0

def main():
    """Main function"""
    qualifications_dir = Path('Speccon-master/qualifications')

    # Check if we're already in Speccon-master
    if not qualifications_dir.exists():
        qualifications_dir = Path('qualifications')

    if not qualifications_dir.exists():
        print(f"Error: Could not find qualifications directory")
        return

    print("Verifying qualification links...")
    print("=" * 60)

    success = verify_links(qualifications_dir)

    if success:
        print("\n" + "=" * 60)
        print("[SUCCESS] ALL QUALIFICATION LINKS ARE VALID!")
    else:
        print("\n" + "=" * 60)
        print("[WARNING] BROKEN LINKS DETECTED - Please review and fix")

if __name__ == "__main__":
    main()