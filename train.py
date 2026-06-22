from ultralytics import YOLO
from multiprocessing import freeze_support

def main():
    # Load pretrained model
    model = YOLO("yolov8n.pt")

    # Train
    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,
        workers=4,
        cache=True,
        name="watermark_detector"
    )

if __name__ == "__main__":
    freeze_support()
    main()