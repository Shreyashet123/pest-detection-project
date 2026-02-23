# utils/pestid.py

# Mapping from predicted class indices to pest names
pest_id_to_name = {
    '1': "Armyworms Group",
    '2': "Corn Worms Group", 
    '3': "Small Sap-Sucking Pests",
    '4': "Africanized Honey Bees (Killer Bees)",
    '5': "Brown Marmorated Stink Bugs",
    '6': "Cabbage Loopers",
    '7': "Citrus Canker",
    '8': "Colorado Potato Beetles",
    '9': "Fruit Flies",
    '10': "Tomato Hornworms",
    '11': "Western Corn Rootworms"
}

# Reverse mapping for easy lookup
pest_name_to_id = {v: k for k, v in pest_id_to_name.items()}

# All available languages
AVAILABLE_LANGUAGES = ['english', 'bangla', 'hindi']

# Default language
DEFAULT_LANGUAGE = 'english'