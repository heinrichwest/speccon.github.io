#!/bin/bash

# Process the remaining files one by one
FILES_TO_PROCESS=(
    "services-business-administration-nqf4.html"
    "mict-software-engineer-nqf6.html"
    "mict-systems-development-nqf4.html"
    "inseta-financial-advisor-nqf6.html"
    "wr-retail-manager-nqf5.html"
    "services-project-manager-nqf5.html"
    "services-quality-manager-nqf6.html"
    "etdp-education-training-nqf5.html"
    "teta-transport-clerk-nqf4.html"
    "agri-farming-nqf1.html"
)

PROCESSED=0

for file in "${FILES_TO_PROCESS[@]}"; do
    filepath="qualifications/$file"

    if [ ! -f "$filepath" ]; then
        echo "❌ File not found: $file"
        continue
    fi

    # Check if already has banner
    if grep -q "stickyBanner" "$filepath"; then
        echo "⏭️  Already has banner: $file"
        continue
    fi

    echo "🔄 Processing: $file"
    ((PROCESSED++))

    # Use Claude to update this specific file
done

echo "✅ Processed $PROCESSED files"