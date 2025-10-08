#!/bin/bash

# Script to update all qualification files with the sticky banner and enhanced navigation

echo "Starting batch update of qualification files..."

QUALIFICATIONS_DIR="qualifications"

# Check if directory exists
if [ ! -d "$QUALIFICATIONS_DIR" ]; then
    echo "Error: $QUALIFICATIONS_DIR directory not found"
    exit 1
fi

# List of files to update
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
    "services-business-administration-nqf3.html"
    "services-business-process-outsourcing-nqf3.html"
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
    "services-new-venture-creation-nqf4.html"
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

UPDATED_COUNT=0
SKIPPED_COUNT=0

# CSS to add for sticky banner (if not already present)
BANNER_CSS='        /* Sticky Banner Styles */
        .sticky-banner {
            position: fixed;
            top: 100px;
            right: 20px;
            background: linear-gradient(135deg, #12265E 0%, #FF9C2A 100%);
            color: white;
            padding: 12px 20px;
            border-radius: 50px;
            cursor: pointer;
            z-index: 1000;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            font-weight: 600;
            font-size: 14px;
            backdrop-filter: blur(10px);
        }
        .sticky-banner:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            background: linear-gradient(135deg, #0d1a47 0%, #e8891f 100%);
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
        .animate-scroll {
            animation: scroll 30s linear infinite;
        }
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-100%); }
        }'

echo "Starting updates..."

for file in "${FILES[@]}"; do
    filepath="$QUALIFICATIONS_DIR/$file"

    if [ ! -f "$filepath" ]; then
        echo "❌ File not found: $filepath"
        ((SKIPPED_COUNT++))
        continue
    fi

    # Create backup
    cp "$filepath" "$filepath.backup"

    # Check if sticky banner CSS is already present
    if ! grep -q "sticky-banner" "$filepath"; then
        # Add banner CSS before closing </style> tag
        sed -i 's|</style>|'"$BANNER_CSS"'\n    </style>|' "$filepath"
        echo "✅ Added banner CSS to: $file"
    fi

    # Add sticky banner HTML if not present
    if ! grep -q "stickyBanner" "$filepath"; then
        # This is a complex HTML insertion - would be better done with a proper tool
        echo "⚠️  Manual addition needed for banner HTML: $file"
    fi

    ((UPDATED_COUNT++))
done

echo ""
echo "📊 Update Summary:"
echo "   ✅ Updated: $UPDATED_COUNT files"
echo "   ⚠️  Skipped: $SKIPPED_COUNT files"
echo "   📁 Total attempted: ${#FILES[@]} files"
echo ""
echo "Note: Some files may need manual review for complete functionality."