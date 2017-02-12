import os
from os import path

class Database:
    def __init__(self, path, *, sort=True):
        self.path = path

        # should we sort? this helps when we have filenames
        # like 1.png, 2.png, and so on so they can be displayed
        # in sequential order
        self.sort = sort

        # *.thumb files
        self.thumbnails = []

        # images
        self.images = []

    @property
    def files(self):
        """ Returns both thumbnail and image pathnames in an array. """
        return self.thumbnails + self.images

    def refresh(self):
        """ Rebuilds the list of thumbnail and image pathnames. """
        generator = os.walk(self.path)

        # TODO: handle nested directories. for now,
        # all of your images should be in a flat folder. imageserver will
        # ignore directories.
        files = next(generator)[2]

        self.thumbnails = list(filter(lambda x: x.endswith('.thumb'), files))
        self.images = list(filter(lambda x: not x.endswith('.thumb'), files))

        if self.sort:
            self.thumbnails = sorted(self.thumbnails)
            self.images = sorted(self.images)
