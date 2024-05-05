from PIL import Image, ImageDraw, ImageFont

def nom1():
    def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))

    im = Image.open('dr.jpg')
    im_new = crop_center(im, 200, 200)
    im_new.save('dr.jpg', quality=95)
    im_new.show()