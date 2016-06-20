#!/usr/bin/python
import sys
import pygame

from net.geolocation import GeoLocation
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

class Nightstand:
    def __init__(self):
        pygame.init()
        self.screen = GUI()
        self.switches = self.initSwitches()
        self.initTimers()

    def initSwitches(self):
        try:
            import tftswitches
            from tftswitches import TFTSwitches
            return TFTSwitches()

        except ImportError:
            return None

    def initTimers(self):
        pygame.time.set_timer(Events.Tick, TimeLengths.Tick)
        pygame.time.set_timer(Events.Switch, TimeLengths.Switch)
        pygame.time.set_timer(Events.UpdateWeatherFeed, TimeLengths.UpdateWeatherFeed)
        pygame.time.set_timer(Events.UpdatePollenFeed, TimeLengths.UpdatePollenFeed)
        pygame.time.set_timer(Events.UpdateSunIntensityFeed, TimeLengths.UpdateSunIntensityFeed)

    def run(self):
        event = pygame.event.wait()

        while event.type != Events.Quit:
            self.route(event)
            self.screen.route(event)
            event = pygame.event.wait()

    def route(self, event):
        if event.type == Events.Button:
            self.resetSwitchTimer()

    def resetSwitchTimer(self):
        pygame.time.set_timer(Events.Switch, 0)
        pygame.time.set_timer(Events.Switch, TimeLengths.Switch)

    def cleanup(self):
        if self.switches is not None:
            self.switches.cleanup()

        pygame.quit()
