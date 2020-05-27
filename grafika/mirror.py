from PIL import Image


def mirror():
    image = Image.open('image.jpg')
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image.save('res.jpg', 'JPEG')
