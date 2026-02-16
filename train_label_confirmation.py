import cv2
import os

# データセットのパス
data_path = "./dataset"
image_dir = os.path.join(data_path, 'images/train')
label_dir = os.path.join(data_path, 'labels/train')
output_dir = 'labeled_images' 

# YAMLから名を読み込む
names = {0: 'tsumugi', 1: 'aoi', 2: 'nagisa'} 

# 出力フォルダが存在しない場合は作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def draw_labels(image_path, label_path, names):
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    if not os.path.exists(label_path):
        return img

    with open(label_path, 'r') as f:
        for line in f.readlines():
            parts = list(map(float, line.strip().split()))
            cls_id = int(parts[0])
            x_center, y_center, w, h = parts[1:]

            # YOLOの座標をピクセル座標に
            x1 = int((x_center - w/2) * width)
            y1 = int((y_center - h/2) * height)
            x2 = int((x_center + w/2) * width)
            y2 = int((y_center + h/2) * height)

            # 描画
            color = (0, 255, 0)  
            font_scale = 1.0 
            thickness = 2 

            label = names.get(cls_id, 'unknown')
            
            # 文字の大きさ計算
            (text_w, text_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)

            # 文字の背景描画
            cv2.rectangle(img, (x1, y1 - text_h - 10), (x1 + text_w, y1), color, -1)
            
            # ラベル描画
            cv2.putText(img, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness)
            
            # バウンディングボックス描画
            cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

    return img

print("ラベリング確認画像の生成を開始")
# train画像処理
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(image_dir, filename)
        label_path = os.path.join(label_dir, os.path.splitext(filename)[0] + '.txt')

        if os.path.exists(label_path):
            labeled_img = draw_labels(image_path, label_path, names)
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, labeled_img)
            print(f"'{filename}' の確認画像を保存")
        else:
            print(f"警告: '{filename}' に対応するラベルファイルが見つかりません")

print("ラベリング確認画像の生成が完了")
