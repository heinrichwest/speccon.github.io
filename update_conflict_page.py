#!/usr/bin/env python3
"""
Update Conflict Management page with correct content
"""

import re

# Read the template file
with open('qualifications/skills-conflict-management-nqf5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update title and meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Conflict Management NQF Level 5 | Skills Programme | SpecCon Holdings</title>',
    content
)

content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Master conflict management with our NQF Level 5 skills programme. 8 credits, 10 days, QCTO recognized training for workplace conflict resolution.">',
    content
)

# Update breadcrumb
content = content.replace(
    '<span class="text-[#12265E] font-semibold">New Venture Creation NQF Level 2</span>',
    '<span class="text-[#12265E] font-semibold">Conflict Management NQF Level 5</span>'
)

# Update hero section
content = content.replace(
    '<i data-lucide="rocket" class="w-8 h-8 text-[#ffa600]"></i>',
    '<i data-lucide="shield-check" class="w-8 h-8 text-[#ffa600]"></i>'
)

content = content.replace(
    '<span class="text-[#ffa600] font-semibold">NQF Level 2 | QCTO Skills Programme</span>',
    '<span class="text-[#ffa600] font-semibold">NQF Level 5 | QCTO Skills Programme</span>'
)

content = content.replace(
    '<h1 class="text-4xl md:text-5xl font-bold text-[#12265E]">New Venture Creation</h1>',
    '<h1 class="text-4xl md:text-5xl font-bold text-[#12265E]">Conflict Management</h1>'
)

# Update hero description
content = re.sub(
    r'Unlock your entrepreneurial potential.*?mainstream economy\.',
    'Elevate your team\'s productivity and harmony with our Conflict Management skills programme. Manage conflicts effectively and keep teams focused on real results with proven workplace techniques.',
    content
)

# Update stats boxes
content = re.sub(
    r'<div class="text-xl font-bold text-\[#ffa600\]">32</div>',
    '<div class="text-xl font-bold text-[#ffa600]">8</div>',
    content,
    count=1
)

content = re.sub(
    r'<div class="text-xl font-bold text-white">15</div>',
    '<div class="text-xl font-bold text-white">10</div>',
    content,
    count=1
)

content = re.sub(
    r'<div class="text-xl font-bold text-\[#ffa600\]">NQF 2</div>',
    '<div class="text-xl font-bold text-[#ffa600]">NQF 5</div>',
    content,
    count=1
)

# Update hero image
content = content.replace(
    'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    'https://images.pexels.com/photos/7640432/pexels-photo-7640432.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
)

content = content.replace(
    'alt="Entrepreneur planning business venture"',
    'alt="Team conflict resolution meeting"'
)

# Update programme overview
content = re.sub(
    r'This skills program equips you.*?expert guidance\.',
    'This skills programme is designed to help individuals manage conflicts and keep teams focused on real results. Equip yourself with the tools to tackle workplace challenges head-on and foster a peaceful, harmonious environment.',
    content
)

# Update programme purpose section
purpose_text = '''<h3 class="text-2xl font-bold text-[#12265E] mb-4">Programme Purpose</h3>
                        <p class="text-gray-600 mb-6">Upon completion, you will be able to:</p>
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Identify and describe the main sources of conflict</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Differentiate between various types of conflict</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Employ effective strategies for conflict management</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Resolve conflicts using proven workplace techniques</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Formulate and execute comprehensive follow-up plans</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Prepare detailed conflict resolution reports</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Apply emotional intelligence in conflict resolution engagement</span>
                            </li>
                        </ul>'''

content = re.sub(
    r'<h3 class="text-2xl font-bold text-\[#12265E\] mb-4">Programme Purpose</h3>.*?</ul>',
    purpose_text,
    content,
    flags=re.DOTALL
)

# Update "Who Should Attend" section
who_should_attend = '''<h3 class="text-2xl font-bold text-[#12265E] mb-4">Who Should Attend?</h3>
                        <p class="text-gray-600 mb-6">This programme is ideal for:</p>
                        <ul class="space-y-2 mb-8 text-gray-600">
                            <li class="flex items-start">
                                <i data-lucide="users" class="w-5 h-5 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Managers seeking to improve conflict resolution capabilities</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="users" class="w-5 h-5 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Supervisors and Team Leaders managing workplace dynamics</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="users" class="w-5 h-5 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Human Resources (HR) Personnel handling employee relations</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="users" class="w-5 h-5 text-[#ffa600] mr-3 mt-1 flex-shrink-0"></i>
                                <span>Project Managers coordinating diverse teams</span>
                            </li>
                        </ul>

                        <h3 class="text-2xl font-bold text-[#12265E] mb-4">Career Possibilities</h3>
                        <div class="grid md:grid-cols-2 gap-4 mb-8">
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-[#ffa600] mr-3"></i>
                                <span>HR Manager</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-[#ffa600] mr-3"></i>
                                <span>Conflict Resolution Specialist</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-[#ffa600] mr-3"></i>
                                <span>Employee Relations Advisor</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-[#ffa600] mr-3"></i>
                                <span>Mediator</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-[#ffa600] mr-3"></i>
                                <span>Arbitrator</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-[#ffa600] mr-3"></i>
                                <span>Conciliator</span>
                            </div>
                        </div>'''

content = re.sub(
    r'<h3 class="text-2xl font-bold text-\[#12265E\] mb-4">Who Should Attend\?</h3>.*?</ul>',
    who_should_attend,
    content,
    flags=re.DOTALL
)

# Update Knowledge Component modules
modules = '''<h3 class="text-2xl font-bold text-[#12265E] mb-6">Knowledge Component</h3>
                    <div class="space-y-6 mb-12">
                        <div class="bg-[#12265E] p-6 rounded-xl">
                            <h4 class="font-bold text-lg text-white mb-3">Conflict Fundamentals</h4>
                            <ul class="list-none space-y-2 text-sm text-white">
                                <li class="flex items-start"><span class="mr-2">•</span><span>Topic 1: Sources of conflict</span></li>
                                <li class="flex items-start"><span class="mr-2">•</span><span>Topic 2: Types of conflicts</span></li>
                            </ul>
                        </div>

                        <div class="bg-[#92abc4] p-6 rounded-xl">
                            <h4 class="font-bold text-lg text-[#12265E] mb-3">Management Strategies</h4>
                            <ul class="list-none space-y-2 text-sm text-white">
                                <li class="flex items-start"><span class="mr-2">•</span><span>Topic 3: Strategies for conflict management</span></li>
                                <li class="flex items-start"><span class="mr-2">•</span><span>Topic 4: Techniques in conflict management</span></li>
                            </ul>
                        </div>

                        <div class="bg-[#12265E] p-6 rounded-xl">
                            <h4 class="font-bold text-lg text-white mb-3">Analysis & Resolution</h4>
                            <ul class="list-none space-y-2 text-sm text-white">
                                <li class="flex items-start"><span class="mr-2">•</span><span>Topic 5: Conflict consequences analysis</span></li>
                                <li class="flex items-start"><span class="mr-2">•</span><span>Topic 6: Emotional intelligence in conflict resolution</span></li>
                                <li class="flex items-start"><span class="mr-2">•</span><span>Topic 7: Components of Conflict Resolution Report</span></li>
                            </ul>
                        </div>
                    </div>'''

content = re.sub(
    r'<h3 class="text-2xl font-bold text-\[#12265E\] mb-6">Knowledge Component</h3>.*?</div>\s*</div>\s*</div>',
    modules + '\n                    </div>',
    content,
    flags=re.DOTALL
)

# Update Application Component
application = '''<h3 class="text-2xl font-bold text-[#12265E] mb-6">Application Component</h3>
                    <div class="bg-gradient-to-r from-[#12265E] to-[#92abc4] p-6 rounded-xl mb-12">
                        <ul class="list-none space-y-2 text-sm text-white">
                            <li class="flex items-start"><span class="mr-2">•</span><span>Topic 1: Apply teamwork in conflict resolution process</span></li>
                            <li class="flex items-start"><span class="mr-2">•</span><span>Topic 2: Profile a conflict at a workplace</span></li>
                            <li class="flex items-start"><span class="mr-2">•</span><span>Topic 3: Analyse a conflict profile and determine the causes of conflict</span></li>
                            <li class="flex items-start"><span class="mr-2">•</span><span>Topic 4: Determine and implement appropriate conflict management strategies</span></li>
                            <li class="flex items-start"><span class="mr-2">•</span><span>Topic 5: Select and apply conflict resolution techniques</span></li>
                            <li class="flex items-start"><span class="mr-2">•</span><span>Topic 6: Analyse and profile conflict consequences</span></li>
                            <li class="flex items-start"><span class="mr-2">•</span><span>Topic 7: Apply emotional intelligence in conflict resolution engagement</span></li>
                            <li class="flex items-start"><span class="mr-2">•</span><span>Topic 8: Compile and implement conflict resolution follow up plan</span></li>
                            <li class="flex items-start"><span class="mr-2">•</span><span>Topic 9: Compile conflict resolution report</span></li>
                        </ul>
                    </div>'''

content = re.sub(
    r'<h3 class="text-2xl font-bold text-\[#12265E\] mb-6">Application Component</h3>.*?</div>\s*</div>',
    application + '\n                    </div>',
    content,
    flags=re.DOTALL
)

# Update Assessment section
assessment = '''<h3 class="text-2xl font-bold text-[#12265E] mb-4">Assessment</h3>
                    <div class="space-y-4 mb-8">
                        <div class="bg-gray-50 p-6 rounded-lg">
                            <h4 class="font-bold text-[#12265E] mb-2">Written Test</h4>
                            <p class="text-gray-600 text-sm">Comprehensive written examination covering all knowledge components of conflict management.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-lg">
                            <h4 class="font-bold text-[#12265E] mb-2">Portfolio of Evidence</h4>
                            <p class="text-gray-600 text-sm">Compilation of practical work demonstrating application of conflict resolution techniques in workplace scenarios.</p>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-lg">
                            <h4 class="font-bold text-[#12265E] mb-2">Continuous Practical Evaluation</h4>
                            <p class="text-gray-600 text-sm">Practical components are evaluated continuously throughout the programme duration.</p>
                        </div>
                        <div class="bg-[#FFA600]/10 p-6 rounded-lg border-l-4 border-[#FFA600]">
                            <h4 class="font-bold text-[#12265E] mb-2">Final Integrated Summative Assessment (FISA)</h4>
                            <p class="text-gray-600 text-sm">All learners gain entrance to the Final Integrated Supervised Assessment by successfully completing all formal summative assessments conducted by the SDP.</p>
                        </div>
                    </div>'''

content = re.sub(
    r'<h3 class="text-2xl font-bold text-\[#12265E\] mb-4">Assessment</h3>.*?</div>\s*</div>',
    assessment + '\n                </div>',
    content,
    flags=re.DOTALL
)

# Update sidebar details
content = re.sub(r'<span class="font-semibold">Level 2</span>', '<span class="font-semibold">Level 5</span>', content)
content = re.sub(r'<span class="font-semibold">32 Credits</span>', '<span class="font-semibold">8 Credits</span>', content)
content = re.sub(r'<span class="font-semibold">15 Days</span>', '<span class="font-semibold">10 Days</span>', content)
content = re.sub(r'<span class="font-semibold">SP-210401</span>', '<span class="font-semibold">SP-210502</span>', content)
content = re.sub(r'<span class="font-semibold">Grade 9 / Level 1</span>', '<span class="font-semibold">Matric / NQF 4</span>', content)

# Update modal title
content = re.sub(
    r'<h2 class="text-2xl font-bold text-gray-900">Enquire About New Venture Creation</h2>',
    '<h2 class="text-2xl font-bold text-gray-900">Enquire About Conflict Management</h2>',
    content
)

# Update form submission
content = re.sub(
    r"Course: 'New Venture Creation NQF 2'",
    "Course: 'Conflict Management NQF 5'",
    content
)
content = re.sub(
    r"Source: 'skills-new-venture-creation-nqf2'",
    "Source: 'skills-conflict-management-nqf5'",
    content
)

# Update related programmes - swap new venture and conflict management
content = content.replace(
    '<a href="skills-conflict-management-nqf5.html"',
    '<a href="skills-new-venture-creation-nqf2.html"'
)
content = re.sub(
    r'<h3 class="font-bold text-lg text-\[#12265E\]">Conflict Management</h3>',
    '<h3 class="font-bold text-lg text-[#12265E]">New Venture Creation</h3>',
    content,
    count=1  # Only replace the first occurrence in related programmes
)
content = re.sub(
    r'<span class="text-sm text-\[#ffa600\] font-medium group-hover:text-\[#92abc4\] transition duration-300">NQF Level 5</span>',
    '<span class="text-sm text-[#ffa600] font-medium group-hover:text-[#92abc4] transition duration-300">NQF Level 2</span>',
    content,
    count=1  # Only in related section
)
content = re.sub(
    r'<p class="text-gray-600 text-sm">Manage workplace conflicts effectively and maintain team productivity\.</p>',
    '<p class="text-gray-600 text-sm">Start and grow sustainable small businesses with entrepreneurial skills.</p>',
    content
)

# Fix the icon in related programmes
content = re.sub(
    r'<div class="w-12 h-12 bg-\[#92abc4\] rounded-lg flex items-center justify-center mr-4">\s*<i data-lucide="shield-check" class="w-6 h-6 text-white"></i>',
    '<div class="w-12 h-12 bg-[#12265E] rounded-lg flex items-center justify-center mr-4">\n                            <i data-lucide="rocket" class="w-6 h-6 text-[#ffa600]"></i>',
    content,
    count=1
)

# Write the updated content
with open('qualifications/skills-conflict-management-nqf5.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('[OK] Updated Conflict Management NQF 5 page')
