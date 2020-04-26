import pygame
from os import path

width = 600
height = 480
fps =  60

#for display
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Making a GIF loop")
clock = pygame.time.Clock()

current_angle = 0

#MAKING AN RECT(IMAGE)
image_orig = pygame.Surface((150,150))
image_orig.set_colorkey((0,0,0))
image_orig.fill((255,255,255))

#COPYING 
image = image_orig.copy()
image.set_colorkey((0,0,0))
rect = image.get_rect()
rect.center = (width//2, height//2)


#Game loop
run = True
while run:
	clock.tick(fps)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill((0,0,0)) #FILL SCREEN

	#ADDING AMGLES
	if current_angle >= 360:current_angle = 0
	else: current_angle -= 1

	old_center  = rect.center #SAVING OLD CENTER

	new_image = pygame.transform.rotate(image_orig, current_angle) #ROTATING A CENTER
	rect = new_image.get_rect() #GETTING NEW RECT
	rect.center = old_center   #PlACING NEW RECT AT OLD POSITION

	screen.blit(new_image,rect)  #BLITING ON SCREEN
	pygame.display.flip()


pygame.quit()
quit()
