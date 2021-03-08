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
    img_io = BytesIO()
    im.save(img_io, "PNG", quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')