// Centralized Modal System for SpecCon Holdings Website
// This file contains all modal components and their functionality
// Edit this file to update all modals across the entire website

// =================================================================
// CONTACT MODAL COMPONENT
// =================================================================
const CONTACT_MODAL_HTML = `
<div id="contactModal" class="fixed inset-0 bg-black bg-opacity-50 z-50 hidden">
    <div class="flex items-center justify-center min-h-screen p-4">
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full max-h-[90vh] overflow-y-auto">
            <div class="p-6">
                <!-- Modal Header -->
                <div class="flex justify-between items-center mb-4">
                    <h3 class="text-2xl font-bold text-[#12265E]">Contact Us</h3>
                    <button id="closeContactModal" class="text-gray-400 hover:text-gray-600 transition-colors">
                        <i data-lucide="x" class="w-6 h-6"></i>
                    </button>
                </div>

                <!-- Learnership Application Notice -->
                <div class="mb-4 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <p class="text-blue-700 text-sm">
                        <i data-lucide="info" class="w-4 h-4 inline mr-2"></i>
                        If you want to apply for a learnership, please don't use this form. <a href="#" id="learnership-link" class="text-blue-600 hover:text-blue-700 underline">Click here</a> to apply for a learnership.
                    </p>
                </div>

                <!-- Contact Form -->
                <form id="contactForm" class="space-y-4">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="contactName" class="block text-sm font-medium mb-1" style="color: #12265E !important">Name</label>
                            <input type="text" id="contactName" name="name" required
                                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                        </div>
                        <div>
                            <label for="contactSurname" class="block text-sm font-medium mb-1" style="color: #12265E !important">Surname</label>
                            <input type="text" id="contactSurname" name="surname" required
                                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                        </div>
                    </div>

                    <div>
                        <label for="contactEmail" class="block text-sm font-medium mb-1" style="color: #12265E !important">Email</label>
                        <input type="email" id="contactEmail" name="email" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="contactPhone" class="block text-sm font-medium mb-1" style="color: #12265E !important">Phone Number</label>
                        <input type="tel" id="contactPhone" name="phone" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="contactJobTitle" class="block text-sm font-medium mb-1" style="color: #12265E !important">Job Title</label>
                        <input type="text" id="contactJobTitle" name="jobTitle"
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="contactCompany" class="block text-sm font-medium mb-1" style="color: #12265E !important">Company</label>
                        <input type="text" id="contactCompany" name="company"
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="contactReason" class="block text-sm font-medium mb-1" style="color: #12265E !important">Reason for Contact</label>
                        <select id="contactReason" name="reason" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                            <option value="">Select a reason</option>
                            <option value="general">General Inquiry</option>
                            <option value="qualification">Qualification Information</option>
                            <option value="learnership">Learnership Application</option>
                            <option value="corporate">Corporate Training</option>
                            <option value="partnership">Partnership Opportunity</option>
                            <option value="support">Technical Support</option>
                            <option value="other">Other</option>
                        </select>
                    </div>

                    <div>
                        <label for="contactMessage" class="block text-sm font-medium mb-1" style="color: #12265E !important">Message</label>
                        <textarea id="contactMessage" name="message" rows="4"
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent"
                            placeholder="Please provide details about your inquiry..."></textarea>
                    </div>



                    <!-- Action Buttons -->
                    <div class="flex space-x-3 pt-4">
                        <button type="button" id="cancelContactForm"
                            class="flex-1 px-4 py-2 bg-[#12265E] text-white font-semibold rounded-lg hover:bg-[#0d1a47] transition-colors">
                            Cancel
                        </button>
                        <button type="submit"
                            class="flex-1 bg-gradient-to-r from-[#12265E] to-[#12265E] text-white font-semibold px-4 py-2 rounded-lg hover:from-[#FFA600] hover:to-[#FFA600] transition duration-300">
                            Send Message
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>`;

// =================================================================
// ENQUIRE NOW MODAL COMPONENT
// =================================================================
const ENQUIRE_NOW_MODAL_HTML = `
<div id="enquireModal" class="fixed inset-0 bg-black bg-opacity-50 z-50 hidden">
    <div class="flex items-center justify-center min-h-screen p-4">
        <div class="bg-white rounded-2xl shadow-2xl max-w-lg w-full max-h-[90vh] overflow-y-auto">
            <div class="p-6">
                <!-- Modal Header -->
                <div class="flex justify-between items-center mb-4">
                    <h3 class="text-2xl font-bold text-[#12265E]">Quick Enquiry</h3>
                    <button id="closeEnquireModal" class="text-gray-400 hover:text-gray-600 transition-colors">
                        <i data-lucide="x" class="w-6 h-6"></i>
                    </button>
                </div>

                <!-- Enquiry Form -->
                <form id="enquireForm" class="space-y-4">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="enquireName" class="block text-sm font-medium mb-1" style="color: #12265E !important">Name</label>
                            <input type="text" id="enquireName" name="name" required
                                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                        </div>
                        <div>
                            <label for="enquireSurname" class="block text-sm font-medium mb-1" style="color: #12265E !important">Surname</label>
                            <input type="text" id="enquireSurname" name="surname" required
                                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                        </div>
                    </div>

                    <div>
                        <label for="enquireEmail" class="block text-sm font-medium mb-1" style="color: #12265E !important">Email</label>
                        <input type="email" id="enquireEmail" name="email" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="enquirePhone" class="block text-sm font-medium mb-1" style="color: #12265E !important">Phone Number</label>
                        <input type="tel" id="enquirePhone" name="phone" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="enquireCompany" class="block text-sm font-medium mb-1" style="color: #12265E !important">Company</label>
                        <input type="text" id="enquireCompany" name="company"
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="enquireInterest" class="block text-sm font-medium mb-1" style="color: #12265E !important">I'm interested in</label>
                        <select id="enquireInterest" name="interest" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                            <option value="">Select your interest</option>
                            <option value="learnerships">Learnership Programs</option>
                            <option value="qualifications">Professional Qualifications</option>
                            <option value="corporate">Corporate Training</option>
                            <option value="online">Online Training Courses</option>
                            <option value="consultation">Training Consultation</option>
                            <option value="partnership">Partnership Opportunities</option>
                        </select>
                    </div>

                    <div>
                        <label for="enquireMessage" class="block text-sm font-medium mb-1" style="color: #12265E !important">Additional Details (Optional)</label>
                        <textarea id="enquireMessage" name="message" rows="3"
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent"
                            placeholder="Tell us more about your training needs..."></textarea>
                    </div>

                    <!-- Action Buttons -->
                    <div class="flex space-x-3 pt-4">
                        <button type="button" id="cancelEnquireForm"
                            class="flex-1 px-4 py-2 bg-[#12265E] text-white font-semibold rounded-lg hover:bg-[#0d1a47] transition-colors">
                            Cancel
                        </button>
                        <button type="submit"
                            class="flex-1 bg-gradient-to-r from-[#12265E] to-[#12265E] text-white font-semibold px-4 py-2 rounded-lg hover:from-[#FFA600] hover:to-[#FFA600] transition duration-300">
                            Submit Enquiry
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>`;

// =================================================================
// BOOK TRAINING MODAL COMPONENT (for short courses)
// =================================================================
const BOOK_NOW_MODAL_HTML = `
<div id="bookNowModal" class="fixed inset-0 bg-black bg-opacity-50 z-50 hidden">
    <div class="flex items-center justify-center min-h-screen p-4">
        <div class="bg-white rounded-2xl shadow-2xl max-w-lg w-full max-h-[90vh] overflow-y-auto">
            <div class="p-6">
                <!-- Modal Header -->
                <div class="flex justify-between items-center mb-4">
                    <h3 class="text-2xl font-bold text-[#12265E]">Book Training</h3>
                    <button id="closeBookNowModal" class="text-gray-400 hover:text-gray-600 transition-colors">
                        <i data-lucide="x" class="w-6 h-6"></i>
                    </button>
                </div>

                <!-- Training booking form -->
                <form id="bookNowForm" class="space-y-4">
                    <div class="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-4">
                        <h4 class="font-semibold text-blue-900 mb-1">Course Information</h4>
                        <p id="courseTitle" class="text-blue-800 text-sm">Course details will be displayed here</p>
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="bookingName" class="block text-sm font-medium mb-1" style="color: #12265E !important">Name *</label>
                            <input type="text" id="bookingName" name="name" required
                                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                        </div>
                        <div>
                            <label for="bookingSurname" class="block text-sm font-medium mb-1" style="color: #12265E !important">Surname *</label>
                            <input type="text" id="bookingSurname" name="surname" required
                                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                        </div>
                    </div>

                    <div>
                        <label for="bookingEmail" class="block text-sm font-medium mb-1" style="color: #12265E !important">Email *</label>
                        <input type="email" id="bookingEmail" name="email" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="bookingPhone" class="block text-sm font-medium mb-1" style="color: #12265E !important">Contact Number *</label>
                        <input type="tel" id="bookingPhone" name="phone" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="bookingCompany" class="block text-sm font-medium mb-1" style="color: #12265E !important">Company *</label>
                        <input type="text" id="bookingCompany" name="company" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="shortCourseSelect" class="block text-sm font-medium mb-1" style="color: #12265E !important">Short Course *</label>
                        <select id="shortCourseSelect" name="short_course" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                            <option value="">Select a short course</option>
                            <optgroup label="Computer Courses">
                                <option value="excel-basic">Excel Training - Basic</option>
                                <option value="excel-intermediate">Excel Training - Intermediate</option>
                                <option value="excel-advanced">Excel Training - Advanced</option>
                                <option value="power-bi">Power BI Training</option>
                                <option value="ai-basic">AI Training - Basic</option>
                                <option value="ai-advanced">AI Training - Advanced</option>
                                <option value="cyber-security">Cyber Security Awareness</option>
                            </optgroup>
                            <optgroup label="Compliance Courses">
                                <option value="health-safety">Health & Safety</option>
                                <option value="environmental">Environmental Compliance</option>
                                <option value="fire-safety">Fire Safety</option>
                                <option value="first-aid">First Aid Training</option>
                            </optgroup>
                            <optgroup label="Professional Development">
                                <option value="leadership">Leadership Skills</option>
                                <option value="project-management">Project Management</option>
                                <option value="communication">Communication Skills</option>
                                <option value="time-management">Time Management</option>
                            </optgroup>
                        </select>
                    </div>

                    <div>
                        <label for="participantCount" class="block text-sm font-medium mb-1" style="color: #12265E !important">Number of People *</label>
                        <select id="participantCount" name="participants" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                            <option value="">Select number of participants</option>
                            <option value="1">1 participant</option>
                            <option value="2">2 participants</option>
                            <option value="3">3 participants</option>
                            <option value="4">4 participants</option>
                            <option value="5">5 participants</option>
                            <option value="6-10">6-10 participants</option>
                            <option value="11-15">11-15 participants</option>
                            <option value="16-20">16-20 participants</option>
                            <option value="20+">More than 20 participants</option>
                        </select>
                    </div>

                    <div>
                        <label for="trainingLocation" class="block text-sm font-medium mb-1" style="color: #12265E !important">Location of Training *</label>
                        <select id="trainingLocation" name="location" required
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                            <option value="">Select training location</option>
                            <option value="client-premises">At client premises</option>
                            <option value="speccon-offices">At SpecCon offices</option>
                            <option value="conference-venue">Conference venue (arranged by SpecCon)</option>
                            <option value="online">Online training</option>
                            <option value="hybrid">Hybrid (online + in-person)</option>
                        </select>
                    </div>

                    <div>
                        <label for="preferredDate" class="block text-sm font-medium mb-1" style="color: #12265E !important">Preferred Training Date</label>
                        <input type="date" id="preferredDate" name="preferred_date"
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent">
                    </div>

                    <div>
                        <label for="bookingNotes" class="block text-sm font-medium mb-1" style="color: #12265E !important">Additional Requirements</label>
                        <textarea id="bookingNotes" name="notes" rows="3"
                            class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#FFA600] focus:border-transparent"
                            placeholder="Any specific requirements, accessibility needs, or questions about the training..."></textarea>
                    </div>

                    <!-- Action Buttons -->
                    <div class="flex space-x-3 pt-4">
                        <button type="button" id="cancelBookingForm"
                            class="flex-1 px-4 py-2 bg-[#12265E] text-white font-semibold rounded-lg hover:bg-[#0d1a47] transition-colors">
                            Cancel
                        </button>
                        <button type="submit"
                            class="flex-1 bg-gradient-to-r from-[#12265E] to-[#12265E] text-white font-semibold px-4 py-2 rounded-lg hover:from-[#FFA600] hover:to-[#FFA600] transition duration-300">
                            Submit Training Request
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>`;

// =================================================================
// MODAL MANAGEMENT FUNCTIONS
// =================================================================

// Function to initialize all modals
function initializeCentralizedModals() {
    // Add modals to the page if they don't exist
    if (!document.getElementById('contactModal')) {
        document.body.insertAdjacentHTML('beforeend', CONTACT_MODAL_HTML);
    }
    if (!document.getElementById('enquireModal')) {
        document.body.insertAdjacentHTML('beforeend', ENQUIRE_NOW_MODAL_HTML);
    }
    if (!document.getElementById('bookNowModal')) {
        document.body.insertAdjacentHTML('beforeend', BOOK_NOW_MODAL_HTML);
    }

    // Setup all modal functionality
    setupContactModal();
    setupEnquireModal();
    setupBookNowModal();

    // Re-initialize Lucide icons for new elements
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

// Contact Modal Functions
function setupContactModal() {
    const modal = document.getElementById('contactModal');
    const closeBtn = document.getElementById('closeContactModal');
    const cancelBtn = document.getElementById('cancelContactForm');
    const form = document.getElementById('contactForm');
    const reasonSelect = document.getElementById('contactReason');
    const learnershipNotice = document.getElementById('learnership-notice');
    const learnershipLink = document.getElementById('learnership-link');

    if (modal && closeBtn && cancelBtn && form) {
        closeBtn.addEventListener('click', closeContactModal);
        cancelBtn.addEventListener('click', closeContactModal);

        // Handle learnership link click
        if (learnershipLink) {
            learnershipLink.addEventListener('click', (e) => {
                e.preventDefault();
                // Determine the correct path based on current location
                const currentPath = window.location.pathname;
                if (currentPath.includes('/qualifications/') || currentPath.includes('/setas/') || currentPath.includes('/short-courses/')) {
                    window.location.href = '../learnership-application.html';
                } else {
                    window.location.href = 'learnership-application.html';
                }
            });
        }

        // Close on outside click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeContactModal();
        });

        // Show learnership notice when relevant
        if (reasonSelect && learnershipNotice) {
            reasonSelect.addEventListener('change', () => {
                if (reasonSelect.value === 'learnership') {
                    learnershipNotice.classList.remove('hidden');
                } else {
                    learnershipNotice.classList.add('hidden');
                }
            });
        }

        // Handle form submission
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Get form data
            const formData = new FormData(form);
            const submitButton = form.querySelector('button[type="submit"]');
            const originalButtonText = submitButton.textContent;

            // Disable submit button and show loading state
            submitButton.disabled = true;
            submitButton.textContent = 'Sending...';

            try {
                // Prepare data for API (matching index.html format)
                const applicationData = {
                    Name: formData.get('name') || '',
                    Surname: formData.get('surname') || '',
                    Email: formData.get('email') || '',
                    MobileNumber: formData.get('phone') || '',
                    JobTitle: formData.get('jobTitle') || '',
                    CompanyName: formData.get('company') || '',
                    NumEmployees: 0,
                    Course: '',
                    NumAttendees: 0,
                    Location: '',
                    Reason: formData.get('reason') || '',
                    Source: 'contactus'
                };

                // Save to localStorage for reference (matching index.html behavior)
                localStorage.setItem('lastApplicationData', JSON.stringify(applicationData));

                // Send to API
                const response = await fetch('https://enquiry.speccon.co.za/api/enquiry/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify(applicationData)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const result = await response.json();

                // Show success message
                alert('Thank you for your message! We will contact you soon.\n\nReference: ' + (result.id || 'Submitted successfully'));
                closeContactModal();

            } catch (error) {
                console.error('Error submitting contact form:', error);
                alert('Sorry, there was an error sending your message. Please try again or contact us directly at help@speccon.co.za');

                // Re-enable submit button
                submitButton.disabled = false;
                submitButton.textContent = originalButtonText;
            }
        });
    }
}

function openContactModal() {
    const modal = document.getElementById('contactModal');
    if (modal) {
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }
}

function closeContactModal() {
    const modal = document.getElementById('contactModal');
    const form = document.getElementById('contactForm');
    if (modal) {
        modal.classList.add('hidden');
        document.body.style.overflow = 'auto';
        if (form) form.reset();
    }
}

// Enquire Modal Functions
function setupEnquireModal() {
    const modal = document.getElementById('enquireModal');
    const closeBtn = document.getElementById('closeEnquireModal');
    const cancelBtn = document.getElementById('cancelEnquireForm');
    const form = document.getElementById('enquireForm');

    if (modal && closeBtn && cancelBtn && form) {
        closeBtn.addEventListener('click', closeEnquireModal);
        cancelBtn.addEventListener('click', closeEnquireModal);

        // Close on outside click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeEnquireModal();
        });

        // Handle form submission
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Get form data
            const formData = new FormData(form);
            const submitButton = form.querySelector('button[type="submit"]');
            const originalButtonText = submitButton.textContent;

            // Disable submit button and show loading state
            submitButton.disabled = true;
            submitButton.textContent = 'Submitting...';

            try {
                // Prepare data for API
                const data = {
                    name: formData.get('name'),
                    surname: formData.get('surname'),
                    email: formData.get('email'),
                    phone: formData.get('phone'),
                    company: formData.get('company') || '',
                    interest: formData.get('interest'),
                    message: formData.get('message') || '',
                    type: 'enquiry',
                    source: 'website',
                    submittedAt: new Date().toISOString()
                };

                // Send to API
                const response = await fetch('https://enquiry.speccon.co.za/api/enquiry/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const result = await response.json();

                // Show success message
                alert('Thank you for your enquiry! We will contact you within 24 hours.\n\nReference: ' + (result.id || 'Submitted successfully'));
                closeEnquireModal();

            } catch (error) {
                console.error('Error submitting enquiry form:', error);
                alert('Sorry, there was an error submitting your enquiry. Please try again or contact us directly at help@speccon.co.za');

                // Re-enable submit button
                submitButton.disabled = false;
                submitButton.textContent = originalButtonText;
            }
        });
    }
}

function openEnquireModal() {
    const modal = document.getElementById('enquireModal');
    if (modal) {
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }
}

function closeEnquireModal() {
    const modal = document.getElementById('enquireModal');
    const form = document.getElementById('enquireForm');
    if (modal) {
        modal.classList.add('hidden');
        document.body.style.overflow = 'auto';
        if (form) form.reset();
    }
}

// Book Now Modal Functions
function setupBookNowModal() {
    const modal = document.getElementById('bookNowModal');
    const closeBtn = document.getElementById('closeBookNowModal');
    const cancelBtn = document.getElementById('cancelBookingForm');
    const form = document.getElementById('bookNowForm');

    if (modal && closeBtn && cancelBtn && form) {
        closeBtn.addEventListener('click', closeBookNowModal);
        cancelBtn.addEventListener('click', closeBookNowModal);

        // Close on outside click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeBookNowModal();
        });

        // Handle form submission
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Get form data
            const formData = new FormData(form);
            const submitButton = form.querySelector('button[type="submit"]');
            const originalButtonText = submitButton.textContent;

            // Disable submit button and show loading state
            submitButton.disabled = true;
            submitButton.textContent = 'Submitting...';

            try {
                // Prepare data for API
                const data = {
                    name: formData.get('name'),
                    surname: formData.get('surname'),
                    email: formData.get('email'),
                    phone: formData.get('phone'),
                    company: formData.get('company'),
                    shortCourse: formData.get('short_course'),
                    participants: formData.get('participants'),
                    location: formData.get('location'),
                    preferredDate: formData.get('preferred_date') || '',
                    notes: formData.get('notes') || '',
                    type: 'booking',
                    source: 'website',
                    submittedAt: new Date().toISOString()
                };

                // Send to API
                const response = await fetch('https://enquiry.speccon.co.za/api/enquiry/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const result = await response.json();

                // Show success message
                alert('Thank you for your booking request! We will contact you within 24 hours to confirm details and pricing.\n\nReference: ' + (result.id || 'Submitted successfully'));
                closeBookNowModal();

            } catch (error) {
                console.error('Error submitting booking form:', error);
                alert('Sorry, there was an error submitting your booking request. Please try again or contact us directly at help@speccon.co.za');

                // Re-enable submit button
                submitButton.disabled = false;
                submitButton.textContent = originalButtonText;
            }
        });
    }
}

function openBookNowModal(courseTitle = '', courseValue = '') {
    const modal = document.getElementById('bookNowModal');
    const courseTitleElement = document.getElementById('courseTitle');
    const shortCourseSelect = document.getElementById('shortCourseSelect');

    if (modal) {
        if (courseTitleElement && courseTitle) {
            courseTitleElement.textContent = courseTitle;
        }

        // Auto-select the course if a specific course value is provided
        if (shortCourseSelect && courseValue) {
            shortCourseSelect.value = courseValue;
        }

        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';

        // Re-initialize Lucide icons for new elements
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    }
}

function closeBookNowModal() {
    const modal = document.getElementById('bookNowModal');
    const form = document.getElementById('bookNowForm');
    if (modal) {
        modal.classList.add('hidden');
        document.body.style.overflow = 'auto';
        if (form) form.reset();
    }
}

// =================================================================
// GLOBAL INITIALIZATION AND EVENT HANDLERS
// =================================================================

// Auto-initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeCentralizedModals);

// Export functions to global scope for easy access
window.openContactModal = openContactModal;
window.closeContactModal = closeContactModal;
window.openEnquireModal = openEnquireModal;
window.closeEnquireModal = closeEnquireModal;
window.openBookNowModal = openBookNowModal;
window.closeBookNowModal = closeBookNowModal;
window.initializeCentralizedModals = initializeCentralizedModals;

// Handle clicks on elements with specific classes or data attributes
document.addEventListener('click', function(e) {
    // Contact modal triggers
    if (e.target.matches('[data-modal="contact"]') ||
        e.target.closest('[data-modal="contact"]') ||
        e.target.matches('.contact-trigger') ||
        e.target.closest('.contact-trigger')) {
        e.preventDefault();
        openContactModal();
    }

    // Enquire modal triggers
    if (e.target.matches('[data-modal="enquire"]') ||
        e.target.closest('[data-modal="enquire"]') ||
        e.target.matches('.enquire-trigger') ||
        e.target.closest('.enquire-trigger')) {
        e.preventDefault();
        openEnquireModal();
    }

    // Book now modal triggers
    if (e.target.matches('[data-modal="book"]') ||
        e.target.closest('[data-modal="book"]') ||
        e.target.matches('.book-trigger') ||
        e.target.closest('.book-trigger')) {
        e.preventDefault();
        const courseTitle = e.target.getAttribute('data-course') ||
                          e.target.closest('[data-course]')?.getAttribute('data-course') ||
                          document.title || '';
        const courseValue = e.target.getAttribute('data-course-value') ||
                          e.target.closest('[data-course-value]')?.getAttribute('data-course-value') ||
                          '';
        openBookNowModal(courseTitle, courseValue);
    }
});

// Handle escape key to close modals
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeContactModal();
        closeEnquireModal();
        closeBookNowModal();
    }
});