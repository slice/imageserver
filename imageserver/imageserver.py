import os
import time
from os import path
from os.path import join
from flask import Flask, Response, render_template, redirect, abort
from .database import Database

def images_folder():
    # get the path to the images folder
    _script_path = path.dirname(path.abspath(__file__))
    images = join(join(_script_path, '..'), 'images')
    return path.abspath(images)

# our app
app = Flask(__name__)

# the database
db = None

# did we initialize the database?
#
# instead of initializing the database upon startup,
# we instead do it once upon a request that requires
# the database and set this variable to True so we don't
# do it again.
#
# why? well, if we call init_db immediately upon startup,
# app.config will not have IMAGES_FOLDER in it yet, which means
# that the image folder will be incorrect. IMAGES_FOLDER needs
# to be set to a special value, specifically for testing images.
_did_init_db = False

def init_db():
    # TODO: don't use globals
    global db
    global _did_init_db
    if _did_init_db:
        return # don't initialize it again
    if 'IMAGES_FOLDER' in app.config:
        imgs = app.config['IMAGES_FOLDER']
        print(f' * Custom database: {imgs}')
        db = Database(imgs)
    else:
        print(f' * Database: {images_folder()}')
        db = Database(images_folder())
    db.refresh()

@app.route('/')
def route_root():
    init_db()
    return redirect('/images')

@app.route('/v/<string:filename>')
def route_image_view(filename):
    init_db()
    imgs = db.images
    try:
        image_index, _ = db.find_by_filename(filename)
    except TypeError:
        abort(404)
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
    init_db()
    begin = ms()
    db.refresh()
    end = ms()
    return str(end - begin)

@app.route('/api/database/redothumbs')
def api_database_redothumbs():
    init_db()
    from .generate_thumbnails import generate_thumbnails
    begin = ms()
    generate_thumbnails(db.path)
    end = ms()
    return str(end - begin)

@app.route('/admin')
def route_admin():
    init_db()
    return render_template('admin.html')

@app.route('/i/<string:filename>')
def route_image_proxy(filename):
    init_db()
    extensions = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.tif': 'image/tiff',
        '.tiff': 'image/tiff',
    }
    target_filename = path.abspath(join(db.path, filename))
    if not target_filename.startswith(db.path) or '/' in filename:
        # tried to escape the boundaries of the database
        abort(404)
    _, extension = path.splitext(target_filename.replace('.thumb', ''))
    try:
        data = open(target_filename, 'rb').read()
    except FileNotFoundError:
        abort(404)
    return Response(data, mimetype=extensions[extension])

@app.route('/images')
def route_images():
    init_db()
    return render_template('images.html', images=db.images)
