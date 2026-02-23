# utils/pest_library.py
"""
Pest Library Data for the 6 existing pests with images
Contains details in English, Hindi, and Bengali languages
"""

# Image to pest name mapping
IMAGE_TO_PEST_MAPPING = {
    'aphids.jpg': 'Aphids',
    'armyworm.jpg': 'Armyworm',
    'leafhopper.jpg': 'Leafhopper',
    'mealybugs.jpg': 'Mealybugs',
    'thrips.jpg': 'Thrips',
    'whitefly.jpg': 'Whitefly'
}

# Pest library data with multilingual support
PEST_LIBRARY_DATA = {
    "Aphids": {
        "english": {
            "name": "Aphids",
            "scientific_name": "Aphidoidea",
            "description": """Aphids are small, soft-bodied insects that feed on plant sap. They are among the most destructive insect pests on cultivated plants. They reproduce rapidly and can cause significant damage to crops by sucking sap, transmitting plant viruses, and secreting honeydew which leads to sooty mold growth.""",
            "harmful_effects": [
                "Suck plant sap causing stunted growth",
                "Transmit plant viruses like mosaic viruses",
                "Cause leaf curling and distortion",
                "Secrete honeydew promoting sooty mold",
                "Reduce crop yield and quality"
            ],
            "organic_solutions": [
                "Spray neem oil solution (5ml per liter)",
                "Use insecticidal soap sprays",
                "Introduce natural predators like ladybugs",
                "Plant companion plants like marigold",
                "Use garlic or chili pepper sprays"
            ],
            "chemical_pesticides": [
                "Imidacloprid 17.8% SL: 0.5ml per liter",
                "Acetamiprid 20% SP: 0.5g per liter",
                "Thiamethoxam 25% WG: 0.3g per liter",
                "Pymetrozine 50% WG: 0.5g per liter",
                "Flonicamid 50% WG: 0.3g per liter"
            ],
            "prevention_methods": [
                "Regular monitoring of plants",
                "Remove weeds that host aphids",
                "Use reflective mulches",
                "Practice crop rotation",
                "Maintain proper plant spacing"
            ],
            "image": "aphids.jpg",
            "severity": "High",
            "detection_count": 0,
            "category": "Sap-Sucking Insects"
        },
        "hindi": {
            "name": "एफिड्स (माहू)",
            "scientific_name": "एफिडोइडिया",
            "description": """एफिड छोटे, नरम शरीर वाले कीट हैं जो पौधों के रस पर भोजन करते हैं। ये खेती वाले पौधों पर सबसे विनाशकारी कीटों में से हैं। वे तेजी से प्रजनन करते हैं और रस चूसकर, पौधों के वायरस फैलाकर और हनीड्यू स्रावित करके फसलों को महत्वपूर्ण नुकसान पहुंचा सकते हैं, जिससे काली फफूंदी उगती है।""",
            "harmful_effects": [
                "पौधों का रस चूसकर विकास अवरुद्ध करना",
                "मोज़ेक वायरस जैसे पौधों के वायरस फैलाना",
                "पत्तियों का मुड़ना और विकृति पैदा करना",
                "हनीड्यू स्रावित करना जो काली फफूंदी को बढ़ावा देता है",
                "फसल की उपज और गुणवत्ता कम करना"
            ],
            "organic_solutions": [
                "नीम तेल का घोल स्प्रे करें (प्रति लीटर 5 मिली)",
                "कीटनाशक साबुन स्प्रे का उपयोग करें",
                "लेडीबग्स जैसे प्राकृतिक शिकारियों को पेश करें",
                "गेंदे जैसे साथी पौधे लगाएं",
                "लहसुन या मिर्च स्प्रे का उपयोग करें"
            ],
            "chemical_pesticides": [
                "इमिडाक्लोप्रिड १७.८% एसएल: प्रति लीटर ०.५ मिली",
                "एसिटामिप्रिड २०% एसपी: प्रति लीटर ०.५ ग्राम",
                "थायामेथोक्साम २५% डब्ल्यूजी: प्रति लीटर ०.३ ग्राम",
                "पाइमेट्रोज़िन ५०% डब्ल्यूजी: प्रति लीटर ०.५ ग्राम",
                "फ्लोनिकामिड ५०% डब्ल्यूजी: प्रति लीटर ०.३ ग्राम"
            ],
            "prevention_methods": [
                "पौधों की नियमित निगरानी",
                "एफिड को रखने वाले खरपतवार हटाएं",
                "परावर्तक मल्च का उपयोग करें",
                "फसल चक्र का अभ्यास करें",
                "उचित पौधों की दूरी बनाए रखें"
            ],
            "image": "aphids.jpg",
            "severity": "उच्च",
            "detection_count": 0,
            "category": "रस-चूसने वाले कीट"
        },
        "bangla": {
            "name": "এফিডস (মাহু)",
            "scientific_name": "এফিডোইডিয়া",
            "description": """এফিড হল ছোট, নরম শরীরের পোকা যা গাছের রস খায়। তারা চাষ করা গাছের সবচেয়ে ধ্বংসাত্মক পোকামাকড়ের মধ্যে রয়েছে। তারা দ্রুত প্রজনন করে এবং রস চুষে, গাছের ভাইরাস ছড়িয়ে এবং হানিডিউ নিঃসরণ করে ফসলের উল্লেখযোগ্য ক্ষতি করতে পারে, যা সূটি মোল্ডের বৃদ্ধি ঘটায়।""",
            "harmful_effects": [
                "গাছের রস চুষে বৃদ্ধি ব্যাহত করা",
                "মোজাইক ভাইরাসের মতো গাছের ভাইরাস ছড়ানো",
                "পাতা কুঁচকানো এবং বিকৃতি সৃষ্টি করা",
                "হানিডিউ নিঃসরণ যা সূটি মোল্ডকে উন্নত করে",
                "ফসলের ফলন এবং গুণমান হ্রাস করা"
            ],
            "organic_solutions": [
                "নিম তেলের দ্রবণ স্প্রে করুন (প্রতি লিটারে ৫ মিলি)",
                "কীটনাশক সাবান স্প্রে ব্যবহার করুন",
                "লেডিবাগের মতো প্রাকৃতিক শিকারীদের পরিচয় করিয়ে দিন",
                "গাঁদার মতো সহযোগী গাছ রোপণ করুন",
                "রসুন বা মরিচ স্প্রে ব্যবহার করুন"
            ],
            "chemical_pesticides": [
                "ইমিডাক্লোপ্রিড ১৭.৮% এসএল: প্রতি লিটারে ০.৫ মিলি",
                "এসিটামিপ্রিড ২০% এসপি: প্রতি লিটারে ০.৫ গ্রাম",
                "থায়ামেথোক্সাম ২৫% ডব্লিউজি: প্রতি লিটারে ০.৩ গ্রাম",
                "পাইমেট্রোজিন ৫০% ডব্লিউজি: প্রতি লিটারে ০.৫ গ্রাম",
                "ফ্লোনিকামিড ৫০% ডব্লিউজি: প্রতি লিটারে ০.৩ গ্রাম"
            ],
            "prevention_methods": [
                "গাছের নিয়মিত পর্যবেক্ষণ",
                "এফিড হোস্ট আগাছা সরান",
                "প্রতিফলিত মালচ ব্যবহার করুন",
                "ফসল আবর্তন অনুশীলন করুন",
                "উপযুক্ত গাছের ব্যবধান বজায় রাখুন"
            ],
            "image": "aphids.jpg",
            "severity": "উচ্চ",
            "detection_count": 0,
            "category": "রস-চোষা পোকা"
        }
    },

    "Armyworm": {
        "english": {
            "name": "Armyworm",
            "scientific_name": "Spodoptera frugiperda (Fall Armyworm)",
            "description": """Armyworms are caterpillars that travel in large groups and feed voraciously on crops. The Fall Armyworm is particularly destructive to maize, rice, sorghum, and other cereal crops. They get their name from their behavior of moving in masses like an army, consuming entire fields rapidly.""",
            "harmful_effects": [
                "Complete defoliation of crops within days",
                "Direct damage to grains and fruits",
                "Reduced photosynthesis leading to stunted growth",
                "Economic losses due to crop failure",
                "Can destroy entire fields overnight"
            ],
            "organic_solutions": [
                "Neem oil spray: 5ml per liter of water",
                "Chili-garlic extract: Blend 100g chili + 100g garlic in 1L water",
                "Trichogramma wasps: Release 50,000 per hectare weekly",
                "Bacillus thuringiensis (Bt) spray: 2g per liter",
                "Bird perches: Install 10-15 per hectare"
            ],
            "chemical_pesticides": [
                "Chlorpyrifos 20% EC: 2.5ml per liter",
                "Lambda-cyhalothrin 5% EC: 1ml per liter",
                "Emamectin benzoate 5% SG: 0.5g per liter",
                "Spinosad 45% SC: 0.3ml per liter",
                "Indoxacarb 15% EC: 1ml per liter"
            ],
            "prevention_methods": [
                "Early planting to avoid peak infestation periods",
                "Regular field monitoring twice weekly",
                "Maintain field sanitation by removing crop residues",
                "Use pheromone traps: 10 traps per acre",
                "Practice crop rotation with non-host plants"
            ],
            "image": "armyworm.jpg",
            "severity": "Very High",
            "detection_count": 0,
            "category": "Caterpillar Pests"
        },
        "hindi": {
            "name": "आर्मीवर्म (सेना कीट)",
            "scientific_name": "स्पोडोप्टेरा फ्रुगिपेर्डा (फॉल आर्मीवर्म)",
            "description": """आर्मीवर्म ऐसे कैटरपिलर हैं जो बड़े समूहों में यात्रा करते हैं और फसलों पर अत्यधिक भोजन करते हैं। फॉल आर्मीवर्म मक्का, चावल, ज्वार और अन्य अनाज फसलों के लिए विशेष रूप से विनाशकारी है। उन्हें उनके व्यवहार से उनका नाम मिला है जैसे सेना की तरह समूहों में चलना, पूरे खेतों को तेजी से नष्ट करना।""",
            "harmful_effects": [
                "कुछ ही दिनों में फसलों की पूरी पत्तियों की क्षति",
                "अनाज और फलों को सीधा नुकसान",
                "प्रकाश संश्लेषण कम होने से विकास अवरुद्ध होता है",
                "फसल विफलता के कारण आर्थिक नुकसान",
                "रातोंरात पूरे खेतों को नष्ट कर सकते हैं"
            ],
            "organic_solutions": [
                "नीम तेल स्प्रे: प्रति लीटर पानी में 5 मिली",
                "मिर्च-लहसुन का अर्क: 100 ग्राम मिर्च + 100 ग्राम लहसुन 1 लीटर पानी में ब्लेंड करें",
                "ट्राइकोग्रामा ततैया: प्रति हेक्टेयर साप्ताहिक 50,000 छोड़ें",
                "बैसिलस थुरिंजिएंसिस (बीटी) स्प्रे: प्रति लीटर 2 ग्राम",
                "पक्षी बैठने की जगह: प्रति हेक्टेयर 10-15 स्थापित करें"
            ],
            "chemical_pesticides": [
                "क्लोरपाइरिफोस २०% EC: प्रति लीटर २.५ मिली",
                "लैम्ब्डा-साइहैलोथ्रिन ५% EC: प्रति लीटर १ मिली",
                "इमामेक्टिन बेंजोएट ५% SG: प्रति लीटर ०.५ ग्राम",
                "स्पिनोसैड ४५% SC: प्रति लीटर ०.३ मिली",
                "इंडोक्साकार्ब १५% EC: प्रति लीटर १ मिली"
            ],
            "prevention_methods": [
                "शीर्ष संक्रमण अवधि से बचने के लिए प्रारंभिक रोपण",
                "साप्ताहिक दो बार नियमित खेत निगरानी",
                "फसल अवशेषों को हटाकर खेत की स्वच्छता बनाए रखें",
                "फेरोमोन जाल का उपयोग करें: प्रति एकड़ 10 जाल",
                "गैर-होस्ट पौधों के साथ फसल चक्र का अभ्यास करें"
            ],
            "image": "armyworm.jpg",
            "severity": "बहुत उच्च",
            "detection_count": 0,
            "category": "कैटरपिलर कीट"
        },
        "bangla": {
            "name": "আর্মিওয়ার্ম (সেনা পোকা)",
            "scientific_name": "স্পোডোপ্টেরা ফ্রুগিপের্ডা (ফল আর্মিওয়ার্ম)",
            "description": """আর্মিওয়ার্ম হল শুঁয়োপোকা যা বড় দলে ভ্রমণ করে এবং ফসলে প্রচুর পরিমাণে খাবার খায়। ফল আর্মিওয়ার্ম ভুট্টা, ধান, জোয়ার এবং অন্যান্য শস্য ফসলের জন্য বিশেষভাবে ধ্বংসাত্মক। তারা তাদের নাম পেয়েছে সৈন্যদলের মতো দলে দলে চলাফেরার আচরণ থেকে, পুরো ক্ষেত্র দ্রুত গ্রাস করে।""",
            "harmful_effects": [
                "কয়েক দিনের মধ্যে ফসলের সম্পূর্ণ পাতার ক্ষতি",
                "শস্য ও ফলের সরাসরি ক্ষতি",
                "হ্রাসিত সালোকসংশ্লেষণ যা বর্ধন বাধাগ্রস্ত করে",
                "ফসল ব্যর্থতার কারণে অর্থনৈতিক ক্ষতি",
                "রাতারাতি পুরো ক্ষেত্র ধ্বংস করতে পারে"
            ],
            "organic_solutions": [
                "নিম তেল স্প্রে: প্রতি লিটার জলে ৫ মিলি",
                "মরিচ-রসুনের নির্যাস: ১০০ গ্রাম মরিচ + ১০০ গ্রাম রসুন ১ লিটার জলে ব্লেন্ড করুন",
                "ট্রাইকোগ্রামা ওয়াস্প: প্রতি হেক্টরে সাপ্তাহিক ৫০,০০০ ছাড়ুন",
                "ব্যাসিলাস থুরিঞ্জিয়েনসিস (বিটি) স্প্রে: প্রতি লিটারে ২ গ্রাম",
                "পাখির বসার জায়গা: প্রতি হেক্টরে ১০-১৫টি ইনস্টল করুন"
            ],
            "chemical_pesticides": [
                "ক্লোরপাইরিফস ২০% EC: প্রতি লিটারে ২.৫ মিলি",
                "ল্যাম্বডা-সাইহ্যালোথ্রিন ৫% EC: প্রতি লিটারে ১ মিলি",
                "ইমামেকটিন বেনজোয়েট ৫% SG: প্রতি লিটারে ০.৫ গ্রাম",
                "স্পিনোসাড ৪৫% SC: প্রতি লিটারে ০.৩ মিলি",
                "ইন্ডোক্সাকার্ব ১৫% EC: প্রতি লিটারে ১ মিলি"
            ],
            "prevention_methods": [
                "শীর্ষ সংক্রমণ সময় এড়াতে প্রাথমিক রোপণ",
                "সাপ্তাহিক দুইবার নিয়মিত ক্ষেত্র পর্যবেক্ষণ",
                "ফসলের অবশিষ্টাংশ সরিয়ে ক্ষেত্রের স্বাস্থ্যবিধি বজায় রাখুন",
                "ফেরোমোন ফাঁদ ব্যবহার করুন: প্রতি একরে ১০টি ফাঁদ",
                "অ-হোস্ট গাছপালা সহ ফসল আবর্তন অনুশীলন করুন"
            ],
            "image": "armyworm.jpg",
            "severity": "অত্যন্ত উচ্চ",
            "detection_count": 0,
            "category": "শুঁয়োপোকা পোকা"
        }
    },

    "Leafhopper": {
        "english": {
            "name": "Leafhopper",
            "scientific_name": "Cicadellidae",
            "description": """Leafhoppers are small, wedge-shaped insects that feed on plant sap. They are known for their ability to jump quickly when disturbed. Leafhoppers can transmit various plant diseases, including phytoplasmas and viruses, making them economically important pests in agriculture.""",
            "harmful_effects": [
                "Transmit viral diseases like aster yellows",
                "Cause leaf stippling (white or yellow spots)",
                "Reduce plant vigor and growth",
                "Secrete honeydew promoting sooty mold",
                "Damage plant tissues through feeding"
            ],
            "organic_solutions": [
                "Insecticidal soap sprays",
                "Neem oil applications",
                "Garlic or pepper sprays",
                "Introduce natural predators like lacewings",
                "Use floating row covers"
            ],
            "chemical_pesticides": [
                "Imidacloprid 17.8% SL: 0.5ml per liter",
                "Thiamethoxam 25% WG: 0.3g per liter",
                "Acetamiprid 20% SP: 0.5g per liter",
                "Dinotefuran 20% SG: 0.5g per liter",
                "Flupyradifurone 17.1% SL: 0.5ml per liter"
            ],
            "prevention_methods": [
                "Remove weed hosts regularly",
                "Use reflective mulches",
                "Practice crop rotation",
                "Maintain proper irrigation",
                "Monitor with yellow sticky traps"
            ],
            "image": "leafhopper.jpg",
            "severity": "Medium",
            "detection_count": 0,
            "category": "Sap-Sucking Insects"
        },
        "hindi": {
            "name": "लीफहॉपर (पत्ता कूदने वाला कीट)",
            "scientific_name": "सिसाडेलिडी",
            "description": """लीफहॉपर छोटे, वेज के आकार के कीट हैं जो पौधों के रस पर भोजन करते हैं। वे परेशान होने पर तेजी से कूदने की क्षमता के लिए जाने जाते हैं। लीफहॉपर विभिन्न पौधों की बीमारियों को फैला सकते हैं, जिनमें फाइटोप्लाज्मा और वायरस शामिल हैं, जिससे वे कृषि में आर्थिक रूप से महत्वपूर्ण कीट बन जाते हैं।""",
            "harmful_effects": [
                "एस्टर येलो जैसे वायरल रोग फैलाना",
                "पत्तियों पर धब्बे (सफेद या पीले धब्बे) पैदा करना",
                "पौधे की शक्ति और वृद्धि कम करना",
                "हनीड्यू स्रावित करना जो काली फफूंदी को बढ़ावा देता है",
                "भोजन के माध्यम से पौधे के ऊतकों को नुकसान पहुंचाना"
            ],
            "organic_solutions": [
                "कीटनाशक साबुन स्प्रे",
                "नीम तेल अनुप्रयोग",
                "लहसुन या मिर्च स्प्रे",
                "लेसविंग्स जैसे प्राकृतिक शिकारियों को पेश करें",
                "फ्लोटिंग रो कवर का उपयोग करें"
            ],
            "chemical_pesticides": [
                "इमिडाक्लोप्रिड १७.८% एसएल: प्रति लीटर ०.५ मिली",
                "थायामेथोक्साम २५% डब्ल्यूजी: प्रति लीटर ०.३ ग्राम",
                "एसिटामिप्रिड २०% एसपी: प्रति लीटर ०.५ ग्राम",
                "डायनोटेफुरान २०% एसजी: प्रति लीटर ०.५ ग्राम",
                "फ्लूपाइराडिफ्यूरोन १७.१% एसएल: प्रति लीटर ०.५ मिली"
            ],
            "prevention_methods": [
                "नियमित रूप से खरपतवार होस्ट हटाएं",
                "परावर्तक मल्च का उपयोग करें",
                "फसल चक्र का अभ्यास करें",
                "उचित सिंचाई बनाए रखें",
                "पीले चिपचिपे जाल के साथ निगरानी करें"
            ],
            "image": "leafhopper.jpg",
            "severity": "मध्यम",
            "detection_count": 0,
            "category": "रस-चूसने वाले कीट"
        },
        "bangla": {
            "name": "লিফহপার (পাতা লাফানো পোকা)",
            "scientific_name": "সিসাডেলিডি",
            "description": """লিফহপার হল ছোট, কীলক-আকৃতির পোকা যা গাছের রস খায়। তারা বিরক্ত হলে দ্রুত লাফানোর ক্ষমতার জন্য পরিচিত। লিফহপারগুলি বিভিন্ন গাছের রোগ ছড়াতে পারে, যার মধ্যে রয়েছে ফাইটোপ্লাজমা এবং ভাইরাস, যা তাদের কৃষিতে অর্থনৈতিকভাবে গুরুত্বপূর্ণ পোকা করে তোলে।""",
            "harmful_effects": [
                "অ্যাস্টার ইয়েলোসের মতো ভাইরাল রোগ ছড়ানো",
                "পাতায় ফোঁটা (সাদা বা হলুদ দাগ) সৃষ্টি করা",
                "গাছের শক্তি এবং বৃদ্ধি হ্রাস করা",
                "হানিডিউ নিঃসরণ যা সূটি মোল্ডকে উন্নত করে",
                "খাওয়ার মাধ্যমে গাছের টিস্যু ক্ষতি করা"
            ],
            "organic_solutions": [
                "কীটনাশক সাবান স্প্রে",
                "নিম তেল প্রয়োগ",
                "রসুন বা মরিচ স্প্রে",
                "লেসউইংসের মতো প্রাকৃতিক শিকারীদের পরিচয় করিয়ে দিন",
                "ভাসমান সারি কভার ব্যবহার করুন"
            ],
            "chemical_pesticides": [
                "ইমিডাক্লোপ্রিড ১৭.৮% এসএল: প্রতি লিটারে ০.৫ মিলি",
                "থায়ামেথোক্সাম ২৫% ডব্লিউজি: প্রতি লিটারে ০.৩ গ্রাম",
                "এসিটামিপ্রিড ২০% এসপি: প্রতি লিটারে ০.৫ গ্রাম",
                "ডাইনোটেফুরান ২০% এসজি: প্রতি লিটারে ০.৫ গ্রাম",
                "ফ্লুপাইরাডিফিউরন ১৭.১% এসএল: প্রতি লিটারে ০.৫ মিলি"
            ],
            "prevention_methods": [
                "নিয়মিত আগাছা হোস্ট সরান",
                "প্রতিফলিত মালচ ব্যবহার করুন",
                "ফসল আবর্তন অনুশীলন করুন",
                "উপযুক্ত সেচ বজায় রাখুন",
                "হলুদ স্টিকি ফাঁদ দিয়ে পর্যবেক্ষণ করুন"
            ],
            "image": "leafhopper.jpg",
            "severity": "মধ্যবর্তী",
            "detection_count": 0,
            "category": "রস-চোষা পোকা"
        }
    },

    "Mealybugs": {
        "english": {
            "name": "Mealybugs",
            "scientific_name": "Pseudococcidae",
            "description": """Mealybugs are small, soft-bodied insects covered with a white, powdery wax coating. They feed on plant sap and are commonly found in clusters on stems, leaves, and fruits. Mealybugs excrete honeydew, which attracts ants and promotes sooty mold growth.""",
            "harmful_effects": [
                "Weaken plants by sucking sap",
                "Cause leaf yellowing and drop",
                "Transmit plant viruses",
                "Produce honeydew leading to sooty mold",
                "Attract ants that protect mealybugs"
            ],
            "organic_solutions": [
                "Alcohol swabs for small infestations",
                "Insecticidal soap sprays",
                "Neem oil applications",
                "Introduce natural predators like Cryptolaemus montrouzieri",
                "Garlic or chili pepper sprays"
            ],
            "chemical_pesticides": [
                "Buprofezin 25% SC: 1ml per liter",
                "Pyriproxyfen 10.8% EC: 0.5ml per liter",
                "Flonicamid 50% WG: 0.3g per liter",
                "Spirotetramat 15.31% OD: 0.5ml per liter",
                "Acetamiprid 20% SP: 0.5g per liter"
            ],
            "prevention_methods": [
                "Inspect new plants before introducing",
                "Maintain proper plant spacing",
                "Avoid over-fertilization with nitrogen",
                "Remove heavily infested plant parts",
                "Use sticky traps for monitoring"
            ],
            "image": "mealybugs.jpg",
            "severity": "Medium",
            "detection_count": 0,
            "category": "Sap-Sucking Insects"
        },
        "hindi": {
            "name": "मिलीबग (सफेद रुई जैसे कीट)",
            "scientific_name": "स्यूडोकोसिडी",
            "description": """मिलीबग छोटे, नरम शरीर वाले कीट हैं जो सफेद, पाउडरी मोम कोटिंग से ढके होते हैं। वे पौधों के रस पर भोजन करते हैं और आमतौर पर तनों, पत्तियों और फलों पर समूहों में पाए जाते हैं। मिलीबग हनीड्यू स्रावित करते हैं, जो चींटियों को आकर्षित करता है और काली फफूंदी के विकास को बढ़ावा देता है।""",
            "harmful_effects": [
                "रस चूसकर पौधों को कमजोर करना",
                "पत्तियों का पीला पड़ना और गिरना",
                "पौधों के वायरस फैलाना",
                "हनीड्यू उत्पादन जो काली फफूंदी की ओर जाता है",
                "चींटियों को आकर्षित करना जो मिलीबग की रक्षा करती हैं"
            ],
            "organic_solutions": [
                "छोटे संक्रमण के लिए अल्कोहल स्वैब",
                "कीटनाशक साबुन स्प्रे",
                "नीम तेल अनुप्रयोग",
                "क्रिप्टोलेमस मोंटरोज़िएरी जैसे प्राकृतिक शिकारियों को पेश करें",
                "लहसुन या मिर्च स्प्रे"
            ],
            "chemical_pesticides": [
                "बुप्रोफेजिन २५% SC: प्रति लीटर १ मिली",
                "पाइरिप्रोक्सीफेन १०.८% EC: प्रति लीटर ०.५ मिली",
                "फ्लोनिकामिड ५०% WG: प्रति लीटर ०.३ ग्राम",
                "स्पाइरोटेट्रामाट १५.३१% OD: प्रति लीटर ०.५ मिली",
                "एसिटामिप्रिड २०% SP: प्रति लीटर ०.५ ग्राम"
            ],
            "prevention_methods": [
                "परिचय से पहले नए पौधों का निरीक्षण करें",
                "उचित पौधों की दूरी बनाए रखें",
                "नाइट्रोजन के साथ अतिरिक्त उर्वरक से बचें",
                "अत्यधिक संक्रमित पौधे के भाग हटाएं",
                "निगरानी के लिए चिपचिपे जाल का उपयोग करें"
            ],
            "image": "mealybugs.jpg",
            "severity": "मध्यम",
            "detection_count": 0,
            "category": "रस-चूसने वाले कीट"
        },
        "bangla": {
            "name": "মিলিবাগ (সাদা তুলার মতো পোকা)",
            "scientific_name": "সিউডোকক্সিডি",
            "description": """মিলিবাগ হল ছোট, নরম শরীরের পোকা যা সাদা, পাউডারি মোমের আবরণ দিয়ে coveredাকা। তারা গাছের রস খায় এবং সাধারণত কান্ড, পাতা এবং ফলে গুচ্ছে পাওয়া যায়। মিলিবাগগুলি হানিডিউ নিঃসরণ করে, যা পিপড়াকে আকর্ষণ করে এবং সূটি মোল্ডের বৃদ্ধিকে উন্নত করে।""",
            "harmful_effects": [
                "রস চুষে গাছ দুর্বল করা",
                "পাতা হলুদ হয়ে যাওয়া এবং পড়া",
                "গাছের ভাইরাস ছড়ানো",
                "হানিডিউ উৎপাদন যা সূটি মোল্ডের দিকে নিয়ে যায়",
                "পিপড়াকে আকর্ষণ করা যা মিলিবাগ রক্ষা করে"
            ],
            "organic_solutions": [
                "ছোট সংক্রমণের জন্য অ্যালকোহল সুয়াব",
                "কীটনাশক সাবান স্প্রে",
                "নিম তেল প্রয়োগ",
                "ক্রিপ্টোলেমাস মন্ট্রোজিয়েরির মতো প্রাকৃতিক শিকারীদের পরিচয় করিয়ে দিন",
                "রসুন বা মরিচ স্প্রে"
            ],
            "chemical_pesticides": [
                "বুপ্রোফেজিন ২৫% SC: প্রতি লিটারে ১ মিলি",
                "পাইরিপ্রোক্সিফেন ১০.৮% EC: প্রতি লিটারে ০.৫ মিলি",
                "ফ্লোনিকামিড ৫০% ডব্লিউজি: প্রতি লিটারে ০.৩ গ্রাম",
                "স্পাইরোটেট্রামাট ১৫.৩১% OD: প্রতি লিটারে ০.৫ মিলি",
                "এসিটামিপ্রিড ২০% এসপি: প্রতি লিটারে ০.৫ গ্রাম"
            ],
            "prevention_methods": [
                "প্রবর্তনের আগে নতুন গাছ পরিদর্শন করুন",
                "উপযুক্ত গাছের ব্যবধান বজায় রাখুন",
                "নাইট্রোজেন দিয়ে অতিরিক্ত সার প্রয়োগ এড়িয়ে চলুন",
                "অত্যধিক সংক্রমিত গাছের অংশগুলি সরান",
                "নিরীক্ষণের জন্য স্টিকি ফাঁদ ব্যবহার করুন"
            ],
            "image": "mealybugs.jpg",
            "severity": "মধ্যবর্তী",
            "detection_count": 0,
            "category": "রস-চোষা পোকা"
        }
    },

    "Thrips": {
        "english": {
            "name": "Thrips",
            "scientific_name": "Thysanoptera",
            "description": """Thrips are tiny, slender insects that feed by puncturing plant cells and sucking out the contents. They cause silvering or bronzing of leaves and can transmit plant viruses. Thrips are difficult to control due to their small size and ability to hide in plant crevices.""",
            "harmful_effects": [
                "Cause silvering or bronzing of leaves",
                "Transmit tomato spotted wilt virus (TSWV)",
                "Deform flowers and fruits",
                "Reduce photosynthesis efficiency",
                "Cause premature leaf drop"
            ],
            "organic_solutions": [
                "Blue sticky traps for monitoring",
                "Neem oil sprays",
                "Insecticidal soaps",
                "Predatory mites (Amblyseius cucumeris)",
                "Garlic or onion extracts"
            ],
            "chemical_pesticides": [
                "Spinosad 45% SC: 0.3ml per liter",
                "Abamectin 1.8% EC: 0.5ml per liter",
                "Fipronil 5% SC: 1ml per liter",
                "Lambda-cyhalothrin 5% EC: 1ml per liter",
                "Chlorfenapyr 10% SC: 1ml per liter"
            ],
            "prevention_methods": [
                "Remove weed hosts near crops",
                "Use reflective mulches",
                "Practice crop rotation",
                "Avoid excessive nitrogen fertilization",
                "Maintain proper irrigation"
            ],
            "image": "thrips.jpg",
            "severity": "High",
            "detection_count": 0,
            "category": "Sap-Sucking Insects"
        },
        "hindi": {
            "name": "थ्रिप्स (सूक्ष्म कीट)",
            "scientific_name": "थाइसैनोप्टेरा",
            "description": """थ्रिप्स छोटे, पतले कीट हैं जो पौधों की कोशिकाओं को छेदकर और सामग्री को चूसकर भोजन करते हैं। वे पत्तियों की चांदी या कांस्य रंगत का कारण बनते हैं और पौधों के वायरस फैला सकते हैं। थ्रिप्स को नियंत्रित करना मुश्किल है क्योंकि उनका आकार छोटा होता है और पौधों की दरारों में छिपने की क्षमता होती है।""",
            "harmful_effects": [
                "पत्तियों की चांदी या कांस्य रंगत का कारण बनना",
                "टमाटर स्पॉटेड विल्ट वायरस (TSWV) फैलाना",
                "फूलों और फलों को विकृत करना",
                "प्रकाश संश्लेषण दक्षता कम करना",
                "समय से पहले पत्ती गिरने का कारण बनना"
            ],
            "organic_solutions": [
                "निगरानी के लिए नीले चिपचिपे जाल",
                "नीम तेल स्प्रे",
                "कीटनाशक साबुन",
                "शिकारी घुन (अम्ब्लिसियस क्यूक्यूमेरिस)",
                "लहसुन या प्याज के अर्क"
            ],
            "chemical_pesticides": [
                "स्पिनोसैड ४५% SC: प्रति लीटर ०.३ मिली",
                "एबामेक्टिन १.८% EC: प्रति लीटर ०.५ मिली",
                "फिप्रोनिल ५% SC: प्रति लीटर १ मिली",
                "लैम्ब्डा-साइहैलोथ्रिन ५% EC: प्रति लीटर १ मिली",
                "क्लोरफेनापायर १०% SC: प्रति लीटर १ मिली"
            ],
            "prevention_methods": [
                "फसलों के पास खरपतवार होस्ट हटाएं",
                "परावर्तक मल्च का उपयोग करें",
                "फसल चक्र का अभ्यास करें",
                "नाइट्रोजन के अत्यधिक उपयोग से बचें",
                "उचित सिंचाई बनाए रखें"
            ],
            "image": "thrips.jpg",
            "severity": "उच्च",
            "detection_count": 0,
            "category": "रस-चूसने वाले कीट"
        },
        "bangla": {
            "name": "থ্রিপস (ক্ষুদ্র পোকা)",
            "scientific_name": "থাইসানোপ্টেরা",
            "description": """থ্রিপস হল ক্ষুদ্র, সরু পোকা যা গাছের কোষ ছিদ্র করে এবং বিষয়বস্তু চুষে খায়। তারা পাতার রূপালী বা ব্রোঞ্জ রঙের কারণ হয় এবং গাছের ভাইরাস ছড়াতে পারে। থ্রিপস নিয়ন্ত্রণ করা কঠিন কারণ তাদের আকার ছোট এবং গাছের ফাটলে লুকানোর ক্ষমতা রয়েছে।""",
            "harmful_effects": [
                "পাতার রূপালী বা ব্রোঞ্জ রঙের কারণ হওয়া",
                "টমেটো স্পটেড উইল্ট ভাইরাস (TSWV) ছড়ানো",
                "ফুল এবং ফল বিকৃত করা",
                "সালোকসংশ্লেষণ দক্ষতা হ্রাস করা",
                "অকালে পাতা পড়ার কারণ হওয়া"
            ],
            "organic_solutions": [
                "নিরীক্ষণের জন্য নীল স্টিকি ফাঁদ",
                "নিম তেল স্প্রে",
                "কীটনাশক সাবান",
                "শিকারী মাইট (অ্যাম্বলিসিয়াস কুকুমেরিস)",
                "রসুন বা পেঁয়াজের নির্যাস"
            ],
            "chemical_pesticides": [
                "স্পিনোসাড ৪৫% SC: প্রতি লিটারে ০.৩ মিলি",
                "অ্যাবামেক্টিন ১.৮% EC: প্রতি লিটারে ০.৫ মিলি",
                "ফিপ্রোনিল ৫% SC: প্রতি লিটারে ১ মিলি",
                "ল্যাম্বডা-সাইহ্যালোথ্রিন ৫% EC: প্রতি লিটারে ১ মিলি",
                "ক্লোরফেনাপাইর ১০% SC: প্রতি লিটারে ১ মিলি"
            ],
            "prevention_methods": [
                "ফসলের কাছাকাছি আগাছা হোস্ট সরান",
                "প্রতিফলিত মালচ ব্যবহার করুন",
                "ফসল আবর্তন অনুশীলন করুন",
                "নাইট্রোজেনের অত্যধিক প্রয়োগ এড়িয়ে চলুন",
                "উপযুক্ত সেচ বজায় রাখুন"
            ],
            "image": "thrips.jpg",
            "severity": "উচ্চ",
            "detection_count": 0,
            "category": "রস-চোষা পোকা"
        }
    },

    "Whitefly": {
        "english": {
            "name": "Whitefly",
            "scientific_name": "Aleyrodidae",
            "description": """Whiteflies are small, white, flying insects that feed on plant sap. They are typically found on the undersides of leaves. Whiteflies are notorious for transmitting plant viruses and causing sooty mold through honeydew excretion. They reproduce rapidly and can be difficult to control.""",
            "harmful_effects": [
                "Transmit geminiviruses and other plant viruses",
                "Cause leaf yellowing and drop",
                "Produce honeydew leading to sooty mold",
                "Reduce plant vigor and growth",
                "Can cause complete crop failure"
            ],
            "organic_solutions": [
                "Yellow sticky traps for monitoring and control",
                "Neem oil sprays",
                "Insecticidal soaps",
                "Introduce natural predators like Encarsia formosa",
                "Garlic or pepper sprays"
            ],
            "chemical_pesticides": [
                "Imidacloprid 17.8% SL: 0.5ml per liter",
                "Thiamethoxam 25% WG: 0.3g per liter",
                "Buprofezin 25% SC: 1ml per liter",
                "Pyriproxyfen 10.8% EC: 0.5ml per liter",
                "Flonicamid 50% WG: 0.3g per liter"
            ],
            "prevention_methods": [
                "Use yellow sticky traps for early detection",
                "Remove weed hosts regularly",
                "Practice crop rotation",
                "Avoid excessive nitrogen fertilization",
                "Use reflective mulches"
            ],
            "image": "whitefly.jpg",
            "severity": "High",
            "detection_count": 0,
            "category": "Sap-Sucking Insects"
        },
        "hindi": {
            "name": "व्हाइटफ्लाई (सफेद मक्खी)",
            "scientific_name": "एलेरोडिडी",
            "description": """व्हाइटफ्लाई छोटे, सफेद, उड़ने वाले कीट हैं जो पौधों के रस पर भोजन करते हैं। वे आमतौर पर पत्तियों के नीचे पाए जाते हैं। व्हाइटफ्लाई पौधों के वायरस फैलाने और हनीड्यू उत्सर्जन के माध्यम से काली फफूंदी पैदा करने के लिए कुख्यात हैं। वे तेजी से प्रजनन करते हैं और नियंत्रित करना मुश्किल हो सकता है।""",
            "harmful_effects": [
                "जेमिनिवायरस और अन्य पौधों के वायरस फैलाना",
                "पत्तियों का पीला पड़ना और गिरना",
                "हनीड्यू उत्पादन जो काली फफूंदी की ओर जाता है",
                "पौधे की शक्ति और वृद्धि कम करना",
                "पूरी फसल विफलता का कारण बन सकता है"
            ],
            "organic_solutions": [
                "निगरानी और नियंत्रण के लिए पीले चिपचिपे जाल",
                "नीम तेल स्प्रे",
                "कीटनाशक साबुन",
                "एन्कार्सिया फॉर्मोसा जैसे प्राकृतिक शिकारियों को पेश करें",
                "लहसुन या मिर्च स्प्रे"
            ],
            "chemical_pesticides": [
                "इमिडाक्लोप्रिड १७.८% एसएल: प्रति लीटर ०.५ मिली",
                "थायामेथोक्साम २५% डब्ल्यूजी: प्रति लीटर ०.३ ग्राम",
                "बुप्रोफेजिन २५% एससी: प्रति लीटर १ मिली",
                "पाइरिप्रोक्सीफेन १०.८% ईसी: प्रति लीटर ०.५ मिली",
                "फ्लोनिकामिड ५०% डब्ल्यूजी: प्रति लीटर ०.३ ग्राम"
            ],
            "prevention_methods": [
                "शीघ्र पता लगाने के लिए पीले चिपचिपे जाल का उपयोग करें",
                "नियमित रूप से खरपतवार होस्ट हटाएं",
                "फसल चक्र का अभ्यास करें",
                "नाइट्रोजन के अत्यधिक उपयोग से बचें",
                "परावर्तक मल्च का उपयोग करें"
            ],
            "image": "whitefly.jpg",
            "severity": "उच्च",
            "detection_count": 0,
            "category": "रस-चूसने वाले कीट"
        },
        "bangla": {
            "name": "হোয়াইটফ্লাই (সাদা মাছি)",
            "scientific_name": "এলিরোডিডি",
            "description": """হোয়াইটফ্লাই হল ছোট, সাদা, উড়ন্ত পোকা যা গাছের রস খায়। তারা সাধারণত পাতার নিচের দিকে পাওয়া যায়। হোয়াইটফ্লাইগুলি গাছের ভাইরাস ছড়ানো এবং হানিডিউ নিঃসরণের মাধ্যমে সূটি মোল্ড সৃষ্টির জন্য কুখ্যাত। তারা দ্রুত প্রজনন করে এবং নিয়ন্ত্রণ করা কঠিন হতে পারে।""",
            "harmful_effects": [
                "জেমিনিভাইরাস এবং অন্যান্য গাছের ভাইরাস ছড়ানো",
                "পাতা হলুদ হয়ে যাওয়া এবং পড়া",
                "হানিডিউ উৎপাদন যা সূটি মোল্ডের দিকে নিয়ে যায়",
                "গাছের শক্তি এবং বৃদ্ধি হ্রাস করা",
                "সম্পূর্ণ ফসল ব্যর্থতা ঘটাতে পারে"
            ],
            "organic_solutions": [
                "নিরীক্ষণ এবং নিয়ন্ত্রণের জন্য হলুদ স্টিকি ফাঁদ",
                "নিম তেল স্প্রে",
                "কীটনাশক সাবান",
                "এনকার্সিয়া ফর্মোসার মতো প্রাকৃতিক শিকারীদের পরিচয় করিয়ে দিন",
                "রসুন বা মরিচ স্প্রে"
            ],
            "chemical_pesticides": [
                "ইমিডাক্লোপ্রিড ১৭.৮% এসএল: প্রতি লিটারে ০.৫ মিলি",
                "থায়ামেথোক্সাম ২৫% ডব্লিউজি: প্রতি লিটারে ০.৩ গ্রাম",
                "বুপ্রোফেজিন ২৫% এসসি: প্রতি লিটারে ১ মিলি",
                "পাইরিপ্রোক্সিফেন ১০.৮% ইসি: প্রতি লিটারে ০.৫ মিলি",
                "ফ্লোনিকামিড ৫০% ডব্লিউজি: প্রতি লিটারে ০.৩ গ্রাম"
            ],
            "prevention_methods": [
                "প্রারম্ভিক সনাক্তকরণের জন্য হলুদ স্টিকি ফাঁদ ব্যবহার করুন",
                "নিয়মিত আগাছা হোস্ট সরান",
                "ফসল আবর্তন অনুশীলন করুন",
                "নাইট্রোজেনের অত্যধিক প্রয়োগ এড়িয়ে চলুন",
                "প্রতিফলিত মালচ ব্যবহার করুন"
            ],
            "image": "whitefly.jpg",
            "severity": "উচ্চ",
            "detection_count": 0,
            "category": "রস-চোষা পোকা"
        }
    }
}


def get_pest_from_image(image_filename):
    """
    Get pest name from image filename
    """
    return IMAGE_TO_PEST_MAPPING.get(image_filename)


def get_pest_details_by_image(image_filename, language='english'):
    """
    Get pest details by image filename
    """
    pest_name = get_pest_from_image(image_filename)
    if pest_name and pest_name in PEST_LIBRARY_DATA:
        return PEST_LIBRARY_DATA[pest_name].get(language.lower(), PEST_LIBRARY_DATA[pest_name]['english'])
    return None


def get_all_pests(language='english'):
    """
    Get all pests with details in specified language
    """
    result = []
    for pest_name, pest_data in PEST_LIBRARY_DATA.items():
        if language.lower() in pest_data:
            result.append(pest_data[language.lower()])
        else:
            result.append(pest_data['english'])
    return result


def get_pest_by_name(pest_name, language='english'):
    """
    Get pest details by pest name
    """
    if pest_name in PEST_LIBRARY_DATA:
        return PEST_LIBRARY_DATA[pest_name].get(language.lower(), PEST_LIBRARY_DATA[pest_name]['english'])
    return None


def get_available_languages():
    """
    Get list of available languages
    """
    return ['english', 'hindi', 'bangla']


def get_pest_image(pest_name):
    """
    Get image filename for a pest
    """
    if pest_name in PEST_LIBRARY_DATA:
        return PEST_LIBRARY_DATA[pest_name]['english']['image']
    return None


# Test the module
if __name__ == "__main__":
    # Test getting pest details
    print("Testing Pest Library Module:")
    print("=" * 50)
    
    # Test 1: Get pest from image
    image_name = "aphids.jpg"
    pest_name = get_pest_from_image(image_name)
    print(f"1. Image '{image_name}' corresponds to pest: {pest_name}")
    
    # Test 2: Get details in English
    details = get_pest_details_by_image(image_name, 'english')
    if details:
        print(f"2. English Details for {pest_name}:")
        print(f"   Name: {details['name']}")
        print(f"   Scientific Name: {details['scientific_name']}")
        print(f"   Description (first 100 chars): {details['description'][:100]}...")
    
    # Test 3: Get details in Hindi
    details_hindi = get_pest_details_by_image(image_name, 'hindi')
    if details_hindi:
        print(f"3. Hindi Details for {pest_name}:")
        print(f"   Name: {details_hindi['name']}")
    
    # Test 4: Get all pests
    all_pests = get_all_pests('english')
    print(f"4. Total pests in library: {len(all_pests)}")
    print("   Pest names:", [pest['name'] for pest in all_pests])
    
    # Test 5: Get available languages
    languages = get_available_languages()
    print(f"5. Available languages: {languages}")