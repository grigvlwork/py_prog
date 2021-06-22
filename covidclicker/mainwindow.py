import os
import random
from math import pi, sin, cos, sqrt

import pygame

from objects import delta_angle

INFECTEVENT = 100
INCREASEINFECT = 101
CUREEVENT = 102
UPDATESYRINGE = 103
pygame.init()
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Covid Clicker")
icon = pygame.image.load('pictures/coronacolor.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
rotate_syringe = False
delta_row = 50
pygame.time.set_timer(INFECTEVENT, 500)
pygame.time.set_timer(CUREEVENT, 1000)
pygame.time.set_timer(INCREASEINFECT, 5000)
pygame.time.set_timer(UPDATESYRINGE, 1000)
fps = 60
syringe_angles = dict()
left_corners = dict()

def rotate_center(image, angle):
    center = image.get_rect().center
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect


def left_corner(angle, center, radius):
    if angle > 2 * pi:
        n = int(angle / (2 * pi))
        angle -= 2 * pi * n
    dx = 5 * cos(angle)
    dy = 5 * sin(angle)
    if angle == pi:
        return center[0] - 5, center[1] - radius - delta_row
    elif angle == 3 * pi / 2:
        return center[0] - 5, center[1] + radius - delta_row
    elif angle == 0:
        return center[0] - radius - delta_row, center[1] - 5
    elif angle == pi / 2:
        return center[0] + radius, center[1] - 5
    elif 0 < angle < pi / 2:
        x = center[0] - (radius + delta_row) * sin(angle)
        y = center[1] - (radius + delta_row) * cos(angle)
        return x - dx, y - dy
    elif pi / 2 < angle < pi:
        angle = pi - angle
        x = center[0] + radius * sin(angle)
        y1 = center[1] + (radius + delta_row) * cos(angle)
        return x - dx, y1 - dy
    elif pi < angle < 3 * pi / 2:
        angle = 3 * pi / 2 - angle
        x1 = center[0] + radius * cos(angle)
        y1 = center[1] - radius * sin(angle)
        return x1 - dx, y1 - dy
    else:
        angle = 2 * pi - angle
        y = center[1] - (radius + delta_row) * cos(angle)
        x1 = center[0] + (radius + delta_row) * sin(angle)
        return x1 - dx, y + dy


def load_image(name, colorkey=None):
    fullname = os.path.join('pictures', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    image = image.convert_alpha()
    return image


class Syringe(pygame.sprite.DirtySprite):
    image = load_image('syringe3.png')

    def __init__(self, group, angle, center, radius, row, id):
        pygame.sprite.DirtySprite.__init__(self, group)
        degrees = angle * 180 / pi
        self.image = pygame.transform.rotate(Syringe.image, degrees)
        self.rect = Syringe.image.get_rect()
        # self.image, self.rect = rotate_center(Syringe.image, degrees)
        self.rect.x, self.rect.y = left_corner(angle, center, radius + (row + 1) * delta_row)
        self.visible = 1
        self.dirty = 1
        self.angle = angle
        self.center = center
        self.radius = radius
        self.row = row
        self.phase = 0
        self.id = id

    def rotate(self):
        self.angle -= delta_angle[self.row] / 3
        degrees = self.angle * 180 / pi
        # self.image, self.rect = rotate_center(Syringe.image, degrees)
        self.image = pygame.transform.rotate(Syringe.image, degrees)
        self.rect = Syringe.image.get_rect()
        if (self.angle, self.center, self.radius + self.row * delta_row + self.phase) in left_corners:
            self.rect.x, self.rect.y = \
                left_corners[(self.angle, self.center, self.radius + self.row * delta_row + self.phase)]
        else:
            self.rect.x, self.rect.y = \
                left_corner(self.angle, self.center, self.radius + self.row * delta_row + self.phase)
            left_corners[(self.angle, self.center, self.radius + self.row * delta_row + self.phase)] = \
                self.rect.x, self.rect.y
        syringe_angles[(self.id, self.row)] = self.angle 

    def update(self):
        self.phase += 1
        if rotate_syringe:
            self.rotate()
        if self.phase == 10:
            self.phase = 0
        self.dirty = 1


class Human:
    def __init__(self, x, y, direction, status, level):
        self.x = x
        self.y = y
        self.direction = direction
        self.status = status
        # self.transparent = 0
        self.age = 0
        self.step = 2
        self.level = level
        self.age_of_death = 120
        self.dx = self.step * cos(self.direction)
        self.dy = self.step * sin(self.direction)

    def render(self):
        if self.status == "болен":
            color = pygame.Color(255, 0, 0)
        else:
            color = pygame.Color(255, 255, 255)
        size = self.level
        pygame.draw.rect(screen, color, [self.x, self.y, size, size], 1)
        self.x = self.x + self.dx
        self.y = self.y - self.dy
        self.age += 1


class AddButton(pygame.sprite.DirtySprite):
    image = load_image('add2.png')
    image = pygame.transform.scale(image, (32, 32))

    def __init__(self, group, x, y, item):
        super().__init__(group)
        self.image = AddButton.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.item = item
        self.visible = 1
        self.dirty = 1

    def click(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return self.item
        return 0
    

class Virus(pygame.sprite.DirtySprite):
    image1 = load_image("coronacolor.png")
    image2 = load_image("coronacolor1.png")
    
    def __init__(self, group, center):
        pygame.sprite.DirtySprite.__init__(self, group)
        self.center = center
        self.angle = 0
        degrees = self.angle * 180 / pi - 90
        self.image, self.rect = rotate_center(Virus.image1, degrees)
        self.rect.x, self.rect.y = center[0] - 64, center[1] - 64
        self.clicked = 0
        self.dirty = 1

    def corner(self, angle, center):
        x = center[0] - 64
        y = center[1] - 64
        if angle > pi / 2:
            n = int(2 * angle / pi)
            angle -= n * pi / 2
        angle += pi / 4
        dx = - (64 - 64 * sqrt(2) * sin(angle))
        return x - dx, y - dx

    def click(self):
        degrees = self.angle * 180 / pi - 90
        self.image, self.rect = rotate_center(Virus.image2, degrees)
        # self.rect.x, self.rect.y = self.center[0] - 64, self.center[1] - 64
        self.rect.x, self.rect.y = self.corner(self.angle, self.center)
        self.clicked = 1


    def update(self):
        self.angle += pi / 180
        degrees = self.angle * 180 / pi - 90
        if self.clicked == 0:
            self.image, self.rect = rotate_center(Virus.image1, degrees)
            # self.rect.x, self.rect.y = self.center[0] - 64, self.center[1] - 64
            self.rect.x, self.rect.y = self.corner(self.angle, self.center)
        else:
            self.image, self.rect = rotate_center(Virus.image2, degrees)
            # self.rect.x, self.rect.y = self.center[0] - 64, self.center[1] - 64
            self.rect.x, self.rect.y = self.corner(self.angle, self.center)
            self.clicked += 1
            if self.clicked > 5:
                self.clicked = 0
        self.dirty = 1


class MainField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_width = int(width * 0.7)
        self.slot_width = self.width - self.game_width
        self.slot_height = self.height // 10
        self.virus_size = 50
        self.infected_size = 2
        self.virus_size_delta = 0
        self.amount_infected = 0
        self.infect_in_tick = 1
        self.infected = []
        self.cured = 0
        self.cured_to_pay = 0
        self.cure_in_sec = 0
        self.virus_clicked = True
        self.counter_size = self.slot_height
        self.syringe_counter_size = self.slot_height
        self.medic_counter_size = self.slot_height
        self.syringe_cost = 100
        self.syringe_amount = 0
        self.medic_cost = 1000
        self.medic_amount = 0
        self.infect_timeout = 500
        self.button_sprites = pygame.sprite.LayeredDirty()
        self.syringe_sprites = pygame.sprite.LayeredDirty()
        self.virus_sprites = pygame.sprite.LayeredDirty()
        self.add_syringe_sprite = AddButton(self.button_sprites,
                                            self.width - 35,
                                            self.slot_height + 10, 1)
        self.add_medic_sprite = AddButton(self.button_sprites,
                                            self.width - 35,
                                            self.slot_height * 2 + 10, 2)
        self.virus_sprite = Virus(self.virus_sprites, (self.game_width // 2, self.height // 2))
        self.sprite_id = [0, 0, 0, 0, 0]
        random.seed()

    def make_infected(self, amount):
        tmp_infected = amount
        while tmp_infected > 10000:
            angle = random.random() * 2 * pi
            x = self.game_width // 2 + (self.virus_size + self.virus_size_delta) * cos(angle)
            y = self.height // 2 - (self.virus_size + self.virus_size_delta) * sin(angle)
            infected = Human(x, y, angle, "болен", 5)
            self.infected.append(infected)
            self.amount_infected += 10000
            tmp_infected -= 10000
        while tmp_infected > 1000:
            angle = random.random() * 2 * pi
            x = self.game_width // 2 + (self.virus_size + self.virus_size_delta) * cos(angle)
            y = self.height // 2 - (self.virus_size + self.virus_size_delta) * sin(angle)
            infected = Human(x, y, angle, "болен", 4)
            self.infected.append(infected)
            self.amount_infected += 1000
            tmp_infected -= 1000
        while tmp_infected > 100:
            angle = random.random() * 2 * pi
            x = self.game_width // 2 + (self.virus_size + self.virus_size_delta) * cos(angle)
            y = self.height // 2 - (self.virus_size + self.virus_size_delta) * sin(angle)
            infected = Human(x, y, angle, "болен", 3)
            self.infected.append(infected)
            self.amount_infected += 100
            tmp_infected -= 100
        while tmp_infected > 10:
            angle = random.random() * 2 * pi
            x = self.game_width // 2 + (self.virus_size + self.virus_size_delta) * cos(angle)
            y = self.height // 2 - (self.virus_size + self.virus_size_delta) * sin(angle)
            infected = Human(x, y, angle, "болен", 2)
            self.infected.append(infected)
            self.amount_infected += 10
            tmp_infected -= 10
        while tmp_infected > 0:
            angle = random.random() * 2 * pi
            x = self.game_width // 2 + (self.virus_size + self.virus_size_delta) * cos(angle)
            y = self.height // 2 - (self.virus_size + self.virus_size_delta) * sin(angle)
            infected = Human(x, y, angle, "болен", 1)
            self.infected.append(infected)
            self.amount_infected += 1
            tmp_infected -= 1

    def make_healthy(self, level):
        if level == 1:
            i = -1
            while i >= -len(self.infected):
                if self.infected[i].status == "болен" and self.infected[i].level == 1:
                    self.infected[i].status = "здоров"
                    self.cured += 1
                    self.cured_to_pay += 1
                    break
                i -= 1
            else:
                i = -1
                while i >= -len(self.infected):
                    if self.infected[i].status == "болен" and self.infected[i].level > level:
                        self.infected[i].status = "здоров"
                        self.make_infected(10 ** (self.infected[i].level - 1) - 1)
                        self.infected[i].level = 1
                        self.cured += 1
                        self.cured_to_pay += 1
                        break
                    i -= 1
        else:
            i = -1
            while i >= -len(self.infected):
                if self.infected[i].status == "болен" and self.infected[i].level == level:
                    self.infected[i].status = "здоров"
                    self.cured += 10 ** (self.infected[i].level - 1)
                    self.cured_to_pay += 10 ** (self.infected[i].level - 1)
                    break
                i -= 1
            else:
                i = -1
                while i >= -len(self.infected):
                    if self.infected[i].status == "болен" and self.infected[i].level > level:
                        self.infected[i].status = "здоров"
                        self.make_infected(10 ** (self.infected[i].level - 1) - 1)
                        self.infected[i].level = 1
                        self.cured += 10 ** (self.infected[i].level - 1)
                        self.cured_to_pay += 10 ** (self.infected[i].level - 1)
                        break
                    i -= 1
                else:
                    i = -1
                    while i >= -len(self.infected):
                        if self.infected[i].status == "болен":
                            self.infected[i].status = "здоров"
                            self.cured += 10 ** (self.infected[i].level - 1)
                            self.cured_to_pay += 10 ** (self.infected[i].level - 1)
                    i -= 1

    def on_virus_click(self):
        self.make_healthy(1)
        self.virus_sprite.click()

    def get_click(self, mouse_pos):
        if ((mouse_pos[0] - self.game_width // 2) ** 2 +
            (mouse_pos[1] - self.height // 2) ** 2) < \
                (self.virus_size + self.virus_size_delta) ** 2:
            self.on_virus_click()

    def draw_frame(self):
        pygame.draw.rect(screen, pygame.Color(255, 0, 0),
                         (0, 0, self.game_width, self.height), 1)
        pygame.draw.rect(screen, pygame.Color(255, 0, 0),
                         (self.game_width + 2, 0, self.slot_width - 2, self.height), 1)

    def draw_virus(self):
        if self.virus_clicked:
            color = pygame.Color(255, 255, 255)
            self.virus_clicked = False
        else:
            color = pygame.Color(0, 255, 0)
        pygame.draw.circle(screen, color,
                           (self.game_width // 2, self.height // 2),
                           self.virus_size + self.virus_size_delta)
        self.virus_size_delta += 1
        if self.virus_size_delta > self.virus_size // 10:
            self.virus_size_delta = 0

    def draw_syringe_slot(self):
        font = pygame.font.Font(None, self.syringe_counter_size)
        text = font.render("Шприцев:" + str(self.syringe_amount), 1, (100, 255, 100))
        text2 = font.render("Цена:" + str(self.syringe_cost), 1, (100, 255, 100))
        text_w = text2.get_width()
        text_h = text2.get_height()
        while text_w > self.slot_width - 50 or text_h > self.slot_height // 3:
            self.syringe_counter_size -= 1
            font = pygame.font.Font(None, self.syringe_counter_size)
            text2 = font.render("Цена:" + str(self.syringe_cost), 1, (100, 255, 100))
            text_w = text2.get_width()
            text_h = text2.get_height()
        text = font.render("Шприцев:" + str(self.syringe_amount), 1, (100, 255, 100))
        text_x = self.game_width + 5
        text_y = self.slot_height + 6
        screen.blit(text, (text_x, text_y))
        text_x = self.game_width + 5
        text_y = self.slot_height * 2 - text_h - 1
        screen.blit(text2, (text_x, text_y))
        pygame.draw.rect(screen, pygame.Color(100, 255, 100),
                         (self.game_width + 3, self.slot_height + 3, self.slot_width - 4, self.slot_height), 1)
        if self.cured_to_pay > self.syringe_cost:
            self.add_syringe_sprite.visible = 1
        else:
            self.add_syringe_sprite.visible = 0
        buttons = self.button_sprites.draw(screen)
        pygame.display.update(buttons)

    def draw_medic_slot(self):
        font = pygame.font.Font(None, self.medic_counter_size)
        text = font.render("Врачей:" + str(self.medic_amount), 1, (100, 255, 100))
        text2 = font.render("Цена:" + str(self.medic_cost), 1, (100, 255, 100))
        text_w = text2.get_width()
        text_h = text2.get_height()
        while text_w > self.slot_width - 50 or text_h > self.slot_height // 3:
            self.medic_counter_size -= 1
            font = pygame.font.Font(None, self.medic_counter_size)
            text2 = font.render("Цена:" + str(self.medic_cost), 1, (100, 255, 100))
            text_w = text2.get_width()
            text_h = text2.get_height()
        text = font.render("Врачей:" + str(self.medic_amount), 1, (100, 255, 100))
        text_x = self.game_width + 5
        text_y = self.slot_height * 2 + 6
        screen.blit(text, (text_x, text_y))
        text_x = self.game_width + 5
        text_y = self.slot_height * 3 - text_h - 1
        screen.blit(text2, (text_x, text_y))
        pygame.draw.rect(screen, pygame.Color(100, 255, 100),
                         (self.game_width + 3, self.slot_height * 2 + 3, self.slot_width - 4, self.slot_height), 1)
        if self.cured_to_pay > self.medic_cost:
            self.add_medic_sprite.visible = 1
        else:
            self.add_medic_sprite.visible = 0
        buttons = self.button_sprites.draw(screen)
        pygame.display.update(buttons)

    def draw_counter(self):
        font = pygame.font.Font(None, self.counter_size)
        text_cured = font.render("Исцелено:" + str(self.cured_to_pay), 1, (100, 255, 100))
        text_infected = font.render("Заражено:" + str(self.amount_infected), 1, (255, 100, 100))
        text_w = text_cured.get_width()
        text_h = text_cured.get_height()
        while (text_w > self.slot_width - 7) or (text_h > (self.slot_height - 5) // 3):
            self.counter_size -= 1
            font = pygame.font.Font(None, self.counter_size)
            text_cured = font.render("Исцелено:" + str(self.cured_to_pay), 1, (100, 255, 100))
            text_w = text_cured.get_width()
            text_h = text_cured.get_height()
        text_x = self.game_width + 3 + (self.slot_width - text_w) // 2
        text_y = 5
        screen.blit(text_cured, (text_x, text_y))
        text_w = text_infected.get_width()
        text_x = self.game_width + 3 + (self.slot_width - text_w) // 2
        text_y = self.slot_height - text_h - 3
        screen.blit(text_infected, (text_x, text_y))
        pygame.draw.rect(screen, pygame.Color(100, 255, 100),
                         (self.game_width + 3, 1, self.slot_width - 4, self.slot_height), 1)

    def fill_syringes(self):
        i = len(self.syringe_sprites)
        while len(self.syringe_sprites) < self.syringe_amount:
            # first row 45
            if i < 45:
                row = 0
            # 2 row 90
            elif i < 135:
                row = 1
            # 3 row 180
            elif i < 315:
                row = 2
            # 4 row 360
            elif i < 775:
                row = 3
            # 5 row 720
            elif i < 1495:
                row = 4
            # 6 row 1440
            elif i < 2935:
                row = 5
            self.sprite_id[row] += 1
            if (self.sprite_id[row] - 1, row) in syringe_angles:
                angle = syringe_angles[(self.sprite_id[row] - 1, row)] + delta_angle[row]
            else:
                angle = pi / 2
            syringe_angles[(self.sprite_id[row], row)] = angle
            Syringe(self.syringe_sprites, angle,
                    (self.game_width // 2, self.height // 2),
                    self.virus_size, row, self.sprite_id[row])

    def cure(self):
        temp_cure = self.cure_in_sec
        while temp_cure > 10000:
            self.make_healthy(5)
            temp_cure -= 10000
        while temp_cure > 1000:
            self.make_healthy(4)
            temp_cure -= 1000
        while temp_cure > 100:
            self.make_healthy(3)
            temp_cure -= 100
        while temp_cure > 10:
            self.make_healthy(2)
            temp_cure -= 10
        while temp_cure > 0:
            self.make_healthy(1)
            temp_cure -= 1

    def render(self):
        self.draw_frame()
        # self.draw_virus()
        self.draw_counter()
        self.draw_syringe_slot()
        self.draw_medic_slot()
        self.fill_syringes()
        self.button_sprites.draw(screen)
        self.syringe_sprites.draw(screen)
        self.virus_sprites.draw(screen)
        i = 0
        while i < len(self.infected):
            if self.infected[i].age > self.infected[i].age_of_death:
                self.infected.remove(self.infected[i])
            else:
                i += 1
        for ill in self.infected:
            if 0 < ill.x < self.game_width and 0 < ill.y < self.height:
                ill.render()


main_field = MainField(640, 480)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            main_field.get_click(event.pos)
            add_syringe = main_field.add_syringe_sprite.click(event)
            if add_syringe == 1 and main_field.cured_to_pay > main_field.syringe_cost:
                main_field.syringe_amount += 1
                main_field.cured_to_pay -= main_field.syringe_cost
                main_field.syringe_cost = int(main_field.syringe_cost * 1.1)
                main_field.cure_in_sec = main_field.syringe_amount
            elif add_syringe == 2 and main_field.cured_to_pay > main_field.medic_cost:
                main_field.medic_amount += 1
                main_field.cured_to_pay -= main_field.medic_cost
                main_field.medic_cost = int(main_field.medic_cost * 1.1)
                main_field.cure_in_sec = main_field.syringe_amount * 10
        if event.type == INFECTEVENT:
            main_field.make_infected(main_field.infect_in_tick)
        if event.type == INCREASEINFECT:
            if main_field.cured > main_field.amount_infected * 0.9:
                main_field.infect_in_tick += 1
                if main_field.infect_in_tick > 50:
                    main_field.infect_in_tick = 10
                    main_field.infected_size += 1
        if event.type == CUREEVENT:
            if main_field.cure_in_sec > 0:
                main_field.cure()
        if event.type == UPDATESYRINGE:
            rotate_syringe = True
    main_field.syringe_sprites.update()
    main_field.virus_sprites.update()
    screen.fill("black")
    main_field.render()
    clock.tick(fps)
    pygame.display.flip()
    rotate_syringe = False
pygame.quit()
