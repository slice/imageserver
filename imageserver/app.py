from flask import Flask, Response, render_template, redirect
from .database import Database
import os
from os import path
from os.path import join

def images_folder():
    # get the path to the images folder
    _script_path = path.dirname(path.abspath(__file__))
    images = join(join(_script_path, '..'), 'images')
    return path.abspath(images)

app = Flask(__name__)
print(f' * Database: {images_folder()}')
db = Database(images_folder())
db.refresh()

@app.route('/')
def route_root():
    return redirect('/images')

@app.route('/v/<string:filename>')
def route_image_view(filename):
    imgs = db.images
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

    for thumbnail_name in db.thumbnails:
        for image_name in db.images:
            if image_name == thumbnail_name.replace('.thumb', ''):
                imthumbs[thumbnail_name] = image_name
    return render_template('images.html',
        images=db.images, imthumbs=imthumbs)
