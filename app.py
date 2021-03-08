from PIL import Image, ImageDraw
from PIL import ImageFont
from flask import Flask, render_template, request, redirect, send_file
from io import BytesIO
from datetime import datetime
import requests
import chartmaker

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    return render_template("index.html")

@app.route('/picture', methods=["POST","GET"])
def picture():
    data = dict(request.form)
    d={key:value for key,value in data.items() if not key in ["name","imageURL"]}
    im=chartmaker.make_chart(data["name"],data["imageURL"],d)
    return send_file(im, mimetype='image/png')

if __name__ == '_main_':
    app.run()