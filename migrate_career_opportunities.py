#!/usr/bin/env python3
"""
Script to migrate Career Opportunities section from main content to sidebar
for all Services SETA qualification pages.
"""

import re
import os
import sys
from pathlib import Path

# Handle Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# List of files to process (excluding the two already completed)
FILES_TO_PROCESS = [
    "services-business-administration-nqf3.html",
    "services-management-nqf3.html",
    "services-generic-management-nqf5.html",
    "services-generic-management-nqf4.html",
    "services-marketing-coordinator-nqf5.html",
    "services-new-venture-creation-nqf4.html",
    "services-new-venture-creation-smme-nqf2.html",
    "services-office-supervision-nqf5.html",
    "services-project-manager-nqf5.html",
    "services-quality-manager-nqf6.html",
    "services-quality-assurer-nqf5.html",
    "services-bookkeeper-nqf5.html",
    "services-business-process-outsourcing-nqf3.html",
    "services-contact-centre-manager-nqf5.html",
]

def extract_career_opportunities(content):
    """Extract the Career Opportunities section from main content."""
    # Pattern to match Career Opportunities section
    pattern = r'(\s*<h3 class="text-2xl font-bold text-\[#12265E\] mb-4">Career Opportunities</h3>.*?)</div>\s*</div>\s*<!-- Modules -->'

    match = re.search(pattern, content, re.DOTALL)
    if match:
        career_section = match.group(1)
        # Extract just the career items
        items_pattern = r'<div class="flex items-center">.*?</div>'
        items = re.findall(items_pattern, career_section, re.DOTALL)
        return items, match.group(0)
    return None, None

def convert_to_sidebar_format(career_items):
    """Convert career items from grid format to sidebar list format."""
    sidebar_items = []

    for item in career_items:
        # Extract the career title from the item
        title_match = re.search(r'<span>(.*?)</span>', item)
        if title_match:
            title = title_match.group(1)
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

        # Extract career opportunities section
        career_items, full_match = extract_career_opportunities(content)

        if not career_items:
            print(f"  ⚠️  Could not find Career Opportunities section in {filepath.name}")
            return False

        print(f"  ✓ Found {len(career_items)} career items")

        # Remove from main content
        # Pattern to match the entire Career Opportunities section including the heading and closing tags
        removal_pattern = r'\s*<h3 class="text-2xl font-bold text-\[#12265E\] mb-4">Career Opportunities</h3>.*?</div>\s*</div>\s*(?=\s*<!-- Modules -->)'

        content_modified = re.sub(removal_pattern, '\n                    </div>\n', content, flags=re.DOTALL)

        if content_modified == content:
            print(f"  ⚠️  Could not remove Career Opportunities from main content")
            return False

        print(f"  ✓ Removed from main content")

        # Convert to sidebar format
        sidebar_section = convert_to_sidebar_format(career_items)

        # Insert into sidebar before "Need Help?" section or at the end of qualification details
        # Pattern to find insertion point
        insertion_patterns = [
            # Pattern 1: Before "Need Help?" section
            (r'(</div>\s*<div class="mt-8 p-4 bg-\[#92abc4\] rounded-lg">\s*<h4 class="font-bold text-\[#12265E\] mb-2">Need Help\?</h4>)',
             lambda m: sidebar_section + '\n' + m.group(1)),
            # Pattern 2: Before closing of qualification details div (if no Need Help section)
            (r'(</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</section>\s*<!-- Related Qualifications -->)',
             lambda m: sidebar_section + '\n                    </div>\n\n                </div>\n            </div>\n        </div>\n    </section>\n\n    <!-- Related Qualifications -->'),
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

    print("Starting Career Opportunities migration...")
    print("=" * 60)

    success_count = 0
    fail_count = 0

    for filename in FILES_TO_PROCESS:
        filepath = qualifications_dir / filename

        if not filepath.exists():
            print(f"⚠️  File not found: {filename}")
            fail_count += 1
            continue

        if process_file(filepath):
            success_count += 1
        else:
            fail_count += 1

        print()

    print("=" * 60)
    print(f"Migration complete!")
    print(f"  ✅ Successfully updated: {success_count} files")
    print(f"  ❌ Failed: {fail_count} files")

if __name__ == "__main__":
    main()
