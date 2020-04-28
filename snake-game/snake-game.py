import pygame
from random import randint
from sys import exit

tile_size = 20
width = tile_size  * 30 #600
height = tile_size * 24 #480
fps = 30

#for display
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#Snake class
class Snake(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((tile_size, tile_size))
		self.image.fill((255,255,255))
		self.rect = self.image.get_rect()
		self.dir = "RIGHT"
		self.last_moved = pygame.time.get_ticks()
		self.kill_ = False
		
	def update(self):
		keystate = pygame.key.get_pressed()

		if keystate[pygame.K_UP] or keystate[pygame.K_w] and not self.dir == "DOWN":
			self.dir = "UP"
		elif keystate[pygame.K_DOWN] or keystate[pygame.K_s] and not self.dir == "UP":
			self.dir = "DOWN"

		if keystate[pygame.K_LEFT] or keystate[pygame.K_a] and not self.dir == "RIGHT":
			self.dir = "LEFT"
		elif keystate[pygame.K_RIGHT] or keystate[pygame.K_d] and not self.dir == "LEFT":
			self.dir = "RIGHT"

			

		self.move()
		self.collide()

	def move(self):
		global body_no

		if pygame.time.get_ticks() - self.last_moved >= 200:
			self.last_moved = pygame.time.get_ticks()

			if self.dir == "UP":
				self.rect.centery -= tile_size
			elif self.dir == "DOWN":
				self.rect.centery += tile_size

			elif self.dir == "LEFT":
				self.rect.centerx -= tile_size
			else:
				self.rect.centerx += tile_size

			player_pos.append([self.rect.left, self.rect.top])
			body_no += 1
			for b in body_sprite:
				b.update()
			
	def collide(self):
		if self.rect.right > width:
			self.kill_ = True
		elif self.rect.left < 0:
			self.kill_ = True

		if self.rect.top < 0:
			self.kill_ = True
		elif self.rect.bottom > height:
			self.kill_ = True

		if self.kill_ or pygame.sprite.spritecollide(snake,body_sprite,False):
			print();print("Your Score is :",food_eaten);print()
			
			self.kill()
			exit()

class Food(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((tile_size, tile_size))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.rect.top = randint(0,23) * tile_size
		self.rect.left = randint(0,29) * tile_size

class Body(pygame.sprite.Sprite):
	def __init__(self, number):
		global minus_body
		pygame.sprite.Sprite.__init__(self)
		self.no = number - minus_body
		minus_body += 1
		self.image = pygame.Surface((tile_size, tile_size))
		self.rect = self.image.get_rect()
		self.image.fill((255,255,255))
		self.rect.left = player_pos[self.no][0]
		self.rect.top = player_pos[self.no][1]

	def update(self):
		self.no += 1
		self.rect.left = player_pos[self.no][0]
		self.rect.top = player_pos[self.no][1]		

def spawn_food():
	global food
	food = Food()
	all_sprite.add(food)
	food_sprite.add(food)

all_sprite = pygame.sprite.Group()
food_sprite = pygame.sprite.Group()
body_sprite = pygame.sprite.Group()

player_pos = []
body_no = -1
minus_body = 1
food_eaten = 0

spawn_food()
snake = Snake()
all_sprite.add(snake)


print();print("Use Arrow or WASD keys to play");print();print("Score :",food_eaten)
#GAMELOOP
run = True
while run:
	clock.tick(fps)
	#pygame.display.set_caption(str(clock.get_fps()))

	#FOR QUITING
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	#SPrite collision
	if pygame.sprite.spritecollide(snake,food_sprite, True):
		food_eaten += 1
		spawn_food()
		body = Body(body_no)
		body_sprite.add(body)
		print("Score :",food_eaten)
	if pygame.sprite.spritecollide(food,body_sprite,False):
		spawn_food()

# UPdate section _____________________
	all_sprite.update()

# Draw section ___________________
	screen.fill((0,0,0))
	body_sprite.draw(screen)
	all_sprite.draw(screen)
	pygame.display.flip()

pygame.quit()
quit()
