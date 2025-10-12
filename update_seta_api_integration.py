#!/usr/bin/env python3
"""
Update all SETA pages to use API integration for form submission
Replaces simple form submission with async fetch to API endpoint
"""

import os
import glob
import re

def get_seta_course_name(filename):
    """Extract SETA name from filename for Course field"""
    seta_names = {
        'services-seta.html': 'Services SETA Qualifications',
        'agriseta.html': 'AgriSETA Qualifications',
        'wr-seta.html': 'W&R SETA Qualifications',
        'inseta.html': 'INSETA Qualifications',
        'mict-seta.html': 'MICT SETA Qualifications',
        'etdp-seta.html': 'ETDP SETA Qualifications',
        'fasset.html': 'FASSET Qualifications',
        'mer-seta.html': 'MER SETA Qualifications',
        'teta-seta.html': 'TETA SETA Qualifications'
    }
    return seta_names.get(os.path.basename(filename), 'SETA Qualifications')

def get_source_name(filename):
    """Extract source identifier from filename"""
    basename = os.path.basename(filename)
    return basename.replace('.html', '')

# New API-integrated submitEnquiry function template
API_SUBMIT_FUNCTION = """        async function submitEnquiry(event) {{
            event.preventDefault();

            const formData = new FormData(event.target);
            const enquiryData = {{
                Name: formData.get('firstName') || '',
                Surname: formData.get('surname') || '',
                Email: formData.get('email') || '',
                MobileNumber: formData.get('phone') || '',
                JobTitle: '',
                CompanyName: formData.get('company') || '',
                NumEmployees: 0,
                Course: '{course_name}',
                NumAttendees: 0,
                Location: '',
                Reason: formData.get('reason') || '',
                Source: '{source_name}'
            }};

            // Save to localStorage as backup
            localStorage.setItem('lastEnquiryData', JSON.stringify(enquiryData));

            try {{
                const response = await fetch('https://enquiry.speccon.co.za/api/enquiry/submit', {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    }},
                    body: JSON.stringify(enquiryData)
                }});

                if (response.ok) {{
                    alert('Thank you for your enquiry! We will get back to you soon.');
                    closeEnquiryModal();
                    event.target.reset();
                }} else {{
                    const errorData = await response.json();
                    alert('There was an error submitting your enquiry. Please try again or contact us directly.');
                    console.error('API Error:', errorData);
                }}
            }} catch (error) {{
                alert('There was an error submitting your enquiry. Please try again or contact us directly.');
                console.error('Network Error:', error);
            }}
        }}"""

def update_seta_api_integration():
    """Update all SETA HTML files with API integration"""

    # Get all SETA HTML files
    setas_dir = "setas"
    html_files = glob.glob(os.path.join(setas_dir, "*.html"))

    print(f"Found {len(html_files)} SETA files to update")
    print("="*60)

    updates_count = 0

    for html_file in html_files:
        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Get SETA-specific values
            course_name = get_seta_course_name(html_file)
            source_name = get_source_name(html_file)

            # Create the API function with SETA-specific values
            api_function = API_SUBMIT_FUNCTION.format(
                course_name=course_name,
                source_name=source_name
            )

            # Pattern to find existing submitEnquiry function
            # Match both simple and existing async versions
            pattern = r'(\s+)(async\s+)?function\s+submitEnquiry\s*\([^)]*\)\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\}'

            # Replace the function
            if re.search(pattern, content):
                content = re.sub(pattern, api_function, content, count=1)

                # Only write if changes were made
                if content != original_content:
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updates_count += 1
                    print(f"[OK] Updated: {os.path.basename(html_file)}")
                    print(f"  Course: {course_name}")
                    print(f"  Source: {source_name}")
                else:
                    print(f"  No changes needed: {os.path.basename(html_file)}")
            else:
                print(f"[WARN] Could not find submitEnquiry function in: {os.path.basename(html_file)}")

        except Exception as e:
            print(f"[ERROR] Error processing {html_file}: {str(e)}")

    print("="*60)
    print(f"API integration update complete!")
    print(f"Total files updated: {updates_count}/{len(html_files)}")
    print("="*60)

if __name__ == "__main__":
    update_seta_api_integration()
