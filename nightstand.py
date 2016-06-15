#!/usr/bin/python
import sys
import pygame
import events
import gui

from events import Events
from gui import GUI

def secToMs(sec):
        return sec * 1000

def minToMs(min):
        return min * 60 * 1000

def hoursToMs(hours):
        return hours * 60 * 60 * 1000

class TimeLengths:
        Tick = secToMs(1)
        Switch = secToMs(7)
        UpdateWeatherFeed = minToMs(15)
        UpdatePollenFeed = hoursToMs(4)
        UpdateSunIntensityFeed = hoursToMs(1)
        

pygame.init()
screen = GUI()

pygame.time.set_timer(Events.Tick, TimeLengths.Tick)
pygame.time.set_timer(Events.Switch, TimeLengths.Switch)
pygame.time.set_timer(Events.UpdateWeatherFeed, TimeLengths.UpdateWeatherFeed)
pygame.time.set_timer(Events.UpdatePollenFeed, TimeLengths.UpdatePollenFeed)
pygame.time.set_timer(Events.UpdateSunIntensityFeed, TimeLengths.UpdateSunIntensityFeed)
event = pygame.event.wait()

while event.type != Events.Quit:
        screen.route(event)
        event = pygame.event.wait()

pygame.quit()
sys.exit()
