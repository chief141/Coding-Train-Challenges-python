import pygame
from random import randint

width=640
height=360
fps = 60

#for display
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Purple Rain")
clock=pygame.time.Clock()


class Rain(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.z = randint(3,10)
		self.len = 1/self.z * 60
		if self.z >= 7:   self.width = 1
		elif self.z >= 5: self.width = 2
		else:			  self.width = 3	
		self.image = pygame.Surface((self.width,self.len))
		self.rect = self.image.get_rect()
		self.image.fill((138, 43, 226))

		self.speedy = 1/self.z * 2500
		self.rect.centerx = randint(5,width)
		self.rect.centery = randint(-500,-30)
		self.gravity = 6 * 1/self.z


	def get_delta_time(self,delta_time):
			self.delta_time = delta_time

	def update(self):
		if self.rect.top > height : 
			self.kill()
			rain = Rain()
			all_sprite.add(rain)
			drops.append(rain)

		self.speedy += self.gravity
		self.rect.centery += self.speedy * self.delta_time



#sprite groups
drops = []
all_sprite = pygame.sprite.Group()

for _ in range(500):
	rain = Rain()
	all_sprite.add(rain)
	drops.append(rain)

#game loop
run=True
while run:
	#clock spped
	delta_time = clock.tick(fps)/1000
	for r in drops:
		r.get_delta_time(delta_time)
	#input(events)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	#update
	all_sprite.update()

	#Draw/render
	screen.fill((230, 230, 250))
	all_sprite.draw(screen)
	pygame.display.flip()


pygame.quit()
quit()
