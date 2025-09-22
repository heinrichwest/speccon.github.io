# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the SpecCon Holdings website codebase - a static HTML website for an accredited training provider specializing in professional qualifications across multiple SETAs (Sector Education and Training Authorities) in South Africa.

## Key Commands

### Development Server
```bash
# Start a local development server (Python)
python -m http.server 8000

# Alternative using npx
npx http-server

# Open the main site
start index.html
```

### Content Management Scripts

**Qualification Pages Updates:**
```bash
# Update all qualification pages with standardized template
./update_qualification_pages.py

# Systematic update with error handling
./complete_systematic_update.py

# Update specific qualification files
./update_files.sh

# Fix qualification page issues
./fix_qualification_pages.py

# Mass update multiple files
./mass_update.sh
```

**Content Processing:**
```bash
# Batch update multiple files
./batch_update.sh

# Process remaining qualification files
./process_remaining.sh

# Comprehensive fix for common issues
./comprehensive_fix.sh
```

**Modal System Management:**
```bash
# Update all pages to use centralized modal system
python update_modals.py

# Update all pages to use centralized value-adds popup
python update_value_adds_popup.py

# Clean up inline popup implementations
./cleanup_inline_popups.sh

# Manual modal implementation (if Python unavailable)
# See MODAL_IMPLEMENTATION_GUIDE.md for step-by-step instructions
```

## Architecture Overview

### Directory Structure
- **`/`** - Main landing page (`index.html`) and root assets
- **`qualifications/`** - Individual qualification detail pages (47+ HTML files)
- **`short-courses/`** - Short course offering pages
- **`setas/`** - SETA-specific information pages
- **`Images/`** - All website imagery and logos
- **`js/`** - JavaScript functionality (popup handling, interactions)
- **`Client Logos/`** - Client reference materials
- **`Videos/`** - Video content assets

### Key Page Types

1. **Main Landing Page** (`index.html`)
   - Tailwind CSS framework
   - Responsive design with hero sections
   - Navigation with dropdown menus
   - Client testimonials and course showcases

2. **Qualification Pages** (`qualifications/*.html`)
   - Standardized template based on `services-business-administration-nqf4.html`
   - SETA-specific branding and content
   - Structured qualification information (NLRD ID, credits, duration, etc.)
   - Color-coded module sections with gradient backgrounds
   - Sticky banner functionality for inquiries

3. **Short Course Pages** (`short-courses/*.html`)
   - Specialized training offerings
   - AI training, compliance, cyber security, etc.

### Technical Stack
- **Frontend**: Static HTML with Tailwind CSS
- **Typography**: Inter font family for qualification pages, Roboto for main site
- **Icons**: Lucide icon library
- **Styling**: CSS gradients and hover effects for professional appearance
- **JavaScript**: Centralized modal system, value-adds popup, interactive elements
- **Modal System**: Centralized in `js/centralized-modals.js` for consistent UX across all pages

### Content Management System

The site uses a systematic approach to manage 47+ qualification pages across 7 SETAs:
- **Services SETA** (15 pages) - Business administration, management, quality assurance
- **AgriSETA** (12 pages) - Agricultural and farming qualifications
- **W&R SETA** (10 pages) - Wholesale and retail qualifications
- **INSETA** (5 pages) - Insurance sector qualifications
- **ETDP SETA** (3 pages) - Education and training development
- **MICT SETA** (3 pages) - Media, IT, and communications
- **FASSET** (1 page) - Financial and accounting services

### Standardization Template

All qualification pages follow a standardized template featuring:
- Hero section with qualification icon, NQF level, SETA, and key statistics
- Structured learning outcomes with check icons
- Career opportunities grid with professional icons
- Comprehensive sidebar with qualification details
- Related qualifications section with hover effects
- Consistent SpecCon branding and color scheme

### Python Scripts

The codebase includes several Python automation scripts:
- **Qualification page generation** and bulk updates
- **SAQA API integration** for qualification data fetching
- **Template standardization** across all qualification pages
- **Content validation** and error checking

### Common Development Tasks

**Adding New Qualifications:**
1. Use existing qualification template from `qualifications/services-business-administration-nqf4.html`
2. Update qualification-specific details (NLRD ID, credits, SETA, etc.)
3. Ensure proper SETA color coding and branding
4. Add to relevant update scripts for future maintenance

**Updating Qualification Content:**
1. Use the Python update scripts for bulk changes
2. Maintain consistency with the standardized template
3. Verify SAQA compliance for qualification details

**Managing Assets:**
- Images stored in `Images/` directory with descriptive naming
- Client logos organized in `Client Logos/` subdirectory
- Videos stored in `Videos/` directory

## Centralized Modal System

### Overview
All website modals are managed through a centralized system located in `js/centralized-modals.js`. This ensures consistency across all pages and makes maintenance easier.

### Modal Types
1. **Contact Modal** - General contact inquiries (all pages)
2. **Enquire Now Modal** - Quick enquiries for training services (SETA/qualification pages)
3. **Book Now Modal** - Course booking requests (short course pages)
4. **Value-Adds Popup** - Free benefits showcase with SDF Service (SETA/qualification pages)

### Implementation
- **Modal Script**: `js/centralized-modals.js` for contact, enquire, and book modals
- **Value-Adds Script**: `js/value-adds-popup.js` for benefits popup with SDF Service
- **Include Scripts**: Add both scripts to page head for full functionality
- **Triggers**: Use `data-modal="type"` attributes or direct function calls
- **Documentation**: See `MODAL_IMPLEMENTATION_GUIDE.md` for complete instructions

### Value-Adds Popup Features
- **7 Core Benefits**: White Labelled LMS, 300+ Online Courses, Employment Equity System, Work Assessments, Compliance Training, Academy Access, **SDF Service**
- **SDF Service**: Skills Development Facilitator support included in all popups
- **Centralized**: Edit `js/value-adds-popup.js` to update all SETA and qualification pages
- **Auto-Generated**: Sticky banner and popup HTML/CSS generated automatically

### Modal Triggers
```html
<!-- Contact Modal -->
<a href="#" data-modal="contact">Contact Us</a>

<!-- Enquire Modal -->
<a href="#" data-modal="enquire">Enquiry now</a>

<!-- Book Training Modal -->
<a href="#" data-modal="book" data-course="Course Name">Book Training</a>

<!-- Book Training Modal with course pre-selection -->
<a href="#" data-modal="book" data-course="Excel Training" data-course-value="excel-basic">Book Now</a>
```

### Header Navigation by Page Type
- **Main Page**: Why Choose us, Qualifications, Accreditations, Classroom Training, Other products (Dropdown), Contact Us, Apply for Learnerships (POPUP)
- **SETA & Qualification Pages**: Why Choose us, Qualifications, Accreditations, Classroom Training, Other products (Dropdown), Enquiry now (POPUP)
- **Short Course Pages**: Why Choose us, Qualifications, Accreditations, Classroom Training, Other products (Dropdown), Book Training (POPUP)

## Brand Guidelines

- **Primary Colors**: SpecCon Blue (#12265E), SpecCon Light Blue (#92abc4)
- **Typography**: Inter (qualifications), Roboto (main site)
- **Professional appearance** with gradient backgrounds and hover effects
- **Consistent branding** across all SETA qualification pages