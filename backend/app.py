from flask import Flask, render_template, request, jsonify

# Ajax通信
from flask_cors import CORS
from datetime import datetime
from random import *
import numpy as np
import cv2
import re
import base64

app = Flask(__name__, static_folder = "../frontend/hack/dist/static", template_folder="../frontend/hack/dist")

app.config.from_object(__name__)

CORS(app)

# 任意のリクエストを受け取った時、index.htmlを参照
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch(path):
    return render_template("index.html")

@app.route('/rand')
def random():
    response = {
        'randomNum': randint(1,100)
    }
    return jsonify(response)

def decode_img(req):
    img_str = re.search(r'base64,(.*)', req.json['img']).group(1)
    nparr = np.fromstring(base64.b64decode(img_str), np.uint8)
    img_src = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite(f"images/{datetime.now().strftime('%s')}.jpg",img_src)
    return 'ok'

def encode_img(img):
    img_base64 = base64.b64encode(img)
    return img_base64

@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        print(request.json['result'])
        result = decode_img(request)
        return jsonify({'result':result})
    elif request.method == 'GET':
        return jsonify({'result':'please post image'})


# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)