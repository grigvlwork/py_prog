from PIL import Image, ImageDraw


def picture(**kwargs):
    file_name = kwargs['file_name']
    width = kwargs['width']
    height = kwargs['height']
    if 'sky_color' in kwargs:
        sky_color = kwargs['sky_color']
    else:
        sky_color = '#75BBFD'
    if 'snow_color' in kwargs:
        snow_color = kwargs['snow_color']
    else:
        snow_color = '#FFFAFA'
    if 'trunk_color' in kwargs:
        trunk_color = kwargs['trunk_color']
    else:
        trunk_color = '#A45A52'
    if 'needls_color' in kwargs:
        needls_color = kwargs['needls_color']
    else:
        needls_color = '#01796F'
    if 'sun_color' in kwargs:
        sun_color = kwargs['sun_color']
    else:
        sun_color = '#FFDB00'
    new_image = Image.new("RGB", (width, height), sky_color)
    draw = ImageDraw.Draw(new_image)
    draw.line([0, int(height * 0.9), width, int(height * 0.9)],
              fill=snow_color, width=int(height * 0.2))
    draw.pieslice([int(width * 0.8), -int(height * 0.2), int(width * 1.2),
                   int(height * 0.2)], 90, 180,
                  fill=sun_color)
    draw.polygon([(int(width * 0.5), int(height * 0.1)),
                  (int(width * 0.6), int(height * 0.3)),
                  (int(width * 0.55), int(height * 0.3)),
                  (int(width * 0.65), int(height * 0.5)),
                  (int(width * 0.6), int(height * 0.5)),
                  (int(width * 0.7), int(height * 0.7)),
                  (int(width * 0.3), int(height * 0.7)),
                  (int(width * 0.4), int(height * 0.5)),
                  (int(width * 0.35), int(height * 0.5)),
                  (int(width * 0.45), int(height * 0.3)),
                  (int(width * 0.4), int(height * 0.3)),
                  (int(width * 0.5), int(height * 0.1))], needls_color)
    draw.line([int(width * 0.5), int(height * 0.7),
               int(width * 0.5), int(height * 0.9)],
              fill=trunk_color, width=int(height * 0.1))
    new_image.save(file_name)

picture(file_name='SexDmaPJrd.bmp',
        height=900,
        needls_color=(55, 163, 31),
        sky_color=(62, 93, 5),
        width=200)
# picture('tree.jpg', 700, 500)
