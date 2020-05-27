from PIL import Image, ImageDraw


def transparency(filename1, filename2):
    image1 = Image.open(filename1)
    pix1 = image1.load()
    image2 = Image.open(filename2)
    pix2 = image2.load()
    new_image = Image.new("RGB", image1.size, (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for x in range(image1.size[0]):
        for y in range(image1.size[1]):
            r1, g1, b1 = pix1[x, y]
            r2, g2, b2 = pix2[x, y]
            r = int(0.5 * r1 + 0.5 * r2)
            g = int(0.5 * g1 + 0.5 * g2)
            b = int(0.5 * b1 + 0.5 * b2)
            color = (r, g, b)
            draw.point([x, y], color)
    new_image.save('res.jpg', 'JPEG')
    return None

