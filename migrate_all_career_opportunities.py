#!/usr/bin/env python3
"""
Script to migrate Career Opportunities section from main content to sidebar
for ALL qualification pages (all SETAs).
"""

import re
import os
import sys
from pathlib import Path

# Handle Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# List of files to process - only files that actually need updates
FILES_TO_PROCESS = [
    "inseta-financial-advisor-nqf6.html",
    "inseta-health-care-benefits-advisor-nqf5.html",
    "inseta-insurance-claims-administrator-assessor-nqf4.html",
    "inseta-insurance-underwriter-nqf5.html",
    "inseta-long-term-insurance-advisor-nqf4.html",
    "etdp-education-training-nqf5.html",
    "mict-business-analysis-nqf6.html",
    "mict-design-thinking-nqf4.html",
    "mict-end-user-computing-nqf3.html",
    "mict-software-engineer-nqf6.html",
    "mict-software-tester-nqf5.html",
    "mict-systems-development-nqf4.html",
    "mict-system-support-nqf5.html",
    "fasset-computer-technician-nqf5.html",
]

def extract_career_opportunities_standard(content):
    """Extract Career Opportunities from standard grid format."""
    # Pattern for standard Career Opportunities section with grid layout (more flexible)
    pattern = r'<h3[^>]*>Career Opportunities</h3>.*?(?=</div>\s*</div>\s*(?:<!-- (?:Modules|Programme Modules|Core Modules|Learning) -->|<h3|<div class="bg-gradient))'

    match = re.search(pattern, content, re.DOTALL)
    if match:
        career_section = match.group(0)
        # Extract career items - look for flex items with briefcase icon or just span
        items_pattern = r'<div class="flex items-(?:center|start)">.*?<span[^>]*>(.*?)</span>\s*</div>'
        items = re.findall(items_pattern, career_section, re.DOTALL)

        if items:
            return items, career_section
    return None, None

def extract_career_opportunities_complex(content):
    """Extract Career Opportunities from complex categorized format."""
    # Pattern for complex Career Opportunities with nested categories
    pattern = r'<h3 class="text-2xl font-bold[^>]*>Career Opportunities</h3>.*?(?=<h3|<!-- Programme Modules -->|<div class="bg-gradient-to-r from-green)'

    match = re.search(pattern, content, re.DOTALL)
    if match:
        career_section = match.group(0)
        # Extract all career items from various structures
        items_pattern = r'<span class="text-gray-700">(.*?)</span>'
        items = re.findall(items_pattern, career_section, re.DOTALL)

        # Remove duplicates and clean up
        items = list(dict.fromkeys(items))
        return items, match.group(0)
    return None, None

def convert_to_sidebar_format(career_items):
    """Convert career items to sidebar list format."""
    sidebar_items = []

    for item in career_items:
        # Clean up the item text
        title = item.strip()
        if not title:
            continue

        sidebar_item = f'''                                <li class="flex items-start">
                                    <i data-lucide="briefcase" class="w-5 h-5 text-[#ffa600] mr-3 mt-0.5 flex-shrink-0"></i>
                                    <span>{title}</span>
                                </li>'''
        sidebar_items.append(sidebar_item)

    # Create the complete sidebar section
    sidebar_section = f'''
                        <!-- Career Opportunities -->
                        <div class="mt-8 pt-8 border-t border-gray-200">
                            <h4 class="text-lg font-bold text-[#12265E] mb-4">Career Opportunities</h4>
                            <ul class="space-y-3 text-gray-700">
{chr(10).join(sidebar_items)}
                            </ul>
                        </div>
'''
    return sidebar_section

def process_file(filepath):
    """Process a single HTML file to migrate Career Opportunities."""
    print(f"Processing {filepath.name}...")

    try:
        # Read file content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has Career Opportunities in sidebar
        if re.search(r'<!-- Career Opportunities -->\s*<div class="mt-8 pt-8 border-t', content):
            print(f"  ✓ Already has Career Opportunities in sidebar")
            return True

        # Try standard extraction first
        career_items, full_match = extract_career_opportunities_standard(content)

        # If standard didn't work, try complex extraction
        if not career_items:
            career_items, full_match = extract_career_opportunities_complex(content)

        if not career_items:
            print(f"  ⚠️  Could not find Career Opportunities section")
            return False

        print(f"  ✓ Found {len(career_items)} career items")

        # Remove from main content - multiple patterns to try
        removal_patterns = [
            # Pattern 1: Most flexible - any h3 with Career Opportunities
            r'\s*<h3[^>]*>Career Opportunities</h3>.*?</div>\s*</div>\s*(?=\s*(?:<!-- (?:Modules|Programme Modules|Core Modules|Learning) -->|<h3|<div class="bg-gradient))',
            # Pattern 2: With specific text classes
            r'\s*<h3 class="text-2xl[^>]*>Career Opportunities</h3>.*?</div>\s*</div>\s*(?=\s*(?:<!--|<h3))',
            # Pattern 3: Complex with nested divs
            r'\s*<h3[^>]*>Career Opportunities</h3>.*?(?=<h3|<!-- Programme Modules -->|<div class="bg-gradient)',
        ]

        content_modified = content
        for pattern in removal_patterns:
            temp_content = re.sub(pattern, '\n                    </div>\n', content_modified, flags=re.DOTALL)
            if temp_content != content_modified:
                content_modified = temp_content
                print(f"  ✓ Removed from main content")
                break

        if content_modified == content:
            print(f"  ⚠️  Could not remove Career Opportunities from main content")
            return False

        # Convert to sidebar format
        sidebar_section = convert_to_sidebar_format(career_items)

        # Insert into sidebar before "Need Help?" or at end of sidebar
        insertion_patterns = [
            # Pattern 1: Before "Need Help?" section
            (r'(</div>\s*<div class="mt-8 p-4 bg-\[#[0-9a-f]{6}\] rounded-lg">\s*<h4 class="font-bold[^>]*>Need Help\?</h4>)',
             lambda m: sidebar_section + '\n' + m.group(1)),
            # Pattern 2: Before closing of sidebar div
            (r'(</div>\s*</div>\s*(?:</div>\s*)?</div>\s*</div>\s*</section>)',
             lambda m: sidebar_section + '\n                    </div>\n\n                </div>\n            </div>\n        </div>\n    </section>'),
        ]

        inserted = False
        for pattern, replacement in insertion_patterns:
            if re.search(pattern, content_modified):
                content_final = re.sub(pattern, replacement, content_modified, count=1)
                if content_final != content_modified:
                    inserted = True
                    print(f"  ✓ Inserted into sidebar")
                    break

        if not inserted:
            print(f"  ⚠️  Could not find insertion point in sidebar")
            return False

        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content_final)

        print(f"  ✅ Successfully updated {filepath.name}")
        return True

    except Exception as e:
        print(f"  ❌ Error processing {filepath.name}: {str(e)}")
        return False

def main():
    """Main execution function."""
    qualifications_dir = Path(__file__).parent / "qualifications"

    if not qualifications_dir.exists():
        print(f"Error: qualifications directory not found at {qualifications_dir}")
        return

    print("Starting Career Opportunities migration for all SETAs...")
    print("=" * 70)

    success_count = 0
    fail_count = 0
    failed_files = []

    for filename in FILES_TO_PROCESS:
        filepath = qualifications_dir / filename

        if not filepath.exists():
            print(f"⚠️  File not found: {filename}")
            fail_count += 1
            failed_files.append(filename)
            continue

        if process_file(filepath):
            success_count += 1
        else:
            fail_count += 1
            failed_files.append(filename)

        print()

    print("=" * 70)
    print(f"Migration complete!")
    print(f"  ✅ Successfully updated: {success_count} files")
    print(f"  ❌ Failed: {fail_count} files")

    if failed_files:
        print(f"\nFailed files:")
        for f in failed_files:
            print(f"  - {f}")

if __name__ == "__main__":
    main()
