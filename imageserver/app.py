from flask import Flask, Response, render_template, redirect
from .images import *
from os.path import join

app = Flask(__name__)

@app.route('/')
def route_root():
    return redirect('/images')

@app.route('/v/<string:filename>')
def route_image_view(filename):
    imgs = sorted(images())
    image_index = imgs.index(filename)
    try:
        next_image = imgs[image_index + 1]
    except IndexError:
        next_image = imgs[0]
    prev_image = imgs[image_index - 1]
    return render_template('view.html',
        filename=filename, next_image=next_image,
        prev_image=prev_image)

@app.route('/i/<string:filename>')
def route_image_proxy(filename):
    target_filename = join(images_folder(), filename)
    data = open(target_filename, 'rb').read()
    return Response(data, mimetype='image/png')

@app.route('/images')
def route_images():
    imthumbs = {}

    for thumbnail_name in sorted(thumbs()):
        for image_name in images():
            if image_name == thumbnail_name.replace('.thumb', ''):
                imthumbs[thumbnail_name] = image_name
    return render_template('images.html',
        files=files(), imthumbs=imthumbs)
