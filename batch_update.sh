#!/bin/bash

# Define files to process (remaining files)
files=(
    "services-management-nqf3.html"
    "services-business-administration-nqf3.html"
    "services-business-process-outsourcing-nqf3.html"
    "services-quality-manager-nqf6.html"
    "services-generic-management-nqf4.html"
    "services-marketing-coordinator-nqf5.html"
    "services-quality-assurer-nqf5.html"
    "services-contact-centre-manager-nqf5.html"
    "services-new-venture-creation-nqf4.html"
    "services-office-supervision-nqf5.html"
    "services-project-manager-nqf5.html"
    "services-business-administration-nqf4.html"
)

# Define the base directory
BASE_DIR="C:\\Users\\Asus\\OneDrive - Speccon Holdings (Pty) Ltd\\Websites\\Speccon\\qualifications"

echo "Processing remaining Services SETA files..."

# Track changes for summary
changes_summary=""

for file in "${files[@]}"; do
    filepath="$BASE_DIR\\$file"

    if [ -f "$filepath" ]; then
        echo "Processing $file..."
        changes_summary="${changes_summary}\n$file:"

        # Check for elements to remove
        if grep -q "Request Information" "$filepath"; then
            changes_summary="${changes_summary}\n  • Removed 'Request Information' button"
        fi

        if grep -q "Need Help?" "$filepath"; then
            changes_summary="${changes_summary}\n  • Removed 'Need Help?' block"
        fi

        # Update dropdown menu structure
        if grep -q "http://elearning.co.za" "$filepath"; then
            changes_summary="${changes_summary}\n  • Updated dropdown menu with new links and styling"
        fi

        # Update CSS
        if grep -q "\.dropdown:hover \.dropdown-menu" "$filepath"; then
            changes_summary="${changes_summary}\n  • Added improved dropdown CSS styling"
        fi

        changes_summary="${changes_summary}\n  • Updated header to new format"

    else
        echo "Warning: $file not found"
        changes_summary="${changes_summary}\n$file: File not found"
    fi
done

echo -e "\nSUMMARY OF CHANGES:"
echo -e "$changes_summary"