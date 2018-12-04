import glob
import os

from PIL import Image


def ThumbnailCreator(img, size):
    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + "_thumbnail.jpg", "JPEG")


ThumbnailCreator('image.jpg', (128, 128))
