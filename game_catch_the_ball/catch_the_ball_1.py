import pygame
from pygame.draw import *
from random import Random, random
from random import randint
import math
pygame.init()

player_name = input()
points = 0
score = 0
screen_width = 1200
screen_height = 800
number_of_balls = 1000
number_of_special_targets = 1000
turnes = 0
difficulty = 10
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
    '''создает массивы с данными о каждом шарике
    ball_x, ball_y - координаты шарика
    ball_r - радиус шарика
    ball_vx, ball_vy - скорость шарика
    ball_color - цвет шарика'''
    ball_x.append(randint(0, screen_width))
    ball_y.append(randint(0, screen_height))
    ball_r.append(randint(5, 15))
    ball_vx.append(random()*2*difficulty - difficulty)
    ball_vy.append(random()*2*difficulty - difficulty)
    ball_color.append(COLORS[randint(0, 5)])


def new_scpecial_target():
    '''создает массив с данными специальных целей
    special_target_x, special_target_y - координаты цели
    special_target_r - половина стороны квадрата цели
    special_target_vx - скорость цели по оси x 
    special_target_vy - скорость цели по оси y
    '''
    special_target_x.append(randint(0, screen_width))
    special_target_y.append(randint(0, screen_height))
    special_target_r.append(randint(10, 50))
    special_target_vy.append(random()*2*difficulty - difficulty)
    special_target_vx.append(random()*2*difficulty - difficulty)
    special_target_color.append(COLORS[randint(0, 5)])

def draw_special_target(x: int, y: int, r: int, color: list):
    '''x, y - координаты  центра специальной цели
    r - радиус специальной цели
    color - цвет специльной цели'''
    polygon(screen, color,
            [(x - r, y - r),(x + r, y - r),(x + r, y + r),(x - r, y + r)])


def scoreboard(text: str , points: int, k: int):
    '''отображает счет на табло
    k - отношение y координаты табло к высоте экрана
    text - надпись на табло
    points - значение, выводимое на табло
    '''
    font = pygame.font.Font(None, 25)
    text = font.render(text+str(points), True, RED)
    screen.blit(text, [screen_width/24, screen_height/k])


for i in range(number_of_balls):
    '''создание шариков
    number_of_balls - количество шариков на экране'''
    new_ball()

for i in range(number_of_special_targets):
    '''создает массивы с характеристиками специальныч целей
    number_of_special targets - количесство специальных целей'''
    new_scpecial_target()

while not finished:
    
    for i in range(number_of_balls):
        '''перебирает все шарики'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            turnes = turnes + 1
            if (event.pos[0] - ball_x[i])**2 + (event.pos[1] - ball_y[i])**2 <= ball_r[i]**2:
                points = points + round(100*((ball_vx[i]**2 + ball_vy[i]**2)**(1/2)/ball_r[i]))

                ball_r[i] = 0

        '''движение шариков'''
        ball_x[i] = ball_x[i] + ball_vx[i]
        ball_y[i] = ball_y[i] + ball_vy[i]

        '''проверка на столкноыение со стенами'''
        if ball_x[i] < ball_r[i]/2:
            ball_vx[i] = random()*difficulty
            ball_vy[i] = random()*2*difficulty - difficulty

        if ball_x[i] > screen_width - ball_r[i]:
            ball_vx[i] = -random()*difficulty
            ball_vy[i] = random()*2*difficulty - difficulty

        if ball_y[i] > screen_height - ball_r[i]:
            ball_vx[i] = random()*2*difficulty - difficulty
            ball_vy[i] = -random()*difficulty

        if ball_y[i] < ball_r[i]/2:
            ball_vx[i] = random()*2*difficulty - difficulty
            ball_vy[i] = random()*difficulty




        '''рисуется шарик'''
        circle(screen, ball_color[i], (ball_x[i], ball_y[i]), ball_r[i])
    for i in range(number_of_special_targets):
        if event.type == pygame.MOUSEBUTTONDOWN:
            turnes = turnes + 1

            '''регистрация попаданий'''
            if abs(event.pos[0] - special_target_x[i]) <= special_target_r[i]  and abs(event.pos[1] - special_target_y[i]) <= special_target_r[i]:
                points = points + 2 * round(300*(((special_target_vx[i])**2 + (special_target_vy[i])**2)**(1/2))/special_target_r[i])
                special_target_r[i] = 0
                special_target_color[i] = BLACK

        '''проверка на выход за пределы экрана'''
        if special_target_x[i] < special_target_r[i]:
            special_target_vx[i] = random()*difficulty
            special_target_vy[i] = random()*2*difficulty - difficulty

        if special_target_x[i] > screen_width - special_target_r[i]:
            special_target_vx[i] = -random()*difficulty
            special_target_vy[i] = random()*2*difficulty - difficulty

        if special_target_y[i] > screen_height - special_target_r[i]:
            special_target_vx[i] = random()*2*difficulty - difficulty
            special_target_vy[i] = -random()*difficulty

        if special_target_y[i] < special_target_r[i]:
            special_target_vx[i] = random()*2*difficulty - difficulty
            special_target_vy[i] = random()*difficulty

        '''движение специальных целей'''
        special_target_x[i] = special_target_x[i] + special_target_vx[i] * \
            (3 - 5*abs(special_target_x[i] - screen_width/2)/screen_width)
        special_target_y[i] = special_target_y[i] + special_target_vy[i] * \
            (3 - 5*abs(special_target_y[i] - screen_height/2)/screen_height)

        draw_special_target(special_target_x[i], special_target_y[i], special_target_r[i], special_target_color[i])

    scoreboard("Очки: ", points, 24)

    score = round(10000*points/(turnes + 1))
    scoreboard("Итоговый счет: ", score, 12)
    pygame.display.update()
    screen.fill(BLACK)

    if turnes == 1000:
        for i in range(number_of_balls):
            ball_r[i] = 0
        for i in range(number_of_special_targets):
            special_target_r[i] = 0
            special_target_color = BLACK
        scoreboard("Конец игры, итоговый счет: ", score, 6)

with open("best_players.txt", 'a') as file:
        file.write(player_name + ":  " + str(score))
        file.write("\n")

pygame.quit()
