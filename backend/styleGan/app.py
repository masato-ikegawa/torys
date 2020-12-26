from flask import Flask, render_template, request, jsonify

# Ajax通信
from flask_cors import CORS
from datetime import datetime
from random import *
import numpy as np
import cv2
import re
import base64
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

def styleGan_predict():
    return img

def decode_img(img_base64):
    img_str = re.search(r'base64,(.*)', img_base64).group(1)
    nparr = np.fromstring(base64.b64decode(img_str), np.uint8)
    img_src = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite(f"images/{datetime.now().strftime('%s')}.jpg",img_src)
    return img_src

def encode_img(img):
    img_base64 = base64.b64encode(img)
    return img_base64

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        number = request.json['result']
        img_base64 = request.json['img']
        img = decode_img(img_base64)
        predicted_img = styleGan_predict(number, img)
        img_predicted_base64 = encode_img(predicted_img)
        return jsonify({'result':img_predicted_base64})
    elif request.method == 'GET':
        return jsonify({'result':'please post image'})

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6007,debug=True)