from PIL import Image, ImageDraw


class CaveImageDraw(ImageDraw.ImageDraw):
    def __init__(self, image):
        super().__init__(image)

    def cave(self, xy, fill):
        x, y, w, h = xy
        c, sa, sd = fill
        self.rectangle((x, y, x + w, y + h), c)
        coords_xy = list()
        coords_xy.append((x + w // 10, y))
        coords_xy.append((x + 3 * w // 10, y))
        coords_xy.append((x + w // 5, y + 5 * h // 8))
        coords_xy.append((x + w // 10, y))
        self.polygon(coords_xy, sa)
        coords_xy = list()
        coords_xy.append((x + 7 * w // 10, y))
        coords_xy.append((x + 9 * w // 10, y))
        coords_xy.append((x + 4 * w // 5, y + 5 * h // 8))
        coords_xy.append((x + 7 * w // 10, y))
        self.polygon(coords_xy, sa)
        coords_xy = list()
        coords_xy.append((x + 3 * w // 20, y + h))
        coords_xy.append((x + w // 4, y + h))
        coords_xy.append((x + w // 5, y + 3 * h // 4))
        coords_xy.append((x + 3 * w // 20, y + h))
        self.polygon(coords_xy, sd)
        coords_xy = list()
        coords_xy.append((x + 3 * w // 4, y + h))
        coords_xy.append((x + 17 * w // 20, y + h))
        coords_xy.append((x + 4 * w // 5, y + 3 * h // 4))
        coords_xy.append((x + 3 * w // 4, y + h))
        self.polygon(coords_xy, sd)
