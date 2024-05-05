def nom3():
    party = Image.open('mart.jpg')
    imdraw = ImageDraw.Draw(party)
    x = input("введите имя: ")
    text = str(x) + ', поздравляю! '
    font = ImageFont.truetype("SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", size = 50)
    y = imdraw.textsize(text, font=font)
    z = party.size
    w = (z[0] // 2) - (y[0] // 2)
    imdraw.text((w, 10), text, font=font, fill=("#ff0000"))
    party.save("newmart.png")
    party.show()