import pygame
from pygame.draw import *
from random import Random, random
from random import randint
pygame.init()

points = 0
screen_width = 1200
screen_height = 900
number_of_balls = 15
difficulty = 0.5
screen = pygame.display.set_mode((screen_width, screen_height))


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
x = []
y = []
vx = []
vy = []
r = []
color = []


def new_ball():
    '''рисует новый шарик '''
    global x, y, r, vy, vx
    x.append(randint(100, 1100))
    y.append(randint(100, 900))
    r.append(randint(10, 50))
    vx.append(random()*2*difficulty - difficulty)
    vy.append(random()*2*difficulty - difficulty)
    color.append(COLORS[randint(0, 5)])


def scoreboard(points):
    font = pygame.font.Font(None, 25)
    text = font.render("Очки: "+str(points), True, RED)
    screen.blit(text, [50, 50])


clock = pygame.time.Clock()
finished = False
for i in range(number_of_balls):
    new_ball()
while not finished:
    for i in range(number_of_balls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x[i])**2 + (event.pos[1] - y[i])**2 <= r[i]**2:
                points = points + 1
                print(points)
                r[i] = 0
        x[i] = x[i] + vx[i]
        y[i] = y[i] + vy[i]
        if x[i] < r[i]/2:
            vx[i] = random()*difficulty
            vy[i] = random()*2*difficulty - difficulty
        if x[i] > screen_width - r[i]/2:
            vx[i] = -random()*difficulty
            vy[i] = random()*2*difficulty - difficulty
        if y[i] > screen_height - r[i]/2:
            vx[i] = random()*2*difficulty - difficulty
            vy[i] = -random()*difficulty
        if y[i] < r[i]/2:
            vx[i] = random()*2*difficulty - difficulty
            vy[i] = random()*difficulty
        circle(screen, color[i], (x[i], y[i]), r[i])
    scoreboard(points)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
