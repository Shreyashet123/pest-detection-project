# utils/pest.py
from .pestid import pest_name_to_id, AVAILABLE_LANGUAGES, DEFAULT_LANGUAGE

# Add this mapping function to handle different naming formats
def map_pest_name(pest_name):
    """
    Map different pest name formats to the standard names in pest_group_data
    """
    # Common variations mapping
    variations_map = {
        # Armyworms variations
        "Armyworms": "Armyworms Group",
        "Army Worms": "Armyworms Group",
        "Army worm": "Armyworms Group",
        
        # Corn Worms variations
        "Corn Worms": "Corn Worms Group", 
        "Cornworms": "Corn Worms Group",
        "Corn worm": "Corn Worms Group",
        
        # Small Sap-Sucking Pests variations
        "Small Sap Sucking Pests": "Small Sap-Sucking Pests",
        "Sap Sucking Pests": "Small Sap-Sucking Pests",
        "Sap-sucking pests": "Small Sap-Sucking Pests",
        
        # Africanized Honey Bees variations
        "Africanized Honey Bees": "Africanized Honey Bees (Killer Bees)",
        "Killer Bees": "Africanized Honey Bees (Killer Bees)",
        "Africanized bees": "Africanized Honey Bees (Killer Bees)",
        
        # Brown Marmorated Stink Bugs variations
        "Brown Marmorated Stink Bug": "Brown Marmorated Stink Bugs",
        "Stink Bugs": "Brown Marmorated Stink Bugs",
        "Stink bug": "Brown Marmorated Stink Bugs",
        
        # Cabbage Loopers variations
        "Cabbage Looper": "Cabbage Loopers",
        
        # Citrus Canker variations
        "Citrus canker": "Citrus Canker",
        
        # Colorado Potato Beetles variations
        "Colorado Potato Beetle": "Colorado Potato Beetles",
        "Potato Beetles": "Colorado Potato Beetles",
        
        # Fruit Flies variations
        "Fruit Fly": "Fruit Flies",
        "Fruitflies": "Fruit Flies",
        
        # Tomato Hornworms variations
        "Tomato Hornworm": "Tomato Hornworms",
        "Hornworms": "Tomato Hornworms",
        
        # Western Corn Rootworms variations
        "Western Corn Rootworm": "Western Corn Rootworms",
        "Corn Rootworms": "Western Corn Rootworms"
    }
    
    # First check exact match
    if pest_name in pest_group_data:
        return pest_name
    
    # Check case-insensitive match
    for key in pest_group_data.keys():
        if pest_name.lower() == key.lower():
            return key
    
    # Check variations map
    if pest_name in variations_map:
        return variations_map[pest_name]
    
    # Check partial matches
    for key in pest_group_data.keys():
        if pest_name.lower() in key.lower() or key.lower() in pest_name.lower():
            return key
    
    # Return original if no match found
    return pest_name

def get_pest_details(pest_name, language='english'):
    # 1. Clean the input name (AI results often have trailing spaces)
    pest_name = pest_name.strip()
    language = language.lower()

    # 2. Check if pest exists in our data
    if pest_name in pest_group_data:
        pest_data = pest_group_data[pest_name]
        
        # 3. Check if language exists, otherwise default to English
        if language in pest_data:
            return pest_data[language]
        else:
            return pest_data.get('english')

    # 4. Fallback if the AI predicted something not in your dictionary
    return {
        'name': pest_name,
        'description': f'No detailed information found for "{pest_name}". Please check the class mapping.',
        'harmful_effects': ['Data unavailable'],
        'organic_solutions': ['Consult local extension office'],
        'chemical_pesticides': ['N/A'],
        'prevention_methods': ['Regular monitoring']
    }
    """
    Get pest details in specified language
    Args:
        pest_name: Name of the pest
        language: 'english', 'bangla', or 'hindi'
    Returns:
        Dictionary with pest details or default if not found
    """
    # Map the pest name to standard format
    mapped_name = map_pest_name(pest_name)
    print(f"DEBUG [pest.py]: Mapping '{pest_name}' -> '{mapped_name}'")
    
    # Default fallback data
    default_data = {
        'name': pest_name,
        'description': f'Details for {pest_name} not available in {language}.',
        'harmful_effects': ['Information coming soon'],
        'organic_solutions': ['Consult agricultural expert'],
        'chemical_pesticides': ['Use appropriate pesticide'],
        'prevention_methods': ['Regular monitoring']
    }
    
    # Check if pest exists
    if mapped_name in pest_group_data:
        pest_data = pest_group_data[mapped_name]
        
        # Check if language exists, fall back to english
        if language.lower() in pest_data:
            return pest_data[language.lower()]
        elif 'english' in pest_data:
            return pest_data['english']
        else:
            # If no language data, use first available
            first_lang = list(pest_data.keys())[0]
            return pest_data[first_lang]
    
    print(f"DEBUG [pest.py]: No data found for '{mapped_name}'")
    return default_data

# ... rest of your pest_group_data remains the same ...

def get_all_pests_list():
    """Get list of all pest names"""
    return list(pest_group_data.keys())

def get_pest_by_id(pest_id, language='english'):
    """Get pest details by ID"""
    from .pestid import pest_id_to_name
    pest_name = pest_id_to_name.get(str(pest_id), "Unknown Pest")
    return get_pest_details(pest_name, language)
pest_group_data = {
    "Armyworms Group": {
        "english": {
            "name": "Armyworms Group",
            "description": """Armyworms are caterpillars that travel in large groups, feeding on grasses, cereals, and other crops. They get their name from their behavior of moving in masses like an army, consuming entire fields rapidly. Common species include Fall Armyworm (Spodoptera frugiperda), Beet Armyworm (Spodoptera exigua), and African Armyworm (Spodoptera exempta).""",
            "harmful_effects": [
                "Complete defoliation of crops within days",
                "Reduced photosynthesis leading to stunted growth",
                "Direct damage to grains and fruits",
                "Economic losses due to crop failure"
            ],
            "organic_solutions": [
                "Neem oil spray: 5ml per liter of water",
                "Chili-garlic extract: Blend 100g chili + 100g garlic in 1L water, dilute 1:10",
                "Trichogramma wasps: Release 50,000 per hectare weekly",
                "Bird perches: Install 10-15 per hectare to attract predatory birds"
            ],
            "chemical_pesticides": [
                "Chlorpyrifos 20% EC: 2.5ml per liter",
                "Lambda-cyhalothrin 5% EC: 1ml per liter",
                "Emamectin benzoate 5% SG: 0.5g per liter",
                "Spinosad 45% SC: 0.3ml per liter"
            ],
            "prevention_methods": [
                "Early planting to avoid peak infestation periods",
                "Regular field monitoring twice weekly",
                "Maintain field sanitation by removing crop residues",
                "Use pheromone traps: 10 traps per acre"
            ]
        },
        "bangla": {
            "name": "আর্মিওয়ার্ম গ্রুপ",
            "description": """আর্মিওয়ার্ম হল শুঁয়োপোকা যা বড় দলে ভ্রমণ করে, ঘাস, শস্য এবং অন্যান্য ফসলে খাবার খায়। তারা তাদের নাম পেয়েছে সৈন্যদলের মতো দলে দলে চলাফেরার আচরণ থেকে, পুরো ক্ষেত্র দ্রুত গ্রাস করে। সাধারণ প্রজাতিগুলির মধ্যে রয়েছে ফল আর্মিওয়ার্ম (Spodoptera frugiperda), বিট আর্মিওয়ার্ম (Spodoptera exigua), এবং আফ্রিকান আর্মিওয়ার্ম (Spodoptera exempta)।""",
            "harmful_effects": [
                "কয়েক দিনের মধ্যে ফসলের সম্পূর্ণ পাতার ক্ষতি",
                "হ্রাসিত সালোকসংশ্লেষণ যা বর্ধন বাধাগ্রস্ত করে",
                "শস্য ও ফলের সরাসরি ক্ষতি",
                "ফসল ব্যর্থতার কারণে অর্থনৈতিক ক্ষতি"
            ],
            "organic_solutions": [
                "নিম তেল স্প্রে: প্রতি লিটার জলে ৫ মিলি",
                "মরিচ-রসুনের নির্যাস: ১০০ গ্রাম মরিচ + ১০০ গ্রাম রসুন ১ লিটার জলে ব্লেন্ড করুন, ১:১০ পাতলা করুন",
                "ট্রাইকোগ্রামা ওয়াস্প: প্রতি হেক্টরে সাপ্তাহিক ৫০,০০০ ছাড়ুন",
                "পাখির বসার জায়গা: শিকারী পাখি আকর্ষণ করতে প্রতি হেক্টরে ১০-১৫টি ইনস্টল করুন"
            ],
            "chemical_pesticides": [
                "ক্লোরপাইরিফস ২০% EC: প্রতি লিটারে ২.৫ মিলি",
                "ল্যাম্বডা-সাইহ্যালোথ্রিন ৫% EC: প্রতি লিটারে ১ মিলি",
                "ইমামেকটিন বেনজোয়েট ৫% SG: প্রতি লিটারে ০.৫ গ্রাম",
                "স্পিনোসাড ৪৫% SC: প্রতি লিটারে ০.৩ মিলি"
            ],
            "prevention_methods": [
                "শীর্ষ সংক্রমণ সময় এড়াতে প্রাথমিক রোপণ",
                "সাপ্তাহিক দুইবার নিয়মিত ক্ষেত্র পর্যবেক্ষণ",
                "ফসলের অবশিষ্টাংশ সরিয়ে ক্ষেত্রের স্বাস্থ্যবিধি বজায় রাখুন",
                "ফেরোমোন ফাঁদ ব্যবহার করুন: প্রতি একরে ১০টি ফাঁদ"
            ]
        },
        "hindi": {
            "name": "आर्मीवर्म समूह",
            "description": """आर्मीवर्म ऐसे कैटरपिलर हैं जो बड़े समूहों में यात्रा करते हैं, घास, अनाज और अन्य फसलों पर भोजन करते हैं। उन्हें उनके व्यवहार से उनका नाम मिला है जैसे सेना की तरह समूहों में चलना, पूरे खेतों को तेजी से नष्ट करना। सामान्य प्रजातियों में फॉल आर्मीवर्म (Spodoptera frugiperda), बीट आर्मीवर्म (Spodoptera exigua), और अफ्रीकन आर्मीवर्म (Spodoptera exempta) शामिल हैं।""",
            "harmful_effects": [
                "कुछ ही दिनों में फसलों की पूरी पत्तियों की क्षति",
                "प्रकाश संश्लेषण कम होने से विकास अवरुद्ध होता है",
                "अनाज और फलों को सीधा नुकसान",
                "फसल विफलता के कारण आर्थिक नुकसान"
            ],
            "organic_solutions": [
                "नीम तेल स्प्रे: प्रति लीटर पानी में 5 मिली",
                "मिर्च-लहसुन का अर्क: 100 ग्राम मिर्च + 100 ग्राम लहसुन 1 लीटर पानी में ब्लेंड करें, 1:10 पतला करें",
                "ट्राइकोग्रामा ततैया: प्रति हेक्टेयर साप्ताहिक 50,000 छोड़ें",
                "पक्षी बैठने की जगह: शिकारी पक्षियों को आकर्षित करने के लिए प्रति हेक्टेयर 10-15 स्थापित करें"
            ],
            "chemical_pesticides": [
                "क्लोरपाइरिफोस 20% EC: प्रति लीटर 2.5 मिली",
                "लैम्ब्डा-साइहैलोथ्रिन 5% EC: प्रति लीटर 1 मिली",
                "इमामेक्टिन बेंजोएट 5% SG: प्रति लीटर 0.5 ग्राम",
                "स्पिनोसैड 45% SC: प्रति लीटर 0.3 मिली"
            ],
            "prevention_methods": [
                "शीर्ष संक्रमण अवधि से बचने के लिए प्रारंभिक रोपण",
                "साप्ताहिक दो बार नियमित खेत निगरानी",
                "फसल अवशेषों को हटाकर खेत की स्वच्छता बनाए रखें",
                "फेरोमोन जाल का उपयोग करें: प्रति एकड़ 10 जाल"
            ]
        }
    },

    "Corn Worms Group": {
        "english": {
            "name": "Corn Worms Group",
            "description": """Corn worms are larvae of various moth species that infest corn and other cereal crops. Major pests include European Corn Borer (Ostrinia nubilalis), Corn Earworm (Helicoverpa zea), and Southwestern Corn Borer (Diatraea grandiosella). These pests bore into stems, ears, and kernels, causing significant yield loss.""",
            "harmful_effects": [
                "Tunnel damage in stems leading to plant lodging",
                "Direct feeding on kernels reducing grain quality",
                "Secondary fungal infections through entry holes",
                "Up to 40% yield reduction in severe infestations"
            ],
            "organic_solutions": [
                "Bacillus thuringiensis (Bt) spray: 2g per liter",
                "Diatomaceous earth: Apply 20kg per acre",
                "Marigold intercropping: Plant every 5th row",
                "Chrysoperla carnea release: 10,000 per acre"
            ],
            "chemical_pesticides": [
                "Carbaryl 50% WP: 2g per liter",
                "Deltamethrin 2.8% EC: 1ml per liter",
                "Cypermethrin 25% EC: 1ml per liter",
                "Chlorantraniliprole 18.5% SC: 0.3ml per liter"
            ],
            "prevention_methods": [
                "Deep plowing after harvest to expose pupae",
                "Use Bt corn varieties",
                "Destroy crop residues within 15 days of harvest",
                "Install light traps: 1 per acre"
            ]
        },
        "bangla": {
            "name": "কর্ন ওয়ার্ম গ্রুপ",
            "description": """কর্ন ওয়ার্ম হল বিভিন্ন প্রজাপতি প্রজাতির লার্ভা যা ভুট্টা এবং অন্যান্য শস্য ফসলে আক্রমণ করে। প্রধান পোকামাকড়ের মধ্যে রয়েছে ইউরোপীয় কর্ন বোরার (Ostrinia nubilalis), কর্ন ইয়ারওয়ার্ম (Helicoverpa zea), এবং সাউথওয়েস্টার্ন কর্ন বোরার (Diatraea grandiosella)। এই পোকামাকড়গুলি কাণ্ড, কান এবং শস্যদানায় সুড়ঙ্গের ক্ষতি করে, উল্লেখযোগ্য ফলন হ্রাস ঘটায়।""",
            "harmful_effects": [
                "কাণ্ডে সুড়ঙ্গের ক্ষতি যা গাছের পড়ে যাওয়ার কারণ হয়",
                "শস্যদানায় সরাসরি খাওয়ানো যা শস্যের গুণমান হ্রাস করে",
                "প্রবেশ গর্তের মাধ্যমে মাধ্যমিক ছত্রাক সংক্রমণ",
                "গুরুতর সংক্রমণে ৪০% পর্যন্ত ফলন হ্রাস"
            ],
            "organic_solutions": [
                "ব্যাসিলাস থুরিঞ্জিয়েনসিস (বিটি) স্প্রে: প্রতি লিটারে ২ গ্রাম",
                "ডায়াটমেসিয়াস আর্থ: প্রতি একরে ২০ কেজি প্রয়োগ করুন",
                "গাঁদা আন্তঃফসল: প্রতি ৫ম সারিতে রোপণ করুন",
                "ক্রাইসোপেরলা কার্নিয়া মুক্ত করুন: প্রতি একরে ১০,০০০"
            ],
            "chemical_pesticides": [
                "কারবারিল ৫০% WP: প্রতি লিটারে ২ গ্রাম",
                "ডেল্টামেথ্রিন ২.৮% EC: প্রতি লিটারে ১ মিলি",
                "সাইপারমেথ্রিন ২৫% EC: প্রতি লিটারে ১ মিলি",
                "ক্লোরান্ট্রানিলিপ্রোল ১৮.৫% SC: প্রতি লিটারে ০.৩ মিলি"
            ],
            "prevention_methods": [
                "ফসল কাটার পর পিউপা প্রকাশ করার জন্য গভীর চাষ",
                "বিটি ভুট্টা জাত ব্যবহার করুন",
                "ফসল কাটার ১৫ দিনের মধ্যে ফসলের অবশিষ্টাংশ ধ্বংস করুন",
                "আলোর ফাঁদ ইনস্টল করুন: প্রতি একরে ১টি"
            ]
        },
        "hindi": {
            "name": "कॉर्न वर्म समूह",
            "description": """कॉर्न वर्म विभिन्न पतंगे प्रजातियों के लार्वा हैं जो मक्का और अन्य अनाज फसलों को संक्रमित करते हैं। प्रमुख कीटों में यूरोपीय कॉर्न बोरर (Ostrinia nubilalis), कॉर्न इयरवर्म (Helicoverpa zea), और दक्षिण-पश्चिमी कॉर्न बोरर (Diatraea grandiosella) शामिल हैं। ये कीट तनों, कानों और दानों में सुरंग बनाते हैं, जिससे उपज में उल्लेखनीय कमी आती है।""",
            "harmful_effects": [
                "तनों में सुरंग क्षति से पौधे गिर जाते हैं",
                "दानों पर सीधा भोजन करने से अनाज की गुणवत्ता कम होती है",
                "प्रवेश छिद्रों के माध्यम से द्वितीयक कवक संक्रमण",
                "गंभीर संक्रमण में ४०% तक उपज में कमी"
            ],
            "organic_solutions": [
                "बैसिलस थुरिंजिएंसिस (बीटी) स्प्रे: प्रति लीटर २ ग्राम",
                "डायटोमेशियस अर्थ: प्रति एकड़ २० किलोग्राम लगाएं",
                "गेंदा अंतरफसल: हर ५वीं पंक्ति में लगाएं",
                "क्राइसोपेरला कार्निया छोड़ें: प्रति एकड़ १०,०००"
            ],
            "chemical_pesticides": [
                "कार्बेरिल ५०% WP: प्रति लीटर २ ग्राम",
                "डेल्टामेथ्रिन २.८% EC: प्रति लीटर १ मिली",
                "साइपरमेथ्रिन २५% EC: प्रति लीटर १ मिली",
                "क्लोरेंट्रानिलिप्रोल १८.५% SC: प्रति लीटर ०.३ मिली"
            ],
            "prevention_methods": [
                "फसल काटने के बाद प्यूपा उजागर करने के लिए गहरी जुताई",
                "बीटी मक्का किस्मों का उपयोग करें",
                "फसल कटाई के १५ दिनों के भीतर फसल अवशेष नष्ट करें",
                "प्रकाश जाल स्थापित करें: प्रति एकड़ १"
            ]
        }
    },

    "Small Sap-Sucking Pests": {
        "english": {
            "name": "Small Sap-Sucking Pests",
            "description": """This group includes aphids, whiteflies, leafhoppers, thrips, and mealybugs that feed on plant sap. They have piercing-sucking mouthparts and can transmit viral diseases while feeding. Common examples include Green Peach Aphid (Myzus persicae), Cotton Whitefly (Bemisia tabaci), and Rice Brown Planthopper (Nilaparvata lugens).""",
            "harmful_effects": [
                "Yellowing and curling of leaves",
                "Honeydew secretion leading to sooty mold",
                "Transmission of viral diseases",
                "Stunted plant growth and reduced vigor"
            ],
            "organic_solutions": [
                "Soap-water spray: 10ml soap per liter",
                "Neem oil: 3ml per liter with soap",
                "Ladybug release: 5,000 per hectare",
                "Reflective mulches to deter pests"
            ],
            "chemical_pesticides": [
                "Imidacloprid 17.8% SL: 0.5ml per liter",
                "Acetamiprid 20% SP: 0.5g per liter",
                "Thiamethoxam 25% WG: 0.3g per liter",
                "Buprofezin 25% SC: 1ml per liter"
            ],
            "prevention_methods": [
                "Use yellow sticky traps: 10-15 per acre",
                "Remove weed hosts regularly",
                "Maintain proper plant spacing",
                "Avoid excessive nitrogen fertilization"
            ]
        },
        "bangla": {
            "name": "ছোট স্যাপ-সাকিং পেস্ট",
            "description": """এই গ্রুপে এফিড, হোয়াইটফ্লাই, লিফহপার, থ্রিপস এবং মিলিবাগ অন্তর্ভুক্ত রয়েছে যা গাছের রস খায়। তাদের ছিদ্র-চোষার মুখের অংশ রয়েছে এবং খাওয়ার সময় ভাইরাল রোগ সংক্রমণ করতে পারে। সাধারণ উদাহরণগুলির মধ্যে রয়েছে গ্রীন পিচ এফিড (Myzus persicae), কটন হোয়াইটফ্লাই (Bemisia tabaci), এবং রাইস ব্রাউন প্ল্যানথপার (Nilaparvata lugens)।""",
            "harmful_effects": [
                "পাতার হলুদ হয়ে যাওয়া এবং কুঁচকানো",
                "হানিডিউ সিক্রেশন যা সুটি মোল্ডের দিকে নিয়ে যায়",
                "ভাইরাল রোগ সংক্রমণ",
                "গাছের বৃদ্ধি ব্যাহত এবং শক্তি হ্রাস"
            ],
            "organic_solutions": [
                "সাবান-পানির স্প্রে: প্রতি লিটারে ১০ মিলি সাবান",
                "নিম তেল: সাবান সহ প্রতি লিটারে ৩ মিলি",
                "লেডিবাগ মুক্ত করুন: প্রতি হেক্টরে ৫,০০০",
                "পোকামাকড় নিরুৎসাহিত করতে প্রতিফলিত মালচ"
            ],
            "chemical_pesticides": [
                "ইমিডাক্লোপ্রিড ১৭.৮% SL: প্রতি লিটারে ০.৫ মিলি",
                "এসিটামিপ্রিড ২০% SP: প্রতি লিটারে ০.৫ গ্রাম",
                "থায়ামেথোক্সাম ২৫% WG: প্রতি লিটারে ০.৩ গ্রাম",
                "বুপ্রোফেজিন ২৫% SC: প্রতি লিটারে ১ মিলি"
            ],
            "prevention_methods": [
                "হলুদ স্টিকি ফাঁদ ব্যবহার করুন: প্রতি একরে ১০-১৫টি",
                "নিয়মিত আগাছা হোস্ট সরান",
                "উপযুক্ত গাছের ব্যবধান বজায় রাখুন",
                "অতিরিক্ত নাইট্রোজেন সারের ব্যবহার এড়িয়ে চলুন"
            ]
        },
        "hindi": {
            "name": "छोटे सैप-चूसने वाले कीट",
            "description": """इस समूह में एफिड्स, व्हाइटफ्लाइज़, लीफहॉपर्स, थ्रिप्स और मीलीबग्स शामिल हैं जो पौधों के रस पर भोजन करते हैं। इनमें छेदने-चूसने वाले मुखांग होते हैं और भोजन करते समय वायरल रोग संचारित कर सकते हैं। सामान्य उदाहरणों में ग्रीन पीच एफिड (Myzus persicae), कपास व्हाइटफ्लाई (Bemisia tabaci), और धान भूरे प्लांथॉपर (Nilaparvata lugens) शामिल हैं।""",
            "harmful_effects": [
                "पत्तियों का पीला पड़ना और मुड़ना",
                "हनीड्यू स्राव से काली फफूंदी",
                "वायरल रोगों का संचरण",
                "पौधे की वृद्धि अवरुद्ध और शक्ति कम"
            ],
            "organic_solutions": [
                "साबुन-पानी का स्प्रे: प्रति लीटर १० मिली साबुन",
                "नीम तेल: साबुन के साथ प्रति लीटर ३ मिली",
                "लेडीबग छोड़ें: प्रति हेक्टेयर ५,०००",
                "कीटों को रोकने के लिए परावर्तक मल्च"
            ],
            "chemical_pesticides": [
                "इमिडाक्लोप्रिड १७.८% SL: प्रति लीटर ०.५ मिली",
                "एसिटामिप्रिड २०% SP: प्रति लीटर ०.५ ग्राम",
                "थायामेथोक्साम २५% WG: प्रति लीटर ०.३ ग्राम",
                "बुप्रोफेजिन २५% SC: प्रति लीटर १ मिली"
            ],
            "prevention_methods": [
                "पीले चिपचिपे जाल का उपयोग करें: प्रति एकड़ १०-१५",
                "नियमित रूप से खरपतवार होस्ट हटाएं",
                "उचित पौधे की दूरी बनाए रखें",
                "अत्यधिक नाइट्रोजन उर्वरक से बचें"
            ]
        }
    },

    "Africanized Honey Bees (Killer Bees)": {
        "english": {
            "name": "Africanized Honey Bees (Killer Bees)",
            "description": """Africanized honey bees, also known as killer bees, are hybrid honey bees resulting from crossbreeding between African honey bees and European honey bees. They are more defensive and aggressive than European honey bees, attacking in larger numbers when threatened. Their venom is not more potent, but they attack in greater numbers.""",
            "harmful_effects": [
                "Aggressive attacks on humans and animals",
                "Displacement of native bee populations",
                "Reduced honey production in some areas",
                "Risk to agricultural workers and livestock"
            ],
            "organic_solutions": [
                "Smoke to calm bees during removal",
                "Vinegar-water solution as deterrent",
                "Natural repellents like citronella",
                "Professional beekeeper assistance"
            ],
            "chemical_pesticides": [
                "Carbaryl 5% dust for nest elimination",
                "Pyrethrin sprays for emergency control",
                "Permethrin for professional use only",
                "Diazinon for agricultural settings"
            ],
            "prevention_methods": [
                "Seal potential nesting sites",
                "Regular property inspections",
                "Keep food sources covered",
                "Avoid strong perfumes and dark clothing"
            ]
        },
        "bangla": {
            "name": "আফ্রিকানাইজড হানি বিস (কিলার বিস)",
            "description": """আফ্রিকানাইজড হানি মধু মৌমাছি, যাকে কিলার মৌমাছিও বলা হয়, আফ্রিকান মধু মৌমাছি এবং ইউরোপীয় মধু মৌমাছির মধ্যে ক্রসব্রিডিং থেকে উদ্ভূত হাইব্রিড মধু মৌমাছি। তারা ইউরোপীয় মধু মৌমাছির চেয়ে বেশি প্রতিরক্ষামূলক এবং আক্রমণাত্মক, হুমকির সময় বড় সংখ্যায় আক্রমণ করে। তাদের বিষ আরও শক্তিশালী নয়, তবে তারা বেশি সংখ্যায় আক্রমণ করে।""",
            "harmful_effects": [
                "মানুষ এবং প্রাণীদের উপর আক্রমণাত্মক আক্রমণ",
                "দেশীয় মৌমাছি জনসংখ্যার স্থানচ্যুতি",
                "কিছু এলাকায় মধু উৎপাদন হ্রাস",
                "কৃষি শ্রমিক এবং পশুসম্পদের জন্য ঝুঁকি"
            ],
            "organic_solutions": [
                "অপসারণের সময় মৌমাছি শান্ত করার জন্য ধোঁয়া",
                "নিবারক হিসাবে ভিনেগার-জল দ্রবণ",
                "সিট্রোনেলা মত প্রাকৃতিক নিবারক",
                "পেশাদার মৌমাছি পালনকারীর সাহায্য"
            ],
            "chemical_pesticides": [
                "বাসা নির্মূলের জন্য কারবারিল ৫% ধূলিকণা",
                "জরুরী নিয়ন্ত্রণের জন্য পাইরেথ্রিন স্প্রে",
                "শুধুমাত্র পেশাদার ব্যবহারের জন্য পারমেথ্রিন",
                "কৃষি সেটিংসের জন্য ডায়াজিনন"
            ],
            "prevention_methods": [
                "সম্ভাব্য বাসা বাঁধার স্থান সিল করুন",
                "নিয়মিত সম্পত্তি পরিদর্শন",
                "খাদ্যের উৎস ঢেকে রাখুন",
                "শক্তিশালী সুগন্ধি এবং কালো পোশাক এড়িয়ে চলুন"
            ]
        },
        "hindi": {
            "name": "अफ्रीकीकृत मधुमक्खियाँ (किलर मधुमक्खियाँ)",
            "description": """अफ्रीकीकृत मधुमक्खियाँ, जिन्हें किलर मधुमक्खियाँ भी कहा जाता है, अफ्रीकी मधुमक्खियों और यूरोपीय मधुमक्खियों के बीच क्रॉसब्रीडिंग से उत्पन्न संकर मधुमक्खियाँ हैं। वे यूरोपीय मधुमक्खियों की तुलना में अधिक रक्षात्मक और आक्रामक हैं, खतरे के समय बड़ी संख्या में हमला करती हैं। उनका जहर अधिक शक्तिशाली नहीं है, लेकिन वे अधिक संख्या में हमला करती हैं।""",
            "harmful_effects": [
                "मनुष्यों और जानवरों पर आक्रामक हमले",
                "देशी मधुमक्खी आबादी का विस्थापन",
                "कुछ क्षेत्रों में शहद उत्पादन कम",
                "कृषि श्रमिकों और पशुधन के लिए जोखिम"
            ],
            "organic_solutions": [
                "निकालने के दौरान मधुमक्खियों को शांत करने के लिए धुआं",
                "निवारक के रूप में सिरका-पानी का घोल",
                "सिट्रोनेला जैसे प्राकृतिक निवारक",
                "पेशेवर मधुमक्खी पालक सहायता"
            ],
            "chemical_pesticides": [
                "घोंसला समाप्ति के लिए कार्बेरिल ५% धूल",
                "आपातकालीन नियंत्रण के लिए पाइरेथ्रिन स्प्रे",
                "केवल पेशेवर उपयोग के लिए परमेथ्रिन",
                "कृषि सेटिंग्स के लिए डायजिनॉन"
            ],
            "prevention_methods": [
                "संभावित घोंसले के शिकार स्थलों को सील करें",
                "नियमित संपत्ति निरीक्षण",
                "भोजन के स्रोतों को ढक कर रखें",
                "तीव्र इत्र और काले कपड़े से बचें"
            ]
        }
    },

    "Brown Marmorated Stink Bugs": {
        "english": {
            "name": "Brown Marmorated Stink Bugs",
            "description": """The Brown Marmorated Stink Bug (Halyomorpha halys) is an invasive pest native to Asia that has spread to North America and Europe. It feeds on a wide range of fruits, vegetables, and ornamental plants, causing cosmetic damage and crop loss. Adults are shield-shaped, about 17mm long, with brown marbled coloration.""",
            "harmful_effects": [
                "Cat-facing on fruits (deformities)",
                "Early fruit drop in orchards",
                "Transmission of plant pathogens",
                "Nuisance in homes during winter"
            ],
            "organic_solutions": [
                "Kaolin clay spray: 3% solution",
                "Garlic-pepper spray: 100g each in 1L water",
                "Diatomaceous earth around plants",
                "Vacuum collection in homes"
            ],
            "chemical_pesticides": [
                "Bifenthrin 10% EC: 1ml per liter",
                "Lambda-cyhalothrin 5% CS: 1ml per liter",
                "Acetamiprid 20% SP: 0.5g per liter",
                "Dinotefuran 20% SG: 0.5g per liter"
            ],
            "prevention_methods": [
                "Seal cracks and crevices in buildings",
                "Use row covers for vegetables",
                "Remove weed hosts near crops",
                "Install bug zappers near orchards"
            ]
        },
        "bangla": {
            "name": "ব্রাউন মারমোরেটেড স্টিঙ্ক বাগস",
            "description": """ব্রাউন মারমোরেটেড স্টিঙ্ক বাগ (Halyomorpha halys) এশিয়ার স্থানীয় একটি আক্রমণাত্মক পোকা যা উত্তর আমেরিকা এবং ইউরোপে ছড়িয়ে পড়েছে। এটি বিভিন্ন ধরনের ফল, সবজি এবং সজ্জা গাছপালা খায়, সৌন্দর্য ক্ষতি এবং ফসলের ক্ষতি করে। প্রাপ্তবয়স্করা ঢালের আকারের, প্রায় ১৭ মিমি লম্বা, বাদামী মার্বেল রঙের।""",
            "harmful_effects": [
                "ফলের উপর বিড়াল-মুখী (বিকৃতি)",
                "বাগানে প্রাথমিক ফল পড়া",
                "গাছের রোগজীবাণু সংক্রমণ",
                "শীতে ঘরে বিরক্তি"
            ],
            "organic_solutions": [
                "কাওলিন কাদামাটি স্প্রে: ৩% দ্রবণ",
                "রসুন-মরিচ স্প্রে: ১ লিটার জলে প্রতিটি ১০০ গ্রাম",
                "গাছের চারপাশে ডায়াটমেসিয়াস আর্থ",
                "ঘরে ভ্যাকুয়াম সংগ্রহ"
            ],
            "chemical_pesticides": [
                "বিফেনথ্রিন ১০% EC: প্রতি লিটারে ১ মিলি",
                "ল্যাম্বডা-সাইহ্যালোথ্রিন ৫% CS: প্রতি লিটারে ১ মিলি",
                "এসিটামিপ্রিড ২০% SP: প্রতি লিটারে ০.৫ গ্রাম",
                "ডাইনোটেফুরান ২০% SG: প্রতি লিটারে ০.৫ গ্রাম"
            ],
            "prevention_methods": [
                "ভবনে ফাটল এবং চিড় সিল করুন",
                "সবজির জন্য সারি কভার ব্যবহার করুন",
                "ফসলের কাছাকাছি আগাছা হোস্ট সরান",
                "বাগানের কাছে বাগ জ্যাপার ইনস্টল করুন"
            ]
        },
        "hindi": {
            "name": "ब्राउन मार्बल्ड स्टिंक बग",
            "description": """ब्राउन मार्बल्ड स्टिंक बग (Halyomorpha halys) एशिया का एक आक्रामक कीट है जो उत्तर अमेरिका और यूरोप में फैल गया है। यह विभिन्न प्रकार के फलों, सब्जियों और सजावटी पौधों पर भोजन करता है, सौंदर्य क्षति और फसल हानि का कारण बनता है। वयस्क ढाल के आकार के, लगभग १७ मिमी लंबे, भूरे संगमरमर के रंग के होते हैं।""",
            "harmful_effects": [
                "फलों पर बिल्ली का चेहरा (विकृति)",
                "बागों में जल्दी फल गिरना",
                "पौधे के रोगजनकों का संचरण",
                "सर्दियों में घरों में परेशानी"
            ],
            "organic_solutions": [
                "काओलिन मिट्टी स्प्रे: ३% घोल",
                "लहसुन-मिर्च स्प्रे: १ लीटर पानी में प्रत्येक १०० ग्राम",
                "पौधों के आसपास डायटोमेशियस अर्थ",
                "घरों में वैक्यूम संग्रह"
            ],
            "chemical_pesticides": [
                "बिफेंथ्रिन १०% EC: प्रति लीटर १ मिली",
                "लैम्ब्डा-साइहैलोथ्रिन ५% CS: प्रति लीटर १ मिली",
                "एसिटामिप्रिड २०% SP: प्रति लीटर ०.५ ग्राम",
                "डायनोटेफुरान २०% SG: प्रति लीटर ०.५ ग्राम"
            ],
            "prevention_methods": [
                "इमारतों में दरारें और दरारें सील करें",
                "सब्जियों के लिए पंक्ति कवर का उपयोग करें",
                "फसलों के पास खरपतवार होस्ट हटाएं",
                "बागों के पास बग जैपर स्थापित करें"
            ]
        }
    },

    "Cabbage Loopers": {
        "english": {
            "name": "Cabbage Loopers",
            "description": """Cabbage Loopers (Trichoplusia ni) are green caterpillars that feed on cruciferous vegetables like cabbage, broccoli, and cauliflower. They are called 'loopers' because of their distinctive looping movement. The adult is a mottled brown moth with a silver figure-eight marking on the forewings.""",
            "harmful_effects": [
                "Irregular holes in leaves",
                "Contamination of harvest with frass",
                "Reduced market quality of vegetables",
                "Complete defoliation in severe cases"
            ],
            "organic_solutions": [
                "Bt (Bacillus thuringiensis) spray: 2g/L",
                "Spinosad: 1ml per liter",
                "Handpicking in small gardens",
                "Floating row covers"
            ],
            "chemical_pesticides": [
                "Chlorpyrifos 20% EC: 2.5ml/L",
                "Cypermethrin 10% EC: 1ml/L",
                "Indoxacarb 15% SC: 0.5ml/L",
                "Emamectin benzoate 5% SG: 0.4g/L"
            ],
            "prevention_methods": [
                "Crop rotation with non-host plants",
                "Regular field scouting",
                "Destruction of crop residues",
                "Use of pheromone traps"
            ]
        },
        "bangla": {
            "name": "ক্যাবেজ লুপার্স",
            "description": """ক্যাবেজ লুপার্স (Trichoplusia ni) সবুজ শুঁয়োপোকা যা ক্যাবেজ, ব্রোকলি এবং ফুলকপির মতো ক্রুসিফেরাস শাকসবজি খায়। তাদের স্বতন্ত্র লুপিং আন্দোলনের কারণে তাদের 'লুপার্স' বলা হয়। প্রাপ্তবয়স্ক একটি বিচিত্র বাদামী মথ যার সামনের ডানায় একটি রূপালী চিত্র-আট চিহ্ন রয়েছে।""",
            "harmful_effects": [
                "পাতায় অনিয়মিত গর্ত",
                "ফ্রাস দিয়ে ফসল দূষণ",
                "শাকসবজির বাজার গুণমান হ্রাস",
                "গুরুতর ক্ষেত্রে সম্পূর্ণ পাতার ক্ষতি"
            ],
            "organic_solutions": [
                "বিটি (ব্যাসিলাস থুরিঞ্জিয়েনসিস) স্প্রে: ২ গ্রাম/লিটার",
                "স্পিনোসাড: প্রতি লিটারে ১ মিলি",
                "ছোট বাগানে হাত দিয়ে সংগ্রহ",
                "ভাসমান সারি কভার"
            ],
            "chemical_pesticides": [
                "ক্লোরপাইরিফস ২০% EC: ২.৫ মিলি/লিটার",
                "সাইপারমেথ্রিন ১০% EC: ১ মিলি/লিটার",
                "ইন্ডোক্সাকার্ব ১৫% SC: ০.৫ মিলি/লিটার",
                "ইমামেকটিন বেনজোয়েট ৫% SG: ০.৪ গ্রাম/লিটার"
            ],
            "prevention_methods": [
                "অ-হোস্ট গাছপালা সহ ফসলের আবর্তন",
                "নিয়মিত ক্ষেত্র স্কাউটিং",
                "ফসলের অবশিষ্টাংশ ধ্বংস",
                "ফেরোমোন ফাঁদ ব্যবহার"
            ]
        },
        "hindi": {
            "name": "गोभी लूपर्स",
            "description": """गोभी लूपर्स (Trichoplusia ni) हरे कैटरपिलर हैं जो गोभी, ब्रोकोली और फूलगोभी जैसी क्रूसिफेरस सब्जियों पर भोजन करते हैं। उन्हें उनकी विशिष्ट लूपिंग गति के कारण 'लूपर्स' कहा जाता है। वयस्क एक चित्तीदार भूरी पतंगी है जिसके अगले पंखों पर एक चाँदी का आठ-आकार का निशान होता है।""",
            "harmful_effects": [
                "पत्तियों में अनियमित छेद",
                "फ्रास से फसल दूषित होना",
                "सब्जियों की बाजार गुणवत्ता कम",
                "गंभीर मामलों में पूरी तरह से पत्तियों का नुकसान"
            ],
            "organic_solutions": [
                "बीटी (बैसिलस थुरिंजिएंसिस) स्प्रे: २ ग्राम/लीटर",
                "स्पिनोसैड: प्रति लीटर १ मिली",
                "छोटे बगीचों में हाथ से चुनना",
                "फ्लोटिंग रो कवर"
            ],
            "chemical_pesticides": [
                "क्लोरपाइरिफोस २०% EC: २.५ मिली/लीटर",
                "साइपरमेथ्रिन १०% EC: १ मिली/लीटर",
                "इंडोक्साकार्ब १५% SC: ०.५ मिली/लीटर",
                "इमामेक्टिन बेंजोएट ५% SG: ०.४ ग्राम/लीटर"
            ],
            "prevention_methods": [
                "गैर-होस्ट पौधों के साथ फसल चक्र",
                "नियमित खेत स्काउटिंग",
                "फसल अवशेषों का विनाश",
                "फेरोमोन जाल का उपयोग"
            ]
        }
    },

    "Citrus Canker": {
        "english": {
            "name": "Citrus Canker",
            "description": """Citrus canker is a bacterial disease caused by Xanthomonas citri subsp. citri. It affects all citrus cultivars and causes raised, corky lesions on leaves, stems, and fruit. The disease spreads through wind-driven rain, irrigation water, and human activities.""",
            "harmful_effects": [
                "Premature fruit drop",
                "Reduced fruit quality and marketability",
                "Defoliation and twig dieback",
                "Economic losses in citrus industry"
            ],
            "organic_solutions": [
                "Copper-based sprays: Bordeaux mixture",
                "Streptomycin for bacterial control",
                "Sanitation: Remove infected plant parts",
                "Windbreaks to reduce spread"
            ],
            "chemical_pesticides": [
                "Copper hydroxide 77% WP: 3g/L",
                "Copper oxychloride 50% WP: 4g/L",
                "Kasugamycin 2% SL: 2ml/L",
                "Streptomycin sulfate 9% SP: 1g/L"
            ],
            "prevention_methods": [
                "Use disease-free planting material",
                "Avoid overhead irrigation",
                "Disinfect pruning tools",
                "Quarantine new plantings"
            ]
        },
        "bangla": {
            "name": "সাইট্রাস ক্যানকার",
            "description": """সাইট্রাস ক্যানকার একটি ব্যাকটেরিয়া রোগ যা Xanthomonas citri subsp. দ্বারা সৃষ্ট। সাইট্রি। এটি সমস্ত সাইট্রাস জাতকে প্রভাবিত করে এবং পাতায়, কান্ডে এবং ফলে উত্থিত, কর্কি ক্ষত সৃষ্টি করে। রোগটি বাতাসে চালিত বৃষ্টি, সেচের জল এবং মানুষের কার্যকলাপের মাধ্যমে ছড়ায়।""",
            "harmful_effects": [
                "অকালে ফল পড়া",
                "ফলের গুণমান এবং বিপণনযোগ্যতা হ্রাস",
                "পাতার ক্ষতি এবং ডাল মারা যাওয়া",
                "সাইট্রাস শিল্পে অর্থনৈতিক ক্ষতি"
            ],
            "organic_solutions": [
                "তামা-ভিত্তিক স্প্রে: বোর্দো মিশ্রণ",
                "ব্যাকটেরিয়া নিয়ন্ত্রণের জন্য স্ট্রেপ্টোমাইসিন",
                "স্বাস্থ্যবিধি: সংক্রমিত গাছের অংশগুলি সরান",
                "ছড়িয়ে পড়া কমাতে বাতাস আটকানো"
            ],
            "chemical_pesticides": [
                "কপার হাইড্রক্সাইড ৭৭% WP: ৩ গ্রাম/লিটার",
                "কপার অক্সিক্লোরাইড ৫০% WP: ৪ গ্রাম/লিটার",
                "কাসুগামাইসিন ২% SL: ২ মিলি/লিটার",
                "স্ট্রেপ্টোমাইসিন সালফেট ৯% SP: ১ গ্রাম/লিটার"
            ],
            "prevention_methods": [
                "রোগমুক্ত রোপণ উপাদান ব্যবহার করুন",
                "ওভারহেড সেচ এড়িয়ে চলুন",
                "ছাঁটাইয়ের সরঞ্জাম জীবাণুমুক্ত করুন",
                "নতুন রোপণ কোয়ারেন্টাইন"
            ]
        },
        "hindi": {
            "name": "सिट्रस कैंकर",
            "description": """सिट्रस कैंकर Xanthomonas citri subsp. के कारण होने वाला एक जीवाणु रोग है। सिट्री। यह सभी सिट्रस किस्मों को प्रभावित करता है और पत्तियों, तनों और फलों पर उभरे हुए, कॉर्की घाव पैदा करता है। बीमारी हवा से चलने वाली बारिश, सिंचाई के पानी और मानव गतिविधियों के माध्यम से फैलती है।""",
            "harmful_effects": [
                "समय से पहले फल गिरना",
                "फल की गुणवत्ता और विपणन क्षमता कम",
                "पत्तियों का नुकसान और टहनी मरना",
                "सिट्रस उद्योग में आर्थिक नुकसान"
            ],
            "organic_solutions": [
                "तांबा आधारित स्प्रे: बोर्डो मिश्रण",
                "जीवाणु नियंत्रण के लिए स्ट्रेप्टोमाइसिन",
                "स्वच्छता: संक्रमित पौधे के भाग हटाएं",
                "फैलने को कम करने के लिए विंडब्रेक"
            ],
            "chemical_pesticides": [
                "कॉपर हाइड्रॉक्साइड ७७% WP: ३ ग्राम/लीटर",
                "कॉपर ऑक्सीक्लोराइड ५०% WP: ४ ग्राम/लीटर",
                "कासुगामाइसिन २% SL: २ मिली/लीटर",
                "स्ट्रेप्टोमाइसिन सल्फेट ९% SP: १ ग्राम/लीटर"
            ],
            "prevention_methods": [
                "रोगमुक्त रोपण सामग्री का उपयोग करें",
                "ओवरहेड सिंचाई से बचें",
                "प्रूनिंग टूल्स को कीटाणुरहित करें",
                "नए रोपण को क्वारंटाइन करें"
            ]
        }
    },

    "Colorado Potato Beetles": {
        "english": {
            "name": "Colorado Potato Beetles",
            "description": """The Colorado potato beetle (Leptinotarsa decemlineata) is a major pest of potato crops worldwide. Both adults and larvae feed on potato foliage, and heavy infestations can completely defoliate plants. Adults are yellow with 10 black stripes on their wing covers.""",
            "harmful_effects": [
                "Complete defoliation of potato plants",
                "Reduced tuber size and yield",
                "Increased susceptibility to diseases",
                "Economic losses in potato production"
            ],
            "organic_solutions": [
                "Neem oil spray: 5ml/L with soap",
                "Diatomaceous earth around plants",
                "Crop rotation with non-solanaceous crops",
                "Handpicking in small plots"
            ],
            "chemical_pesticides": [
                "Imidacloprid 17.8% SL: 0.3ml/L",
                "Thiamethoxam 25% WG: 0.2g/L",
                "Chlorpyrifos 20% EC: 2ml/L",
                "Spinosad 45% SC: 0.4ml/L"
            ],
            "prevention_methods": [
                "Deep plowing to expose overwintering beetles",
                "Use of floating row covers",
                "Early planting to avoid peak populations",
                "Destruction of volunteer potatoes"
            ]
        },
        "bangla": {
            "name": "কলোরাডো পটেটো বিটল",
            "description": """কলোরাডো আলু বিটল (Leptinotarsa decemlineata) বিশ্বব্যাপী আলু ফসলের একটি প্রধান কীট। প্রাপ্তবয়স্ক এবং লার্ভা উভয়ই আলুর পাতার উপর খাবার খায়, এবং ভারী সংক্রমণ সম্পূর্ণরূপে গাছের পাতার ক্ষতি করতে পারে। প্রাপ্তবয়স্করা হলুদ রঙের হয় যাদের ডানার কভারে ১০টি কালো দাগ রয়েছে।""",
            "harmful_effects": [
                "আলু গাছের সম্পূর্ণ পাতার ক্ষতি",
                "কন্দের আকার এবং ফলন হ্রাস",
                "রোগের প্রতি সংবেদনশীলতা বৃদ্ধি",
                "আলু উৎপাদনে অর্থনৈতিক ক্ষতি"
            ],
            "organic_solutions": [
                "নিম তেল স্প্রে: সাবান সহ ৫ মিলি/লিটার",
                "গাছের চারপাশে ডায়াটমেসিয়াস আর্থ",
                "অ-সলানাসিয়াস ফসল সহ ফসল আবর্তন",
                "ছোট জমিতে হাত দিয়ে সংগ্রহ"
            ],
            "chemical_pesticides": [
                "ইমিডাক্লোপ্রিড ১৭.৮% SL: ০.৩ মিলি/লিটার",
                "থায়ামেথোক্সাম ২৫% WG: ০.২ গ্রাম/লিটার",
                "ক্লোরপাইরিফস ২০% EC: ২ মিলি/লিটার",
                "স্পিনোসাড ৪৫% SC: ০.৪ মিলি/লিটার"
            ],
            "prevention_methods": [
                "শীতকালীন বিটল প্রকাশ করার জন্য গভীর চাষ",
                "ভাসমান সারি কভার ব্যবহার",
                "শীর্ষ জনসংখ্যা এড়াতে প্রাথমিক রোপণ",
                "স্বেচ্ছাসেবী আলু ধ্বংস"
            ]
        },
        "hindi": {
            "name": "कोलोराडो आलू बीटल",
            "description": """कोलोराडो आलू बीटल (Leptinotarsa decemlineata) दुनिया भर में आलू की फसल का एक प्रमुख कीट है। वयस्क और लार्वा दोनों आलू की पत्तियों पर भोजन करते हैं, और भारी संक्रमण पौधों की पत्तियों को पूरी तरह से नष्ट कर सकता है। वयस्क पीले रंग के होते हैं जिनके पंखों के कवर पर १० काले धारियाँ होती हैं।""",
            "harmful_effects": [
                "आलू के पौधों की पूरी तरह से पत्तियों का नुकसान",
                "कंद का आकार और उपज कम",
                "रोगों के प्रति संवेदनशीलता बढ़ी",
                "आलू उत्पादन में आर्थिक नुकसान"
            ],
            "organic_solutions": [
                "नीम तेल स्प्रे: साबुन के साथ ५ मिली/लीटर",
                "पौधों के आसपास डायटोमेशियस अर्थ",
                "गैर-सोलानेशियस फसलों के साथ फसल चक्र",
                "छोटे भूखंडों में हाथ से चुनना"
            ],
            "chemical_pesticides": [
                "इमिडाक्लोप्रिड १७.८% SL: ०.३ मिली/लीटर",
                "थायामेथोक्साम २५% WG: ०.२ ग्राम/लीटर",
                "क्लोरपाइरिफोस २०% EC: २ मिली/लीटर",
                "स्पिनोसैड ४५% SC: ०.४ मिली/लीटर"
            ],
            "prevention_methods": [
                "ओवरविन्टरिंग बीटल्स को उजागर करने के लिए गहरी जुताई",
                "फ्लोटिंग रो कवर का उपयोग",
                "शीर्ष आबादी से बचने के लिए जल्दी रोपण",
                "स्वयंसेवक आलू का विनाश"
            ]
        }
    },

    "Fruit Flies": {
        "english": {
            "name": "Fruit Flies",
            "description": """Fruit flies include several species that infest fruits and vegetables. Major species include Mediterranean fruit fly (Ceratitis capitata), Oriental fruit fly (Bactrocera dorsalis), and Queensland fruit fly (Bactrocera tryoni). Females lay eggs in ripening fruits, and larvae feed inside, causing fruit rot.""",
            "harmful_effects": [
                "Internal fruit damage and rot",
                "Premature fruit drop",
                "Reduced fruit quality and market value",
                "Quarantine restrictions on exports"
            ],
            "organic_solutions": [
                "Protein bait traps",
                "Mass trapping with pheromones",
                "Sanitation: Remove fallen fruits",
                "Bagging individual fruits"
            ],
            "chemical_pesticides": [
                "Malathion 50% EC: 2ml/L",
                "Fipronil 5% SC: 1ml/L",
                "Spinosad 0.02% bait",
                "Lambda-cyhalothrin 5% EC: 1ml/L"
            ],
            "prevention_methods": [
                "Regular orchard sanitation",
                "Use of fruit fly traps for monitoring",
                "Early harvesting",
                "Area-wide management programs"
            ]
        },
        "bangla": {
            "name": "ফ্রুট ফ্লাইস",
            "description": """ফ্রুট ফ্লাইসে বেশ কয়েকটি প্রজাতি রয়েছে যা ফল এবং সবজিকে সংক্রমণ করে। প্রধান প্রজাতিগুলির মধ্যে রয়েছে ভূমধ্যসাগরীয় ফলের মাছি (Ceratitis capitata), ওরিয়েন্টাল ফলের মাছি (Bactrocera dorsalis), এবং কুইন্সল্যান্ড ফলের মাছি (Bactrocera tryoni)। মহিলারা পাকা ফলে ডিম পাড়ে, এবং লার্ভা ভিতরে খাবার খায়, ফলে ফল পচন সৃষ্টি করে।""",
            "harmful_effects": [
                "অভ্যন্তরীণ ফল ক্ষতি এবং পচন",
                "অকালে ফল পড়া",
                "ফলের গুণমান এবং বাজার মূল্য হ্রাস",
                "রপ্তানিতে কোয়ারেন্টাইন বিধিনিষেধ"
            ],
            "organic_solutions": [
                "প্রোটিন চর্বি ফাঁদ",
                "ফেরোমোন দিয়ে গণ ফাঁদ",
                "স্বাস্থ্যবিধি: পড়ে যাওয়া ফল সরান",
                "স্বতন্ত্র ফল ব্যাগিং"
            ],
            "chemical_pesticides": [
                "ম্যালাথিয়ন ৫০% EC: ২ মিলি/লিটার",
                "ফিপ্রোনিল ৫% SC: ১ মিলি/লিটার",
                "স্পিনোসাড ০.০২% চর্বি",
                "ল্যাম্বডা-সাইহ্যালোথ্রিন ৫% EC: ১ মিলি/লিটার"
            ],
            "prevention_methods": [
                "নিয়মিত বাগান স্বাস্থ্যবিধি",
                "নিরীক্ষণের জন্য ফলের মাছি ফাঁদ ব্যবহার",
                "প্রাথমিক ফসল কাটা",
                "এলাকা-ব্যাপী ব্যবস্থাপনা প্রোগ্রাম"
            ]
        },
        "hindi": {
            "name": "फल मक्खियाँ",
            "description": """फल मक्खियों में कई प्रजातियाँ शामिल हैं जो फलों और सब्जियों को संक्रमित करती हैं। प्रमुख प्रजातियों में भूमध्यसागरीय फल मक्खी (Ceratitis capitata), ओरिएंटल फल मक्खी (Bactrocera dorsalis), और क्वींसलैंड फल मक्खी (Bactrocera tryoni) शामिल हैं। मादाएं पके फलों में अंडे देती हैं, और लार्वा अंदर भोजन करते हैं, जिससे फल सड़ जाता है।""",
            "harmful_effects": [
                "आंतरिक फल क्षति और सड़न",
                "समय से पहले फल गिरना",
                "फल की गुणवत्ता और बाजार मूल्य कम",
                "निर्यात पर संगरोध प्रतिबंध"
            ],
            "organic_solutions": [
                "प्रोटीन चारा जाल",
                "फेरोमोन के साथ सामूहिक जाल",
                "स्वच्छता: गिरे हुए फल हटाएं",
                "व्यक्तिगत फलों को बैगिंग"
            ],
            "chemical_pesticides": [
                "मैलाथियान ५०% EC: २ मिली/लीटर",
                "फिप्रोनिल ५% SC: १ मिली/लीटर",
                "स्पिनोसैड ०.०२% चारा",
                "लैम्ब्डा-साइहैलोथ्रिन ५% EC: १ मिली/लीटर"
            ],
            "prevention_methods": [
                "नियमित बगीचे की स्वच्छता",
                "निगरानी के लिए फल मक्खी जाल का उपयोग",
                "जल्दी फसल कटाई",
                "क्षेत्र-व्यापी प्रबंधन कार्यक्रम"
            ]
        }
    },

    "Tomato Hornworms": {
        "english": {
            "name": "Tomato Hornworms",
            "description": """Tomato hornworms are large green caterpillars of the hawk moth (Manduca quinquemaculata). They feed on tomato, pepper, eggplant, and other solanaceous plants. They can grow up to 4 inches long and have a distinctive horn on their rear end.""",
            "harmful_effects": [
                "Rapid defoliation of plants",
                "Damage to fruits and stems",
                "Reduced yield and fruit quality",
                "Secondary infections through feeding wounds"
            ],
            "organic_solutions": [
                "Handpicking (wear gloves)",
                "Bt (Bacillus thuringiensis) spray",
                "Parasitic wasps (Trichogramma)",
                "Neem oil spray"
            ],
            "chemical_pesticides": [
                "Carbaryl 50% WP: 2g/L",
                "Permethrin 10% EC: 1ml/L",
                "Chlorpyrifos 20% EC: 2ml/L",
                "Spinosad 45% SC: 0.5ml/L"
            ],
            "prevention_methods": [
                "Crop rotation with non-host plants",
                "Deep tilling after harvest",
                "Use of floating row covers",
                "Regular garden inspection"
            ]
        },
        "bangla": {
            "name": "টমেটো হর্নওয়ার্মস",
            "description": """টমেটো হর্নওয়ার্মস হক মথের (Manduca quinquemaculata) বড় সবুজ শুঁয়োপোকা। তারা টমেটো, মরিচ, বেগুন এবং অন্যান্য সোলানাসিয়াস গাছপালা খায়। তারা ৪ ইঞ্চি পর্যন্ত লম্বা হতে পারে এবং তাদের পিছনের প্রান্তে একটি স্বতন্ত্র শিং থাকে।""",
            "harmful_effects": [
                "গাছের দ্রুত পাতার ক্ষতি",
                "ফল এবং কান্ডের ক্ষতি",
                "ফলন এবং ফলের গুণমান হ্রাস",
                "খাওয়ার ক্ষতের মাধ্যমে মাধ্যমিক সংক্রমণ"
            ],
            "organic_solutions": [
                "হাত দিয়ে সংগ্রহ (গ্লাভস পরুন)",
                "বিটি (ব্যাসিলাস থুরিঞ্জিয়েনসিস) স্প্রে",
                "পরজীবী ততৈয়া (ট্রাইকোগ্রামা)",
                "নিম তেল স্প্রে"
            ],
            "chemical_pesticides": [
                "কারবারিল ৫০% WP: ২ গ্রাম/লিটার",
                "পারমেথ্রিন ১০% EC: ১ মিলি/লিটার",
                "ক্লোরপাইরিফস ২০% EC: ২ মিলি/লিটার",
                "স্পিনোসাড ৪৫% SC: ০.৫ মিলি/লিটার"
            ],
            "prevention_methods": [
                "অ-হোস্ট গাছপালা সহ ফসল আবর্তন",
                "ফসল কাটার পর গভীর চাষ",
                "ভাসমান সারি কভার ব্যবহার",
                "নিয়মিত বাগান পরিদর্শন"
            ]
        },
        "hindi": {
            "name": "टमाटर हॉर्नवर्म",
            "description": """टमाटर हॉर्नवर्म हॉक मॉथ (Manduca quinquemaculata) के बड़े हरे कैटरपिलर हैं। वे टमाटर, मिर्च, बैंगन और अन्य सोलानेशियस पौधों पर भोजन करते हैं। वे ४ इंच तक लंबे हो सकते हैं और उनके पिछले सिरे पर एक विशिष्ट सींग होता है।""",
            "harmful_effects": [
                "पौधों की तेजी से पत्तियों का नुकसान",
                "फलों और तनों को नुकसान",
                "उपज और फल की गुणवत्ता कम",
                "खाने के घावों के माध्यम से द्वितीयक संक्रमण"
            ],
            "organic_solutions": [
                "हाथ से चुनना (दस्ताने पहनें)",
                "बीटी (बैसिलस थुरिंजिएंसिस) स्प्रे",
                "परजीवी ततैया (ट्राइकोग्रामा)",
                "नीम तेल स्प्रे"
            ],
            "chemical_pesticides": [
                "कार्बेरिल ५०% WP: २ ग्राम/लीटर",
                "परमेथ्रिन १०% EC: १ मिली/लीटर",
                "क्लोरपाइरिफोस २०% EC: २ मिली/लीटर",
                "स्पिनोसैड ४५% SC: ०.५ मिली/लीटर"
            ],
            "prevention_methods": [
                "गैर-होस्ट पौधों के साथ फसल चक्र",
                "फसल कटाई के बाद गहरी जुताई",
                "फ्लोटिंग रो कवर का उपयोग",
                "नियमित बगीचे निरीक्षण"
            ]
        }
    },

    "Western Corn Rootworms": {
        "english": {
            "name": "Western Corn Rootworms",
            "description": """Western corn rootworm (Diabrotica virgifera virgifera) is a major pest of corn in North America and Europe. Larvae feed on corn roots, causing lodging and reduced water/nutrient uptake. Adults feed on silks and leaves, interfering with pollination.""",
            "harmful_effects": [
                "Root pruning leading to lodging",
                "Reduced nutrient and water uptake",
                "Yield losses up to 30%",
                "Increased susceptibility to drought"
            ],
            "organic_solutions": [
                "Crop rotation with non-host crops",
                "Use of trap crops",
                "Conservation tillage practices",
                "Biological control with nematodes"
            ],
            "chemical_pesticides": [
                "Tefluthrin 2% GR: 15kg/ha",
                "Chlorpyrifos 5% GR: 20kg/ha",
                "Bifenthrin 0.5% GR: 25kg/ha",
                "Thiamethoxam 30% FS: seed treatment"
            ],
            "prevention_methods": [
                "Extended crop rotation (3-4 years)",
                "Use of Bt corn hybrids",
                "Soil insecticides at planting",
                "Monitoring with pheromone traps"
            ]
        },
        "bangla": {
            "name": "ওয়েস্টার্ন কর্ন রুটওয়ার্মস",
            "description": """ওয়েস্টার্ন কর্ন রুটওয়ার্ম (Diabrotica virgifera virgifera) উত্তর আমেরিকা এবং ইউরোপে ভুট্টার একটি প্রধান কীট। লার্ভা ভুট্টার শিকড় খায়, যা পড়ে যাওয়া এবং জল/পুষ্টি শোষণ হ্রাস করে। প্রাপ্তবয়স্করা সিল্ক এবং পাতা খায়, যা পরাগায়নে বাধা দেয়।""",
            "harmful_effects": [
                "শিকড় ছাঁটাই যা পড়ে যাওয়ার দিকে নিয়ে যায়",
                "পুষ্টি এবং জল শোষণ হ্রাস",
                "৩০% পর্যন্ত ফলন হ্রাস",
                "খরার প্রতি সংবেদনশীলতা বৃদ্ধি"
            ],
            "organic_solutions": [
                "অ-হোস্ট ফসল সহ ফসল আবর্তন",
                "ফাঁদ ফসল ব্যবহার",
                "সংরক্ষণ চাষ পদ্ধতি",
                "নিমাটোড দিয়ে জৈবিক নিয়ন্ত্রণ"
            ],
            "chemical_pesticides": [
                "টেফলুথ্রিন ২% GR: ১৫ কেজি/হেক্টর",
                "ক্লোরপাইরিফস ৫% GR: ২০ কেজি/হেক্টর",
                "বিফেনথ্রিন ০.৫% GR: ২৫ কেজি/হেক্টর",
                "থায়ামেথোক্সাম ৩০% FS: বীজ চিকিত্সা"
            ],
            "prevention_methods": [
                "বর্ধিত ফসল আবর্তন (৩-৪ বছর)",
                "বিটি ভুট্টা হাইব্রিড ব্যবহার",
                "রোপণের সময় মাটির কীটনাশক",
                "ফেরোমোন ফাঁদ দিয়ে পর্যবেক্ষণ"
            ]
        },
        "hindi": {
            "name": "पश्चिमी कॉर्न रूटवर्म",
            "description": """पश्चिमी कॉर्न रूटवर्म (Diabrotica virgifera virgifera) उत्तरी अमेरिका और यूरोप में मक्का का एक प्रमुख कीट है। लार्वा मक्का की जड़ों पर भोजन करते हैं, जिससे लॉजिंग और पानी/पोषक तत्वों का अवशोषण कम होता है। वयस्क सिल्क और पत्तियों पर भोजन करते हैं, जिससे परागण में बाधा आती है।""",
            "harmful_effects": [
                "जड़ छंटाई से लॉजिंग होता है",
                "पोषक तत्व और पानी का अवशोषण कम",
                "३०% तक उपज हानि",
                "सूखे के प्रति संवेदनशीलता बढ़ी"
            ],
            "organic_solutions": [
                "गैर-होस्ट फसलों के साथ फसल चक्र",
                "ट्रैप फसलों का उपयोग",
                "संरक्षण जुताई प्रथाएँ",
                "निमेटोड के साथ जैविक नियंत्रण"
            ],
            "chemical_pesticides": [
                "टेफ्लुथ्रिन २% GR: १५ किग्रा/हेक्टेयर",
                "क्लोरपाइरिफोस ५% GR: २० किग्रा/हेक्टेयर",
                "बिफेंथ्रिन ०.५% GR: २५ किग्रा/हेक्टेयर",
                "थायामेथोक्साम ३०% FS: बीज उपचार"
            ],
            "prevention_methods": [
                "विस्तारित फसल चक्र (३-४ वर्ष)",
                "बीटी मक्का संकर का उपयोग",
                "रोपण के समय मिट्टी के कीटनाशक",
                "फेरोमोन जाल के साथ निगरानी"
            ]
        }
    }
}