from PIL import Image


def mirror():
    image = Image.open('image.jpg')
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image = image.transpose(Image.ROTATE_90)
    image.save('res.jpg', 'JPEG')
