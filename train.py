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
    data="cat_config.yaml",  # ステップ1で作成したyamlファイル
    epochs=100,              # エポック数（モデルの学習回数）
    imgsz=640,               # 画像サイズ
    batch=8,                 # バッチサイズ
    iou=0.5,                 # 重複検出を減らすための閾値
    name="cat_detector_v2"   # 学習結果を保存するフォルダ名
)