#!/usr/bin/env python3
"""
Update services-project-manager-nqf5.html with correct qualification details:
- Occupational Certificate: Project Manager
- ETA SETA
- NQF Level 5
- 240 Credits
- NLRD ID: 101869
"""

import re

# Read the file
file_path = r'qualifications\services-project-manager-nqf5.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make all the replacements
replacements = [
    # Title and meta
    (r'<title>.*?</title>', '<title>Occupational Certificate: Project Manager NQF Level 5 | ETA | SpecCon Holdings</title>'),
    (r'<meta name="description" content=".*?"', '<meta name="description" content="Lead projects from initiation to completion with our NQF Level 5 Occupational Certificate: Project Manager qualification accredited by ETA. 240 credits, NLRD ID 101869, comprehensive project management training."'),

    # Header SETA reference
    (r'<p class="text-sm text-\[#ffa600\]">Services SETA Qualifications</p>', '<p class="text-sm text-[#ffa600]">ETA Qualifications</p>'),

    # Breadcrumb
    (r'<a href="\.\./setas/services-seta\.html" class="hover:text-\[#ffa600\]">Services SETA</a>', '<a href="../setas/eta-seta.html" class="hover:text-[#ffa600]">ETA</a>'),
    (r'<span class="text-\[#12265E\] font-semibold">.*? NQF Level \d+</span>', '<span class="text-[#12265E] font-semibold">Occupational Certificate: Project Manager NQF Level 5</span>'),

    # Hero section - qualification name and SETA
    (r'<span class="text-\[#ffa600\] font-semibold">NQF Level \d+ \| Services SETA</span>', '<span class="text-[#ffa600] font-semibold">NQF Level 5 | ETA</span>'),
    (r'<h1 class="text-4xl md:text-5xl font-bold text-\[#12265E\]">Project Manager</h1>', '<h1 class="text-4xl md:text-5xl font-bold text-[#12265E]">Occupational Certificate: Project Manager</h1>'),

    # Hero description
    (r'Develop essential customer service skills.*?various industries\.', 'Lead projects from initiation to completion with comprehensive project management skills. This occupational qualification prepares you for professional project management roles across various industries.'),

    # Stats boxes - duration and NQF level
    (r'<div class="text-xl font-bold text-white">12</div>\s*<div class="text-sm text-white/80">Months</div>', '<div class="text-xl font-bold text-white">18</div>\n                            <div class="text-sm text-white/80">Months</div>'),
    (r'<div class="text-xl font-bold text-white">NQF 2</div>', '<div class="text-xl font-bold text-white">NQF 5</div>'),

    # Qualification overview
    (r'This Customer Service qualification is designed to provide learners with the knowledge, skills,\s*and attitudes required to deliver excellent customer service in various business environments\.\s*The qualification covers fundamental customer service principles, communication techniques,\s*and problem-solving strategies\.',
     'This Occupational Certificate: Project Manager qualification is designed to provide learners with the knowledge, skills, and competencies required to effectively manage projects from initiation through to completion. The qualification covers project planning, resource management, risk assessment, stakeholder engagement, and project monitoring and evaluation.'),

    # Learning outcomes
    (r'Apply customer service principles and best practices', 'Develop comprehensive project plans and schedules'),
    (r'Communicate effectively with customers using various channels', 'Manage project resources, budgets, and timelines effectively'),
    (r'Handle customer complaints and resolve conflicts professionally', 'Identify, assess, and mitigate project risks'),
    (r'Use customer service technology and systems effectively', 'Lead project teams and manage stakeholder expectations'),
    (r'Work as part of a customer service team', 'Monitor project progress and implement corrective actions'),
    (r'Maintain professional standards and ethics', 'Apply project management methodologies and best practices'),

    # Career opportunities
    (r'Customer Service Representative', 'Project Manager'),
    (r'Call Center Agent', 'Programme Manager'),
    (r'Reception Desk Officer', 'Project Coordinator'),
    (r'Retail Sales Assistant', 'Construction Project Manager'),
    (r'Help Desk Support', 'IT Project Manager'),
    (r'Customer Relations Officer', 'Project Team Leader'),

    # Core modules
    (r'Customer Service Fundamentals</h4>\s*<p class="text-white text-sm">Introduction to customer service principles, customer types, and service standards\.',
     'Project Planning & Initiation</h4>\n                            <p class="text-white text-sm">Defining project scope, objectives, deliverables, and developing comprehensive project plans.'),
    (r'Communication Skills</h4>\s*<p class="text-white text-sm">Verbal and non-verbal communication, active listening, and professional language\.',
     'Resource & Budget Management</h4>\n                            <p class="text-white text-sm">Allocating resources, managing budgets, and optimizing project costs.'),
    (r'Problem Solving</h4>\s*<p class="text-white text-sm">Identifying customer needs, complaint handling, and conflict resolution\.',
     'Risk Management</h4>\n                            <p class="text-white text-sm">Identifying, assessing, and mitigating project risks throughout the project lifecycle.'),
    (r'Technology in Customer Service</h4>\s*<p class="text-white text-sm">Using CRM systems, databases, and digital communication tools\.',
     'Stakeholder Management</h4>\n                            <p class="text-white text-sm">Engaging stakeholders, managing expectations, and ensuring effective communication.'),

    # Sidebar - SETA and add NLRD ID
    (r'<span class="text-gray-600">SETA</span>\s*<span class="font-semibold">Services SETA</span>',
     '<span class="text-gray-600">SETA</span>\n                                <span class="font-semibold">ETA</span>'),
    (r'(<div class="flex justify-between items-center py-3 border-b border-gray-100">\s*<span class="text-gray-600">SETA</span>\s*<span class="font-semibold">ETA</span>\s*</div>)',
     r'\1\n                            <div class="flex justify-between items-center py-3 border-b border-gray-100">\n                                <span class="text-gray-600">NLRD ID</span>\n                                <span class="font-semibold">101869</span>\n                            </div>'),
    (r'<span class="text-gray-600">NQF Level</span>\s*<span class="font-semibold">Level 2</span>',
     '<span class="text-gray-600">NQF Level</span>\n                                <span class="font-semibold">Level 5</span>'),
    (r'<span class="text-gray-600">Duration</span>\s*<span class="font-semibold">12 Months</span>',
     '<span class="text-gray-600">Duration</span>\n                                <span class="font-semibold">18 Months</span>'),

    # Related qualifications section
    (r'Explore other Services SETA qualifications', 'Explore other ETA qualifications'),

    # Modal title
    (r'Enquire About Project Manager NQF5', 'Enquire About Occupational Certificate: Project Manager NQF5'),

    # Form qualification field
    (r"qualification: 'Project Manager NQF5'", "qualification: 'Occupational Certificate: Project Manager NQF5 - NLRD ID: 101869'"),

    # Image alt text
    (r'alt="Customer service professional"', 'alt="Project Manager professional"'),
]

# Apply all replacements
for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write the updated content
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Successfully updated services-project-manager-nqf5.html")
print("  - Title: Occupational Certificate: Project Manager")
print("  - SETA: ETA")
print("  - NQF Level: 5")
print("  - Credits: 240")
print("  - Duration: 18 Months")
print("  - NLRD ID: 101869")
