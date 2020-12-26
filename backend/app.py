from flask import Flask, render_template, jsonify

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
    img_str = re.search(r'base64,(.*)', req.form['img']).group(1) # 1
    nparr = np.fromstring(base64.b64decode(img_str), np.uint8) # 2
    img_src = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # 3
    # img_negaposi = 255 - img_src # 4
    # img_gray = cv2.cvtColor(img_negaposi, cv2.COLOR_BGR2GRAY) # 5
    img_resize = cv2.resize(img_gray,(28,28)) # 6
    cv2.imwrite(f"images/{datetime.now().strftime('%s')}.jpg",img_resize) # 7
    return 'ok'

@app.route('/upload',methods=['POST'])
def upload():
    if request.method == 'POST':
        result = decode_img(request)
        return jsonify({'result':result})


# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run()