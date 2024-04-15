from PIL import Image, ImageDraw, ImageFont
def znak(mesto, text):
    image = Image.open(mesto)

    drawing = ImageDraw.Draw(image)

    colour = (255, 255, 255)
    font = ImageFont.truetype("arial.ttf", 40)
    drawing.text((0,0), text, fill=colour, font=font)

    image.save("znak" + mesto)


image_files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
znak_text = "Знак"
for file in image_files:
    znak(file, znak_text)