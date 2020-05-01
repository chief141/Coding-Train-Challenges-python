import pygame
from random import randint

width = 600
height = 480
fps = 30


black = (0,0,0)

#for display
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Sprite Animation")
clock=pygame.time.Clock()


# Loading Images
images = [pygame.transform.scale(pygame.image.load(f"img/horse-run-0{i}.png"),(96,72)) for i in range(6)]



class Horse(pygame.sprite.Sprite):
	def __init__(self,place):
		pygame.sprite.Sprite.__init__(self)
		self.image = images[0]
		self.rect = self.image.get_rect()
		self.current_frame = 0
		self.last_changed = pygame.time.get_ticks()
		self.rect.center = (70, 72*place)
		self.pos = self.rect.center
		self.current_frame = 0
		self.speed = randint(1,10)
		if 1 < self.speed <= 3: self.fps = 80
		elif 3 < self.speed <= 5: self.fps = 70
		elif 5 < self.speed <= 7: self.fps = 50
		elif 7 < self.speed <= 10: self.fps = 40
		else :  self.fps = 45
		

	def update(self):
		if pygame.time.get_ticks() - self.last_changed >=  self.fps:
			self.last_changed = pygame.time.get_ticks()
			if self.current_frame == len(images) - 1: self.current_frame = 0
			else: self.current_frame += 1

			self.pos = self.rect.center
			self.image = images[self.current_frame]
			self.rect = self.image.get_rect()
			self.rect.center = self.pos

		self.rect.centerx += self.speed
		if self.rect.left >= width : self.kill()

#sprite groups
all_sprite = pygame.sprite.Group()

for i in range(1,6):
	horse = Horse(i)
	all_sprite.add(horse)

#game loop
run=True
while run:
	#clock spped
	clock.tick(fps)
	
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