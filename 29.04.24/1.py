from PIL import Image
img = Image.open("flow.jpg")
new_img = img.crop((100, 10, 600, 300))
new_img.save("new.jpg")