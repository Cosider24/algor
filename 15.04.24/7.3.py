from PIL import Image, ImageFilter
import os
def filter(mesto):
    image = Image.open(mesto)
    new = image.filter(ImageFilter.SHARPEN)
    new_mesto = os.path.join("new_papka", os.path.basename(mesto))
    new.save(new_mesto)

images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
for file in images:
    filter(file)