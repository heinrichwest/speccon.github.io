#!/bin/bash

# Comprehensive script to fix all qualification pages
# Files to fix based on user request

FILES=(
    "agri-animal-production-nqf2.html"
    "agri-animal-production-nqf4.html"
    "agri-farming-nqf1.html"
    "agri-farming-nqf2.html"
    "agri-fruit-packaging-nqf3.html"
    "agri-mixed-farming-nqf1.html"
    "agri-mixed-farming-nqf2.html"
    "agri-plant-production-nqf1.html"
    "agri-plant-production-nqf2.html"
    "agri-plant-production-nqf3.html"
    "agri-plant-production-nqf4.html"
    "etdp-education-training-nqf5.html"
    "fasset-computer-technician-nqf5.html"
    "inseta-financial-advisor-nqf6.html"
    "inseta-health-care-benefits-advisor-nqf5.html"
    "inseta-insurance-claims-administrator-assessor-nqf4.html"
    "inseta-insurance-underwriter-nqf5.html"
    "inseta-long-term-insurance-advisor-nqf4.html"
    "mer-automotive-sales-advisor-nqf4.html"
    "mict-systems-development-nqf4.html"
    "mict-business-analysis-nqf6.html"
    "mict-end-user-computing-nqf3.html"
    "mict-design-thinking-nqf4.html"
    "mict-software-engineer-nqf6.html"
    "mict-software-tester-nqf5.html"
    "services-new-venture-creation-nqf4.html"
    "services-generic-management-nqf5.html"
    "services-generic-management-nqf4.html"
    "services-new-venture-creation-smme-nqf2.html"
    "services-management-nqf3.html"
    "services-quality-manager-nqf6.html"
    "services-marketing-coordinator-nqf5.html"
    "services-contact-centre-manager-nqf5.html"
    "services-office-supervision-nqf5.html"
    "services-project-manager-nqf5.html"
    "services-quality-assurer-nqf5.html"
    "teta-transport-clerk-nqf4.html"
    "wr-planner-nqf5.html"
    "wr-retail-buyer-nqf5.html"
    "wr-retail-manager-nqf5.html"
    "wr-retail-supervisor-nqf4.html"
    "wr-sales-assistant-nqf3.html"
    "wr-service-station-assistant-nqf2.html"
    "wr-store-person-nqf2.html"
    "wr-visual-merchandiser-nqf3.html"
)

cd "qualifications"

echo "Checking status of files..."
echo "=========================="

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        if grep -q "Why Choose Us" "$file"; then
            echo "✅ $file - Already has correct header"
        elif grep -q "sticky-banner" "$file"; then
            echo "🔄 $file - Has banner but needs header update"
        else
            echo "❌ $file - Needs complete update"
        fi
    else
        echo "⚠️  $file - File not found"
    fi
done

echo ""
echo "Summary complete. Files checked: ${#FILES[@]}"