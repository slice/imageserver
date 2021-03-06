from PIL import Image
import os
from os import path

def generate_thumbnail(file_path, target):
    print(f'MAKE: {file_path}')
    img = Image.open(file_path)
    width, height = img.size
    th_ratio = 10
    th_width = int(width / th_ratio)
    th_height = int(height / th_ratio)
    print(f'  Size: {width}, {height} → {th_width}, {th_height}')
    print(f'  Format: {img.format}')
    img.thumbnail((th_width, th_height))
    img.save(target, img.format)
    print(f'  ✔ Generated')

def generate_thumbnails(imagedir):
    for root, dirs, files in os.walk(imagedir):
        for file in files:
            if file.endswith('.thumb'):
                # don't try to make thumbnails of thumbnails
                continue
            file_path = path.abspath(path.join(imagedir, file))
            thumbnail_path = f'{file_path}.thumb'
            generate_thumbnail(file_path, thumbnail_path)

if __name__ == '__main__':
    # get the path to the images folder
    _script_path = path.dirname(path.abspath(__file__))
    _images = path.join(path.join(_script_path, '..'), 'images')
    generate_thumbnails(path.abspath(_images))
