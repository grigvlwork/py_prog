import pygame

pygame.init()
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Human:
    def __init__(self, x, y, direction, status):
        self.x = x
        self.y = y
        self.direction = direction
        self.status = status
        self.transparent = 0
        self.age = 0
        self.step = 5
        self.size = 3

    def render(self):
        if self.status == "болен":
            color = pygame.Color(255, 0, 0)
        else:
            color = pygame.Color(255, 255, 255)


class MainField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_width = int(width * 0.7)
        self.slot_width = self.width - self.game_width
        self.slot_height = self.height // 10
        self.virus_size = self.game_width // 6
        self.virus_size_delta = 0
        self.amount_infected = 4
        self.infected = []

    def render(self):
        pygame.draw.rect(screen, pygame.Color(255, 0, 0),
                         (0, 0, self.game_width, self.height), 1)
        pygame.draw.rect(screen, pygame.Color(255, 0, 0),
                         (self.game_width + 2, 0, self.slot_width - 2, self.height), 1)
        pygame.draw.circle(screen, pygame.Color(0, 255, 0),
                           (self.game_width // 2, self.height // 2),
                           self.virus_size + self.virus_size_delta)
        self.virus_size_delta += 1
        if self.virus_size_delta > self.virus_size // 10:
            self.virus_size_delta = 0


main_field = MainField(640, 480)
running = True
while running:
    for event in pygame.event.get():
        if pygame.event.wait().type == pygame.QUIT:
            running = False
    screen.fill("black")
    main_field.render()
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
