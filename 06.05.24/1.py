def z1():
    from pathlib import Path
    from PIL import Image
    input_dir = Path(r'Z:\1-мд-21\Торхов Владислав\b\1')
    output_dir = Path(r'Z:\1-мд-21\Торхов Владислав\b\2')
    output_dir.mkdir(parents=True, exist_ok=True)
    for file in input_dir.iterdir():
        if file.suffix in ['.jpg', '.png', '.bmp']:
            input_path = file
            output_path = output_dir / file.name
            image = Image.open(input_path)
            image = image.convert('L')
            image.save(output_path)
    print("Все изображения успешно обработаны!")
z1()