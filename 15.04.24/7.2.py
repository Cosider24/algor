from PIL import Image

def main():
    image_path = "C:/Users/torho/Downloads/15.04.24/3.jpg.jpg"

    img = Image.open(image_path)

    resized_img = img.resize((img.width // 3, img.height // 3))
    mirrored_horizontal = img.rotate(180)
    mirrored_vertical = img.rotate(90)

    resized_img.save("resized_image.jpg")
    mirrored_horizontal.save("mirrored_horizontal.jpg")
    mirrored_vertical.save("mirrored_vertical.jpg")

    print("Уменьшенное изображение и зеркальные отражения сохранены.")

if __name__ == "__main__":
    main()