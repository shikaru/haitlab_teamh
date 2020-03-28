import cv2
import numpy as np
 
# モジュール読み込み 
import sys
sys.path.append('~/intel/openvino/python/python3.5/armv7l')
from openvino.inference_engine import IENetwork, IEPlugin
 
# ターゲットデバイスの指定 
plugin = IEPlugin(device="CPU")
 
# モデルの読み込み 
net = IENetwork(model='face-detection-retail-0004.xml', weights='face-detection-retail-0004.bin')
exec_net = plugin.load(network=net)
 

def g_mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(src, x, y, width, height, ratio=0.03):
    dst = src.copy()
    dst[y:y + height, x:x + width] = g_mosaic(dst[y:y + height, x:x + width], ratio)
    return dst 
# 入力画像読み込み 

def mosaic(frame):
 
# 入力データフォーマットへ変換 
    img = cv2.resize(frame, (300, 300))   # サイズ変更 
    img = img.transpose((2, 0, 1))    # HWC > CHW 
    img = np.expand_dims(img, axis=0) # 次元合せ 
 
# 推論実行 
    out = exec_net.infer(inputs={'data': img})
 
    out = out['detection_out']
    out = np.squeeze(out) #サイズ1の次元を全て削除 
 
# 検出されたすべての顔領域に対して１つずつ処理 
    for detection in out:
    # conf値の取得 
        confidence = float(detection[2])
 
    # バウンディングボックス座標を入力画像のスケールに変換 
        xmin = int(detection[3] * frame.shape[1])
        ymin = int(detection[4] * frame.shape[0])
        xmax = int(detection[5] * frame.shape[1])
        ymax = int(detection[6] * frame.shape[0])
 
    # conf値が0.5より大きい場合のみバウンディングボックス表示 
        if confidence > 0.3:
            w = xmax - xmin
            h = ymax - ymin
            frame = mosaic_area(frame, xmin, ymin, w, h)
    return frame
