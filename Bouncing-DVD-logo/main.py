import pygame

width=800
height=600
fps = 60

#for display
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Bouncing DVD logo")
clock=pygame.time.Clock()

#IMAGE
dvd_image = pygame.image.load('dvd_logo.png')

class Logo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(dvd_image, (68,38))
		self.rect = self.image.get_rect()
		self.image.set_colorkey((0,0,0))
		self.speedx = 120
		self.speedy = 120
		self.last_x_changed = pygame.time.get_ticks()
		self.last_y_changed = pygame.time.get_ticks()

	def get_delta_time(self,delta_time):
			self.delta_time = delta_time

	def update(self):
		if self.rect.right > width or self.rect.left < 0 :
			if pygame.time.get_ticks() - self.last_x_changed >= 1000 : 
				self.speedx = self.speedx * (-1)
				self.last_x_changed = pygame.time.get_ticks()



		if self.rect.bottom > height or self.rect.top < 0 :
			if pygame.time.get_ticks() - self.last_y_changed >= 1000 : 
				self.speedy = self.speedy * (-1)
				self.last_y_changed = pygame.time.get_ticks()
 
		self.rect.centerx += self.speedx * self.delta_time
		self.rect.centery += self.speedy * self.delta_time


#sprite groups
all_sprite = pygame.sprite.Group()

logo = Logo()
all_sprite.add(logo)

#game loop
run=True
while run:
	#clock spped
	delta_time = clock.tick(fps)/1000
	logo.get_delta_time(delta_time)
	#input(events)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	#update
	all_sprite.update()

	#Draw/render
	screen.fill((0,0,0))
	all_sprite.draw(screen)
	pygame.display.flip()


pygame.quit()
quit()
