string_a = " Length of bars are propotional to the number of times that digit"
string_b = "is repeated in the first One Million Digits of PI (estimated time=50seconds)"

import pygame
from sys import exit
from pygame.locals import *

width = min_width = 1000
height = min_height = 600
fps = 100

black = (0,0,0)
white = (255,255,255)
red = (255,28,28)

#for display
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height),pygame.RESIZABLE)
pygame.display.set_caption("VISUALIZiING PI")
clock=pygame.time.Clock()

file = "one-million-digits-pi.txt"

with open(file, 'r') as f:
    data = f.read()[2:]

chars = [int(i) for i in data[:-1]]

frequency = [i * 0 for i in range(10)]


# Positions of circles
pos = [[i*width//12, height//2] for i in range(1,11)]

def draw_text(surf,text,size,x,y,color=white):
    font_name=pygame.font.match_font('aerial')
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,color)
    text_rect=text_surface.get_rect()
    text_rect.center=(x,y)
    surf.blit(text_surface,text_rect)

class Bar(pygame.sprite.Sprite):
    def __init__(self, i):
        global pos
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width//15, 1))
        self.rect = self.image.get_rect()
        self.image.fill(red)
        self.i = i
        self.rect.left = pos[self.i][0] - width//30
        self.rect.bottom = 95/100*height
        self.per = 0
        self.j = 0

    def update(self, j, total):
        global pos, max_per
        self.j = j
        if self.per == max_per:color = white
        else:color = red
        self.per = (j/total)*100
        h = map_(self.per,0,max_per,0,(height- (2/10*height)))
        pers.append(self.per)
        self.image = pygame.Surface((width//15, h))
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.rect.left = pos[self.i ][0] - width//30
        self.rect.bottom = 95/100*height


def map_(value, start1, stop1, start2, stop2):
    outgoing = start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))
    return outgoing

all_sprite = pygame.sprite.Group()
bars = [Bar(i) for i in range(10)]
all_sprite.add(bars)

#game loop
screen.fill(black)
run=True
i = -1
plus_i = True
fullscreen = False
max_per  = 1
drawn_time = pygame.time.get_ticks()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:

            if event.h < min_height: height = min_height
            else:height = event.h

            if event.w < min_width: width = min_width
            else: width = event.w

            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            pos = [[i*event.w//11, event.h//2] for i in range(1,11)]

    for _ in range(200):
        pers = []
        if i >= len(chars) - 1: plus_i = False
        if plus_i: i += 1

        if plus_i:
            char = chars[i]
            frequency[char-1] += 1

            for k,bar in enumerate(bars):
                bar.update(frequency[k], i+1)
            max_per = max(pers)

    screen.fill(black)
    all_sprite.draw(screen)
    if not pygame.time.get_ticks() - drawn_time >= 10000:
        draw_text(screen, string_a, 22,width//2, 10)
        draw_text(screen, string_b, 22,width//2, 25)

    draw_text(screen,"Number of digits counted : "+ str(i), 22,150,10)

    for l in range(10):
        b = bars[l]
        draw_text(screen,str(l),22, b.rect.centerx, b.rect.bottom + 8)
        draw_text(screen,str(b.j) + " times",22, b.rect.centerx, b.rect.bottom + 25)
    pygame.display.flip()

pygame.quit()
exit()