import pygame
from random import randint
from math import sqrt

width = 400
height= 400
fps   = 100

#for display
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Approximating PI")
clock = pygame.time.Clock()

dots_inside_circle = 0
total_dots = 0
r = 200

drawing_dots_x = []
drawing_dots_y = []
drawing_dots_color = []

actual_pi = 3.141592653589793238462643 ##ACTUAL PI JUST TO COMPARE WITH ESTIMATED ONE
print()
print("Actual PI :",actual_pi)
print()

#game loop
run=True
last_time_print = pygame.time.get_ticks()
while run:
	#clock spped
	delta_time = clock.tick(fps)/1000
	
	#input(events)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	x = randint(0,r*2)
	y = randint(0,r*2)
	distance = sqrt((r - x)**2 + (r  - y)**2)

	if distance < 200:
		dots_inside_circle += 1
		total_dots += 1
		color = (0,255,0)
	else:
		total_dots += 1
		color = (255,0,0)

	drawing_dots_x.append(x)
	drawing_dots_y.append(y)
	drawing_dots_color.append(color)

	#Draw/render
	screen.fill((0, 0, 0))

	pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,width,height))
	pygame.draw.rect(screen, (0,0,0), pygame.Rect(2,2,width-4,height-4))

	pygame.draw.circle(screen,(255,255,255),(width//2,height//2), r)
	pygame.draw.circle(screen,(0,0,0),(width//2,height//2), 199)

	for i in range(len(drawing_dots_x)- 1):
		x_ = drawing_dots_x[i]
		y_ = drawing_dots_y[i]
		color = drawing_dots_color[i]
		screen.set_at((x_, y_), color)

	if pygame.time.get_ticks() - last_time_print >= 1000:
		PI = 4 * (dots_inside_circle/total_dots)
		last_time_print = pygame.time.get_ticks()
		print("Current estimated PI :",PI)
		
	pygame.display.flip()
	
pygame.quit()
quit()
