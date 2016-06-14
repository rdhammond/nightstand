#!/usr/bin/python
import sys
import pygame
import events
import gui

from events import Events
from gui import GUI

TICK_TIME_MS = 1000
SWITCH_TIME_MS = 7000

pygame.init()
screen = GUI()

pygame.time.set_timer(Events.Tick, TICK_TIME_MS)
pygame.time.set_timer(Events.Switch, SWITCH_TIME_MS)
event = pygame.event.wait()

while event.type != Events.Quit:
        screen.route(event)
        event = pygame.event.wait()

pygame.quit()
sys.exit()
