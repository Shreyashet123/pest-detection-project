# pest_predict.py - SIMPLE VERSION
print("Hello, Pest Detection!")
print("Testing if Python works...")

# Test basic imports
try:
    import torch
    print(f"PyTorch version: {torch.__version__}")
except:
    print("PyTorch not installed")

try:
    import cv2
    print(f"OpenCV version: {cv2.__version__}")
except:
    print("OpenCV not installed")

print("\nStep 1 complete!")