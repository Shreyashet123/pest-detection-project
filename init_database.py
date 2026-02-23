from pymongo import MongoClient  
import os  
from dotenv import load_dotenv  
from datetime import datetime  
  
load_dotenv()  
uri = os.getenv("MONGO_URI")  
  
print("Initializing MongoDB Atlas database...")  
  
try:  
    # Connect to Atlas  
    client = MongoClient(uri)  
    print("Connected to MongoDB Atlas")  
  
    # Create/Connect to pest database  
    db = client["pest"]  
    print("Using database: pest")  
  
    # Create collections  
    collections = ["pest_details", "user_query", "users", "admin_users"]  
    for coll in collections:  
        if coll not in db.list_collection_names():  
            db.create_collection(coll)  
            print(f"  Created: {coll}")  
        else:  
            print(f"  Exists: {coll}")  
  
    # Insert sample pest data  
    print("\nAdding sample pest data...")  
    sample_pests = [  
        {"name": "Aphid", "treatment": "Neem oil", "description": "Small sap-sucking insects"},  
        {"name": "Caterpillar", "treatment": "Manual removal", "description": "Leaf-eating larvae"},  
        {"name": "Whitefly", "treatment": "Yellow sticky traps", "description": "Tiny white flying pests"}  
    ]  
  
    db.pest_details.delete_many({})  
    result = db.pest_details.insert_many(sample_pests)  
    print(f"Added {len(result.inserted_ids)} pest records")  
  
    # Create admin user  
    import hashlib  
    admin_hash = hashlib.sha256("officer123".encode()).hexdigest()  
    db.admin_users.delete_many({})  
    db.admin_users.insert_one({  
        "username": "officer",  
        "password": admin_hash,  
        "created_at": datetime.now()  
    })  
    print("Created admin user: officer / officer123")  
  
    print("\n? Database setup complete!")  
    print(f"?? Database: {db.name}")  
    print(f"?? Collections: {db.list_collection_names()}")  
  
except Exception as e:  
    print(f"? Error: {e}") 
