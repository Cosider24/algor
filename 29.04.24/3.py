from PIL import Image, ImageDraw, ImageFont
img = Image.open("newyear.jpg")
name = input()
new_img = img.crop((100, 10, 600, 200))
draw = ImageDraw.Draw(new_img)
text = name + " , поздравляю!"
font = ImageFont.truetype("arialbd.ttf", 30)
draw.text((50, 20), text, fill="blue", font=font)
new_name = "new1.png"
new_img.save(new_name)