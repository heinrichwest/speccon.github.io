#!/usr/bin/env python3
"""
Remove all references to services-hospitality-management-nqf4 from qualification pages
and replace with appropriate valid qualification links
"""

import os
import re
from pathlib import Path

def get_replacement_qualifications():
    """Define replacement qualifications based on NQF level"""
    return {
        'nqf2': 'services-customer-service-nqf2.html',
        'nqf3': 'services-business-administration-nqf3.html',
        'nqf4': 'services-business-administration-nqf4.html',
        'nqf5': 'services-project-manager-nqf5.html',
        'nqf6': 'services-quality-manager-nqf6.html'
    }

def extract_nqf_level(filename):
    """Extract NQF level from filename"""
    match = re.search(r'nqf(\d)', filename.lower())
    if match:
        return f'nqf{match.group(1)}'
    return 'nqf4'  # default

def find_hospitality_block(content):
    """Find and return the entire hospitality management qualification block"""
    # Pattern to match the entire <a> block for hospitality management
    pattern = r'<a href="services-hospitality-management-nqf4\.html"[^>]*>.*?</a>'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    return matches

def get_replacement_block(nqf_level):
    """Generate replacement qualification block based on NQF level"""
    replacements = {
        'nqf2': '''<a href="services-business-administration-nqf3.html" class="bg-white rounded-2xl shadow-lg p-6 card-hover transition-all duration-300 block">
                    <div class="flex items-center mb-4">
                        <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mr-4">
                            <i data-lucide="clipboard" class="w-6 h-6 text-blue-600"></i>
                        </div>
                        <div>
                            <span class="text-sm text-blue-600 font-medium">NQF Level 3</span>
                            <h3 class="font-bold text-lg text-gray-900">Business Administration</h3>
                        </div>
                    </div>
                    <p class="text-gray-600 text-sm">Core business administration and office management skills.</p>
                </a>''',
        'nqf3': '''<a href="services-generic-management-nqf4.html" class="bg-white rounded-2xl shadow-lg p-6 card-hover transition-all duration-300 block">
                    <div class="flex items-center mb-4">
                        <div class="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center mr-4">
                            <i data-lucide="users" class="w-6 h-6 text-indigo-600"></i>
                        </div>
                        <div>
                            <span class="text-sm text-indigo-600 font-medium">NQF Level 4</span>
                            <h3 class="font-bold text-lg text-gray-900">Generic Management</h3>
                        </div>
                    </div>
                    <p class="text-gray-600 text-sm">First line management and supervisory skills.</p>
                </a>''',
        'nqf4': '''<a href="services-project-manager-nqf5.html" class="bg-white rounded-2xl shadow-lg p-6 card-hover transition-all duration-300 block">
                    <div class="flex items-center mb-4">
                        <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mr-4">
                            <i data-lucide="target" class="w-6 h-6 text-purple-600"></i>
                        </div>
                        <div>
                            <span class="text-sm text-purple-600 font-medium">NQF Level 5</span>
                            <h3 class="font-bold text-lg text-gray-900">Project Manager</h3>
                        </div>
                    </div>
                    <p class="text-gray-600 text-sm">Project management and leadership development.</p>
                </a>''',
        'nqf5': '''<a href="services-quality-manager-nqf6.html" class="bg-white rounded-2xl shadow-lg p-6 card-hover transition-all duration-300 block">
                    <div class="flex items-center mb-4">
                        <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mr-4">
                            <i data-lucide="award" class="w-6 h-6 text-green-600"></i>
                        </div>
                        <div>
                            <span class="text-sm text-green-600 font-medium">NQF Level 6</span>
                            <h3 class="font-bold text-lg text-gray-900">Quality Manager</h3>
                        </div>
                    </div>
                    <p class="text-gray-600 text-sm">Advanced quality management and systems optimization.</p>
                </a>''',
        'nqf6': '''<a href="services-generic-management-nqf5.html" class="bg-white rounded-2xl shadow-lg p-6 card-hover transition-all duration-300 block">
                    <div class="flex items-center mb-4">
                        <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mr-4">
                            <i data-lucide="briefcase" class="w-6 h-6 text-blue-600"></i>
                        </div>
                        <div>
                            <span class="text-sm text-blue-600 font-medium">NQF Level 5</span>
                            <h3 class="font-bold text-lg text-gray-900">Generic Management</h3>
                        </div>
                    </div>
                    <p class="text-gray-600 text-sm">Middle management and strategic planning skills.</p>
                </a>'''
    }
    return replacements.get(nqf_level, replacements['nqf4'])

def process_file(filepath):
    """Process a single file to remove hospitality management references"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all hospitality blocks
        matches = find_hospitality_block(content)

        if not matches:
            return False, "No hospitality management references found"

        # Get the NQF level of current file
        filename = os.path.basename(filepath)
        nqf_level = extract_nqf_level(filename)

        # Get appropriate replacement block
        replacement = get_replacement_block(nqf_level)

        # Replace all occurrences
        modified_content = content
        for match in reversed(matches):  # Process in reverse to maintain positions
            modified_content = modified_content[:match.start()] + replacement + modified_content[match.end():]

        # Write back the modified content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified_content)

        return True, f"Replaced {len(matches)} hospitality management reference(s)"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main function to process all qualification files"""
    qualifications_dir = Path('qualifications')

    # Files that need processing (excluding backup files)
    files_to_process = [
        'services-business-administration-nqf3.html',
        'services-business-process-outsourcing-nqf3.html',
        'services-customer-service-nqf2.html',
        'services-generic-management-nqf4.html',
        'services-marketing-coordinator-nqf5.html',
        'services-new-venture-creation-nqf4.html',
        'services-new-venture-creation-smme-nqf2.html',
        'services-office-supervision-nqf5.html',
        'services-project-manager-nqf5.html',
        'services-quality-manager-nqf6.html'
    ]

    print("Removing services-hospitality-management-nqf4 references...")
    print("=" * 60)

    success_count = 0
    for filename in files_to_process:
        filepath = qualifications_dir / filename
        if filepath.exists():
            success, message = process_file(filepath)
            if success:
                print(f"[SUCCESS] {filename}: {message}")
                success_count += 1
            else:
                print(f"[FAILED] {filename}: {message}")
        else:
            print(f"[WARNING] {filename}: File not found")

    print("=" * 60)
    print(f"Processing complete: {success_count}/{len(files_to_process)} files updated")

    # Clean up backup files if they exist
    print("\nCleaning up backup files...")
    backup_count = 0
    for backup_file in qualifications_dir.glob('*.backup'):
        try:
            backup_file.unlink()
            backup_count += 1
            print(f"[REMOVED] {backup_file.name}")
        except Exception as e:
            print(f"[ERROR] Could not remove {backup_file.name}: {e}")

    if backup_count > 0:
        print(f"Removed {backup_count} backup files")

if __name__ == "__main__":
    main()