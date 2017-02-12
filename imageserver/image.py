from PIL import Image as PILImage

class Image:
    def __init__(self, image, thumbnail):
        self.thumbnail = thumbnail
        self.image = image
        self.size = (0, 0)

    def calculate_size(self):
        self.size = PILImage.open(self.image).size
