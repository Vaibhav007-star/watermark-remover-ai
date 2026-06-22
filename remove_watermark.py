import cv2
import numpy as np
from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/watermark_detector-4/weights/best.pt")

# Load image
img = cv2.imread("images/input/sample.jpg")

# Detect watermark
results = model(img)

# Create mask
mask = np.zeros(img.shape[:2], dtype=np.uint8)

for r in results:
    boxes = r.boxes.xyxy.cpu().numpy()

    for box in boxes:
        x1, y1, x2, y2 = map(int, box)

        # Expand box slightly
        pad = 10
        x1 = max(0, x1 - pad)
        y1 = max(0, y1 - pad)
        x2 = min(img.shape[1], x2 + pad)
        y2 = min(img.shape[0], y2 + pad)

        mask[y1:y2, x1:x2] = 255

# Inpaint
result = cv2.inpaint(img, mask, 7, cv2.INPAINT_TELEA)

# Save
cv2.imwrite("images/output/result.jpg", result)

print("Watermark removed.")