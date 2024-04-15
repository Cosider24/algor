from PIL import Image

image = Image.open("1.jpg")
image.show()
print(image.size)
print(image.format)
print(image.mode)