import os
from os import path

def images_folder():
    # get the path to the images folder
    _script_path = path.dirname(path.abspath(__file__))
    images = path.join(path.join(_script_path, '..'), 'images')
    return path.abspath(images)

def files():
    generator = os.walk(images_folder())
    images = next(generator)[2]
    return images

def thumbs():
    return list(filter(lambda f: f.endswith('.thumb'), files()))

def images():
    return list(filter(lambda f: not f.endswith('.thumb'), files()))
