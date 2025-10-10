#!/usr/bin/env python3
"""
Update services-quality-manager-nqf6.html with correct qualification details:
- Occupational Certificate: Quality Manager
- Services SETA
- NQF Level 6
- 270 Credits
- NLRD ID: 118768
"""

import re

# Read the file
file_path = r'qualifications\services-quality-manager-nqf6.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make all the replacements
replacements = [
    # Title and meta
    (r'<title>.*?</title>', '<title>Occupational Certificate: Quality Manager NQF Level 6 | Services SETA | SpecCon Holdings</title>'),
    (r'<meta name="description" content=".*?"', '<meta name="description" content="Master quality management systems with our NQF Level 6 Occupational Certificate: Quality Manager qualification accredited by Services SETA. 270 credits, NLRD ID 118768, comprehensive quality leadership training."'),

    # Breadcrumb
    (r'<span class="text-\[#12265E\] font-semibold">.*?NQF Level \d+</span>', '<span class="text-[#12265E] font-semibold">Occupational Certificate: Quality Manager NQF Level 6</span>'),

    # Hero section - qualification name and SETA
    (r'<span class="text-\[#ffa600\] font-semibold">NQF Level \d+ \| Services SETA</span>', '<span class="text-[#ffa600] font-semibold">NQF Level 6 | Services SETA</span>'),
    (r'<h1 class="text-4xl md:text-5xl font-bold text-\[#12265E\]">Quality Manager</h1>', '<h1 class="text-4xl md:text-5xl font-bold text-[#12265E]">Occupational Certificate: Quality Manager</h1>'),

    # Hero description
    (r'Develop essential customer service skills.*?various industries\.', 'Master quality management systems, lead quality assurance initiatives, and drive organizational excellence. This advanced qualification prepares you for senior quality management and leadership roles across various industries.'),

    # Stats boxes - credits, duration and NQF level
    (r'<div class="text-xl font-bold text-white">144</div>\s*<div class="text-sm text-white/80">Credits</div>', '<div class="text-xl font-bold text-white">270</div>\n                            <div class="text-sm text-white/80">Credits</div>'),
    (r'<div class="text-xl font-bold text-white">12</div>\s*<div class="text-sm text-white/80">Months</div>', '<div class="text-xl font-bold text-white">24</div>\n                            <div class="text-sm text-white/80">Months</div>'),
    (r'<div class="text-xl font-bold text-white">NQF 2</div>', '<div class="text-xl font-bold text-white">NQF 6</div>'),

    # Qualification overview
    (r'This Customer Service qualification is designed to provide learners with the knowledge, skills,\s*and attitudes required to deliver excellent customer service in various business environments\.\s*The qualification covers fundamental customer service principles, communication techniques,\s*and problem-solving strategies\.',
     'This Occupational Certificate: Quality Manager qualification is designed to provide learners with advanced knowledge, skills, and competencies required to lead quality management systems and drive continuous improvement. The qualification covers quality management principles, ISO standards implementation, process optimization, auditing, and organizational quality leadership.'),

    # Learning outcomes
    (r'Apply customer service principles and best practices', 'Develop and implement comprehensive quality management systems'),
    (r'Communicate effectively with customers using various channels', 'Lead quality audits and ensure compliance with international standards'),
    (r'Handle customer complaints and resolve conflicts professionally', 'Drive continuous improvement initiatives across the organization'),
    (r'Use customer service technology and systems effectively', 'Analyze quality metrics and implement corrective actions'),
    (r'Work as part of a customer service team', 'Manage quality assurance teams and stakeholder relationships'),
    (r'Maintain professional standards and ethics', 'Apply ISO 9001 and other quality management frameworks'),

    # Career opportunities
    (r'Customer Service Representative', 'Quality Manager'),
    (r'Call Center Agent', 'Quality Assurance Manager'),
    (r'Reception Desk Officer', 'Quality Systems Manager'),
    (r'Retail Sales Assistant', 'Compliance Manager'),
    (r'Help Desk Support', 'Process Improvement Manager'),
    (r'Customer Relations Officer', 'ISO Implementation Specialist'),

    # Core modules
    (r'Customer Service Fundamentals</h4>\s*<p class="text-white text-sm">Introduction to customer service principles, customer types, and service standards\.',
     'Quality Management Systems</h4>\n                            <p class="text-white text-sm">ISO 9001 standards, quality frameworks, and organizational quality infrastructure.'),
    (r'Communication Skills</h4>\s*<p class="text-white text-sm">Verbal and non-verbal communication, active listening, and professional language\.',
     'Quality Auditing & Compliance</h4>\n                            <p class="text-white text-sm">Internal and external audits, compliance monitoring, and regulatory requirements.'),
    (r'Problem Solving</h4>\s*<p class="text-white text-sm">Identifying customer needs, complaint handling, and conflict resolution\.',
     'Continuous Improvement</h4>\n                            <p class="text-white text-sm">Lean Six Sigma, process optimization, and performance measurement systems.'),
    (r'Technology in Customer Service</h4>\s*<p class="text-white text-sm">Using CRM systems, databases, and digital communication tools\.',
     'Quality Leadership</h4>\n                            <p class="text-white text-sm">Strategic quality planning, team management, and organizational change management.'),

    # Sidebar - add NLRD ID
    (r'(<div class="flex justify-between items-center py-3 border-b border-gray-100">\s*<span class="text-gray-600">SETA</span>\s*<span class="font-semibold">Services SETA</span>\s*</div>)',
     r'\1\n                            <div class="flex justify-between items-center py-3 border-b border-gray-100">\n                                <span class="text-gray-600">NLRD ID</span>\n                                <span class="font-semibold">118768</span>\n                            </div>'),
    (r'<span class="text-gray-600">NQF Level</span>\s*<span class="font-semibold">Level 2</span>',
     '<span class="text-gray-600">NQF Level</span>\n                                <span class="font-semibold">Level 6</span>'),
    (r'<span class="text-gray-600">Duration</span>\s*<span class="font-semibold">12 Months</span>',
     '<span class="text-gray-600">Duration</span>\n                                <span class="font-semibold">24 Months</span>'),

    # Modal title
    (r'Enquire About Quality Manager NQF6', 'Enquire About Occupational Certificate: Quality Manager NQF6'),

    # Form qualification field
    (r"qualification: 'Quality Manager NQF6'", "qualification: 'Occupational Certificate: Quality Manager NQF6 - NLRD ID: 118768'"),

    # Image alt text
    (r'alt="Customer service professional"', 'alt="Quality Manager professional"'),
]

# Apply all replacements
for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write the updated content
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated services-quality-manager-nqf6.html")
print("  - Title: Occupational Certificate: Quality Manager")
print("  - SETA: Services SETA")
print("  - NQF Level: 6")
print("  - Credits: 270")
print("  - Duration: 24 Months")
print("  - NLRD ID: 118768")
