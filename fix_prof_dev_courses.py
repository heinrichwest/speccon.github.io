#!/usr/bin/env python3
"""
Fix Professional Development course pages - Apply SpecCon brand colors
"""

import os
import re
import glob

# List of course files to update
course_files = [
    'short-courses/sales-training.html',
    'short-courses/finance-for-non-financial-managers.html',
    'short-courses/time-management-training.html',
    'short-courses/stress-management-training.html',
    'short-courses/b-bbee-training.html',
    'short-courses/personal-finance-management.html',
    'short-courses/disciplinary-procedures-training.html'
]

print(f"Processing {len(course_files)} professional development course files\n")

for file_path in course_files:
    if not os.path.exists(file_path):
        print(f"[SKIP] File not found: {file_path}\n")
        continue

    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # ===== FIX BODY/BACKGROUND COLORS =====

    # Body background gradients
    content = re.sub(r'bg-gradient-to-br from-blue-50 to-indigo-100', r'bg-gradient-to-br from-[#12265E]/10 to-white', content)
    content = re.sub(r'bg-gradient-to-br from-green-50 to-emerald-100', r'bg-gradient-to-br from-[#12265E]/10 to-white', content)
    content = re.sub(r'bg-gradient-to-br from-orange-50 to-yellow-100', r'bg-gradient-to-br from-[#12265E]/10 to-white', content)
    content = re.sub(r'bg-gradient-to-br from-purple-50 to-pink-100', r'bg-gradient-to-br from-[#12265E]/10 to-white', content)
    content = re.sub(r'bg-gradient-to-br from-red-50 to-pink-100', r'bg-gradient-to-br from-[#12265E]/10 to-white', content)
    content = re.sub(r'bg-gradient-to-br from-teal-50 to-cyan-100', r'bg-gradient-to-br from-[#12265E]/10 to-white', content)
    content = re.sub(r'bg-gradient-to-br from-yellow-50 to-orange-100', r'bg-gradient-to-br from-[#12265E]/10 to-white', content)

    # ===== FIX HEADER BUTTON COLORS =====

    # Book Training buttons with various color gradients
    content = re.sub(r'from-green-500 to-green-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'hover:from-green-600 hover:to-green-700', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]', content)

    content = re.sub(r'from-blue-500 to-blue-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'hover:from-blue-600 hover:to-blue-700', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]', content)

    content = re.sub(r'from-orange-500 to-orange-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'hover:from-orange-600 hover:to-orange-700', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]', content)

    content = re.sub(r'from-purple-500 to-purple-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'hover:from-purple-600 hover:to-purple-700', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]', content)

    content = re.sub(r'from-red-500 to-red-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'hover:from-red-600 hover:to-red-700', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]', content)

    content = re.sub(r'from-teal-500 to-teal-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'hover:from-teal-600 hover:to-teal-700', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]', content)

    content = re.sub(r'from-yellow-500 to-yellow-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'hover:from-yellow-600 hover:to-yellow-700', r'hover:from-[#0d1a47] hover:to-[#3a7bc8]', content)

    # ===== FIX BREADCRUMB COLORS =====

    content = re.sub(r'text-blue-600 hover:text-blue-800', r'text-[#ffa600] hover:text-[#ffa600]', content)
    content = re.sub(r'text-green-600 hover:text-green-800', r'text-[#ffa600] hover:text-[#ffa600]', content)
    content = re.sub(r'text-orange-600 hover:text-orange-800', r'text-[#ffa600] hover:text-[#ffa600]', content)
    content = re.sub(r'text-purple-600 hover:text-purple-800', r'text-[#ffa600] hover:text-[#ffa600]', content)
    content = re.sub(r'text-red-600 hover:text-red-800', r'text-[#ffa600] hover:text-[#ffa600]', content)
    content = re.sub(r'text-teal-600 hover:text-teal-800', r'text-[#ffa600] hover:text-[#ffa600]', content)
    content = re.sub(r'text-yellow-600 hover:text-yellow-800', r'text-[#ffa600] hover:text-[#ffa600]', content)

    # ===== FIX ICON BACKGROUND COLORS =====

    # Icon backgrounds with -100 colors
    content = re.sub(r'bg-green-100', r'bg-[#ffa600]/20', content)
    content = re.sub(r'bg-blue-100', r'bg-[#12265E]/20', content)
    content = re.sub(r'bg-orange-100', r'bg-[#ffa600]/20', content)
    content = re.sub(r'bg-purple-100', r'bg-[#92abc4]/30', content)
    content = re.sub(r'bg-red-100', r'bg-[#ffa600]/20', content)
    content = re.sub(r'bg-teal-100', r'bg-[#92abc4]/30', content)
    content = re.sub(r'bg-yellow-100', r'bg-[#ffa600]/20', content)
    content = re.sub(r'bg-pink-100', r'bg-[#ffa600]/20', content)
    content = re.sub(r'bg-indigo-100', r'bg-[#12265E]/20', content)
    content = re.sub(r'bg-emerald-100', r'bg-[#92abc4]/30', content)

    # ===== FIX TEXT COLORS =====

    # Primary text colors
    content = re.sub(r'text-green-600', r'text-[#ffa600]', content)
    content = re.sub(r'text-blue-600', r'text-[#12265E]', content)
    content = re.sub(r'text-orange-600', r'text-[#ffa600]', content)
    content = re.sub(r'text-purple-600', r'text-[#92abc4]', content)
    content = re.sub(r'text-red-600', r'text-[#ffa600]', content)
    content = re.sub(r'text-teal-600', r'text-[#92abc4]', content)
    content = re.sub(r'text-yellow-600', r'text-[#ffa600]', content)
    content = re.sub(r'text-pink-600', r'text-[#ffa600]', content)
    content = re.sub(r'text-indigo-600', r'text-[#12265E]', content)
    content = re.sub(r'text-emerald-600', r'text-[#92abc4]', content)

    # Lighter variations
    content = re.sub(r'text-green-500', r'text-[#ffa600]', content)
    content = re.sub(r'text-blue-500', r'text-[#12265E]', content)
    content = re.sub(r'text-orange-500', r'text-[#ffa600]', content)
    content = re.sub(r'text-purple-500', r'text-[#92abc4]', content)

    # ===== FIX SECTION BACKGROUNDS =====

    # Section backgrounds with gradients
    content = re.sub(r'from-green-50 to-emerald-50', r'from-[#12265E]/5 to-[#92abc4]/10', content)
    content = re.sub(r'from-blue-50 to-indigo-50', r'from-[#12265E]/5 to-[#92abc4]/10', content)
    content = re.sub(r'from-orange-50 to-yellow-50', r'from-[#12265E]/5 to-[#92abc4]/10', content)
    content = re.sub(r'from-purple-50 to-pink-50', r'from-[#12265E]/5 to-[#92abc4]/10', content)
    content = re.sub(r'from-red-50 to-pink-50', r'from-[#12265E]/5 to-[#92abc4]/10', content)
    content = re.sub(r'from-teal-50 to-cyan-50', r'from-[#12265E]/5 to-[#92abc4]/10', content)

    # ===== FIX CTA SECTION =====

    # CTA section gradients
    content = re.sub(r'from-green-600 to-emerald-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'from-blue-600 to-indigo-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'from-orange-600 to-yellow-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'from-purple-600 to-pink-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'from-red-600 to-pink-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'from-teal-600 to-cyan-600', r'from-[#12265E] to-[#92abc4]', content)
    content = re.sub(r'from-yellow-600 to-orange-600', r'from-[#12265E] to-[#92abc4]', content)

    # CTA button text colors
    content = re.sub(r'text-green-600 font-bold', r'text-[#ffa600] font-bold', content)
    content = re.sub(r'text-blue-600 font-bold', r'text-[#ffa600] font-bold', content)
    content = re.sub(r'text-orange-600 font-bold', r'text-[#ffa600] font-bold', content)
    content = re.sub(r'text-purple-600 font-bold', r'text-[#ffa600] font-bold', content)

    # Hover states for CTA buttons
    content = re.sub(r'hover:text-green-600', r'hover:text-[#ffa600]', content)
    content = re.sub(r'hover:text-blue-600', r'hover:text-[#ffa600]', content)
    content = re.sub(r'hover:text-orange-600', r'hover:text-[#ffa600]', content)
    content = re.sub(r'hover:text-purple-600', r'hover:text-[#ffa600]', content)

    # ===== FIX FORM FOCUS RINGS =====

    content = re.sub(r'focus:ring-green-500', r'focus:ring-[#12265E]', content)
    content = re.sub(r'focus:ring-blue-500', r'focus:ring-[#12265E]', content)
    content = re.sub(r'focus:ring-orange-500', r'focus:ring-[#12265E]', content)
    content = re.sub(r'focus:ring-purple-500', r'focus:ring-[#12265E]', content)
    content = re.sub(r'focus:ring-red-500', r'focus:ring-[#12265E]', content)
    content = re.sub(r'focus:ring-teal-500', r'focus:ring-[#12265E]', content)

    # ===== FIX BORDER COLORS =====

    content = re.sub(r'border-green-200', r'border-[#ffa600]/30', content)
    content = re.sub(r'border-blue-200', r'border-[#12265E]/30', content)
    content = re.sub(r'border-orange-200', r'border-[#ffa600]/30', content)
    content = re.sub(r'border-purple-200', r'border-[#92abc4]/30', content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {file_path}\n")
    else:
        print(f"[-] No changes needed for {file_path}\n")

print("\n[OK] All professional development course pages processed!")
print("Summary:")
print("- Updated body backgrounds to #12265E/10 gradient")
print("- Changed all buttons to #12265E/#92abc4 gradient")
print("- Updated breadcrumbs to #ffa600")
print("- Applied brand colors to all icons and text")
print("- Fixed CTA sections to use brand colors")
print("- Updated form focus rings to #12265E")
