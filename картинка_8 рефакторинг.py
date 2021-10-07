import pygame
from pygame import color
from pygame.draw import *

pygame.init()
def draw_background(wall_color, floor_color):
    '''
    функция рисует пол и стену
    wall_color - цвет стены
    floor_color - цвет пола
    '''
    pygame.draw.polygon(screen, wall_color,
                        [(0, 0), (0, 300), (700, 300), (700, 0)])
    pygame.draw.polygon(screen, floor_color, [
                        (0, 300), (0, 700), (700, 700), (700, 300)])


def draw_tail(tail_x, tail_y, tail_height, tail_lenght, body_color):
    '''
    функция рисует хвост кошки
    tail_x , tail_y - координаты хвоста
    tail_height - толщина хвоста
    tail_lenght - длина хвоста
    body_color - цвет хвоста
    '''
    ellipse(screen, WHITE,
            [tail_x, tail_y, tail_lenght, tail_height], 2)
    ellipse(screen, body_color,
            (tail_x, tail_y, tail_lenght, tail_height))


def draw_body(x, y, height, lenght, body_color):
    '''
    функция рисует туловище кошки
    x , y - координаты кошки
    height - высота туловища
    lenght - длина туловища кошки
    body_color - цвет туловища кошки
    '''
    ellipse(screen, body_color,
            (x - abs(lenght/2), y - height/2, abs(lenght), height))
    ellipse(screen, WHITE,
            [x - abs(lenght/2), y - height/2, abs(lenght), height], 2)


def draw_head(head_x, head_y, head_size, body_color):
    '''
    функция рисует голову кошки
    x , y - координаты кошки
    height - высота туловища
    lenght - длина туловища кошки
    body_color - цвет туловища кошки
    '''
    circle(screen, body_color,
           (head_x, head_y), head_size)
    circle(screen, WHITE,
           (head_x, head_y), head_size, 2)


def draw_legs(x, y, height, lenght, body_color):
    '''
    функция рисует лапы кошки
    x , y - координаты кошки
    height - высота туловища
    lenght - длина туловища кошки
    body_color - цвет туловища кошки
    '''
    ellipse(screen, WHITE,
            [x - 13/20 * lenght + 6/5 * lenght / 6, y - 5/4 * height/5 - height/2 + 5/4 * height * 6 / 7, 6/5 * lenght / 5, 5/4 * height / 5], 2)
    ellipse(screen, WHITE,
            [x - 13/20 * lenght + 6/5 * lenght / 20, y - 5/4 * height/5 - height/2 + 5/4 * height / 2, 6/5 * lenght / 8, 5/4 * height / 2], 2)
    circle(screen, WHITE,
           (x - 13/20 * lenght + 5 * 6/5 * lenght / 6, y - 5/4 * height/5 - height/2 + 4 / 5 * 5/4 * height), 5/4 * height / 4, 2)
    ellipse(screen, body_color,
            (x - 9/20 * lenght, y + 9/28 * height, 6/25 * lenght, 1/4 * height))
    ellipse(screen, body_color,
            (x - 13/20 * lenght + 6/5 * lenght / 20, y - 5/4 * height/5 - height/2 + 5/4 * height / 2, 6/5 * lenght / 8, 5/4 * height / 2))
    circle(screen, body_color,
           (x - 13/20 * lenght + 5 * 6/5 * lenght / 6, y - 5/4 * height/5 - height/2 + 4 / 5 * 5/4 * height), 5/4 * height / 4)

def draw_eyes(x, y, height, lenght, eye_color):
    '''функция рисует глаза кошки
    x , y - координаты кошки
    height - высота туловища
    lenght - длина туловища кошки
    body_color - цвет туловища кошки
    '''
    circle(screen, eye_color,
           (x - 37/100 * lenght, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 10), 5/4 * height / 14)
    circle(screen, eye_color,
           (x - 53/100 * lenght, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 10), 5/4 * height / 14)
    circle(screen, BLACK,
           (x - 37/100 * lenght, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 10), 5/4 * height / 14, 1)
    circle(screen, BLACK,
           (x - 53/100 * lenght, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 10), 5/4 * height / 14, 1)
    ellipse(screen, BLACK,
            (x - 37/100 * lenght + 6/5 * lenght / 100, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 10 - 5/4 * height / 20, 6/5 * lenght / 100, 5/4 * height / 10))
    ellipse(screen, BLACK,
            (x - 53/100 * lenght + 6/5 * lenght / 100, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 10 - 5/4 * height / 20, 6/5 * lenght / 100, 5/4 * height / 10))


def draw_ears(x, y, height, lenght, body_color):
    '''функция рисует уши кошки
    x , y - координаты кошки
    height - высота туловища
    lenght - длина туловища кошки
    body_color - цвет туловища кошки
    '''
    pygame.draw.polygon(screen, WHITE,
                        [(x - 13/20 * lenght + (0.316 * 6/5 * lenght) * 2 / 3, y - 5/4 * height/5 - height/2 + 0.19 * 5/4 * height), (x - 13/20 * lenght + (0.44 * 6/5 * lenght) * 2 / 3, y - 5/4 * height/5 - height/2 + 0.314 * 5/4 * height),
                         (x - 13/20 * lenght + (0.45 * 6/5 * lenght) * 2 / 3, y - 5/4 * height/5 - height/2 + 0.1 * 5/4 * height)], 4)
    pygame.draw.polygon(screen, body_color,
                        [(x - 13/20 * lenght + (0.316 * 6/5 * lenght) * 2 / 3, y - 5/4 * height/5 - height/2 + 0.19 * 5/4 * height), (x - 13/20 * lenght + (0.44 * 6/5 * lenght) * 2 / 3, y - 5/4 * height/5 - height/2 + 0.314 * 5/4 * height),
                         (x - 13/20 * lenght + (0.45 * 6/5 * lenght) * 2 / 3, y - 5/4 * height/5 - height/2 + 0.1 * 5/4 * height)])
    pygame.draw.polygon(screen, WHITE,
                        [(x - 13/20 * lenght + 6/5 * lenght / 10, y - 5/4 * height/5 - height/2 + 0.19 * 5/4 * height), (x - 13/20 * lenght - (0.12 * 6/5 * lenght) * 2 / 3 + 6/5 * lenght / 10, y - 5/4 * height/5 - height/2 + 0.314 * 5/4 * height),
                         (x - 13/20 * lenght - (0.17 * 6/5 * lenght) * 2 / 3 + 6/5 * lenght / 10, y - 5/4 * height/5 - height/2 + 0.1 * 5/4 * height)], 5)
    pygame.draw.polygon(screen, body_color,
                        [(x - 13/20 * lenght + 6/5 * lenght / 10, y - 5/4 * height/5 - height/2 + 0.19 * 5/4 * height), (x - 13/20 * lenght - (0.12 * 6/5 * lenght) * 2 / 3 + 6/5 * lenght / 10, y - 5/4 * height/5 - height/2 + 0.314 * 5/4 * height),
                         (x - 13/20 * lenght - (17/100 * 6/5 * lenght) * 2 / 3 + 6/5 * lenght / 10, y - 5/4 * height/5 - height/2 + 0.1 * 5/4 * height)])
    pygame.draw.polygon(screen, WHITE,
                        [(x - 13/20 * lenght + 6/5 * lenght / 6 + 6/5 * lenght / 50, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 50), (x - 13/20 * lenght + 6/5 * lenght / 6 - 6/5 * lenght / 50, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 50),
                         (x - 13/20 * lenght + 6/5 * lenght / 6, y - 5/4 * height/5 - height/2 + 5/4 * height / 2)], 2)


def draw_moustache(x, y, height, lenght):
    '''функция рисует усы кошки
    x , y - координаты кошки
    height - высота туловища
    lenght - длина туловища кошки'''

    for i in range(5):
        pygame.draw.line(screen, WHITE, (x - 13/20 * lenght + 6/5 * lenght / 6 + 6/5 * lenght / 30, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 + 5/4 * height / 20 + 5/4 * height / 50 * i),
                         (x - 13/20 * lenght + 6/5 * lenght / 6 + 6/5 * lenght / 4, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 30 + 5/4 * height / 20 + 5/4 * height / 35 * i), 1)
        pygame.draw.line(screen, WHITE, (x - 13/20 * lenght + 6/5 * lenght / 6 - 6/5 * lenght / 30, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 + 5/4 * height / 20 + 5/4 * height / 50 * i),
                         (x - 13/20 * lenght + 6/5 * lenght / 6 - 6/5 * lenght / 4, y - 5/4 * height/5 - height/2 + 5/4 * height / 2 - 5/4 * height / 30 + 5/4 * height / 20 + 5/4 * height / 35 * i), 1)
        ellipse(screen, WHITE,
                (x - 13/20 * lenght + 6/5 * lenght / 6, y - 5/4 * height/5 - height/2 + 5/4 * height / 2, 2, 5/4 * height / 8), 2)


def draw_ball(x, y, ball_color, r, direction):
    '''
    функция рисует клубок 
    x, y - координаты центра 
    lenghtall_color - цвет клубка
    r - радиус клубка
    direction - напрвление нити клубка ( может принимать значения +1 (влево) или -1 (вправо)) 
    '''
    circle(screen, ball_color, (x, y), r)
    circle(screen, WHITE, (x, y), r, 2)
    for i in range(3):
        pygame.draw.line(screen, WHITE, (x, y - 4 / 5 * r + i * r / 4),
                         (x + r / 4 + i * r / 4, y - r / 2 + i * r / 4))
        pygame.draw.line(screen, WHITE, (x - r / 2, y + r / 2 -
                         r / 4 * i), (x + r / 3, y + r * 2 / 3 - r / 5 * i))
    pygame.draw.lines(screen, WHITE, False, [(x + 1.41 / 2 * r * direction, y + 1.41 / 2 * r), (x + r * direction, y + r),
                                             (x + (1.41 / 2 + 1) * r *
                                              direction, y + 1.41 / 2 * r),
                                             (x + 2 * r * direction, y + r)])


def draw_window(x, y, window_color, lenght, height):
    ''' 
    функция рисует окно
    x, y - координаты левогго нижнего угла окна
    window_color - цвет оконных рам
    lenght - ширина окна
    height - высота окна
    '''
    pygame.draw.polygon(screen, window_color, [
                        (x, y), (x, y + height), (x + lenght, y + height), (x + lenght, y)])
    pygame.draw.polygon(screen, BLUE, [(x + 1 / 13 * lenght, y + 1 / 13 * height), (x + 1 / 13 * lenght, y + 1 / 13 * height + 3 / 13 * height),
                                       (x + 1 / 13 * lenght + lenght * 5 / 13,
                                        y + 1 / 13 * height + 3 / 13 * height),
                                       (x + 1 / 13 * lenght + lenght * 5 / 13, y + 1 / 13 * height)])
    pygame.draw.polygon(screen, BLUE, [(x + 7 / 13 * lenght, y + 1 / 13 * height), (x + 7 / 13 * lenght, y + 1 / 13 * height + 3 / 13 * height),
                                       (x + 7 / 13 * lenght + lenght * 5 / 13,
                                        y + 1 / 13 * height + 3 / 13 * height),
                                       (x + 7 / 13 * lenght + lenght * 5 / 13, y + 1 / 13 * height)])
    pygame.draw.polygon(screen, BLUE, [(x + 1 / 13 * lenght, y + 5 / 13 * height), (x + 1 / 13 * lenght, y + 5 / 13 * height + 7 / 13 * height),
                                       (x + 1 / 13 * lenght + lenght * 5 / 13,
                                        y + 5 / 13 * height + 7 / 13 * height),
                                       (x + 1 / 13 * lenght + lenght * 5 / 13, y + 5 / 13 * height)])
    pygame.draw.polygon(screen, BLUE, [(x + 7 / 13 * lenght, y + 5 / 13 * height), (x + 7 / 13 * lenght, y + 5 / 13 * height + 7 / 13 * height),
                                       (x + 7 / 13 * lenght + lenght * 5 / 13,
                                        y + 5 / 13 * height + 7 / 13 * height),
                                       (x + 7 / 13 * lenght + lenght * 5 / 13, y + 5 / 13 * height)])


def draw_cat(x, y, lenght, height, body_color, eye_color):
    '''
    функция рисует кошку
    x , y - координаты кошки
    lenght - длина туловища
    height - высота туловища
    body_color - цвет кошки
    eye_color - цвет глаз кошки
    '''
    draw_tail(x - 3/10 * lenght, y - height, 5 /
              12 * height, 2/5 * lenght, body_color)
    draw_legs(x - 13/20 * lenght, y - 5/4 * height/5 -
              height/2, 5/4 * height, 6/5 * lenght, body_color)
    draw_body(x - 13/20 * lenght, y - 5/4 * height/5 -
              height/2, 5/4 * height, 6/5 * lenght, body_color)
    draw_head(x - 12/10 * lenght, y - 31/30*height, 5/12 * height, body_color)
    draw_eyes(x - 13/20 * lenght, y - 5/4 * height/5 -
              height/2, 5/4 * height, 6/5 * lenght, eye_color)
    draw_ears(x - 13/20 * lenght, y - 5/4 * height/5 -
              height/2, 5/4 * height, 6/5 * lenght, body_color)
    draw_moustache(x - 13/20 * lenght, y - 5/4 * height /
                   5 - height/2, 5/4 * height, 6/5 * lenght)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (204, 229, 252)
BLUE = (50, 148, 240)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
BROWN = (134, 77, 28)
LIGHT_GREEN = (134, 153, 28)
pi = 3.1415
FPS = 30
screen = pygame.display.set_mode((700, 700))


draw_background(BROWN, LIGHT_GREEN)

draw_cat(300, 400, 100, 50, GRAY, GREEN)
draw_cat(500, 600, 150, 100, GRAY, GREEN)
draw_cat(400, 500, -150, 100, GRAY, GREEN)

draw_ball(400, 400, GREEN, 30, -1)
draw_ball(650, 400, GREEN, 20, 1)
draw_ball(200, 450, GREEN, 30, 1)
draw_ball(100, 550, GREEN, 30, -1)
draw_ball(600, 600, GREEN, 60, 1)
draw_window(100, 50, LIGHT_GREEN, -200, 200)
draw_window(400, 50, LIGHT_GREEN,  -200, 200)
draw_window(650, 50, LIGHT_GREEN, -200, 200)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
