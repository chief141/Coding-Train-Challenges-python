import pygame
from sys import exit
import random


width=1000
height=720
fps = 30

black = ( 30, 30, 30)
white = (255,255,255)
gravity = 28
colors = [(240,0,0), (240,240,0), (135,206,210)]

#for display
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("My game")
clock=pygame.time.Clock()

vec = pygame.math.Vector2
class Particle(pygame.sprite.Sprite):
    def __init__(self, x=False, y=False, i=0, color=None):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        if x and y and i:
            self.life = 4
            self.image = pygame.Surface((self.life,self.life))
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            self.firework = False
            self.acc = vec(0,gravity)
            self.vel = vec(0,random.randint(3,6)).rotate(i)
            self.pos = vec(x,y)
            self.rect.center = (x, y)
            self.originated = pygame.time.get_ticks()
            self.last = pygame.time.get_ticks()

        else:
            self.image = pygame.Surface((6,6))
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            self.firework = True
            self.acc = vec(0,random.randint(-180,-120))
            self.vel = vec(0,-12)
            self.pos = vec(random.randint(0, width),610)
            self.rect.center = (self.pos.x, self.pos.y)

    def update(self):
        if self.vel.y >= 2 and self.firework:
            for i in range(1,360,25):#360, 20):
                particles = Particle(self.rect.centerx, self.rect.centery, i, self.color)
                all_sprite.add(particles)

            self.kill()
            particle = Particle(color=random.choice(colors))
            all_sprite.add(particle)


        elif not self.firework :
            if self.life < 1:
                self.kill()


        if self.firework:
            if self.acc.y < 0:
                self.acc += vec(0, gravity)
            else:
                self.acc = vec(0,gravity)
        else:
            if pygame.time.get_ticks() - self.last >= 200:
                self.last = pygame.time.get_ticks()
                self.image = pygame.Surface((self.life, self.life))
                self.image.fill(self.color)
                old_center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = old_center
                self.life -= 1

        self.vel +=  (self.acc * DELTA_TIME)
        self.pos += self.vel
        self.rect.center = self.pos


#sprite groups
all_sprite = pygame.sprite.Group()

for _ in range(3):
    particl = Particle(color=random.choice(colors))
    all_sprite.add(particl)


#game loop
run=True
while run:
    #clock spped
    DELTA_TIME =  clock.tick(fps)/1000

    #input(events)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    #update
    all_sprite.update()

    #Draw/render
    screen.fill(black)
    all_sprite.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()