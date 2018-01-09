import pygame, sys, time
from UltraColor import *

pygame.init()

tile_size = 32

def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "Rpg window"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

# render gfx
create_window()
window.fill((0, 0, 0))

# render grid
for x in range(0, 640, tile_size):
    for y in range(0, 480, tile_size):
        pygame.draw.rect(window, Color.White, (x, y, tile_size + 1, tile_size + 1), 1)




isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    pygame.display.update()
#end render

pygame.quit()
sys.exit()
