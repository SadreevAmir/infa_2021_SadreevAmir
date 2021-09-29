import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (255, 255, 255), (0, 0, 1000, 1000))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 2)
circle(screen, (255, 0, 0), (150, 150), 20)
circle(screen, (255, 0, 0), (250, 150), 30)
circle(screen, (0, 0, 0), (150, 150), 5)
circle(screen, (0, 0, 0), (250, 150), 10)
rect(screen, (0, 0, 0), (150, 250, 100, 10))
x = 70
y = 100
polygon(screen,(0, 0, 0), [(x, y), (x + 100, y + 50), (x + 120, y + 40), (x + 20, y - 10), (x, y)])
x = 200
y = 130
polygon(screen,(0, 0, 0), [(x, y), (x + 100, y - 50), (x + 120, y - 40), (x + 20, y + 10), (x, y)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()