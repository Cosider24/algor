from PIL import Image

image = Image.open("1.jpg")
new = image.resize((image.width // 3, image.height // 3))

gorizont = image.rotate(180)
vertical = image.rotate(90)

new.save("new.jpg")
gorizont.save("gorizont.jpg")
vertical.save("vertical.jpg")