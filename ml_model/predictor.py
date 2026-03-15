import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json
import os
import gc  # ADD THIS - for garbage collection

# Get the directory of this file
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))

print("🔄 Loading Pest Detection Model...")
MODEL_PATH = os.path.join(MODEL_DIR, 'pest_grouped_model_v1.h5')

# CHANGE THIS LINE (add compile=False)
model = tf.keras.models.load_model(MODEL_PATH, compile=False)  # ← ADD compile=False

# ADD THIS LINE right after loading model
tf.keras.backend.clear_session()  # ← ADD THIS - clears memory

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
        # ADD THIS - garbage collection before prediction
        gc.collect()  # ← ADD THIS
        
        # Open and preprocess image
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((IMG_SIZE, IMG_SIZE))
        
        # CHANGE THIS LINE (use float32)
        img_array = np.array(img, dtype=np.float32) / 255.0  # ← ADD dtype=np.float32
        img_batch = np.expand_dims(img_array, axis=0)
        
        # Make prediction
        predictions = model.predict(img_batch, verbose=0)[0]
        
        # Get top prediction
        top_idx = int(np.argmax(predictions))
        predicted_class = class_names[top_idx]
        confidence = float(predictions[top_idx]) * 100
        
        # CHANGE THIS - only return top 5 predictions
        all_predictions = {}
        # Get indices of top 5 predictions
        top_indices = np.argsort(predictions)[-5:][::-1]  # ← ADD THIS
        for idx in top_indices:  # ← CHANGE THIS
            all_predictions[class_names[idx]] = round(float(predictions[idx]) * 100, 2)
        
        # ADD THESE LINES - clean up
        del img_array  # ← ADD THIS
        del img_batch  # ← ADD THIS
        gc.collect()   # ← ADD THIS
        
        print(f"✅ Predicted: {predicted_class} ({confidence:.1f}%)")
        
        return {
            "success": True,
            "predicted_class": predicted_class,
            "confidence": round(confidence, 2),
            "all_predictions": all_predictions  # Now only top 5
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