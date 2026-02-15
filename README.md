# Cat YOLO Detector

## Overview
This project is a cat image detection system built using YOLOv8 and Python.  
It was developed as a computer vision practice project to train a model capable of identifying individual cats from images.

The workflow includes dataset preparation, label verification, model training, and visual result confirmation.

---

## Features
- Custom YOLOv8 training pipeline
- Label verification tool using OpenCV
- Sample inference results included
- Modular training configuration via YAML

---

## Tech Stack
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Machine Learning / Computer Vision

---

## Project Structure
```
cat-yolo-detector/
├── train.py
├── train_label_confirmation.py
├── cat_config.yaml
├── sample_images/
└── README.md
```

---

## Sample Results
Example input and detection outputs are provided in the `sample_images` directory.

- `input_cat*.jpg` : Original images  
- `result_cat*.jpg` : Detection results  

---

## How to Train
1. Prepare dataset following YOLO format  
2. Configure `cat_config.yaml`
3. Run:

```bash
python train.py
```

---

## Notes
- Model weights (`.pt`) and dataset are excluded from this repository due to size considerations.
- Paths should be adjusted depending on environment.

---

## Future Improvements
- Hyperparameter tuning
- Dataset expansion
- Streamlit demo interface
- Model performance evaluation metrics visualization

---

## Author
Machine Learning / Computer Vision focused developer  
Portfolio in progress
