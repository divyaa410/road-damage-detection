from ultralytics import YOLO

model = YOLO("runs/detect/train-3/weights/last.pt")

results = model.predict(
    source="dataset/valid/images",
    save=True,
    show=True
)