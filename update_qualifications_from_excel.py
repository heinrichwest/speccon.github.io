#!/usr/bin/env python3
"""
Script to update qualification pages and SETA tiles based on Excel data
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
                    'credits': int(row[' Credits'])  # Note the space in column name
                })
    return qualifications

# Mapping of qualifications to HTML files
QUALIFICATION_FILE_MAP = {
    # Services SETA
    ('services', 'business administration', 3): 'services-business-administration-nqf3.html',
    ('services', 'business administration', 4): 'services-business-administration-nqf4.html',
    ('services', 'business process outsourcing', 3): 'services-business-process-outsourcing-nqf3.html',
    ('services', 'generic management', 4): 'services-generic-management-nqf4.html',
    ('services', 'generic management', 5): 'services-generic-management-nqf5.html',
    ('services', 'management', 3): 'services-management-nqf3.html',
    ('services', 'new venture creation', 2): 'services-new-venture-creation-smme-nqf2.html',
    ('services', 'new venture creation', 4): 'services-new-venture-creation-nqf4.html',
    ('services', 'bookkeeper', 5): 'services-bookkeeper-nqf5.html',
    ('services', 'contact centre manager', 5): 'services-contact-centre-manager-nqf5.html',
    ('services', 'marketing coordinator', 5): 'services-marketing-coordinator-nqf5.html',
    ('services', 'office supervision', 5): 'services-office-supervision-nqf5.html',
    ('services', 'project manager', 5): 'services-project-manager-nqf5.html',
    ('services', 'quality assurer', 5): 'services-quality-assurer-nqf5.html',
    ('services', 'quality manager', 6): 'services-quality-manager-nqf6.html',

    # AgriSETA
    ('agriseta', 'animal production', 1): 'agri-animal-production-nqf1.html',
    ('agriseta', 'animal production', 2): 'agri-animal-production-nqf2.html',
    ('agriseta', 'animal production', 4): 'agri-animal-production-nqf4.html',
    ('agriseta', 'farming', 1): 'agri-farming-nqf1.html',
    ('agriseta', 'farming', 2): 'agri-farming-nqf2.html',
    ('agriseta', 'fruit packaging', 3): 'agri-fruit-packaging-nqf3.html',
    ('agriseta', 'mixed farming', 1): 'agri-mixed-farming-nqf1.html',
    ('agriseta', 'mixed farming', 2): 'agri-mixed-farming-nqf2.html',
    ('agriseta', 'plant production', 1): 'agri-plant-production-nqf1.html',
    ('agriseta', 'plant production', 2): 'agri-plant-production-nqf2.html',
    ('agriseta', 'plant production', 3): 'agri-plant-production-nqf3.html',
    ('agriseta', 'plant production', 4): 'agri-plant-production-nqf4.html',

    # W&R SETA
    ('w&r', 'planner', 5): 'wr-planner-nqf5.html',
    ('w&r', 'retail buyer', 5): 'wr-retail-buyer-nqf5.html',
    ('w&r', 'retail manager', 5): 'wr-retail-manager-nqf5.html',
    ('w&r', 'retail supervisor', 4): 'wr-retail-supervisor-nqf4.html',
    ('w&r', 'sales assistant', 3): 'wr-sales-assistant-nqf3.html',
    ('w&r', 'service station assistant', 2): 'wr-service-station-assistant-nqf2.html',
    ('w&r', 'store person', 2): 'wr-store-person-nqf2.html',
    ('w&r', 'visual merchandiser', 3): 'wr-visual-merchandiser-nqf3.html',
    ('w&r', 'wholesale and retail', 3): 'wr-retail-operations-nqf2.html',  # May need adjustment
    ('w&r', 'generic management', 5): 'wr-generic-management-nqf5.html',  # If exists

    # MICT SETA
    ('mict', 'business analysis', 6): 'mict-business-analysis-nqf6.html',
    ('mict', 'design thinking', 4): 'mict-design-thinking-nqf4.html',
    ('mict', 'end user computing', 3): 'mict-end-user-computing-nqf3.html',
    ('mict', 'software engineer', 6): 'mict-software-engineer-nqf6.html',
    ('mict', 'software tester', 5): 'mict-software-tester-nqf5.html',
    ('mict', 'systems development', 4): 'mict-systems-development-nqf4.html',
    ('mict', 'system support', 5): 'mict-system-support-nqf5.html',

    # INSETA
    ('inseta', 'financial advisor', 6): 'inseta-financial-advisor-nqf6.html',
    ('inseta', 'health care benefits advisor', 5): 'inseta-health-care-benefits-advisor-nqf5.html',
    ('inseta', 'insurance claims', 4): 'inseta-insurance-claims-administrator-assessor-nqf4.html',
    ('inseta', 'insurance underwriter', 5): 'inseta-insurance-underwriter-nqf5.html',
    ('inseta', 'long term insurance', 4): 'inseta-long-term-insurance-advisor-nqf4.html',

    # FASSET
    ('fasset', 'computer technician', 5): 'fasset-computer-technician-nqf5.html',

    # TETA
    ('teta', 'transport clerk', 4): 'teta-transport-clerk-nqf4.html',
}

def get_qualification_key(qual_name, seta, level):
    """Generate a key for matching qualifications to files"""
    seta_lower = seta.lower()
    name_lower = qual_name.lower()

    # Extract key terms from qualification name
    if 'business administration' in name_lower:
        return (seta_lower, 'business administration', level)
    elif 'business process outsourcing' in name_lower:
        return (seta_lower, 'business process outsourcing', level)
    elif 'generic management' in name_lower or 'general management' in name_lower:
        return (seta_lower, 'generic management', level)
    elif 'management nqf 3' in name_lower or (seta_lower == 'services' and 'management' in name_lower and level == 3):
        return (seta_lower, 'management', level)
    elif 'new venture creation' in name_lower:
        return (seta_lower, 'new venture creation', level)
    elif 'bookkeeper' in name_lower:
        return (seta_lower, 'bookkeeper', level)
    elif 'contact centre manager' in name_lower:
        return (seta_lower, 'contact centre manager', level)
    elif 'marketing coordinator' in name_lower:
        return (seta_lower, 'marketing coordinator', level)
    elif 'office supervision' in name_lower or 'office supervisor' in name_lower:
        return (seta_lower, 'office supervision', level)
    elif 'project manager' in name_lower:
        return (seta_lower, 'project manager', level)
    elif 'quality assurer' in name_lower:
        return (seta_lower, 'quality assurer', level)
    elif 'quality manager' in name_lower:
        return (seta_lower, 'quality manager', level)
    elif 'animal production' in name_lower:
        return (seta_lower, 'animal production', level)
    elif 'farming' in name_lower and 'mixed' not in name_lower:
        return (seta_lower, 'farming', level)
    elif 'mixed farming' in name_lower:
        return (seta_lower, 'mixed farming', level)
    elif 'plant production' in name_lower:
        return (seta_lower, 'plant production', level)
    elif 'fruit packaging' in name_lower:
        return (seta_lower, 'fruit packaging', level)
    elif 'planner' in name_lower:
        return (seta_lower, 'planner', level)
    elif 'retail buyer' in name_lower:
        return (seta_lower, 'retail buyer', level)
    elif 'retail manager' in name_lower or 'chain store manager' in name_lower:
        return (seta_lower, 'retail manager', level)
    elif 'retail supervisor' in name_lower:
        return (seta_lower, 'retail supervisor', level)
    elif 'sales assistant' in name_lower:
        return (seta_lower, 'sales assistant', level)
    elif 'service station assistant' in name_lower:
        return (seta_lower, 'service station assistant', level)
    elif 'store person' in name_lower:
        return (seta_lower, 'store person', level)
    elif 'visual merchandiser' in name_lower:
        return (seta_lower, 'visual merchandiser', level)
    elif 'wholesale and retail' in name_lower and 'operation' in name_lower:
        return (seta_lower, 'wholesale and retail', level)
    elif 'business analysis' in name_lower:
        return (seta_lower, 'business analysis', level)
    elif 'design thinking' in name_lower:
        return (seta_lower, 'design thinking', level)
    elif 'end user computing' in name_lower:
        return (seta_lower, 'end user computing', level)
    elif 'software engineer' in name_lower:
        return (seta_lower, 'software engineer', level)
    elif 'software tester' in name_lower:
        return (seta_lower, 'software tester', level)
    elif 'systems development' in name_lower:
        return (seta_lower, 'systems development', level)
    elif 'system support' in name_lower:
        return (seta_lower, 'system support', level)
    elif 'financial advisor' in name_lower:
        return (seta_lower, 'financial advisor', level)
    elif 'health care benefits' in name_lower:
        return (seta_lower, 'health care benefits advisor', level)
    elif 'insurance claims' in name_lower or 'claims administrator' in name_lower:
        return (seta_lower, 'insurance claims', level)
    elif 'insurance underwriter' in name_lower:
        return (seta_lower, 'insurance underwriter', level)
    elif 'long term insurance' in name_lower:
        return (seta_lower, 'long term insurance', level)
    elif 'computer technician' in name_lower:
        return (seta_lower, 'computer technician', level)
    elif 'transport clerk' in name_lower:
        return (seta_lower, 'transport clerk', level)

    return None

def update_qualification_page(file_path, new_credits):
    """Update credits in a qualification HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern 1: Update credits in stats boxes (hero section)
        # <div class="text-xl font-bold text-white">XXX</div>
        # <div class="text-sm text-white/80">Credits</div>
        content = re.sub(
            r'(<div class="text-xl font-bold text-white">)\d+(<\/div>\s*<div class="text-sm text-white/80">Credits<\/div>)',
            rf'\g<1>{new_credits}\g<2>',
            content
        )

        # Pattern 2: Update credits in sidebar
        # <span class="text-gray-600">Credits</span>
        # <span class="font-semibold">XXX Credits</span>
        content = re.sub(
            r'(<span class="text-gray-600">Credits<\/span>\s*<span class="font-semibold">)\d+( Credits<\/span>)',
            rf'\g<1>{new_credits}\g<2>',
            content
        )

        # Pattern 3: Alternative sidebar format
        # <div class="flex justify-between items-center py-3 border-b border-gray-100">
        # <span class="text-gray-600">Credits</span>
        # <span class="font-semibold">XXX Credits</span>
        content = re.sub(
            r'(<span class="text-gray-600">Credits<\/span>\s*<span class="font-semibold">)\d+( Credits<\/span>)',
            rf'\g<1>{new_credits}\g<2>',
            content
        )

        # Pattern 4: Card credits display (for SETA listing pages)
        # <span class="text-white">XXX Credits</span>
        content = re.sub(
            r'(<span class="text-white">)\d+( Credits<\/span>)',
            rf'\g<1>{new_credits}\g<2>',
            content
        )

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"[ERROR] Error updating {file_path}: {str(e)}")
        return False

def main():
    """Main function to update all qualification pages"""

    # Read qualifications data
    qualifications = read_qualifications_data()

    print(f"Found {len(qualifications)} qualifications in Excel file")
    print("="*60)

    qualifications_dir = Path('qualifications')
    updated_count = 0
    skipped_count = 0
    error_count = 0

    for qual in qualifications:
        qual_key = get_qualification_key(qual['name'], qual['seta'], qual['level'])

        if qual_key and qual_key in QUALIFICATION_FILE_MAP:
            filename = QUALIFICATION_FILE_MAP[qual_key]
            file_path = qualifications_dir / filename

            if file_path.exists():
                success = update_qualification_page(file_path, qual['credits'])
                if success:
                    print(f"[OK] Updated: {filename} - {qual['credits']} credits")
                    updated_count += 1
                else:
                    print(f"[SKIP] No changes: {filename}")
                    skipped_count += 1
            else:
                print(f"[SKIP] File not found: {filename}")
                skipped_count += 1
        else:
            print(f"[SKIP] No mapping: {qual['name']} (Level {qual['level']})")
            skipped_count += 1

    print("="*60)
    print(f"Update complete!")
    print(f"Files updated: {updated_count}")
    print(f"Files skipped: {skipped_count}")
    print(f"Errors: {error_count}")
    print("="*60)

if __name__ == '__main__':
    main()
