from PIL import Image, ImageDraw


def board(num, size):
    new_image = Image.new("RGB", (num * size, num * size), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for i in range(num):
        for j in range(num):
            if (i + j) % 2 == 1:
                draw.rectangle([i * size, j * size,
                                (i + 1) * size - 1, (j + 1) * size - 1],
                               fill=(255, 255, 255))
    new_image.save('res.png', 'PNG')


board(5, 30)

