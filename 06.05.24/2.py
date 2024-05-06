def z2():
    import os
    from PIL import Image
    input_dir = (r'Z:\1-мд-21\Торхов Владислав\b\1')
    input_files = os.listdir(input_dir)
    output_dir = (r'Z:\1-мд-21\Торхов Владислав\b\2')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for file in input_files:
        extension = os.path.splitext(file)[1]
        if extension.lower() in ['.jpg', '.png']:
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            image = Image.open(input_path)
            image = image.convert('L')
            image.save(output_path)
    print("Все изображения JPG и PNG успешно обработаны!")
z2()