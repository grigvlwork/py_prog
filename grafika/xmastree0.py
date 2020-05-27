from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75BBFD',
            snow_color='#FFFAFA', trunk_color='#A45A52',
            needls_color='#01796F', sun_color='#FFDB00'):
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
              fill=trunk_color, width=int(width * 0.1))
    new_image.save(file_name)
