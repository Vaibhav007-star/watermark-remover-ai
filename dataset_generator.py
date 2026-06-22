import os
import random
from PIL import Image, ImageDraw, ImageFont

# Paths
INPUT_DIR = "clean_images"
OUTPUT_IMAGE_DIR = "dataset/images/train"
OUTPUT_LABEL_DIR = "dataset/labels/train"

os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)
os.makedirs(OUTPUT_LABEL_DIR, exist_ok=True)

# Watermark texts
watermarks = [
    "© MyBrand",
    "WATERMARK",
    "CONFIDENTIAL",
    "SAMPLE",
    "PHOTO STUDIO",
]

image_counter = 0

for filename in os.listdir(INPUT_DIR):

    path = os.path.join(INPUT_DIR, filename)

    try:
        image = Image.open(path).convert("RGB")
    except:
        continue

    width, height = image.size

    for i in range(20):      # 20 versions per image

        img_copy = image.copy()
        draw = ImageDraw.Draw(img_copy)

        font_size = random.randint(20, 50)

        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

        text = random.choice(watermarks)

        bbox = draw.textbbox((0,0), text, font=font)
        text_w = bbox[2]-bbox[0]
        text_h = bbox[3]-bbox[1]

        x = random.randint(0, width-text_w)
        y = random.randint(0, height-text_h)

        draw.text(
            (x, y),
            text,
            fill=(255,255,255),
            font=font
        )

        output_name = f"img_{image_counter}.jpg"

        img_copy.save(
            os.path.join(OUTPUT_IMAGE_DIR, output_name)
        )

        # YOLO format
        x_center = (x + text_w/2)/width
        y_center = (y + text_h/2)/height
        w_norm = text_w/width
        h_norm = text_h/height

        with open(
            os.path.join(
                OUTPUT_LABEL_DIR,
                output_name.replace(".jpg",".txt")
            ),
            "w"
        ) as f:

            f.write(
                f"0 {x_center} {y_center} {w_norm} {h_norm}"
            )

        image_counter += 1

print("Dataset generation completed!")