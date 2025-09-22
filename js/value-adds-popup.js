// Centralized Value-Added Benefits Popup
// This file contains the popup content and functionality used across all SETA pages

const VALUE_ADDS_POPUP_HTML = `
<div id="bannerPopup" class="banner-popup">
    <div class="p-6">
        <div class="flex items-center justify-between mb-4">
            <h3 class="text-xl font-bold text-gray-900">Value-Added Benefits</h3>
            <button id="closePopup" class="text-gray-400 hover:text-gray-600">
                <i data-lucide="x" class="w-5 h-5"></i>
            </button>
        </div>
        <p class="text-gray-600 text-sm mb-6">You can get these value adds for free when you do learnerships with SpecCon</p>

        <!-- Value Adds Grid -->
        <div class="grid grid-cols-1 gap-4 mb-6">
            <div class="flex items-center p-3 bg-blue-50 rounded-lg">
                <div class="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center mr-3">
                    <i data-lucide="layout-template" class="w-4 h-4 text-white"></i>
                </div>
                <div>
                    <h4 class="font-semibold text-sm text-gray-900">White Labelled LMS</h4>
                    <p class="text-xs text-gray-600">Complete Learning Management System</p>
                </div>
            </div>
            <div class="flex items-center p-3 bg-green-50 rounded-lg">
                <div class="w-8 h-8 bg-green-500 rounded-lg flex items-center justify-center mr-3">
                    <i data-lucide="book-open" class="w-4 h-4 text-white"></i>
                </div>
                <div>
                    <h4 class="font-semibold text-sm text-gray-900">300+ Online Courses</h4>
                    <p class="text-xs text-gray-600">Comprehensive course library</p>
                </div>
            </div>
            <div class="flex items-center p-3 bg-purple-50 rounded-lg">
                <div class="w-8 h-8 bg-purple-500 rounded-lg flex items-center justify-center mr-3">
                    <i data-lucide="users" class="w-4 h-4 text-white"></i>
                </div>
                <div>
                    <h4 class="font-semibold text-sm text-gray-900">Employment Equity System</h4>
                    <p class="text-xs text-gray-600">Compliance and reporting</p>
                </div>
            </div>
            <div class="flex items-center p-3 bg-blue-50 rounded-lg">
                <div class="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center mr-3">
                    <i data-lucide="clipboard-check" class="w-4 h-4 text-white"></i>
                </div>
                <div>
                    <h4 class="font-semibold text-sm text-gray-900">10+ Work Assessments</h4>
                    <p class="text-xs text-gray-600">Excel & workplace skills tests</p>
                </div>
            </div>
            <div class="flex items-center p-3 bg-red-50 rounded-lg">
                <div class="w-8 h-8 bg-red-500 rounded-lg flex items-center justify-center mr-3">
                    <i data-lucide="shield-check" class="w-4 h-4 text-white"></i>
                </div>
                <div>
                    <h4 class="font-semibold text-sm text-gray-900">Compliance Training</h4>
                    <p class="text-xs text-gray-600">First Aid, Fire Fighter, OHS</p>
                </div>
            </div>
            <div class="flex items-center p-3 bg-teal-50 rounded-lg">
                <div class="w-8 h-8 bg-teal-500 rounded-lg flex items-center justify-center mr-3">
                    <i data-lucide="graduation-cap" class="w-4 h-4 text-white"></i>
                </div>
                <div>
                    <h4 class="font-semibold text-sm text-gray-900">Academy Access</h4>
                    <p class="text-xs text-gray-600">Resources for staff children</p>
                </div>
            </div>
            <div class="flex items-center p-3 bg-orange-50 rounded-lg">
                <div class="w-8 h-8 bg-orange-500 rounded-lg flex items-center justify-center mr-3">
                    <i data-lucide="briefcase" class="w-4 h-4 text-white"></i>
                </div>
                <div>
                    <h4 class="font-semibold text-sm text-gray-900">SDF Service</h4>
                    <p class="text-xs text-gray-600">Skills Development Facilitator support</p>
                </div>
            </div>
        </div>

        <!-- Client Testimonials -->
        <div class="border-t pt-4">
            <h4 class="font-bold text-gray-900 mb-3 text-sm">What Our Clients Say</h4>
            <div class="space-y-3">
                <div class="flex items-start space-x-3">
                    <img src="../Client Logos/AVI.PNG" alt="AVI" class="w-8 h-8 object-contain">
                    <div class="flex-1">
                        <p class="text-xs text-gray-600 italic">"SpecCon is knowledgeable, passionate and always goes the extra mile..."</p>
                        <p class="text-xs text-gray-500 mt-1">- Netselise Gerber, AVI</p>
                    </div>
                </div>
                <div class="flex items-start space-x-3">
                    <img src="../Client Logos/isuzu.PNG" alt="Isuzu" class="w-8 h-8 object-contain">
                    <div class="flex-1">
                        <p class="text-xs text-gray-600 italic">"The SpecCon LMS has transformed our training approach..."</p>
                        <p class="text-xs text-gray-500 mt-1">- Lisa van Aswegen, Isuzu</p>
                    </div>
                </div>
            </div>

            <!-- Trusted Companies -->
            <div class="mt-4 pt-3 border-t">
                <p class="text-xs text-gray-500 mb-2">Trusted by Leading Companies</p>
                <div class="flex items-center justify-between opacity-60">
                    <img src="../Client Logos/capitec.PNG" alt="Capitec" class="h-6 object-contain">
                    <img src="../Client Logos/engen.PNG" alt="Engen" class="h-6 object-contain">
                    <img src="../Client Logos/absa.png" alt="ABSA" class="h-6 object-contain">
                </div>
            </div>

            <div class="mt-4 text-center">
                <button class="bg-gradient-to-r from-blue-600 to-blue-700 text-white text-sm font-semibold px-4 py-2 rounded-lg hover:from-blue-700 hover:to-blue-800 transition duration-300">
                    Enquire Now
                </button>
            </div>
        </div>
    </div>
</div>`;

const VALUE_ADDS_CSS = `
<style>
    .sticky-banner {
        position: fixed;
        top: 100px;
        right: 20px;
        background: linear-gradient(135deg, #12265E 0%, #4A90E2 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 50px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        cursor: pointer;
        z-index: 998;
        transition: all 0.3s ease;
        font-weight: 600;
        font-size: 14px;
        backdrop-filter: blur(10px);
    }

    .sticky-banner:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        background: linear-gradient(135deg, #0d1a47 0%, #3a7bc8 100%);
    }

    .banner-popup {
        position: fixed;
        top: 160px;
        right: 20px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        z-index: 999;
        overflow: hidden;
        transform: translateY(-20px);
        opacity: 0;
        pointer-events: none;
        transition: all 0.3s ease;
        max-width: 420px;
        width: 90vw;
    }

    .banner-popup.show {
        transform: translateY(0);
        opacity: 1;
        pointer-events: all;
    }
</style>`;

// Function to initialize the value-adds popup
function initializeValueAddsPopup() {
    // Add CSS to the head
    const head = document.querySelector('head');
    head.insertAdjacentHTML('beforeend', VALUE_ADDS_CSS);

    // Add sticky banner if it doesn't exist
    if (!document.getElementById('stickyBanner')) {
        const stickyBannerHTML = `
        <div id="stickyBanner" class="sticky-banner">
            <i data-lucide="gift" class="w-4 h-4 inline mr-2"></i>
            Our Free Value Adds
        </div>`;
        document.body.insertAdjacentHTML('beforeend', stickyBannerHTML);
    }

    // Add popup HTML if it doesn't exist
    if (!document.getElementById('bannerPopup')) {
        document.body.insertAdjacentHTML('beforeend', VALUE_ADDS_POPUP_HTML);
    }

    // Initialize functionality
    setupPopupFunctionality();

    // Re-initialize Lucide icons for new elements
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

// Function to setup popup functionality
function setupPopupFunctionality() {
    const stickyBanner = document.getElementById('stickyBanner');
    const bannerPopup = document.getElementById('bannerPopup');
    const closePopup = document.getElementById('closePopup');

    if (stickyBanner && bannerPopup && closePopup) {
        // Show popup when banner is hovered
        stickyBanner.addEventListener('mouseenter', () => {
            bannerPopup.classList.add('show');
        });

        // Show popup when banner is clicked (backup)
        stickyBanner.addEventListener('click', () => {
            bannerPopup.classList.add('show');
        });

        // Hide popup when mouse leaves both banner and popup
        let hideTimeout;
        const hidePopup = () => {
            hideTimeout = setTimeout(() => {
                bannerPopup.classList.remove('show');
            }, 300); // Small delay to allow moving between elements
        };

        const cancelHide = () => {
            if (hideTimeout) {
                clearTimeout(hideTimeout);
                hideTimeout = null;
            }
        };

        stickyBanner.addEventListener('mouseleave', hidePopup);
        bannerPopup.addEventListener('mouseenter', cancelHide);
        bannerPopup.addEventListener('mouseleave', hidePopup);

        // Hide popup when close button is clicked
        closePopup.addEventListener('click', () => {
            bannerPopup.classList.remove('show');
        });

        // Hide popup when clicking outside
        document.addEventListener('click', (e) => {
            if (!bannerPopup.contains(e.target) && !stickyBanner.contains(e.target)) {
                bannerPopup.classList.remove('show');
            }
        });
    }
}

// Auto-initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeValueAddsPopup);

// Export for manual initialization if needed
window.initializeValueAddsPopup = initializeValueAddsPopup;