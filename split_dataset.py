import os
import random
import shutil

# Paths
image_train_dir = "dataset/images/train"
label_train_dir = "dataset/labels/train"

image_val_dir = "dataset/images/val"
label_val_dir = "dataset/labels/val"

# Create val folders if they don't exist
os.makedirs(image_val_dir, exist_ok=True)
os.makedirs(label_val_dir, exist_ok=True)

# Get all training images
images = [f for f in os.listdir(image_train_dir) if f.endswith(".jpg")]

# Shuffle images randomly
random.shuffle(images)

# Move 10% to validation
val_size = int(len(images) * 0.1)

val_images = images[:val_size]

for img_file in val_images:
    txt_file = img_file.replace(".jpg", ".txt")

    # Source paths
    img_src = os.path.join(image_train_dir, img_file)
    txt_src = os.path.join(label_train_dir, txt_file)

    # Destination paths
    img_dst = os.path.join(image_val_dir, img_file)
    txt_dst = os.path.join(label_val_dir, txt_file)

    # Move files
    shutil.move(img_src, img_dst)
    shutil.move(txt_src, txt_dst)

print(f"{val_size} image-label pairs moved to validation set.")