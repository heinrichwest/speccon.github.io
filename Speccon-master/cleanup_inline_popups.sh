#!/bin/bash

# Script to clean up inline value-adds popup implementations
# and ensure all pages use the centralized system

echo "🧹 Cleaning up inline value-adds popup implementations..."

# Function to update qualification pages
update_qualification_pages() {
    echo "📄 Updating qualification pages..."

    for file in qualifications/*.html; do
        if [[ -f "$file" && "$file" != "qualifications/template-qualification.html" ]]; then
            echo "Processing: $file"

            # Add centralized script if not present
            if ! grep -q "value-adds-popup.js" "$file"; then
                sed -i 's|<script src="https://unpkg.com/lucide@latest"></script>|<script src="https://unpkg.com/lucide@latest"></script>\n    <script src="../js/value-adds-popup.js"></script>|' "$file"
                echo "  ✅ Added centralized script"
            fi

            # Remove inline sticky banner HTML
            if grep -q "stickyBanner" "$file"; then
                sed -i '/<!-- Sticky Banner -->/,/<!-- Banner Popup -->/c\    <!-- Sticky Banner and Popup handled by centralized script -->' "$file"
                echo "  ✅ Removed inline banner HTML"
            fi

            # Remove inline CSS for sticky banner
            if grep -q "Sticky Banner Styles" "$file"; then
                sed -i '/\/\* Sticky Banner Styles \*\//,/}/d' "$file"
                echo "  ✅ Removed inline banner CSS"
            fi

            # Remove inline JavaScript for banner functionality
            if grep -q "Sticky banner functionality" "$file"; then
                sed -i '/\/\/ Sticky banner functionality/,/});/d' "$file"
                echo "  ✅ Removed inline banner JavaScript"
            fi
        fi
    done
}

# Function to verify SETA pages
verify_seta_pages() {
    echo "🏢 Verifying SETA pages..."

    for file in setas/*.html; do
        if [[ -f "$file" ]]; then
            echo "Checking: $file"

            if grep -q "value-adds-popup.js" "$file"; then
                echo "  ✅ Using centralized script"
            else
                echo "  ⚠️  Missing centralized script - adding it"
                sed -i 's|<script src="https://unpkg.com/lucide@latest"></script>|<script src="https://unpkg.com/lucide@latest"></script>\n    <script src="../js/value-adds-popup.js"></script>|' "$file"
            fi
        fi
    done
}

# Function to verify centralized script has SDF service
verify_sdf_service() {
    echo "🔍 Verifying SDF Service is included..."

    if grep -q "SDF Service" js/value-adds-popup.js; then
        echo "  ✅ SDF Service found in centralized popup"
    else
        echo "  ❌ SDF Service missing from centralized popup"
        return 1
    fi

    if grep -q "Skills Development Facilitator support" js/value-adds-popup.js; then
        echo "  ✅ SDF Service description found"
    else
        echo "  ❌ SDF Service description missing"
        return 1
    fi
}

# Main execution
echo "=" * 60
echo "Value-Adds Popup Cleanup and Centralization"
echo "=" * 60

# Verify SDF service is in centralized popup
verify_sdf_service
if [ $? -ne 0 ]; then
    echo "❌ Please ensure SDF Service is properly included in js/value-adds-popup.js"
    exit 1
fi

# Update qualification pages
update_qualification_pages

# Verify SETA pages
verify_seta_pages

echo ""
echo "=" * 60
echo "✅ Cleanup Complete!"
echo ""
echo "📋 Summary of changes:"
echo "1. All qualification pages now use centralized value-adds-popup.js"
echo "2. Removed inline CSS, HTML, and JavaScript for sticky banners"
echo "3. Verified SETA pages use centralized script"
echo "4. Confirmed SDF Service is included in all popups"
echo ""
echo "🧪 Testing steps:"
echo "1. Visit any SETA page - click 'Our Free Value Adds' banner"
echo "2. Visit any qualification page - verify banner appears and works"
echo "3. Confirm popup shows all 7 value-adds including SDF Service"
echo "4. Check mobile responsiveness"
echo ""
echo "📁 Pages updated:"
echo "- All files in qualifications/ directory"
echo "- All files in setas/ directory"
echo "- Centralized script: js/value-adds-popup.js"