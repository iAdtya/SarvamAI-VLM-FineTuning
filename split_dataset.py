import os
import shutil
import random

# Step 1: Set up paths
source_folder = "Sarvam-AI/images"  # Replace with your folder path (e.g., "images" or "/content/images")
train_folder = "dataset/train"
test_folder = "dataset/test"

# Create train and test folders if they don’t exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Step 2: Get list of all JPG files
image_files = [f for f in os.listdir(source_folder) if f.endswith(".jpg")]
print(f"Total images found: {len(image_files)}")  # Should be 160

# Step 3: Shuffle the list randomly
random.shuffle(image_files)

# Step 4: Split into 80% train (128) and 20% test (32)
train_size = int(0.8 * len(image_files))  # 128 images
train_files = image_files[:train_size]
test_files = image_files[train_size:]

print(f"Training set: {len(train_files)} images")
print(f"Test set: {len(test_files)} images")

# Step 5: Move or copy files to respective folders
for file in train_files:
    src_path = os.path.join(source_folder, file)
    dest_path = os.path.join(train_folder, file)
    shutil.copy(src_path, dest_path)  # Use shutil.move() if you want to move instead of copy

for file in test_files:
    src_path = os.path.join(source_folder, file)
    dest_path = os.path.join(test_folder, file)
    shutil.copy(src_path, dest_path)

print("Dataset split complete!")
print(f"Training images saved in: {train_folder}")
print(f"Test images saved in: {test_folder}")