# ml_model/predictor.py
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json
import os

# Get the directory of this file
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))

print("🔄 Loading Pest Detection Model...")
MODEL_PATH = os.path.join(MODEL_DIR, 'pest_grouped_model_v1.h5')
model = tf.keras.models.load_model(MODEL_PATH)

# Load class mapping
MAPPING_PATH = os.path.join(MODEL_DIR, 'class_mapping.json')
with open(MAPPING_PATH, 'r') as f:
    class_map = json.load(f)

# Get class names (your 11 pest classes)
class_names = [class_map[str(i)] for i in range(len(class_map))]
IMG_SIZE = 224

print(f"✅ Model loaded! Found {len(class_names)} pest classes")
print(f"🐛 Classes: {class_names}")

def predict_pest(image_bytes):
    """
    Predict pest from image bytes
    Returns: dict with predicted_class, confidence, all_predictions
    """
    try:
        # Open and preprocess image
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((IMG_SIZE, IMG_SIZE))
        img_array = np.array(img) / 255.0
        img_batch = np.expand_dims(img_array, axis=0)
        
        # Make prediction
        predictions = model.predict(img_batch, verbose=0)[0]
        
        # Get top prediction
        top_idx = int(np.argmax(predictions))
        predicted_class = class_names[top_idx]
        confidence = float(predictions[top_idx]) * 100
        
        # Get all predictions
        all_predictions = {}
        for i, class_name in enumerate(class_names):
            all_predictions[class_name] = round(float(predictions[i]) * 100, 2)
        
        print(f"✅ Predicted: {predicted_class} ({confidence:.1f}%)")
        
        return {
            "success": True,
            "predicted_class": predicted_class,
            "confidence": round(confidence, 2),
            "all_predictions": all_predictions
        }
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return {
            "success": False,
            "error": str(e)
        }

# Test function
if __name__ == "__main__":
    print("=" * 50)
    print("Model loaded successfully!")
    print(f"Number of classes: {len(class_names)}")
    print("Classes:", class_names)
    print("=" * 50)