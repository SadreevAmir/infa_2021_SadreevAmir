import pygame
from pygame.draw import *
from random import Random, random
from random import randint
import math
pygame.init()

points = 0
screen_width = 1200
screen_height = 900
number_of_balls = 10
number_of_special_targets = 2
difficulty = 1
finished = False
screen = pygame.display.set_mode((screen_width, screen_height))


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
ball_x = []
ball_y = []
ball_vx = []
ball_vy = []
ball_r = []
ball_color = []
special_target_x = []
special_target_y = []
special_target_vx = []
special_target_vy = []
special_target_r = []
special_target_color = []


def new_ball():
    '''создает массивы с данными о каждом шарике'''
    ball_x.append(randint(0, screen_width))
    ball_y.append(randint(0, screen_height))
    ball_r.append(randint(10, 50))
    ball_vx.append(random()*2*difficulty - difficulty)
    ball_vy.append(random()*2*difficulty - difficulty)
    ball_color.append(COLORS[randint(0, 5)])

def new_scpecial_target():
    '''создает массив с данными специальных целей '''
    special_target_x.append(randint(0, screen_width))
    special_target_y.append(randint(0, screen_height))
    special_target_r.append(randint(10, 50))
    special_target_vy.append(random()*2*difficulty - difficulty)
    special_target_vx.append(random()*2*difficulty - difficulty)
    special_target_color.append(COLORS[randint(0, 5)])

def scoreboard(points):
    '''отображает счет на табло'''
    font = pygame.font.Font(None, 25)
    text = font.render("Очки: "+str(points), True, RED)
    screen.blit(text, [screen_width/24, screen_height/24])

for i in range(number_of_balls):
    '''создание шариков'''
    new_ball()

for i in range(number_of_special_targets):
    '''создает специальные цели'''
    new_scpecial_target()

while not finished:
    
    for i in range(number_of_balls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] -ball_x[i])**2 + (event.pos[1] - ball_y[i])**2 <= ball_r[i]**2:
                points = points + 1
                print(points)
                ball_r[i] = 0
                
        ball_x[i] = ball_x[i] + ball_vx[i]
        ball_y[i] = ball_y[i] + ball_vy[i]

        if ball_x[i] < ball_r[i]/2:
            ball_vx[i] = random()*difficulty
            ball_vy[i] = random()*2*difficulty - difficulty

        if ball_x[i] > screen_width - ball_r[i]/2:
            ball_vx[i] = -random()*difficulty
            ball_vy[i] = random()*2*difficulty - difficulty

        if ball_y[i] > screen_height - ball_r[i]/2:
            ball_vx[i] = random()*2*difficulty - difficulty
            ball_vy[i] = -random()*difficulty

        if ball_y[i] < ball_r[i]/2:
            ball_vx[i] = random()*2*difficulty - difficulty
            ball_vy[i] = random()*difficulty

        circle(screen, ball_color[i], (ball_x[i], ball_y[i]), ball_r[i])
    for i in range(number_of_special_targets):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if abs(event.pos[0] - special_target_x[i]) <= special_target_r[i] or abs(event.pos[1] - special_target_y[i]) <= special_target_r[i]:
                special_target_r[i] = 0
                points = points + 2

        if special_target_x[i] < special_target_r[i]/2:
            special_target_vx[i] = random()*difficulty
            special_target_vy[i] = random()*2*difficulty - difficulty

        if special_target_x[i] > screen_width - special_target_r[i]/2:
            special_target_vx[i] = -random()*difficulty
            special_target_vy[i] = random()*2*difficulty - difficulty

        if special_target_y[i] > screen_height - special_target_r[i]/2:
            special_target_vx[i] = random()*2*difficulty - difficulty
            special_target_vy[i] = -random()*difficulty

        if special_target_y[i] < special_target_r[i]/2:
            special_target_vx[i] = random()*2*difficulty - difficulty
            special_target_vy[i] = random()*difficulty

        special_target_x[i] = special_target_x[i] + special_target_vx[i] * (3- 3.8*abs(special_target_x[i] - screen_width/2)/screen_width)
        special_target_y[i] = special_target_y[i] + special_target_vy[i] * (3 - 3.8*abs(special_target_y[i] - screen_height/2)/screen_height)

        polygon(screen, special_target_color[i], 
                        [(special_target_x[i] - special_target_r[i], special_target_y[i] - special_target_r[i]), 
                        (special_target_x[i] + special_target_r[i], special_target_y[i] - special_target_r[i]),
                        (special_target_x[i] + special_target_r[i], special_target_y[i] + special_target_r[i]),
                        (special_target_x[i] - special_target_r[i], special_target_y[i] + special_target_r[i])])
        
    scoreboard(points)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
