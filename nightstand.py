#!/usr/bin/python
import sys
import pygame
import pygame.freetype

SCREEN_SIZE = (320,240)
WINDOW_TITLE = 'Nightstand'

pygame.init()
screen_surface = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

import screen
gui = screen.Screen(screen_surface)
gui.display_sunintensity()

event = pygame.event.wait()
while event.type != pygame.QUIT:
        event = pygame.event.wait()

pygame.quit()
sys.exit()
