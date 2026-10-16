import os
import random
import shutil

# Source folders
images_dir = "dataset/images"
labels_dir = "dataset/labels-YOLO"

train_img_dir = "dataset/train/images"
train_lbl_dir = "dataset/train/labels-YOLO"

valid_img_dir = "dataset/valid/images"
valid_lbl_dir = "dataset/valid/labels-YOLO"

# Destination folders
train_img_dir = "../dataset/train/images"
train_lbl_dir = "../dataset/train/labels"

valid_img_dir = "../dataset/valid/images"
valid_lbl_dir = "../dataset/valid/labels"

# Create folders if they don't exist
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_lbl_dir, exist_ok=True)
os.makedirs(valid_img_dir, exist_ok=True)
os.makedirs(valid_lbl_dir, exist_ok=True)

# Get image files
images = [
    f for f in os.listdir(images_dir)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

# Shuffle images
random.shuffle(images)

# 80% train, 20% validation
split_idx = int(len(images) * 0.8)

train_images = images[:split_idx]
valid_images = images[split_idx:]

# Copy train files
for img in train_images:
    shutil.copy(
        os.path.join(images_dir, img),
        train_img_dir
    )

    label = os.path.splitext(img)[0] + ".txt"

    if os.path.exists(os.path.join(labels_dir, label)):
        shutil.copy(
            os.path.join(labels_dir, label),
            train_lbl_dir
        )

# Copy validation files
for img in valid_images:
    shutil.copy(
        os.path.join(images_dir, img),
        valid_img_dir
    )

    label = os.path.splitext(img)[0] + ".txt"

    if os.path.exists(os.path.join(labels_dir, label)):
        shutil.copy(
            os.path.join(labels_dir, label),
            valid_lbl_dir
        )

print("Dataset Split Completed Successfully!")
print(f"Training Images: {len(train_images)}")
print(f"Validation Images: {len(valid_images)}")