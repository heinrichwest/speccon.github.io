#!/usr/bin/env python3
"""
Reorganize sections in index.html according to the new sequence
"""

import re
from pathlib import Path

def extract_section(content, start_marker, end_marker=None):
    """
    Extract a section from content based on markers
    Returns (section_content, remaining_content)
    """
    pattern = re.escape(start_marker) + r'.*?(?=' + (re.escape(end_marker) if end_marker else r'</section>') + r')'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        section = match.group(0)
        if not end_marker:
            # Include the closing </section> tag
            section_end = content.find('</section>', match.end())
            if section_end != -1:
                section = content[match.start():section_end + len('</section>')]
        return section
    return None

def main():
    """Main reorganization function"""

    # Read the original file
    file_path = Path('index.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define section markers
    hero_end = content.find('<!-- Why Choose Us Section -->')
    header_and_hero = content[:hero_end]

    # Extract each section
    sections = {}

    # 1. Our Story section (Why Choose Us)
    start = content.find('<!-- Why Choose Us Section -->')
    end = content.find('<!-- Vision & Mission Section -->', start)
    sections['our_story'] = content[start:end].strip()

    # 2. Vision & Mission Section
    start = content.find('<!-- Vision & Mission Section -->')
    end = content.find('<!-- Contact Section -->', start)
    sections['vision_mission'] = content[start:end].strip()

    # 3. Extract "Our Values in Action" from What SpecCon Means section
    values_start = content.find('<!-- Company values highlight -->')
    values_end = content.find('</section>', values_start)
    sections['values'] = content[values_start:values_end].strip()

    # 4. Our Leadership & Success (from Why Choose Us section)
    leadership_start = content.find('<!-- Management & Success Stories -->')
    leadership_end = content.find('</div>\n    </section>', leadership_start)
    sections['leadership'] = content[leadership_start:leadership_end + len('</div>')].strip()

    # 5. What We're Proud About (from Why Choose Us section)
    proud_start = content.find('<!-- What We\'re Proud About -->')
    proud_end = content.find('<!-- Management & Success Stories -->')
    sections['proud'] = content[proud_start:proud_end].strip()

    # 6. Employee Success Stories
    start = content.find('<!-- Employee Success Stories Section -->')
    end = content.find('<!-- Client Success Stories Section -->', start)
    sections['employee_stories'] = content[start:end].strip()

    # 7. Client Success Stories (What our clients say)
    start = content.find('<!-- Client Success Stories Section -->')
    end = content.find('<!-- What SpecCon Means to Our Team Section -->', start)
    sections['client_stories'] = content[start:end].strip()

    # 8. What SpecCon Means to Our Team
    start = content.find('<!-- What SpecCon Means to Our Team Section -->')
    end = content.find('<!-- Qualifications Section -->', start)
    # Remove the values section from this
    team_section = content[start:end].strip()
    # Remove values part
    values_part_start = team_section.find('<!-- Company values highlight -->')
    if values_part_start != -1:
        team_section = team_section[:values_part_start].strip() + '\n        </div>\n    </section>'
    sections['team'] = team_section

    # 9. Value-Added Benefits
    start = content.find('<!-- Value Adds Section -->')
    end = content.find('<!-- Classroom Training Section -->', start)
    sections['value_adds'] = content[start:end].strip()

    # 10. Qualifications
    start = content.find('<!-- Qualifications Section -->')
    end = content.find('<!-- Accreditations Section -->', start)
    sections['qualifications'] = content[start:end].strip()

    # 11. Our SETAs (Accreditations)
    start = content.find('<!-- Accreditations Section -->')
    end = content.find('<!-- Value Adds Section -->', start)
    sections['accreditations'] = content[start:end].strip()

    # 12. Classroom Training
    start = content.find('<!-- Classroom Training Section -->')
    end = content.find('<!-- Contact Section -->', start)
    # Fix: Find the correct end
    end = content.find('<section id="contact"', start)
    if end == -1:
        # Try alternative pattern
        contact_patterns = ['<!-- Contact Section -->', '<section class="py-20 bg-gray-50">\n        <div class="container mx-auto px-6">\n            <div class="text-center mb-12">\n                <h2 class="text-4xl md:text-5xl font-bold text-[#12265E] mb-4">Contact Us']
        for pattern in contact_patterns:
            end = content.find(pattern, start)
            if end != -1:
                break
    sections['classroom'] = content[start:end].strip()

    # Extract Contact Section (comes after Classroom Training)
    contact_start = content.find('<!-- Contact Section -->')
    contact_end = content.find('<!-- Employee Success Stories Section -->', contact_start)
    sections['contact'] = content[contact_start:contact_end].strip()

    # Get footer and scripts
    footer_start = content.find('<!-- Footer -->')
    footer_and_scripts = content[footer_start:]

    print("Sections extracted:")
    for key in sections:
        print(f"  - {key}: {len(sections[key])} characters")

    # Now reconstruct in the new order
    new_content = header_and_hero + '\n\n'

    # NEW SEQUENCE according to requirements:
    # 1. Our story + Vision and mission + Our values in action (combined, no image)

    # Remove image from Our Story section
    our_story_modified = sections['our_story']
    # Find and remove the image div
    image_start = our_story_modified.find('<div class="relative max-w-md mx-auto">')
    if image_start != -1:
        image_end = our_story_modified.find('</div>\n            </div>', image_start)
        if image_end != -1:
            # Remove the image column
            our_story_modified = our_story_modified[:image_start] + '</div>\n            </div>' + our_story_modified[image_end + len('</div>\n            </div>'):]

    # Also change grid to single column
    our_story_modified = our_story_modified.replace('grid lg:grid-cols-2', 'max-w-4xl mx-auto')

    # Remove the Management & Success and Proud sections from our_story temporarily
    our_story_modified = our_story_modified[:our_story_modified.find('<!-- What We\'re Proud About -->')].strip()

    # Close the section properly
    our_story_modified += '\n        </div>\n    </section>\n\n'

    new_content += our_story_modified
    new_content += sections['vision_mission'] + '\n\n'

    # Add Values in Action as separate section
    new_content += '    <!-- Our Values in Action Section -->\n'
    new_content += '    <section class="py-20 bg-gray-50">\n'
    new_content += '        <div class="container mx-auto px-6">\n'
    new_content += '            ' + sections['values'] + '\n'
    new_content += '        </div>\n'
    new_content += '    </section>\n\n'

    # 2. Our Leadership & Success
    new_content += '    <!-- Our Leadership & Success Section -->\n'
    new_content += '    <section class="py-20 bg-white">\n'
    new_content += '        <div class="container mx-auto px-6">\n'
    new_content += '            ' + sections['leadership'] + '\n'
    new_content += '        </div>\n'
    new_content += '    </section>\n\n'

    # 3. What we are proud of
    new_content += '    <!-- What We Are Proud Of Section -->\n'
    new_content += '    <section class="py-20 bg-gray-50">\n'
    new_content += '        <div class="container mx-auto px-6">\n'
    new_content += '            ' + sections['proud'] + '\n'
    new_content += '        </div>\n'
    new_content += '    </section>\n\n'

    # 4. Employee success stories
    new_content += sections['employee_stories'] + '\n\n'

    # 5. What our clients say
    new_content += sections['client_stories'] + '\n\n'

    # 6. What speccon means to our team
    new_content += sections['team'] + '\n\n'

    # 7. Value-Added Benefits
    new_content += sections['value_adds'] + '\n\n'

    # 8. Our Qualifications
    new_content += sections['qualifications'] + '\n\n'

    # 9. Our SETA's
    new_content += sections['accreditations'] + '\n\n'

    # 10. Classroom Training
    new_content += sections['classroom'] + '\n\n'

    # Add Contact section at the end
    new_content += sections['contact'] + '\n\n'

    # Add footer and scripts
    new_content += footer_and_scripts

    # Backup original
    backup_path = Path('index.html.backup')
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nBackup created: {backup_path}")

    # Write new content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"[SUCCESS] Successfully reorganized sections in {file_path}")
    print("\nNew sequence:")
    print("1. Our story (no image) + Vision/Mission + Values in Action")
    print("2. Our Leadership & Success")
    print("3. What we are proud of")
    print("4. Employee success stories")
    print("5. What our clients say")
    print("6. What speccon means to our team")
    print("7. Value-Added Benefits")
    print("8. Our Qualifications")
    print("9. Our SETA's")
    print("10. Classroom Training")
    print("11. Contact")

if __name__ == '__main__':
    main()
