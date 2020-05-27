from PIL import Image, ImageFilter


def motion_blur(n):
    image = Image.open('image.jpg')
    image = image.transpose(Image.ROTATE_90)
    image = image.filter(ImageFilter.GaussianBlur(radius=n))
    image.save('res.jpg', 'JPEG')
