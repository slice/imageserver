from flask import Flask, render_template
import os
from os import path
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('images.html')
