from ultralytics import YOLO

model = YOLO("runs/detect/watermark_detector-4/weights/best.pt")

results = model.predict(
    source="images/input/sample.jpg",
    conf=0.05,      # lower threshold
    save=True,
    show_labels=True,
    show_conf=True
)

for r in results:
    print("Boxes:", r.boxes)