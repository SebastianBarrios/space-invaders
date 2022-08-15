#import requeired lybrari
import pygame

#intialize pygame
pygame. init()

#window size
screen_width = 600
screen_height = 800

#size variable
size = (screen_height, screen_width)

#display the window
screen = pygame.display.set_mode(size)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False