import os
from ultralytics import YOLO
import cv2
from shutil import copy2, rmtree
from moviepy.editor import VideoFileClip
import time

# 学習済みモデルのロード
model = YOLO("best.pt")

input_dir = "new_photos"
output_base = "sorted_photos"
temp_dir = "temp_frames"

print("写真と動画の振り分けを開始")
# 推論・分類
for fname in os.listdir(input_dir):
    path = os.path.join(input_dir, fname)
    cats = set()

    # 動画ファイル
    if fname.lower().endswith(('.mp4', '.mov')):
        os.makedirs(temp_dir, exist_ok=True)
        try:
            clip = VideoFileClip(path)
            # 1秒から1フレームごとに抽出し推論
            for t in range(0, int(clip.duration), 1):
                frame = clip.get_frame(t)
                cv2.imwrite(os.path.join(temp_dir, f"temp_frame_{t}.jpg"), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                results = model(os.path.join(temp_dir, f"temp_frame_{t}.jpg"), verbose=False)
                for box in results[0].boxes:
                    cls_id = int(box.cls)
                    cats.add(model.names[cls_id])
                if len(cats) >= 3: 
                    break
            
                        clip.close()
            
                        time.sleep(0.5)
        except Exception as e:
            print(f"動画ファイル '{fname}' の処理中にエラーが発生: {e}")
            
        # 一時フォルダを削除
        if os.path.exists(temp_dir):
            try:
                rmtree(temp_dir)
            except OSError as e:
                print(f"一時フォルダ '{temp_dir}' の削除に失敗: {e}")
    
    # 画像の場合
    elif fname.lower().endswith(('.jpg', '.jpeg', '.png')):
        results = model(path, verbose=False)
        for box in results[0].boxes:
            cls_id = int(box.cls)
            cats.add(model.names[cls_id])
    else:
        print(f"サポートされていないファイル形式です: {fname}")
        continue 

    # 分類ロジック
    if not cats:
        folder = "unknown"
    elif len(cats) == 1:
        folder = list(cats)[0]
    elif len(cats) == 2:
        folder = "_".join(sorted(cats))
    else:
        folder = "all_cats"
    
    # フォルダを作成・ファイルをコピー
    os.makedirs(os.path.join(output_base, folder), exist_ok=True)
    copy2(path, os.path.join(output_base, folder, fname))
    print(f"'{fname}' を '{folder}' に振り分けました")

print("写真と動画の振り分けが完了")