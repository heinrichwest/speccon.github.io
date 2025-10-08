#!/usr/bin/env python3
"""
Update etdp-education-training-nqf5.html to match services-bookkeeper format
"""

import os

def create_updated_page():
    """Create the updated page content"""

    updated_content = '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Education Training & Development Practices NQF Level 5 | ETDP SETA | SpecCon Holdings</title>
    <meta name="description" content="Occupationally Directed Education Training and Development Practices NQF Level 5 qualification accredited by ETDP SETA. 120 credits, comprehensive training.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>

    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .card-hover:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 10px 10px -5px rgb(0 0 0 / 0.04);
        }
        .dropdown:hover .dropdown-menu {
            display: block;
        }
        .dropdown-menu {
            display: none;
        }
        .dropdown {
            padding-bottom: 8px;
            display: flex;
            align-items: center;
        }
        .dropdown button {
            display: flex;
            align-items: center;
        }
        .dropdown-menu {
            top: 100%;
            margin-top: 0;
            padding-top: 8px;
        }
        /* Sticky Banner Styles */
        .sticky-banner {
            position: fixed;
            top: 100px;
            right: 20px;
            background: linear-gradient(135deg, #12265E 0%, #4A90E2 100%);
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
            background: linear-gradient(135deg, #0d1a47 0%, #3a7bc8 100%);
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
        }

        /* Enquiry Popup Modal Styles */
        .enquiry-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 2000;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
        }
        .enquiry-modal.show {
            opacity: 1;
            visibility: visible;
        }
        .enquiry-modal-content {
            background: white;
            border-radius: 20px;
            max-width: 500px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
            transform: translateY(20px);
            transition: transform 0.3s ease;
        }
        .enquiry-modal.show .enquiry-modal-content {
            transform: translateY(0);
        }
    </style>
</head>

<body class="bg-white text-gray-900">
    <!-- Header -->
    <header class="bg-white/95 backdrop-blur-md shadow-lg fixed w-full z-50 top-0">
        <div class="container mx-auto px-4 lg:px-6 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center">
                    <a href="../index.html">
                        <img src="../images/Logo.png" alt="SpecCon Holdings Logo" class="h-12">
                    </a>
                    <div class="ml-3">
                        <h1 class="text-xl font-bold text-gray-900">SpecCon Holdings</h1>
                        <p class="text-sm text-gray-600">ETDP SETA Qualifications</p>
                    </div>
                </div>

                <nav class="hidden lg:flex items-center space-x-8">
                    <a href="../index.html#about" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">Why Choose Us</a>
                    <a href="../index.html#qualifications" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">Qualifications</a>
                    <a href="../index.html#accreditations" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">Accreditations</a>
                    <a href="../index.html#classroom-training" class="text-gray-700 hover:text-blue-600 font-medium transition duration-300">Classroom Training</a>
                    <div class="relative dropdown">
                        <button class="text-gray-700 hover:text-blue-600 font-medium transition duration-300 inline-flex items-center">
                            Other Products <i data-lucide="chevron-down" class="w-4 h-4 ml-1"></i>
                        </button>
                        <div class="dropdown-menu absolute left-0 w-64 bg-white rounded-lg shadow-xl py-2 z-20 border">
                            <a href="https://elearning.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="monitor" class="w-4 h-4 inline mr-2"></i>Online Training
                            </a>
                            <a href="https://employmentequityact.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="shield-check" class="w-4 h-4 inline mr-2"></i>Employment Equity
                            </a>
                            <a href="https://learningmanagementsystem.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="graduation-cap" class="w-4 h-4 inline mr-2"></i>Learning Management System
                            </a>
                            <a href="https://skillsdevelopment.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="trending-up" class="w-4 h-4 inline mr-2"></i>Skills Development
                            </a>
                            <a href="https://www.specconacademy.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="school" class="w-4 h-4 inline mr-2"></i>SpecCon Academy
                            </a>
                            <a href="https://bbbee.co.za/" target="_blank" class="block px-4 py-3 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition duration-200">
                                <i data-lucide="award" class="w-4 h-4 inline mr-2"></i>BBBEE Consulting
                            </a>
                        </div>
                    </div>
                </nav>

                <div class="hidden lg:block">
                    <button onclick="openEnquiryModal()" class="bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-6 py-3 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg">
                        Enquire Now
                    </button>
                </div>

                <button id="mobile-menu-button" class="lg:hidden">
                    <i data-lucide="menu" class="w-6 h-6"></i>
                </button>
            </div>

            <!-- Mobile Menu -->
            <div id="mobile-menu" class="hidden lg:hidden mt-4">
                <a href="../index.html#about" class="block py-2 text-gray-600 hover:text-blue-600">About Us</a>
                <a href="../index.html#qualifications" class="block py-2 text-gray-600 hover:text-blue-600">Qualifications</a>
                <a href="../index.html#accreditations" class="block py-2 text-gray-600 hover:text-blue-600">Accreditations</a>
                <a href="../index.html#classroom-training" class="block py-2 text-gray-600 hover:text-blue-600">Classroom Training</a>
                <button onclick="openEnquiryModal()" class="mt-2 w-full bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold px-5 py-2 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300 shadow-lg text-center block">
                    Enquire Now
                </button>
            </div>
        </div>
    </header>

    <!-- Breadcrumb -->
    <section class="pt-24 pb-8 bg-gray-50">
        <div class="container mx-auto px-6">
            <nav class="text-sm text-gray-600">
                <a href="../index.html" class="hover:text-blue-600">Home</a>
                <span class="mx-2">/</span>
                <a href="../setas/etdp-seta.html" class="hover:text-blue-600">ETDP SETA</a>
                <span class="mx-2">/</span>
                <span class="text-gray-900">Education Training & Development Practices NQF Level 5</span>
            </nav>
        </div>
    </section>

    <!-- Hero Section -->
    <section class="py-16 bg-gradient-to-br from-purple-50 to-white">
        <div class="container mx-auto px-6">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <div>
                    <div class="flex items-center mb-6">
                        <div class="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mr-6">
                            <i data-lucide="book-open" class="w-8 h-8 text-purple-600"></i>
                        </div>
                        <div>
                            <span class="text-purple-600 font-semibold">NQF Level 5 | ETDP SETA</span>
                            <h1 class="text-4xl md:text-5xl font-bold text-gray-900">Education Training & Development Practices</h1>
                        </div>
                    </div>
                    <p class="text-lg text-gray-600 leading-relaxed mb-8">
                        Build on your FETC to enter the field of Occupationally Directed Education Training and Development.
                        This qualification prepares learning facilitators, assessors, learner supporters, and skills development facilitators.
                    </p>
                    <div class="grid grid-cols-3 gap-4 mb-8">
                        <div class="text-center p-4 bg-white rounded-lg shadow">
                            <div class="text-xl font-bold text-purple-600">120</div>
                            <div class="text-sm text-gray-600">Credits</div>
                        </div>
                        <div class="text-center p-4 bg-white rounded-lg shadow">
                            <div class="text-xl font-bold text-indigo-600">18</div>
                            <div class="text-sm text-gray-600">Months</div>
                        </div>
                        <div class="text-center p-4 bg-white rounded-lg shadow">
                            <div class="text-xl font-bold text-blue-600">NQF 5</div>
                            <div class="text-sm text-gray-600">Level</div>
                        </div>
                    </div>
                </div>
                <div>
                    <img src="https://images.pexels.com/photos/3184328/pexels-photo-3184328.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
                         alt="Education training and development professionals"
                         class="rounded-2xl shadow-2xl">
                </div>
            </div>
        </div>
    </section>

    <!-- Qualification Details -->
    <section class="py-20">
        <div class="container mx-auto px-6">
            <div class="grid lg:grid-cols-3 gap-12">
                <!-- Main Content -->
                <div class="lg:col-span-2">
                    <h2 class="text-3xl font-bold text-gray-900 mb-8">Qualification Overview</h2>

                    <div class="prose max-w-none mb-12">
                        <p class="text-gray-600 text-lg leading-relaxed mb-6">
                            This qualification is designed for those who want to build on a FETC in any field to enter the field of
                            Occupationally Directed Education Training and Development (ODETD) as a potential career with little previous
                            ETD exposure. It prepares learning facilitators, assessors, learner and learning supporters, and skills
                            development facilitators.
                        </p>

                        <h3 class="text-2xl font-bold text-gray-900 mb-4">Learning Outcomes</h3>
                        <p class="text-gray-600 mb-6">Upon completion of this qualification, learners will be able to:</p>
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-green-500 mr-3 mt-1 flex-shrink-0"></i>
                                <span>Communicate effectively in education, training and development environments</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-green-500 mr-3 mt-1 flex-shrink-0"></i>
                                <span>Design and develop comprehensive learning programmes for various contexts</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-green-500 mr-3 mt-1 flex-shrink-0"></i>
                                <span>Facilitate learning processes and evaluate their effectiveness</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-green-500 mr-3 mt-1 flex-shrink-0"></i>
                                <span>Engage in and promote effective assessment practices</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-green-500 mr-3 mt-1 flex-shrink-0"></i>
                                <span>Provide learning support to learners and organizations</span>
                            </li>
                            <li class="flex items-start">
                                <i data-lucide="check-circle" class="w-6 h-6 text-green-500 mr-3 mt-1 flex-shrink-0"></i>
                                <span>Conduct skills development facilitation activities</span>
                            </li>
                        </ul>

                        <h3 class="text-2xl font-bold text-gray-900 mb-4">Career Opportunities</h3>
                        <p class="text-gray-600 mb-6">This qualification opens doors to various career opportunities including:</p>
                        <div class="grid md:grid-cols-2 gap-4 mb-8">
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-blue-600 mr-3"></i>
                                <span>Learning Facilitator</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-blue-600 mr-3"></i>
                                <span>Assessor</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-blue-600 mr-3"></i>
                                <span>Learner Support Practitioner</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-blue-600 mr-3"></i>
                                <span>Skills Development Facilitator</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-blue-600 mr-3"></i>
                                <span>Training Coordinator</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-blue-600 mr-3"></i>
                                <span>Learning Programme Developer</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-blue-600 mr-3"></i>
                                <span>Workplace Skills Assessor</span>
                            </div>
                            <div class="flex items-center">
                                <i data-lucide="briefcase" class="w-5 h-5 text-blue-600 mr-3"></i>
                                <span>Adult Education Practitioner</span>
                            </div>
                        </div>
                    </div>

                    <!-- Modules -->
                    <h3 class="text-2xl font-bold text-gray-900 mb-6">Core Modules</h3>
                    <div class="space-y-6 mb-12">
                        <div class="bg-gradient-to-r from-purple-50 to-pink-50 p-6 rounded-xl">
                            <h4 class="font-bold text-lg text-gray-900 mb-3">Fundamental Component (10 credits)</h4>
                            <ul class="space-y-2 text-sm text-gray-600">
                                <li>• Communications skills essential for education and training contexts</li>
                                <li>• Professional communication in ETD settings</li>
                                <li>• Written and verbal communication excellence</li>
                            </ul>
                        </div>

                        <div class="bg-gradient-to-r from-blue-50 to-indigo-50 p-6 rounded-xl">
                            <h4 class="font-bold text-lg text-gray-900 mb-3">Core Component (61 credits)</h4>
                            <ul class="space-y-2 text-sm text-gray-600">
                                <li>• Essential competencies in education, training and development practices</li>
                                <li>• Learning programme design and development</li>
                                <li>• Facilitation and assessment methodologies</li>
                                <li>• Learning support and skills development</li>
                            </ul>
                        </div>

                        <div class="bg-gradient-to-r from-green-50 to-emerald-50 p-6 rounded-xl">
                            <h4 class="font-bold text-lg text-gray-900 mb-3">Elective Component (49 credits)</h4>
                            <ul class="space-y-2 text-sm text-gray-600">
                                <li>• Choose from 116 available elective credits</li>
                                <li>• Specialize in specific areas of ETD practice</li>
                                <li>• Customized learning pathways</li>
                                <li>• Industry-specific specializations</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Sidebar -->
                <div class="lg:col-span-1">
                    <div class="bg-white border border-gray-200 rounded-2xl shadow-lg p-8 sticky top-24">
                        <h3 class="text-xl font-bold text-gray-900 mb-6">Qualification Details</h3>

                        <div class="space-y-4 mb-8">
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-600">SETA</span>
                                <span class="font-semibold">ETDP SETA</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-600">NQF Level</span>
                                <span class="font-semibold">Level 5</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-600">Credits</span>
                                <span class="font-semibold">120 Credits</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-600">Duration</span>
                                <span class="font-semibold">18 Months</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-600">Delivery Mode</span>
                                <span class="font-semibold">Blended Learning</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-600">Assessment</span>
                                <span class="font-semibold">Competency Based</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-600">NLRD ID</span>
                                <span class="font-semibold">50334</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-600">Status</span>
                                <span class="font-semibold">Accredited</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-600">Provider</span>
                                <span class="font-semibold">SpecCon</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Enquiry Modal -->
    <div id="enquiryModal" class="enquiry-modal">
        <div class="enquiry-modal-content">
            <div class="p-8">
                <div class="flex items-center justify-between mb-6">
                    <h2 class="text-2xl font-bold text-gray-900">Enquire About Education Training & Development Practices NQF5</h2>
                    <button onclick="closeEnquiryModal()" class="text-gray-400 hover:text-gray-600 text-xl">
                        <i data-lucide="x" class="w-6 h-6"></i>
                    </button>
                </div>

                <div class="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <p class="text-blue-700 text-sm">
                        <i data-lucide="info" class="w-4 h-4 inline mr-2"></i>
                        If you are applying for a learnership, please <a href="../learnership-application.html" class="font-semibold underline hover:text-blue-800">click here</a>.
                    </p>
                </div>

                <form id="enquiryForm" onsubmit="submitEnquiry(event)">
                    <div class="grid md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <label for="firstName" class="block text-sm font-medium text-gray-700 mb-2">Name *</label>
                            <input type="text" id="firstName" name="firstName" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                        <div>
                            <label for="surname" class="block text-sm font-medium text-gray-700 mb-2">Surname *</label>
                            <input type="text" id="surname" name="surname" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                    </div>

                    <div class="grid md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <label for="email" class="block text-sm font-medium text-gray-700 mb-2">Email *</label>
                            <input type="email" id="email" name="email" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                        <div>
                            <label for="phone" class="block text-sm font-medium text-gray-700 mb-2">Phone Number *</label>
                            <input type="tel" id="phone" name="phone" required
                                   class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>
                    </div>

                    <div class="mb-4">
                        <label for="company" class="block text-sm font-medium text-gray-700 mb-2">Company *</label>
                        <input type="text" id="company" name="company" required
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                    </div>

                    <div class="mb-6">
                        <label for="reason" class="block text-sm font-medium text-gray-700 mb-2">Reason for Enquiry *</label>
                        <textarea id="reason" name="reason" rows="4" required
                                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                                  placeholder="Please tell us about your enquiry and how we can help you..."></textarea>
                    </div>

                    <div class="flex flex-col sm:flex-row gap-3">
                        <button type="submit" class="flex-1 bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white font-semibold py-3 px-6 rounded-lg hover:from-[#0d1a47] hover:to-[#3a7bc8] transition duration-300">
                            <i data-lucide="send" class="w-4 h-4 inline mr-2"></i>
                            Send Enquiry
                        </button>
                        <button type="button" onclick="closeEnquiryModal()" class="flex-1 bg-gray-500 text-white font-semibold py-3 px-6 rounded-lg hover:bg-gray-600 transition duration-300">
                            Cancel
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-gradient-to-r from-[#12265E] to-[#4A90E2] text-white py-12">
        <div class="container mx-auto px-6">
            <div class="grid md:grid-cols-4 gap-8">
                <div class="md:col-span-2">
                    <div class="flex items-center mb-4">
                        <img src="../images/SpecCon-LOGO.png" alt="SpecCon Holdings Logo" class="h-12 mr-3">
                        <div>
                            <h3 class="text-xl font-bold">SpecCon Holdings</h3>
                            <p class="text-white/80">Education Training & Development Practices</p>
                        </div>
                    </div>
                    <p class="text-white/80 mb-4">Building education and training professionals through comprehensive development programs.</p>
                </div>

                <div>
                    <h4 class="text-lg font-semibold mb-4">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="../index.html" class="text-white/80 hover:text-[#ff9c2a] transition duration-200">Home</a></li>
                        <li><a href="../setas/etdp-seta.html" class="text-white/80 hover:text-[#ff9c2a] transition duration-200">ETDP SETA</a></li>
                        <li><a href="../index.html#qualifications" class="text-white/80 hover:text-[#ff9c2a] transition duration-200">All Qualifications</a></li>
                        <li><a href="../index.html#contact" class="text-white/80 hover:text-[#ff9c2a] transition duration-200">Contact</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-semibold mb-4">Get Started</h4>
                    <ul class="space-y-2">
                        <li><a href="../index.html#contact" class="text-white/80 hover:text-[#ff9c2a] transition duration-200">Get Information</a></li>
                        <li><a href="mailto:help@speccon.co.za" class="text-white/80 hover:text-[#ff9c2a] transition duration-200">Email Us</a></li>
                    </ul>
                </div>
            </div>

            <div class="border-t border-gray-800 mt-8 pt-8 text-center">
                <p class="text-white/80">&copy; 2025 SpecCon Holdings. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        // Enquiry Modal Functions
        function openEnquiryModal() {
            const modal = document.getElementById('enquiryModal');
            if (modal) {
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
            }
        }

        function closeEnquiryModal() {
            const modal = document.getElementById('enquiryModal');
            if (modal) {
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
            }
        }

        function submitEnquiry(event) {
            event.preventDefault();

            const formData = new FormData(event.target);
            const enquiryData = {
                firstName: formData.get('firstName'),
                surname: formData.get('surname'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                company: formData.get('company'),
                reason: formData.get('reason'),
                qualification: 'Education Training & Development Practices NQF Level 5'
            };

            alert('Thank you for your enquiry! We will get back to you soon.');
            closeEnquiryModal();
            event.target.reset();

            console.log('Enquiry submitted:', enquiryData);
        }

        // Initialize when DOM is ready
        document.addEventListener('DOMContentLoaded', function() {
            lucide.createIcons();

            // Mobile menu toggle
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');

            if (mobileMenuButton && mobileMenu) {
                mobileMenuButton.addEventListener('click', () => {
                    mobileMenu.classList.toggle('hidden');
                });
            }

            // Close modal when clicking outside
            const enquiryModal = document.getElementById('enquiryModal');
            if (enquiryModal) {
                enquiryModal.addEventListener('click', function(e) {
                    if (e.target === this) {
                        closeEnquiryModal();
                    }
                });
            }

            // Close modal with Escape key
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    closeEnquiryModal();
                }
            });
        });
    </script>
</body>
</html>'''

    return updated_content

def main():
    filepath = 'qualifications/etdp-education-training-nqf5.html'

    try:
        # Create the updated content
        updated_content = create_updated_page()

        # Write the updated content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"[SUCCESS] Updated {filepath}")
        print("The page now has:")
        print("  - Header matching services-bookkeeper format")
        print("  - SpecCon Holdings logo and title")
        print("  - ETDP SETA Qualifications subtitle")
        print("  - Enquire Now button with modal popup")
        print("  - Learnership application link in modal")
        print("  - Complete navigation menu with dropdown")
        print("  - Mobile menu support")

    except Exception as e:
        print(f"[ERROR] Failed to update {filepath}: {str(e)}")

if __name__ == "__main__":
    main()