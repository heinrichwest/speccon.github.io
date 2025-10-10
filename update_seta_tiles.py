#!/usr/bin/env python3
"""
Script to update SETA listing page tiles with correct credit values
"""

import csv
import re
from pathlib import Path

# Read CSV data
def read_qualifications_data():
    """Read qualifications from CSV file"""
    qualifications = []
    with open('qualifications_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Qualification Name'] and row['SETA']:
                # Clean up SETA name
                seta = row['SETA'].strip()
                if seta in ['SSETA', 'SERVICES']:
                    seta = 'Services'
                elif seta == 'EDTP':
                    seta = 'ETDP'

                qualifications.append({
                    'name': row['Qualification Name'].strip(),
                    'seta': seta,
                    'level': int(row['NQF Level']),
                    'credits': int(row[' Credits'])
                })
    return qualifications

def get_qualification_short_name(qual_name):
    """Extract short name from full qualification name"""
    name_lower = qual_name.lower()

    # Remove common prefixes
    name_lower = re.sub(r'^(fet certificate:|fetc:|national certificate:|nc:|occupational certificate:|occupation certificate:|certificate:|certitificate:)\s*', '', name_lower)

    # Clean up
    name_lower = name_lower.strip()

    return name_lower

def update_seta_page_tiles(file_path, qualifications_for_seta):
    """Update credit values in SETA listing page tiles"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        updates_made = 0

        for qual in qualifications_for_seta:
            short_name = get_qualification_short_name(qual['name'])
            credits = qual['credits']
            level = qual['level']

            # Try to find and update the tile for this qualification
            # Pattern: Look for tiles with matching NQF level and then update credits

            # Pattern for tiles with specific qualification names
            patterns_to_try = []

            # Build pattern based on qualification type
            if 'bookkeeper' in short_name:
                patterns_to_try.append((r'(Bookkeeper.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'business administration' in short_name:
                if level == 3:
                    patterns_to_try.append((r'(Business Administration Services.*?NQF Level 3.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
                elif level == 4:
                    patterns_to_try.append((r'(Business Administration Services.*?NQF Level 4.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'business process outsourcing' in short_name:
                patterns_to_try.append((r'(Business Process Outsourcing Support.*?NQF Level 3.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'contact centre manager' in short_name:
                patterns_to_try.append((r'(Contact Centre Manager.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'generic management' in short_name or 'general management' in short_name:
                if level == 4:
                    patterns_to_try.append((r'(Generic Management.*?NQF Level 4.*?<span class="text-white[^"]*">)\d+( Credits<\/span>)', credits))
                elif level == 5:
                    patterns_to_try.append((r'(Generic Management.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'management' in short_name and level == 3:
                patterns_to_try.append((r'(Management.*?NQF Level 3.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'marketing coordinator' in short_name:
                patterns_to_try.append((r'(Marketing Coordinator.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'new venture creation' in short_name:
                if level == 2:
                    patterns_to_try.append((r'(New Venture Creation \(SMME\).*?NQF Level 2.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
                elif level == 4:
                    patterns_to_try.append((r'(New Venture Creation.*?NQF Level 4.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'office supervision' in short_name or 'office supervisor' in short_name:
                patterns_to_try.append((r'(Office Supervision.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'project manager' in short_name:
                patterns_to_try.append((r'(Project Manager.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'quality assurer' in short_name:
                patterns_to_try.append((r'(Quality Assurer.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'quality manager' in short_name:
                patterns_to_try.append((r'(Quality Manager.*?NQF Level 6.*?<span class="text-white[^"]*">)\d+( Credits<\/span>)', credits))

            # AgriSETA qualifications
            elif 'animal production' in short_name:
                patterns_to_try.append((rf'(Animal Production.*?NQF Level {level}.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'farming' in short_name and 'mixed' not in short_name:
                patterns_to_try.append((rf'(Farming.*?NQF Level {level}.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'mixed farming' in short_name:
                patterns_to_try.append((rf'(Mixed Farming.*?NQF Level {level}.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'plant production' in short_name:
                patterns_to_try.append((rf'(Plant Production.*?NQF Level {level}.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'fruit packaging' in short_name:
                patterns_to_try.append((rf'(Fruit Packaging.*?NQF Level {level}.*?<span class="text-white">)\d+( Credits<\/span>)', credits))

            # W&R SETA qualifications
            elif 'planner' in short_name:
                patterns_to_try.append((r'(Planner.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'retail buyer' in short_name:
                patterns_to_try.append((r'(Retail Buyer.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'retail manager' in short_name:
                patterns_to_try.append((r'(Retail Manager.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'retail supervisor' in short_name:
                patterns_to_try.append((r'(Retail Supervisor.*?NQF Level 4.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'sales assistant' in short_name:
                patterns_to_try.append((r'(Sales Assistant.*?NQF Level 3.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'service station assistant' in short_name:
                patterns_to_try.append((r'(Service Station Assistant.*?NQF Level 2.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'store person' in short_name:
                patterns_to_try.append((r'(Store Person.*?NQF Level 2.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'visual merchandiser' in short_name:
                patterns_to_try.append((r'(Visual Merchandiser.*?NQF Level 3.*?<span class="text-white">)\d+( Credits<\/span>)', credits))

            # MICT SETA qualifications
            elif 'business analysis' in short_name:
                patterns_to_try.append((r'(Business Analysis.*?NQF Level 6.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'design thinking' in short_name:
                patterns_to_try.append((r'(Design Thinking.*?NQF Level 4.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'end user computing' in short_name:
                patterns_to_try.append((r'(End User Computing.*?NQF Level 3.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'software engineer' in short_name:
                patterns_to_try.append((r'(Software Engineer.*?NQF Level 6.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'software tester' in short_name:
                patterns_to_try.append((r'(Software tester.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'systems development' in short_name:
                patterns_to_try.append((r'(Systems Development.*?NQF Level 4.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'system support' in short_name:
                patterns_to_try.append((r'(System Support.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))

            # INSETA qualifications
            elif 'financial advisor' in short_name:
                patterns_to_try.append((r'(Financial Advisor.*?NQF Level 6.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'health care benefits' in short_name:
                patterns_to_try.append((r'(Health Care [Bb]enefits Advisor.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'insurance claims' in short_name:
                patterns_to_try.append((r'(Insurance Claims.*?NQF Level 4.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'insurance underwriter' in short_name:
                patterns_to_try.append((r'(Insurance Underwriter.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))
            elif 'long term insurance' in short_name:
                patterns_to_try.append((r'(Long term Insurance Advisor.*?NQF Level 4.*?<span class="text-white">)\d+( Credits<\/span>)', credits))

            # FASSET
            elif 'computer technician' in short_name:
                patterns_to_try.append((r'(Computer Technician.*?NQF Level 5.*?<span class="text-white">)\d+( Credits<\/span>)', credits))

            # TETA
            elif 'transport clerk' in short_name:
                patterns_to_try.append((r'(Transport Clerk.*?NQF Level 4.*?<span class="text-white">)\d+( Credits<\/span>)', credits))

            # Try each pattern
            for pattern, new_credits in patterns_to_try:
                new_content = re.sub(pattern, rf'\g<1>{new_credits}\g<2>', content, flags=re.DOTALL)
                if new_content != content:
                    content = new_content
                    updates_made += 1
                    print(f"    [OK] Updated {short_name} (Level {level}): {new_credits} credits")
                    break

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, updates_made
        return False, 0

    except Exception as e:
        print(f"[ERROR] Error updating {file_path}: {str(e)}")
        return False, 0

def main():
    """Main function to update all SETA listing pages"""

    # Read qualifications data
    qualifications = read_qualifications_data()

    print(f"Found {len(qualifications)} qualifications in Excel file")
    print("="*60)

    setas_dir = Path('setas')

    # Group qualifications by SETA
    seta_groups = {}
    for qual in qualifications:
        seta = qual['seta']
        if seta not in seta_groups:
            seta_groups[seta] = []
        seta_groups[seta].append(qual)

    # Map SETA names to file names
    seta_file_map = {
        'Services': 'services-seta.html',
        'AgriSETA': 'agriseta.html',
        'W&R': 'wr-seta.html',
        'MICT': 'mict-seta.html',
        'INSETA': 'inseta.html',
        'FASSET': 'fasset.html',
        'ETDP': 'etdp-seta.html',
        'TETA': 'teta-seta.html',
        'MERSETA': 'mer-seta.html'
    }

    total_updated = 0
    total_tiles_updated = 0

    for seta, quals in seta_groups.items():
        if seta in seta_file_map:
            file_path = setas_dir / seta_file_map[seta]
            if file_path.exists():
                print(f"\nUpdating {seta} SETA page ({file_path.name})...")
                success, tiles_updated = update_seta_page_tiles(file_path, quals)
                if success:
                    print(f"[OK] Updated {file_path.name} - {tiles_updated} tiles updated")
                    total_updated += 1
                    total_tiles_updated += tiles_updated
                else:
                    print(f"[SKIP] No changes to {file_path.name}")
            else:
                print(f"[SKIP] File not found: {file_path}")

    print("="*60)
    print(f"Update complete!")
    print(f"SETA pages updated: {total_updated}")
    print(f"Total tiles updated: {total_tiles_updated}")
    print("="*60)

if __name__ == '__main__':
    main()
