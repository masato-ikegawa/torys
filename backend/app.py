from flask import Flask, render_template, jsonify

# Ajax通信
from flask_cors import CORS
from random import *

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

# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run()