# check_model.py
import tensorflow as tf
import numpy as np
import json

print("=" * 60)
print("MODEL DIAGNOSTIC CHECK")
print("=" * 60)

try:
    # 1. Load model
    print("1. Loading model...")
    model = tf.keras.models.load_model("pest_grouped_model_v1.h5")
    print("   ✓ Model loaded successfully")
    
    # 2. Check model summary
    print("\n2. Model architecture:")
    model.summary()
    
    # 3. Check output shape
    print(f"\n3. Output shape: {model.output_shape}")
    print(f"   Number of classes expected: {model.output_shape[-1]}")
    
    # 4. Load class mapping
    print("\n4. Loading class mapping...")
    with open("class_mapping.json") as f:
        class_map = json.load(f)
    print(f"   Class mapping: {class_map}")
    print(f"   Number of classes in mapping: {len(class_map)}")
    
    # 5. Test with random input
    print("\n5. Testing with random input...")
    test_input = np.random.random((1, 224, 224, 3))
    predictions = model.predict(test_input)[0]
    
    print(f"   Predictions shape: {predictions.shape}")
    print(f"   Predictions sum: {np.sum(predictions):.4f} (should be ~1.0)")
    
    # Check if all predictions are the same
    unique_values = np.unique(predictions)
    print(f"   Unique prediction values: {len(unique_values)}")
    
    if len(unique_values) == 1:
        print("   ✗ CRITICAL: All predictions are the same!")
        print(f"   All values are: {unique_values[0]}")
    else:
        print("   ✓ Predictions vary across classes")
        
    # Show top predictions
    sorted_indices = np.argsort(predictions)[::-1]
    print("\n   Top 3 predictions:")
    for i, idx in enumerate(sorted_indices[:3]):
        class_name = class_map.get(str(idx), f"Class {idx}")
        confidence = predictions[idx] * 100
        print(f"   {i+1}. {class_name}: {confidence:.2f}%")
        
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()

print("=" * 60)