# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 14:16:55 2025

@author: kedad
"""

# train.py
from ultralytics import YOLO

# 学習済みモデルのロード
model = YOLO("yolov8n.pt")

# モデルの学習
results = model.train(
    data="cat_config.yaml",  
    epochs=100,              
    imgsz=640,               
    batch=8,                 
    iou=0.5,                 
    name="cat_detector_v2"   
)
