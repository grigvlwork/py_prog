import pygame
import random
from math import pi, sin, cos
from objects import syringe_poly


INFECTEVENT = 100
INCREASEINFECT = 101
pygame.init()
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Covid Clicker")
icon = pygame.image.load('pictures/coronacolor.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
pygame.time.set_timer(INFECTEVENT, 500)
pygame.time.set_timer(INCREASEINFECT, 5000)
fps = 60


class Syringe:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.row = 0
        self.color = pygame.Color((100, 100, 255))
        self.phase = 0

    def render(self, center_x, center_y):
        new_poly = []
        for x, y in syringe_poly:
            x1 = x - center_x + self.phase * cos(self.angle)
            y1 = y - center_y - self.phase * sin(self.angle)
            x2 = x1 * cos(self.angle) + y1 * sin(self.angle)
            y2 = x1 * sin(self.angle) - y1 * cos(self.angle)
            new_poly.append((x2, y2))
        pygame.draw.polygon(screen, self.color, new_poly)
        self.phase += 1
        if self.phase > 5:
            self.phase = 0


class Human:
    def __init__(self, x, y, direction, status, size):
        self.x = x
        self.y = y
        self.direction = direction
        self.status = status
        # self.transparent = 0
        self.age = 0
        self.step = 2
        self.size = size
        self.age_of_death = 120

    def render(self):
        if self.status == "болен":
            color = pygame.Color(255, 0, 0)
        else:
            color = pygame.Color(255, 255, 255)
        pygame.draw.rect(screen, color, [self.x, self.y, self.size, self.size], 1)
        self.x = self.x + self.step * cos(self.direction)
        self.y = self.y - self.step * sin(self.direction)
        self.age += 1


class MainField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_width = int(width * 0.7)
        self.slot_width = self.width - self.game_width
        self.slot_height = self.height // 10
        self.virus_size = self.game_width // 6
        self.infected_size = 2
        self.virus_size_delta = 0
        self.amount_infected = 0
        self.infect_in_tick = 1
        self.infected = []
        self.cured = 0
        self.cured_to_pay = 0
        self.virus_clicked = True
        self.counter_size = self.slot_height
        self.syringe_counter_size = self.slot_height
        self.syringe_cost = 100
        self.syringe_amount = 0
        self.infect_timeout = 500

        random.seed()

    def make_infected(self):
        for i in range(self.infect_in_tick):
            angle = random.random() * 2 * pi
            x = self.game_width // 2 + (self.virus_size + self.virus_size_delta) * cos(angle)
            y = self.height // 2 - (self.virus_size + self.virus_size_delta) * sin(angle)
            infected = Human(x, y, angle, "болен", self.infected_size)
            self.infected.append(infected)
            self.amount_infected += 1

    def make_healthy(self):
        i = -1
        while i > -len(self.infected):
            if self.infected[i].status == "болен":
                self.infected[i].status = "здоров"
                self.cured += 1
                self.cured_to_pay += 1
                break
            i -= 1

    def on_virus_click(self):
        self.make_healthy()
        self.virus_clicked = True

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
        text = font.render("Шприцев:" + str(self.syringe_amount) + "  Цена:" +
                           str(self.syringe_cost), 1, (100, 255, 100))
        text_w = text.get_width()
        while text_w > self.slot_width:
            self.syringe_counter_size -= 1
            font = pygame.font.Font(None, self.syringe_counter_size)
            text = font.render("Шприцев:" + str(self.syringe_amount) + "  Цена:" +
                               str(self.syringe_cost), 1, (100, 255, 100))
            text_w = text.get_width()
        text_x = self.game_width + 3 + (self.slot_width - text_w) // 2
        text_y = 3 + self.slot_height
        screen.blit(text, (text_x, text_y))

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
                         (self.game_width + 3,1, self.slot_width - 4, self.slot_height), 1)

    def render(self):
        self.draw_frame()
        self.draw_virus()
        self.draw_counter()
        self.draw_syringe_slot()
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
        if event.type == INFECTEVENT:
            main_field.make_infected()
        if event.type == INCREASEINFECT:
            main_field.infect_in_tick += 1
            if main_field.infect_in_tick > 50:
                main_field.infect_in_tick = 10
                main_field.infected_size += 1

    screen.fill("black")
    main_field.render()
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
