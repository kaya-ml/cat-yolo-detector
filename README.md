# Cat YOLO Detector 🐾

## Overview
愛猫3匹を個別に識別するための物体検出システムです。
YOLOv8をベースに、自作データセットを用いてファインチューニングを行いました。
「多頭飼い環境で、どの子がどこにいるかを自動で判別したい」という日常の課題を技術で解決するプロジェクトです。

---

## Sample Results
学習済みのモデルを用いて、未知の画像に対して推論を行った結果です。

| Input Image | Detection Result |
|:---:|:---:|
| ![Input](./sample_images/input_cat1.jpg) | ![Result](./sample_images/result_cat1.jpg) |

> **Point:** 似た毛色の子でも、顔の特徴や体格の差を学習させることで、高い精度で識別が可能になりました。

---

## Features
- **Custom YOLOv8 Training**: 独自の猫データセットによる個体識別。
- **Label Verification Tool**: アノテーションのズレを視覚的に確認する `train_label_confirmation.py` を実装。
- **Modular Config**: `cat_config.yaml` による柔軟な学習環境設定。

---

## Motivation (開発の経緯)
私は3匹の猫と暮らしていますが、写真を見返した際に個体の判別に迷うことがありました。
「機械学習を使えば、この『愛着のある悩み』を解決できるのでは？」と考えたのがきっかけです。
データの収集からアノテーション、モデルの評価までを一貫して行うことで、物体検出のパイプラインを深く理解することを目指しました。

---

## Tech Stack
- Python 3.9+
- Ultralytics (YOLOv8)
- OpenCV (Visualization)

---

## Project Structure
(以前の構成に `best.pt` などを追加して記載)

---

## How to Run
1. **Environment Setup**:
   ```bash
   pip install -r requirements.txt
