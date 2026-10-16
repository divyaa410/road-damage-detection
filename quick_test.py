from ultralytics import YOLO

model = YOLO("runs/detect/train-3/weights/last.pt")

model.predict(
    source="dataset/valid/images",
    save=True,
    conf=0.25
)

print("Prediction Done")