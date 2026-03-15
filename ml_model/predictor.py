import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json
import os
import gc  # Essential for clearing RAM

# Get the directory of this file
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))

print("🔄 Loading Pest Detection Model (Memory Optimized)...")
MODEL_PATH = os.path.join(MODEL_DIR, 'pest_grouped_model_v1.h5')

# OPTIMIZATION 1: Load without optimizer weights (Saves ~30% RAM)
try:
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    # OPTIMIZATION 2: Clear any loading artifacts from memory
    tf.keras.backend.clear_session()
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    model = None

# Load class mapping
MAPPING_PATH = os.path.join(MODEL_DIR, 'class_mapping.json')
with open(MAPPING_PATH, 'r') as f:
    class_map = json.load(f)

class_names = [class_map[str(i)] for i in range(len(class_map))]
IMG_SIZE = 224

def predict_pest(image_bytes):
    """
    High-efficiency prediction for low-memory environments
    """
    if model is None:
        return {"success": False, "error": "Model failed to load"}

    try:
        # OPTIMIZATION 3: Force garbage collection before starting
        gc.collect()

        # Preprocessing
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((IMG_SIZE, IMG_SIZE))
        
        # Use float32 to save precision/memory over float64
        img_array = np.array(img, dtype=np.float32) / 255.0
        img_batch = np.expand_dims(img_array, axis=0)
        
        # Prediction
        predictions = model.predict(img_batch, verbose=0)[0]
        
        # Get results
        top_idx = int(np.argmax(predictions))
        predicted_class = class_names[top_idx]
        confidence = float(predictions[top_idx]) * 100
        
        # OPTIMIZATION 4: Only return top 5 results to keep the response light
        all_predictions = {}
        top_indices = np.argsort(predictions)[-5:][::-1]
        for idx in top_indices:
            all_predictions[class_names[idx]] = round(float(predictions[idx]) * 100, 2)
        
        # OPTIMIZATION 5: Explicitly delete large arrays and clear session
        del img_array
        del img_batch
        gc.collect()
        
        print(f"✅ Predicted: {predicted_class} ({confidence:.1f}%)")
        
        return {
            "success": True,
            "predicted_class": predicted_class,
            "confidence": round(confidence, 2),
            "all_predictions": all_predictions
        }
        
    except Exception as e:
        print(f"❌ Prediction Error: {e}")
        return {"success": False, "error": str(e)}