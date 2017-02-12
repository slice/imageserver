import os
from os import path
from .image import Image

class Database:
    def __init__(self, path, *, sort=True):
        self.path = path

        # should we sort? this helps when we have filenames
        # like 1.png, 2.png, and so on so they can be displayed
        # in sequential order
        self.sort = sort

        # list of thumbnail/image pathnames. they are not fully qualified
        # paths
        self.thumbnail_paths = []
        self.image_paths = []

        self.images = []

    @property
    def files(self):
        """ Returns both thumbnail and image pathnames in an array. """
        return self.thumbnail_paths + self.image_paths

    def find_by_filename(self, filename):
        """ Returns a tuple containing the index and Image object by its filename. """
        for i, image in enumerate(self.images):
            if image.image == filename:
                return (i, image)

    def refresh(self):
        """ Rebuilds the list of images. """
        generator = os.walk(self.path)

        # TODO: handle nested directories. for now,
        # all of your images should be in a flat folder. imageserver will
        # ignore directories.
        try:
            files = next(generator)[2]
        except StopIteration:
            # no files :(
            files = []

        self.thumbnail_paths = list(filter(lambda x: x.endswith('.thumb'), files))
        self.image_paths = list(filter(lambda x: not x.endswith('.thumb'), files))

        if self.sort:
            self.thumbnail_paths = sorted(self.thumbnail_paths)
            self.image_paths = sorted(self.image_paths)

        # generate image objects
        for i, image in enumerate(self.image_paths):
            thumb = self.thumbnail_paths[i]
            print(f' * Build: {image}')
            self.images.append(Image(image, thumb))
