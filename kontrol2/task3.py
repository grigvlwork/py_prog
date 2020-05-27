from PIL import Image, ImageDraw
from math import sqrt


class MaskImageDraw(ImageDraw.ImageDraw):
    def __init__(self, image):
        super().__init__(image)

    def mask(self, xy, fill):
        coords_xy = list()
        coords_xy.append((xy[0], xy[1]))
        coords_xy.append((xy[0] + xy[2], xy[1]))
        coords_xy.append((xy[0] + xy[2] // 3 * 2, xy[1] + xy[3]))
        coords_xy.append((xy[0] + xy[2] // 3, xy[1] + xy[3]))
        coords_xy.append((xy[0], xy[1]))
        self.polygon(coords_xy, fill=fill[0])
        self.ellipse((xy[0] + xy[2] // 3 - xy[3] // 8,
                      xy[1] + xy[3] // 3 - xy[3] // 8, xy[0] + xy[2] // 3 + xy[3] // 8,
                      xy[1] + xy[3] // 3 + xy[3] // 8), fill=fill[1])
        self.ellipse((xy[0] + 2 * xy[2] // 3 - xy[3] // 8,
                      xy[1] + xy[3] // 3 - xy[3] // 8, xy[0] + 2 * xy[2] // 3 + xy[3] // 8,
                      xy[1] + xy[3] // 3 + xy[3] // 8), fill=fill[1])
        coords_xy = list()
        coords_xy.append((xy[0] + xy[2] // 2 - xy[3] // 8,
                          xy[1] + 2 * xy[3] // 3 - int(sqrt(3) * xy[3] // 8)))
        coords_xy.append((xy[0] + xy[2] // 2 + xy[3] // 8,
                          xy[1] + 2 * xy[3] // 3 - int(sqrt(3) * xy[3] // 8)))
        coords_xy.append((xy[0] + xy[2] // 2,
                          xy[1] + xy[3] // 3 * 2))
        coords_xy.append((xy[0] + xy[2] // 2 - xy[3] // 8,
                          xy[1] + 2 * xy[3] // 3 - int(sqrt(3) * xy[3] // 8)))
        self.polygon(coords_xy, fill=fill[2])
