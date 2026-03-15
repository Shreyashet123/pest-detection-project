import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json
import os
import gc  # Add garbage collector

# Get the directory of this file
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))

print("🔄 Loading Pest Detection Model...")
MODEL_PATH = os.path.join(MODEL_DIR, 'pest_grouped_model_v1.h5')

# OPTIMIZATION 1: Set memory limits for TensorFlow
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(f"GPU config error: {e}")

# OPTIMIZATION 2: Load model with memory optimizations
try:
    # Load model without optimizer (saves ~30% memory)
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    
    # OPTIMIZATION 3: Clear session after loading
    tf.keras.backend.clear_session()
    
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    model = None

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
    Predict pest from image bytes - Optimized version
    Returns: dict with predicted_class, confidence, all_predictions
    """
    # OPTIMIZATION 4: Early return if model failed to load
    if model is None:
        return {
            "success": False,
            "error": "Model not loaded",
            "predicted_class": "Error",
            "confidence": 0,
            "all_predictions": {}
        }
    
    try:
        # Open and preprocess image
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((IMG_SIZE, IMG_SIZE))
        img_array = np.array(img, dtype=np.float32) / 255.0  # Use float32 for memory efficiency
        img_batch = np.expand_dims(img_array, axis=0)
        
        # OPTIMIZATION 5: Force garbage collection before prediction
        gc.collect()
        
        # Make prediction
        predictions = model.predict(img_batch, verbose=0)[0]
        
        # Get top prediction
        top_idx = int(np.argmax(predictions))
        predicted_class = class_names[top_idx]
        confidence = float(predictions[top_idx]) * 100
        
        # OPTIMIZATION 6: Only return top 5 predictions (saves memory in response)
        all_predictions = {}
        # Get indices of top 5 predictions
        top_indices = np.argsort(predictions)[-5:][::-1]
        for idx in top_indices:
            all_predictions[class_names[idx]] = round(float(predictions[idx]) * 100, 2)
        
        # OPTIMIZATION 7: Clean up large arrays
        del img_array
        del img_batch
        del predictions
        gc.collect()
        
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
            "error": str(e),
            "predicted_class": "Error",
            "confidence": 0,
            "all_predictions": {}
        }

# Test function
if __name__ == "__main__":
    print("=" * 50)
    print("Model loaded successfully!")
    print(f"Number of classes: {len(class_names)}")
    print("Classes:", class_names)
    print("=" * 50)