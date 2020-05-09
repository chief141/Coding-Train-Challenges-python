import pygame
from random import randint
from sys import exit
from math import ceil

width = 640
height = 360
fps = 60

black = (0,0,0)
background = (230, 230, 250)
rain_color = (138, 43, 226)

#for display
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Purple Rain")
clock=pygame.time.Clock()

def map_(value, start1, stop1, start2, stop2):
    outgoing = start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))
    return outgoing

def draw_text(surf,text,size,x,y,color=black):
	font_name=pygame.font.match_font('aerial')
	font=pygame.font.Font(font_name,size)
	text_surface=font.render(text,True,color)
	text_rect=text_surface.get_rect()
	text_rect.center=(x,y)
	surf.blit(text_surface,text_rect)

class Rain(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.z = randint(1,100)
		self.len = int(map_(self.z, 0,100, 17,2))
		self.width = int(map_(self.z, 1,100,3,1))

		self.image = pygame.Surface((self.width,self.len))
		self.rect = self.image.get_rect()
		self.image.fill(rain_color)

		self.speedy = map_(self.z, 1, 100,580,350)
		self.rect.centerx = randint(5,width)
		self.rect.centery = randint(-500,-30)
		self.gravity = map_(self.z, 1,100,2, 0.4 )

	def update(self):
		global delta_time
		self.delta_time = delta_time

		if self.rect.top > height :
			self.kill()
			rain = Rain()
			all_sprite.add(rain)
			drops.append(rain)

		mouse_x = pygame.mouse.get_pos()[0]
		self.speedy = map_(mouse_x, 0, width , ceil(self.speedy- self.speedy/35), self.speedy + self.speedy/50)
		self.speedy += self.gravity
		self.rect.centery += (self.speedy * self.delta_time)

#sprite groups
drops = []
all_sprite = pygame.sprite.Group()

for _ in range(500):
	rain = Rain()
	all_sprite.add(rain)
	drops.append(rain)

#game loop
show_text = pygame.time.get_ticks()
run = True
while run:
	#print(clock.get_fps())
	delta_time = clock.tick(fps)/1000

	#input(events)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	#update
	all_sprite.update()

	#Draw/render
	screen.fill(background)
	all_sprite.draw(screen)
	if not pygame.time.get_ticks() - show_text >= 5000:
		draw_text(screen, 'Move your mouse LEFT and RIGHT', 25, width/2,15)
	pygame.display.flip()

pygame.quit()
exit()
