#!/bin/bash

# Script to update all qualification pages:
# 1. Change button colors from orange to blue gradient (to match home page)
# 2. Add "Our Free Value Adds" sticky banner
# 3. Remove any remaining "Apply for learnership" text

echo "Starting batch update of qualification pages..."

# Directory containing qualification files
QUAL_DIR="qualifications"

# Counter for files processed
count=0

# Get the sticky banner HTML from the home page (we'll extract it manually)
STICKY_BANNER='    <!-- Sticky Banner -->
    <div id="stickyBanner" class="sticky-banner">
        <i data-lucide="gift" class="w-4 h-4 inline mr-2"></i>
        Our Free Value Adds
    </div>

    <!-- Banner Popup -->
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
            </div>

            <!-- Client Testimonials -->
            <div class="border-t pt-4">
                <h4 class="font-bold text-gray-900 mb-3 text-sm">What Our Clients Say</h4>
                <div class="space-y-3">
                    <div class="flex items-start space-x-3">
                        <img src="../Client Logos/AVI.PNG" alt="AVI" class="w-8 h-8 object-contain">
                        <div>
                            <p class="text-xs text-gray-700 italic">"SpecCon is knowledgeable, passionate and always goes the extra mile..."</p>
                            <p class="text-xs text-gray-500 mt-1">- Neteske Gerber, AVI</p>
                        </div>
                    </div>
                    <div class="flex items-start space-x-3">
                        <img src="../Client Logos/isuzu.PNG" alt="Isuzu" class="w-8 h-8 object-contain">
                        <div>
                            <p class="text-xs text-gray-700 italic">"The SpecCon LMS has transformed our training approach..."</p>
                            <p class="text-xs text-gray-500 mt-1">- Lisa van Aswegen, Isuzu</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Client Logos Scrolling Bar -->
            <div class="border-t pt-4 mt-4">
                <p class="text-xs text-gray-500 text-center mb-2">Trusted by Leading Companies</p>
                <div class="overflow-hidden">
                    <div class="flex animate-scroll">
                        <div class="flex space-x-4 min-w-max">
                            <img src="../Client Logos/AVI.PNG" alt="AVI" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/isuzu.PNG" alt="Isuzu" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/imperial.PNG" alt="Imperial" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/Afgri.png" alt="AFGRI" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/servest.png" alt="Servest" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/labournet.png" alt="LabourNet" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/absa.png" alt="ABSA" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/Heinekin.PNG" alt="Heineken" class="h-6 object-contain grayscale">
                        </div>
                        <div class="flex space-x-4 min-w-max">
                            <img src="../Client Logos/AVI.PNG" alt="AVI" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/isuzu.PNG" alt="Isuzu" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/imperial.PNG" alt="Imperial" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/Afgri.png" alt="AFGRI" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/servest.png" alt="Servest" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/labournet.png" alt="LabourNet" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/absa.png" alt="ABSA" class="h-6 object-contain grayscale">
                            <img src="../Client Logos/Heinekin.PNG" alt="Heineken" class="h-6 object-contain grayscale">
                        </div>
                    </div>
                </div>
            </div>

            <div class="mt-4">
                <a href="../index.html#contact" class="w-full bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white text-center py-3 px-4 rounded-lg text-sm font-semibold hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 block">
                    Enquire Now
                </a>
            </div>
        </div>
    </div>'

# Loop through all HTML files in qualifications directory
for file in "$QUAL_DIR"/*.html; do
    if [ -f "$file" ]; then
        echo "Processing: $file"

        # 1. Change button colors from orange gradient to blue gradient
        sed -i 's/from-\[#12265E\] to-\[#FF9C2A\]/from-[#12265E] to-[#4A90E2]/g' "$file"
        sed -i 's/hover:to-\[#e8891f\]/hover:to-[#3a7bc8]/g' "$file"

        # 2. Change "Apply for a Learnership" to "Enquire Now" if still present
        sed -i 's/Apply for a Learnership/Enquire Now/g' "$file"

        # 3. Add sticky banner styles to the <style> section if not already present
        if ! grep -q "sticky-banner" "$file"; then
            sed -i '/<\/style>/i \
        /* Sticky Banner Styles */\
        .sticky-banner {\
            position: fixed;\
            top: 100px;\
            right: 20px;\
            background: linear-gradient(135deg, #12265E 0%, #4A90E2 100%);\
            color: white;\
            padding: 12px 20px;\
            border-radius: 50px;\
            cursor: pointer;\
            z-index: 1000;\
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);\
            transition: all 0.3s ease;\
            font-weight: 600;\
            font-size: 14px;\
            backdrop-filter: blur(10px);\
        }\
        .sticky-banner:hover {\
            transform: translateY(-2px);\
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);\
            background: linear-gradient(135deg, #0d1a47 0%, #3a7bc8 100%);\
        }\
        .banner-popup {\
            position: fixed;\
            top: 160px;\
            right: 20px;\
            background: white;\
            border-radius: 20px;\
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);\
            z-index: 999;\
            overflow: hidden;\
            transform: translateY(-20px);\
            opacity: 0;\
            pointer-events: none;\
            transition: all 0.3s ease;\
            max-width: 420px;\
            width: 90vw;\
        }\
        .banner-popup.show {\
            transform: translateY(0);\
            opacity: 1;\
            pointer-events: all;\
        }\
        .animate-scroll {\
            animation: scroll 30s linear infinite;\
        }\
        @keyframes scroll {\
            0% { transform: translateX(0); }\
            100% { transform: translateX(-100%); }\
        }' "$file"
        fi

        # 4. Add sticky banner HTML before footer if not already present
        if ! grep -q "stickyBanner" "$file"; then
            sed -i '/<footer/i \'"$STICKY_BANNER"'' "$file"
        fi

        # 5. Add banner JavaScript before closing </body> tag if not already present
        if ! grep -q "stickyBanner" "$file"; then
            sed -i '/<\/body>/i \
    <script>\
        // Sticky Banner Functionality\
        const stickyBanner = document.getElementById("stickyBanner");\
        const bannerPopup = document.getElementById("bannerPopup");\
        const closePopup = document.getElementById("closePopup");\
        let isPopupOpen = false;\
\
        // Show banner immediately when page loads\
        stickyBanner.style.display = "block";\
\
        // Toggle popup on banner hover/click\
        stickyBanner.addEventListener("mouseenter", function() {\
            if (!isPopupOpen) {\
                bannerPopup.classList.add("show");\
                isPopupOpen = true;\
            }\
        });\
\
        stickyBanner.addEventListener("click", function() {\
            bannerPopup.classList.toggle("show");\
            isPopupOpen = !isPopupOpen;\
        });\
\
        // Close popup\
        closePopup.addEventListener("click", function() {\
            bannerPopup.classList.remove("show");\
            isPopupOpen = false;\
        });\
\
        // Close popup when clicking outside\
        document.addEventListener("click", function(e) {\
            if (!stickyBanner.contains(e.target) && !bannerPopup.contains(e.target)) {\
                bannerPopup.classList.remove("show");\
                isPopupOpen = false;\
            }\
        });\
    </script>' "$file"
        fi

        ((count++))
    fi
done

echo "Completed! Processed $count files."
echo "Changes made:"
echo "- Updated button colors to match home page (blue gradient)"
echo "- Added 'Our Free Value Adds' sticky banner"
echo "- Removed any remaining 'Apply for learnership' text"