import os
import time
from os import path
from os.path import join
from flask import Flask, Response, render_template, redirect
from .database import Database

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
    image_index, _ = db.find_by_filename(filename)
    try:
        next_image = imgs[image_index + 1].image
    except IndexError:
        next_image = imgs[0].image
    prev_image = imgs[image_index - 1].image
    return render_template('view.html',
        filename=filename, next_image=next_image,
        prev_image=prev_image)

def ms():
    return int(round(time.time() * 1000))

@app.route('/api/database/refresh')
def api_database_refresh():
    begin = ms()
    db.refresh()
    end = ms()
    return str(end - begin)

@app.route('/api/database/redothumbs')
def api_database_redothumbs():
    from .generate_thumbnails import generate_thumbnails
    begin = ms()
    generate_thumbnails()
    end = ms()
    return str(end - begin)

@app.route('/admin')
def route_admin():
    return render_template('admin.html')

@app.route('/i/<string:filename>')
def route_image_proxy(filename):
    extensions = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.tif': 'image/tiff',
        '.tiff': 'image/tiff',
    }
    target_filename = join(images_folder(), filename)
    _, extension = path.splitext(target_filename.replace('.thumb', ''))
    data = open(target_filename, 'rb').read()
    return Response(data, mimetype=extensions[extension])

@app.route('/images')
def route_images():
    return render_template('images.html', images=db.images)
