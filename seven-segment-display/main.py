import pygame
from sys import exit

width=360
height=515
fps = 30
black = (0,0,0)

bar_img_active_horizontal = pygame.image.load('bar.png')
bar_img_active_vertical = pygame.transform.rotate(bar_img_active_horizontal,90)

bar_img_deactive_horizontal = pygame.image.load('bar2.png')
bar_img_deactive_vertical = pygame.transform.rotate(bar_img_deactive_horizontal,90)

#for display
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Display")
clock=pygame.time.Clock()

class Bar(pygame.sprite.Sprite):
	def __init__(self, x,y,active,orientation='horizontal'):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.active = active
		self.image = bar_img_deactive_horizontal
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)
		self.old_active = False
		self.orientation = orientation

	def update(self):
		if self.old_active != self.active:
			self.old_active  = self.active
			if self.orientation == "vertical":
				if self.active: self.image = bar_img_active_vertical
				else: self.image = bar_img_deactive_vertical
			else:
				if self.active: self.image = bar_img_active_horizontal
				else: self.image = bar_img_deactive_horizontal

#sprite groups
all_sprite = pygame.sprite.Group()

bar = Bar(width//2, 30, True)
bar1 = Bar(width//2,height//2, True)
bar2 = Bar(width//2, height - 30, True)

bar3 = Bar(160, 60, True, "vertical")
bar4  = Bar(370, 60, True, "vertical")
bar5 = Bar(160, 290,True,'vertical')
bar6 =  Bar(370,290, True,'vertical')

bars = [bar,bar1,bar2,bar3,bar4,bar5,bar6]
all_sprite.add(bars)

#NUMBERS
NUMBERS = [
	[1, 0, 1, 1, 1, 1, 1],
	[0, 0, 0, 0, 1, 0, 1],
	[1, 1, 1, 0, 1, 1, 0],
	[1, 1, 1, 0, 1, 0, 1],
	[0, 1, 0, 1, 1, 0, 1],
	[1, 1, 1, 1, 0, 0, 1] ,
 	[1, 1, 1, 1, 0, 1, 1],
 	[1, 0, 0, 0, 1, 0, 1],
	[1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 0, 1]
	]

#game loop
current_no = 0
run=True
last_time_changed = pygame.time.get_ticks()
while run:
	#clock spped
	clock.tick(fps)
	
	#input(events)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	#update
	if pygame.time.get_ticks() - last_time_changed >= 1000:
		last_time_changed = pygame.time.get_ticks()
		if current_no == 9 : current_no =  0 
		else : current_no += 1

	i = 0
	for b in bars:
		b.active = NUMBERS[current_no][i]
		i += 1

	all_sprite.update()

	#Draw/render
	screen.fill(black)
	all_sprite.draw(screen)
	pygame.display.flip()

pygame.quit()
exit()