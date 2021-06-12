import pygame

pygame.init()
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)

class MainField:

def draw():
    # screen.fill((102, 217, 255))
    screen.fill("lightblue")



draw()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
