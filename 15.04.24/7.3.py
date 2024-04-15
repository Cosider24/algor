from PIL import Image, ImageFilter
import os
def filter(place1):
    image = Image.open(place1)
    new = image.filter(ImageFilter.SHARPEN)
    new_place1 = os.path.join("new_save", os.path.basename(place1))
    new.save(new_place1)

images = ["1.jpg.jpg", "2.jpg.jpg", "3.jpg.jpg", "4.jpg.jpg", "5.jpg.jpg"]
for file in images:
    filter("C:/Users/torho/Downloads/15.04.24/"+file)