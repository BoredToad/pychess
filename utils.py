import os
from PIL import Image
import PIL.ImageOps

DIR = "images/text/"

def invert_images():
    for filename in os.listdir(DIR):
        r, g, b, a = Image.open(DIR + filename).split()
        rgb_img = Image.merge("RGB", (r, g, b))

        r2, g2, b2 = PIL.ImageOps.invert(rgb_img).split()

        inverted = Image.merge("RGBA", (r2, g2, b2, a))

        inverted.save(f"{DIR}s{filename}")

invert_images()
