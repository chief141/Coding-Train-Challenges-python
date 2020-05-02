import pygame
from sys import exit
from random import randint

width=800
height=500
fps = 60

black = (0,0,0)

#for display
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Bubble Sorting")
clock=pygame.time.Clock()

values = [randint(0,height) for _ in range(width)]

#game loop
i = 0
j = 0
run=True
Sorting = True
start_time = pygame.time.get_ticks()
while run:
	#clock spped
	clock.tick(fps)

	# SORTING Algorithm
	if Sorting:
		if i < len(values):
			for j in range(len(values) - i - 1):
				a = values[j]
				b = values[j + 1]
				
				if a > b : 
					values[j], values[j + 1] = values[j + 1], values[j]
			i += 1
		else : 
			time_taken = pygame.time.get_ticks() - start_time
			print()
			print(f"Done Sorting in {time_taken/1000} seconds")
			Sorting = False
	#  _________________________________
		
	#input(events)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	#Draw/render
	screen.fill(black)

	# DRAWING LINES ____________________
	for k in range(len(values)):
		pygame.draw.line(screen, (255,255,255), (k, height), (k,height-values[k]) )
	# _____________________________________________

	pygame.display.flip()
	

pygame.quit()
exit()