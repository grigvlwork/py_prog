from PIL import Image, ImageDraw
from math import pi


new_image = Image.new("RGB", (1100, 480), (0, 0, 0))
draw = ImageDraw.Draw(new_image)
color = (200, 200, 255)
draw.line([50, 0, 50, 480], fill=color, width=40)
color = (200, 0, 255)
for x in range(40):
    draw.arc([-100 + x, 0, 150 + x, 200], -90, 90, fill=color)
color = (100, 200, 255)
for x in range(40):
    draw.arc([-100 + x, 200, 250 + x, 480], -90, 90, fill=color)
color = (100, 200, 50)
draw.ellipse((300, 200, 500, 480), 'red')
draw.ellipse((340, 220, 460, 460), 'black')
for y in range(200, 480, 40):
    draw.ellipse((530, y, 570, y + 40), 'blue')
draw.pieslice([510, 200, 640, 300], -90, 90, fill='green')
draw.pieslice([470, 310, 680, 480], -90, 90, fill='yellow')
color = (100, 100, 255)
draw.line([700, 480, 800, 200], fill=color, width=40)
draw.line([900, 480, 800, 200], fill=color, width=40)
color = (255, 150, 100)
for y in range(40):
    draw.arc([700, 250 + y, 900, 350 + y], 45, 135, fill=color)
new_image.save('res.png', 'PNG')
