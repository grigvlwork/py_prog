from PIL import Image

image = Image.open('image.jpg')
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
n = width * height
pix = image.load()  # Выгружаем значения пикселей
r = g = b = 0
for x in range(width):
    for y in range(height):
        r += pix[x, y][0]
        g += pix[x, y][1]
        b += pix[x, y][2]

print(r // n, g // n, b // n)

