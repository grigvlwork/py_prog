from PIL import Image, ImageDraw


def makeanagliph(filename, delta):
    image = Image.open(filename)
    pix = image.load()
    new_image = Image.new("RGB", image.size, (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if x < delta:
                color = pix[x, y]
            else:
                color = (pix[x - delta, y][0], pix[x, y][1],
                         pix[x, y][2])
            draw.point([x, y], color)
    new_image.save('res.jpg', 'JPEG')
    return None