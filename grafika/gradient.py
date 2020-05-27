from PIL import Image, ImageDraw


def gradient(color):
    if color.lower() == 'r':
        delta = (1, 0, 0)
    elif color.lower() == 'g':
        delta = (0, 1, 0)
    else:
        delta = (0, 0, 1)
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for x in range(256):
        color = (delta[0] * x, delta[1] * x, delta[2] * x)
        draw.line((x * 2, 0, x * 2, 200), fill=color, width=2)
    new_image.save('res.png', 'PNG')


gradient(input())
