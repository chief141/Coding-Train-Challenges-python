import pygame
from sys import exit
from random import choice

width=600
height=480
fps = 30

black = (0,0,0)
white = (255,255,255)
blue = (65,105,225)

#for display
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong Game")
clock=pygame.time.Clock()

#defining a function for text
def draw_text(surf,text,size,x,y,color=white):
	font_name=pygame.font.match_font('aerial')
	font=pygame.font.Font(font_name,size)
	text_surface=font.render(text,True,color)
	text_rect=text_surface.get_rect()
	text_rect.center=(x,y)
	surf.blit(text_surface,text_rect)

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30,30))
		#self.image.fill((255,0,0))
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.center = (width//2, height//2)
		self.speedx = choice([-7,-6,-5,5,6,7])
		self.speedy = choice([-7,-6,-5,5,6,7])
		self.last_hit =  0
		self.create_new_self =False
		self.first = True

	def update(self):
		global current_ball
		self.rect.centerx += self.speedx
		self.rect.centery += self.speedy

		if self.rect.top < 0 or self.rect.bottom > height:
			self.speedy *= -1

		hits = pygame.sprite.spritecollide(self, player_sprite,False)
		if pygame.time.get_ticks() - self.last_hit >= 500 or self.first:
			if hits:
				self.speedx *= -1
				self.last_hit =  pygame.time.get_ticks()
				self.first = False
				self.speedx += choice([-2,-1,1,2])

		if self.rect.left >= width :
			players[0].score += 1
			self.create_new_self = True

		elif  self.rect.right <= 0:
			players[1].score += 1
			self.create_new_self = True

		if self.create_new_self:
			self.create_new_self = False
			self.kill()
			ball = Ball()
			all_sprite.add(ball)
			balls.append(ball)
			current_ball += 1

class Player(pygame.sprite.Sprite):
	def __init__(self, player_number):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((20,70))
		self.image.fill(white)
		self.rect  = self.image.get_rect()
		if player_number == 0 : self.rect.center = (25,height//2)
		else: self.rect.center = (width - 30, height//2)
		self.number = player_number
		self.speed = 7
		self.score = 0

	def update(self):
		keystate = pygame.key.get_pressed()

		if self.number == 0:
			if keystate[pygame.K_w]:
				self.rect.centery -= self.speed
			elif keystate[pygame.K_s]:
				self.rect.centery += self.speed
		else:
			if keystate[pygame.K_UP]:
				self.rect.centery -= self.speed
			elif keystate[pygame.K_DOWN]:
				self.rect.centery += self.speed

		if self.rect.top <= 0:
			self.rect.top = 0
		elif self.rect.bottom >= height:
			self.rect.bottom = height


#sprite groups
all_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()

players = [Player(i) for i in range(2)]

player_sprite.add(players)
all_sprite.add(players)

balls = []
ball = Ball()
all_sprite.add(ball)
balls.append(ball)
current_ball =  0

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
	pygame.draw.circle(screen, (255,0,0), (balls[current_ball].rect.centerx, balls[current_ball].rect.centery), 15 )
	draw_text(screen, str(players[0].score), 25, 20,50,blue)
	draw_text(screen, str(players[1].score), 25, width -20,50,blue)
	pygame.display.flip()

pygame.quit()
exit()