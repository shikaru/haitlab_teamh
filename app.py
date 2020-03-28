from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np
import cv2
from image_process import mosaic #将来的にはmosaic
from datetime import datetime
import os
import string
import random

SAVE_DIR = "./images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

app = Flask(__name__, static_url_path="")

def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

@app.route('/')
@app.route('/home')  
def home():
 # 引数にpostsを追加
    return render_template('home.html', images=os.listdir(SAVE_DIR)[::-1])  
  
  
@app.route('/about')  
def about():  
    return render_template('about.html', title='About')

@app.route('/processing')
def processing():
    return render_template('processing.html')

@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory(SAVE_DIR, path)

@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:
        # 画像として読み込み
        stream = request.files['image'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # 変換
        img = mosaic(img) ##将来的にはmosaic(img)

        # 保存
        dt_now = datetime.now().strftime("%Y_%m_%d%_H_%M_%S_") + random_str(5)
        save_path = os.path.join(SAVE_DIR, dt_now + ".png")
        cv2.imwrite(save_path, img)

        print("save", save_path)

        return redirect('/')

if __name__ == "__main__":
    app.run(port=8000, debug=True)