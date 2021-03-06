
import math
import random

import pygame
from pygame import surface
from pygame import draw
from pygame.constants import K_UP, KEYDOWN, KEYUP, MOUSEMOTION
from pygame.draw import circle, polygon

FPS = 60
number_of_targets = 2
number_of_guns = 3

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, CYAN]

WIDTH = 800
HEIGHT = 600

score = 0
time = 0
targets = []
guns = []
move = True


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        g - ускорение свообжного падения
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = GREEN
        self.live = 30
        self.g = 1
        self.type = random.randint(-3, 1)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.type != 1:
            self.x += self.vx
            self.vy -= self.g
            self.y -= self.vy

        if self.type == 1:
            self.x += self.vx
            self.y -= self.vy

    def draw(self):
        'рисует мячик'
        if self.type == 1:
            self.color = MAGENTA
        if self.type == 2:
            self.color = GREY
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2
           

    def screen_limits(self):
        '''функция проверяет, сталкивается ли шарик со стеной и меняет знак скорости  так,

         чтобы шарики отскакивали от стен'''
        if self.x < self.r and self.vx <= 0:
            self.vx = -self.vx*3/5
        if self.x > WIDTH - self.r and b.vx >= 0:
            self.vx = -self.vx*3/5
        if self.y < self.r and self.vy >= 0:
            self.vy = -self.vy*4/5 - 2
        if self.y > HEIGHT - self.r and b.vy <= 0:
            self.vy = -self.vy*4/5
        if self.y >= HEIGHT - 2*self.r and abs(self.vy) < 0.2:
            self.vy = 0
            self.g = 0
            self.y = HEIGHT - self.r
        if abs(self.vx) < 1.5 and abs(self.x - WIDTH/2) < WIDTH*11/23 - self.r:
            self.r = 0

def new_ball(obj, type):
    'создает новый объект класса Ball, координаты которого совпадают с координитами obj '
    ball_1 = Ball(screen)
    balls.append(ball_1)
    ball_1.vx= random.randint(-20, 20)
    ball_1.vy = random.randint(-20, 20)
    ball_1.type = type                             
    ball_1.x = obj.x
    ball_1.y = obj.y



class Gun:

    def __init__(self, screen, x=200, y=450):
        '''конструктор класса Gun
        Args:
        x , y - координаты объекта
        vx, vy - проекции скоростей объекта
        lenght - длина пушки
        thickness - ширина ствола пушки
        color - цвет пушки
        lives - число жизней пушки
        an - угол наклона пушки
        f2_power - мощность выстрела
        '''
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.lenght = 0
        self.thickness = 10
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.lives = 100

    def fire2_start(self, event):
        'переход в режим стрельбы'
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = Ball(self.screen)
        new_ball.r += 5
        new_ball.x = self.x
        new_ball.y = self.y
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        'функция рисует танк'
        polygon(self.screen, BLACK,
                [[self.x - 50*math.cos(math.pi/4 + self.an), self.y - 50*math.sin(math.pi/4 + self.an)],
                 [self.x - 50*math.cos(math.pi/4 - self.an),
                  self.y + 50*math.sin(math.pi/4 - self.an)],
                 [self.x + 50*math.cos(math.pi/4 + self.an),
                  self.y + 50*math.sin(math.pi/4 + self.an)],
                 [self.x + 50*math.cos(math.pi/4 - self.an), self.y - 50*math.sin(math.pi/4 - self.an)]])

        polygon(self.screen, self.color,
                [[self.x, self.y],
                 [self.x - self.thickness *
                     math.sin(self.an), self.y + self.thickness*math.cos(self.an)],
                 [self.x - self.thickness*math.sin(self.an) + (self.lenght + self.f2_power)*math.cos(self.an),
                 self.y + self.thickness*math.cos(self.an) + (self.lenght + self.f2_power)*math.sin(self.an)],
                 [self.x + (self.lenght + self.f2_power)*math.cos(self.an), self.y + (self.lenght + self.f2_power)*math.sin(self.an)]])

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (50 + obj.r)**2:
            return True
        else:
            return False

    def move_gun(self):
        '''движение пушки, 
        зависит от положения мыши'''
        if event.type == MOUSEMOTION:
            if self.x == event.pos[0]:
                self.an = math.pi/2
            else:
                self.an = math.atan2(
                    (event.pos[1] - self.y), (event.pos[0] - self.x))
        self.vx = 5*math.cos(self.an)
        self.vy = 5*math.sin(self.an)
        self.x += self.vx
        self.y += self.vy

    def power_up(self):
        '''функция регулирует мощность выстрела'''
        if self.f2_on:
            if self.f2_power < 1000:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


def scoreboard(text: str, points: int, y):
    '''отображает счет на табло
    k - отношение y координаты табло к высоте экрана
    text - надпись на табло
    points - значение, выводимое на табло
    y - координата табло
    '''
    font = pygame.font.Font(None, 25)
    text = font.render(text+str(points), True, RED)
    screen.blit(text, [WIDTH/24, y])


class Target:
    def __init__(self, screen):
        '''points - число уничтоженных мишеней
        vx, vy - проекции скоростей на соотвествующие оси
        type - тип мишени'''
        self.points = 0
        self.new_target()
        self.screen = screen
        self.vy = 3
        self.vx = 0
        self.type = random.randint(0, 3)

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = random.randint(0, 780)
        y = self.y = random.randint(300, 550)
        r = self.r = random.randint(2, 50)
        color = self.color = RED
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        '''рисует цель'''
        if self.type == 1:
            self.color = BLACK
        circle(screen, self.color, (self.x, self.y), self.r)

    def move_target(self):
        '''функция отвечает за движение мишени'''
        if self.type == 1:
            self.vx = 10*math.sin(time/2)
        self.y += self.vy
        self.x += self.vx

        if self.y <= self.r or self.y >= HEIGHT - self.r:
            self.vy = -self.vy

            
def new_ball(obj, type):
    'создает новый объект класса Ball, координаты которого совпадают с координитами obj '
    ball_1 = Ball(screen)
    balls.append(ball_1)
    ball_1.vx= random.randint(-20, 20)
    ball_1.vy = random.randint(-20, 20)
    ball_1.type = type                             
    ball_1.x = obj.x
    ball_1.y = obj.y


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
gun = Gun(screen)
gun_2 = Gun(screen)
gun_2.x = random.randint(0, 500)

finished = False
balls = []
for i in range(number_of_targets):
    target = Target(screen)
    target.new_target()
    targets.append(target)

while not finished:

    screen.fill(WHITE)
    scoreboard("Очки: ", score, 50)
    scoreboard("Жизни: ", gun.lives, 100)
    gun.draw()
    gun_2.draw()
    for target in targets:
        target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)               
    time += 1

    if time % 100 == 0:
        new_ball(gun_2, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        if event.type == KEYDOWN and event.key == K_UP:
            move = True
        if event.type == KEYDOWN:
            move = False
        if move:
            gun.move_gun() 

    for b in balls:
        b.move()
        for target in targets:
            if b.hittest(target) and target.live == 1:
                target.live = 0
                target.hit()
                target.new_target()
                score += 1
        b.screen_limits()
   

    for target in targets:
        target.move_target()
        if gun.hittest(target) and target.type == 1:
            gun.lives -= 1
        for b in balls:
            if gun.hittest(b) and b.type == 2:
                gun.lives -= 1
    
    if gun.lives <= 0:
        screen.fill(WHITE)
        scoreboard("вы проиграли ", score)
        pygame.display.update()

        clock.tick(1/10)
        break

    gun.power_up()

screen.fill(WHITE)

pygame.quit()
