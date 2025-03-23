import pytesseract
from PIL import Image
import os
import json

# Step 1: Define and verify the test folder path
test_folder = os.path.expanduser("~/dataset/test")  # Expands ~ to /home/user
print(f"Looking in folder: {os.path.abspath(test_folder)}")

# Check if folder exists
if not os.path.exists(test_folder):
    print(f"Error: Folder {test_folder} does not exist")
    exit()

# Get image list
test_images = [os.path.join(test_folder, f) for f in os.listdir(test_folder) if f.endswith(".jpg")]
print(f"Found {len(test_images)} test images")
if len(test_images) == 0:
    print("No .jpg files found. Listing folder contents:")
    print(os.listdir(test_folder))  # Show what’s in the folder
    exit()

# Step 2: Verify Tesseract is available
try:
    print(f"Tesseract version: {pytesseract.get_tesseract_version()}")
except Exception as e:
    print(f"Tesseract not found or misconfigured: {e}")
    print("Install it with: !apt-get install tesseract-ocr && pip install pytesseract")
    exit()

# Step 3: Generate ground truth using Tesseract
ground_truth = {}
for image_path in test_images:
    try:
        print(f"Processing: {image_path}")
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        image_name = os.path.basename(image_path)
        ground_truth[image_name] = text.strip()
        print(f"Processed {image_name}: {text[:50] or 'EMPTY'}...")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Step 4: Check and save ground truth
print(f"Ground truth contains {len(ground_truth)} entries")
if not ground_truth:
    print("Warning: ground_truth is empty. Check image processing or Tesseract output.")

with open("test_ground_truth.json", "w") as f:
    json.dump(ground_truth, f, indent=4)

print("Ground truth saved to test_ground_truth.json")