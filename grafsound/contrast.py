from PIL import Image, ImageDraw


def contrast(filename):
    """ contrast - линейное контрастирование изображения"""
    image = Image.open(filename)
    pix = image.load()
    new_image = Image.new("RGB", image.size, (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    min_color = [256, 256, 256]
    max_color = [0, 0, 0]
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            for i in range(3):
                if min_color[i] > pix[x, y][i]:
                    min_color[i] = pix[x, y][i]
                if max_color[i] < pix[x, y][i]:
                    max_color[i] = pix[x, y][i]
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            color = list(pix[x, y])
            for i in range(3):
                color[i] = int(255 * (color[i] - min_color[i]) /
                               (max_color[i] - min_color[i]))
            draw.point([x, y], tuple(color))
    new_image.save('res.jpg', 'JPEG')
    return None
