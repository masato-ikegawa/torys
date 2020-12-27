from flask import Flask, render_template, request, jsonify

# Ajax通信
from flask_cors import CORS
from datetime import datetime
from random import *
import numpy as np
import cv2
import re
import base64
import shutil
import os
app = Flask(__name__)

import my_edit_new_image
from PIL import Image

app = Flask(__name__, static_folder = "../../frontend/hack/dist/static", template_folder="../../frontend/hack/dist")

app.config.from_object(__name__)

CORS(app)

# 任意のリクエストを受け取った時、index.htmlを参照
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch(path):
    return render_template("index.html")

"""
def styleGan_predict(number, img_path):
    #todo

    return img"""

def decode_img(img_base64):
    img_str = re.search(r'base64,(.*)', img_base64).group(1)
    nparr = np.fromstring(base64.b64decode(img_str), np.uint8)
    img_src = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_path = "images/"+datetime.now().strftime("%Y%m%d_%H%M%S")+".jpg"
    cv2.imwrite("images/"+datetime.now().strftime("%Y%m%d_%H%M%S")+".jpg",img_src)
    return img_src, img_path

def encode_img(img):
    img_base64 = base64.b64encode(img)
    return img_base64

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        number = request.json['result']
        print(f'omikuji{number}')
        img_base64 = request.json['img']
        _, img_path = decode_img(img_base64)

        print('start')
        # predict
        result_img_path = my_edit_new_image.predict(number,img_path)
        print('finish')

        img = Image.open(result_img_path)
        img_resize = img.resize((256,256))
        img_resize.save(result_img_path)
        with open(result_img_path,'rb') as f:
            predicted_img = f.read()
        print(os.path.getsize(result_img_path))

        #Base64で画像をエンコード
        img_predicted_base64 = encode_img(predicted_img)
        print(type(img_predicted_base64))

        # 作ったディレクトリとか保存した.jpgファイルとかを消す
        #os.remove(img_path)
        #shutil.rmtree(img_path.replace('.jpg','')+'/') # ←my_edit_new_image.predictで勝手に作ってたディレクトリ　生成物入ってる
        return jsonify({'result':base64.b64encode(img_predicted_base64).decode('utf-8')})
    elif request.method == 'GET':
        return jsonify({'result':'please post image'})

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)