#!/usr/bin/env python3
"""
Script to update all short-courses pages to:
1. Add Book Now form popup functionality
2. Update Book This Training buttons to trigger the popup
3. Update footer logos to use SpecCon-LOGO.png with correct path
"""

import os
import re

def add_book_now_popup_html():
    """Generate the Book Now popup HTML"""
    return '''
    <!-- Book Now Modal -->
    <div id="bookNowModal" class="fixed inset-0 bg-black bg-opacity-50 z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
            <div class="p-8">
                <div class="flex items-center justify-between mb-6">
                    <h2 class="text-2xl font-bold text-gray-900">Book This Training</h2>
                    <button onclick="closeBookNowModal()" class="text-gray-400 hover:text-gray-600">
                        <i data-lucide="x" class="w-6 h-6"></i>
                    </button>
                </div>

                <form id="bookNowForm" onsubmit="submitBooking(event)">
                    <div class="grid md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <label for="firstName" class="block text-sm font-medium text-gray-700 mb-2">First Name *</label>
                            <input type="text" id="firstName" name="firstName" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                        <div>
                            <label for="lastName" class="block text-sm font-medium text-gray-700 mb-2">Last Name *</label>
                            <input type="text" id="lastName" name="lastName" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                    </div>

                    <div class="grid md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <label for="email" class="block text-sm font-medium text-gray-700 mb-2">Email *</label>
                            <input type="email" id="email" name="email" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                        <div>
                            <label for="phone" class="block text-sm font-medium text-gray-700 mb-2">Phone Number *</label>
                            <input type="tel" id="phone" name="phone" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                    </div>

                    <div class="mb-4">
                        <label for="company" class="block text-sm font-medium text-gray-700 mb-2">Company Name *</label>
                        <input type="text" id="company" name="company" required
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                    </div>

                    <div class="mb-4">
                        <label for="numberOfParticipants" class="block text-sm font-medium text-gray-700 mb-2">Number of Participants *</label>
                        <select id="numberOfParticipants" name="numberOfParticipants" required
                                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                            <option value="">Select number of participants</option>
                            <option value="1">1 participant</option>
                            <option value="2-5">2-5 participants</option>
                            <option value="6-10">6-10 participants</option>
                            <option value="11-20">11-20 participants</option>
                            <option value="20+">More than 20 participants</option>
                        </select>
                    </div>

                    <div class="mb-4">
                        <label for="preferredDate" class="block text-sm font-medium text-gray-700 mb-2">Preferred Training Date</label>
                        <input type="date" id="preferredDate" name="preferredDate"
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                    </div>

                    <div class="mb-6">
                        <label for="additionalInfo" class="block text-sm font-medium text-gray-700 mb-2">Additional Information</label>
                        <textarea id="additionalInfo" name="additionalInfo" rows="4"
                                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                                  placeholder="Any specific requirements or questions about the training..."></textarea>
                    </div>

                    <div class="flex flex-col sm:flex-row gap-3">
                        <button type="submit" class="flex-1 bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold py-3 px-6 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300">
                            <i data-lucide="send" class="w-4 h-4 inline mr-2"></i>
                            Submit Booking Request
                        </button>
                        <button type="button" onclick="closeBookNowModal()" class="flex-1 bg-gray-500 text-white font-semibold py-3 px-6 rounded-lg hover:bg-gray-600 transition duration-300">
                            Cancel
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>'''

def add_book_now_popup_script():
    """Generate the Book Now popup JavaScript"""
    return '''
    <script>
        // Book Now Modal Functions
        function openBookNowModal() {
            const modal = document.getElementById('bookNowModal');
            if (modal) {
                modal.classList.remove('hidden');
                document.body.style.overflow = 'hidden';
            }
        }

        function closeBookNowModal() {
            const modal = document.getElementById('bookNowModal');
            if (modal) {
                modal.classList.add('hidden');
                document.body.style.overflow = 'auto';
            }
        }

        function submitBooking(event) {
            event.preventDefault();

            // Get form data
            const formData = new FormData(event.target);
            const bookingData = {
                firstName: formData.get('firstName'),
                lastName: formData.get('lastName'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                company: formData.get('company'),
                numberOfParticipants: formData.get('numberOfParticipants'),
                preferredDate: formData.get('preferredDate'),
                additionalInfo: formData.get('additionalInfo'),
                trainingCourse: document.title.split('|')[0].trim()
            };

            // Show success message
            alert('Thank you for your booking request! We will contact you shortly to confirm the details.');
            closeBookNowModal();

            // Reset form
            event.target.reset();

            // In a real implementation, you would send this data to your server
            console.log('Booking submitted:', bookingData);
        }

        // Close modal when clicking outside
        document.addEventListener('DOMContentLoaded', function() {
            const bookNowModal = document.getElementById('bookNowModal');
            if (bookNowModal) {
                bookNowModal.addEventListener('click', function(e) {
                    if (e.target === this) {
                        closeBookNowModal();
                    }
                });
            }

            // Close modal with Escape key
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    closeBookNowModal();
                }
            });
        });
    </script>'''

def update_short_course_page(file_path):
    """Update a single short course HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = False

        # 1. Update Book This Training button to trigger popup
        # Find and replace href="#" or href="../index.html#contact" with onclick
        button_patterns = [
            r'<a href="[^"]*"([^>]*>[\s\S]*?Book This Training[\s\S]*?</a>)',
            r'<a href="#"([^>]*>[\s\S]*?Book This Training[\s\S]*?</a>)',
            r'<button([^>]*>[\s\S]*?Book This Training[\s\S]*?</button>)'
        ]

        for pattern in button_patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                old_button = match.group(0)
                # Check if it already has onclick
                if 'onclick="openBookNowModal()"' not in old_button:
                    # Replace href with onclick
                    new_button = re.sub(r'href="[^"]*"', 'href="#" onclick="openBookNowModal(); return false;"', old_button)
                    # If it's already a button, add onclick
                    if '<button' in old_button:
                        new_button = old_button.replace('<button', '<button onclick="openBookNowModal()"')
                    content = content.replace(old_button, new_button)
                    changes_made = True

        # 2. Add Book Now popup HTML before closing body tag if not already present
        if 'id="bookNowModal"' not in content:
            popup_html = add_book_now_popup_html()
            # Find the closing body tag and insert before it
            body_close_pos = content.rfind('</body>')
            if body_close_pos != -1:
                content = content[:body_close_pos] + popup_html + '\n' + content[body_close_pos:]
                changes_made = True

        # 3. Add Book Now popup script if not already present
        if 'function openBookNowModal()' not in content:
            popup_script = add_book_now_popup_script()
            # Insert before closing body tag
            body_close_pos = content.rfind('</body>')
            if body_close_pos != -1:
                content = content[:body_close_pos] + popup_script + '\n' + content[body_close_pos:]
                changes_made = True

        # 4. Update footer logo to use SpecCon-LOGO.png with correct path
        # Since short-courses is a subfolder, the path should be ../images/
        footer_logo_patterns = [
            r'<img src="[^"]*" alt="[^"]*SpecCon[^"]*" class="h-12[^"]*">',
            r'<img src="images/[^"]*\.png" alt="[^"]*" class="h-12[^"]*">',
            r'<img src="[^"]*SpecCon[^"]*\.png" alt="[^"]*" class="h-12[^"]*">'
        ]

        new_footer_logo = '<img src="../images/SpecCon-LOGO.png" alt="SpecCon Holdings Logo" class="h-12 mr-3">'

        for pattern in footer_logo_patterns:
            # Only look in footer section
            footer_match = re.search(r'<footer[^>]*>(.*?)</footer>', content, re.DOTALL | re.IGNORECASE)
            if footer_match:
                footer_content = footer_match.group(0)
                if re.search(pattern, footer_content):
                    updated_footer = re.sub(pattern, new_footer_logo, footer_content)
                    content = content.replace(footer_content, updated_footer)
                    changes_made = True
                    break

        # Only write if changes were made
        if changes_made:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated: {os.path.basename(file_path)}")
            return True
        else:
            print(f"[SKIP] No changes needed: {os.path.basename(file_path)}")
            return False

    except Exception as e:
        print(f"[ERROR] Error updating {os.path.basename(file_path)}: {e}")
        return False

def main():
    short_courses_dir = 'short-courses'

    if not os.path.exists(short_courses_dir):
        print(f"Error: {short_courses_dir} directory not found")
        return

    # Get all HTML files in short-courses directory
    html_files = [f for f in os.listdir(short_courses_dir) if f.endswith('.html')]

    if not html_files:
        print("No HTML files found in short-courses directory")
        return

    print(f"Found {len(html_files)} HTML files to update\n")

    success_count = 0
    for file_name in html_files:
        file_path = os.path.join(short_courses_dir, file_name)
        if update_short_course_page(file_path):
            success_count += 1

    print(f"\n[DONE] Successfully updated {success_count}/{len(html_files)} files")

if __name__ == "__main__":
    main()