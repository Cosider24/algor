from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark_to_image(input_image_path, output_image_path, watermark_text):
    img = Image.open(input_image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 50)
    #text_width, text_height = draw.textsize(watermark_text, font=font)
    text_position = ((img.width ) // 2, (img.height ) // 2)
    text_color = (255, 255, 255)
    draw.text(text_position, watermark_text, fill=text_color, font=font)

    draw = img.convert('RGB')
    draw.save(output_image_path)

def main():
    input_folder = "C:/Users/torho/Downloads/15.04.24"
    output_folder = "C:/Users/torho/Downloads/15.04.24"
    watermark_text = "ЫЫЫ"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, f"watermarked_{filename}")
            add_watermark_to_image(input_image_path, output_image_path, watermark_text)

if __name__ == "__main__":
    main()