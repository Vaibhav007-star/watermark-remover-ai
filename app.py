import cv2
import numpy as np

# Load original image
image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Error loading image!")
    exit()

# Create mask
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Watermark coordinates
cv2.rectangle(mask, (390, 300), (690, 390), 255, -1)

# Remove watermark using inpainting
result = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

# Save result
cv2.imwrite("images/output/result.jpg", result)

print("Watermark removed successfully!")