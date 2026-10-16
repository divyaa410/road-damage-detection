# Smart Road Damage Detection and Reporting System

## Project Overview
The Smart Road Damage Detection and Reporting System aims to identify road damage from uploaded road images using computer vision. It provides a user interface for detecting road damage and supports reporting and government-side review.

## Objectives
- Detect potential road damage from road images.
- Use a YOLO-based model for object detection.
- Provide a simple interface for submitting images and viewing detection results.
- Support road-damage reporting and government review through separate application pages.

## Technologies Used
- **Programming Language:** Python
- **User Interface:** Streamlit
- **Computer Vision:** Ultralytics YOLO, PIL
- **Model:** YOLOv8 nano (`yolov8n.pt`)

## Project Structure
```text
RoadDamageDetection/
├── dataset/
│   ├── app.py
│   └── government.py
├── src/
│   ├── demo.py
│   ├── quick_test.py
│   ├── split_dataset.py
│   └── train.py
├── data.yaml
├── test.py
├── yolov8n.pt
└── .gitignore
```

## Features
- Road-image upload interface.
- YOLO-based road-damage detection.
- Separate government-facing interface.
- Supporting scripts for model training, testing, and dataset preparation.

## Running the Project
1. Install Python and Git.
2. Install the required dependencies, including Streamlit, Ultralytics, and Pillow.
3. Verify that the model weights and configuration files are available.
4. Run the application from the appropriate project directory:
   `streamlit run app.py`

The exact dependencies and paths may need adjustment to match the local setup.

## Current Status
This repository contains the uploaded application code, supporting scripts, configuration, and model weights. Further testing and deployment may be required.

## Author
Divya Sri
