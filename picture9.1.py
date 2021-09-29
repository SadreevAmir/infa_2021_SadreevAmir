import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((800, 1000))
#background
polygon(screen, (255, 255, 255), [(0, 0), (1000, 0), (1000, 1200),(0, 1200), (0, 0)])
polygon(screen, (136, 206, 250), [(0, 0), (0, 650), (1000, 650),(1000, 0), (0, 0)])
polygon(screen, (0, 0, 0), [(0, 650), (1000, 650), (1000, 651),(0, 651), (0, 650)])
#sun
def sun(x, y, r, d):
    circle(screen, (254, 240,0, 1), (x, y), r, d)
    rect(screen, (254, 240, 0, 1), [x - r/5, y - r, 2/5*r, 2*r])
    rect(screen, (254, 240, 0, 1), [x - r, y - r/5, 2*r, 2/5*r])
#bear
def bear(x, y, d):
    #body
    ellipse(screen, (255, 255, 255), [x - d, y - 2*d, 2*d, 4*d])
    ellipse(screen, (0, 0, 0), [x - d, y - 2*d, 2*d, 4*d], 1)
    #leg2
    ellipse(screen, (255, 255, 255), [x , y + d, 2*d, 3/2*d])
    ellipse(screen, (0, 0, 0), [x , y + d, 2*d, 3/2*d], 1)
    #head
    ellipse(screen, (255, 255, 255), [x , y - 5/2*d, 2*d, 3/2*d])
    ellipse(screen, (0, 0, 0), [x , y - 5/2*d, 2*d, 3/2*d], 1)
    #leg2
    ellipse(screen, (255, 255, 255), [x + 3/2*d , y + 2*d, d, 1/2*d])
    ellipse(screen, (0, 0, 0), [x + 3/2*d  , y + 2*d, d, 1/2*d], 1)
    #eyes
    circle(screen, (0, 0, 0), (x + d, y - 2*d), d/10)
    circle(screen, (0, 0, 0), (x  + 15/8*d, y - 2*d), d/10)
    #ear
    ellipse(screen, (255, 255, 255), [x + d/4 , y - 5/2*d, d/3, d/2])
    ellipse(screen, (0, 0, 0), [x + d/4 , y - 5/2*d, d/3, d/2], 1)
    #arm
    ellipse(screen, (255, 255, 255), [x + d*2/3, y - d/2, d, 1/2*d])
    ellipse(screen, (0, 0, 0), [x + d*2/3, y - d/2, d, 1/2*d], 1)
    #mouth
    polygon(screen, (0, 0, 0), [(x + d/2, y - 3/2*d), (x + 3/2*d, y - 3/2*d), (x + 3/2*d, y - 3/2*d + 1),(x + d/2, y - 3/2*d + 1), (x + d/2, y - 3/2*d)])
     #ice hole
    ellipse(screen, (66, 49, 137), [x + d*4.8, y + d*1.5,1.5*d, 3/4*d])
    ellipse(screen, (44, 146, 242), [x + d*5, y + d*1.7, d, 1/2*d])
    #fishing rod
    arc(screen, (0, 0, 0), [x + 3/2*d, y - 2*d, 5*d, 5*d], 1, 3 , 5)
    aaline(screen, (0, 0, 0), [x + 5.36*d, y + 2*d], [x + 5.36*d, y - 1.6*d], 3)
    #fish
    ellipse(screen, (255, 0, 0), [x + d*5, y + d*2.5, 0.5*d, 1/4*d])
    polygon(screen, (100, 0, 0), [(x + 5*d, y + 2.6*d), (x + 4.8*d, y + 2.7*d), (x + 4.8*d, y + 2.5*d),(x + 5*d, y + 2.6*d)])
    circle(screen, (254, 240,0, 1), (x + 5.3*d, y + 2.6*d), d/20)




bear(105, 600, 100)
sun(680, 150, 100, 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
