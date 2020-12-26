from flask import Flask, render_template, request, jsonify
import urllib.request
import json

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

@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        baseurl = 'http://172.18.02:6007/predict'
        data = request
        headers = {
            'Content-Type': 'application/json',
        }
        print(type(data))
        # req = urllib.request.Request(baseurl, json.dumps(data.json).encode(), headers)
        req = urllib.request.Request(baseurl, json.dumps(data.json).encode(), headers)
        with urllib.request.urlopen(req) as res:
            predicted_img_base64 = res.read()
        return jsonify({'img':predicted_img_base64.decode('utf-8')})
    elif request.method == 'GET':
        return jsonify({'result':'please post image'})
        return render_template("index.html")


# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)