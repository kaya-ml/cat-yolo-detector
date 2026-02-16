from ultralytics import YOLO

# 学習済みモデルのロード
model = YOLO("best.pt")

# モデルの性能を評価
results = model.val(data="cat_config.yaml")

print("検証完了")