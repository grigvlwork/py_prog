from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#87CEEB',
            ocean_color='#017B92', boat_color='#874535',
            sail_color='#FFFFFF', sun_color='#FFCF40'):
    new_image = Image.new("RGB", (width, height), sky_color)
    draw = ImageDraw.Draw(new_image)
    draw.line([0, height, width, height], fill=ocean_color, width=int(height * 0.2))
    draw.pieslice([int(width * 0.8), -int(height * 0.2) , int(width * 1.2), int(height * 0.2)], 90, 180,
                  fill=sun_color)
    new_image.save(file_name, 'JPEG')


picture('boat.jpg', 600, 400)
