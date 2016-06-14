#!/usr/bin/python
import datetime
import pygame
import pygame.freetype
import events
import weathericons

from events import Events
from weathericons import *

MINUTE_DELTA = datetime.timedelta(minutes=1)
CLOCK_TIME_FORMAT = '%I:%M %p'

class Window:
    Size = (320,240)
    Title = 'Nightstand'

class FontInfo:
    Path = 'fonts/DejaVuSans.ttf'
    Size = 28

class Colors:
    White = pygame.Color(255,255,255,255)

class IconPos:
    Left = (15,15)
    Right = (155,15)

class TextPosRect:
    Left = pygame.Rect(0,0,160,180)
    Right = pygame.Rect(160,0,160,180)

class ToolbarPos:
    Time = (20,195)
    Weather = (100,195)
    Pollen = (180,195)
    SunIntensity = (260,195)
    LineRect = pygame.Rect(0,180,320,5)

class GUI:
    def __init__(self):
        self.initComponents()
        self.initSwitchTracking()
        self.initTimeUpdates()
        self.display_functions[self.current_display]()

    def initComponents(self):
        self.screen = self.createWindow()
        self.font = pygame.freetype.Font(FontInfo.Path, FontInfo.Size)

        self.initIcons()
        self.background = self.createBackground()

    def initSwitchTracking(self):
        self.current_display = 0
        
        self.display_functions = [
            self.displayTime,
            self.displayWeather,
            self.displayPollen,
            self.displaySunIntensity
        ]

    def initTimeUpdates(self):
        self.next_minute = self.addMinute()

    def initIcons(self):
        self.TimeIcons = weathericons.TimeIcons()
        self.WeatherIcons = weathericons.WeatherIcons()
        self.PollenIcons = weathericons.PollenIcons()
        self.SunIntensityIcons = weathericons.SunIntensityIcons()
        self.ToolbarIcons = weathericons.ToolbarIcons()

    def createWindow(self):
        screen_surface = pygame.display.set_mode(Window.Size)
        pygame.display.set_caption(Window.Title)
        return screen_surface
    
    def createBackground(self):
        background_size = self.screen.get_size()
        background = pygame.Surface(background_size).convert()
        background.blit(self.ToolbarIcons.Time, ToolbarPos.Time)
        background.blit(self.ToolbarIcons.Weather, ToolbarPos.Weather)
        background.blit(self.ToolbarIcons.Pollen, ToolbarPos.Pollen)
        background.blit(self.ToolbarIcons.SunIntensity, ToolbarPos.SunIntensity)
        background.fill(Colors.White, ToolbarPos.LineRect)
        return background

    def addMinute(self):
        return (datetime.datetime.now() + MINUTE_DELTA).replace(second=0, microsecond=0)

    def centerText(self, text, bounds_rect):
        size_rect = self.font.get_rect(text)
        pos_x = bounds_rect.left + float(bounds_rect.width - size_rect.width) / 2
        pos_y = bounds_rect.top + float(bounds_rect.height - size_rect.height) / 2
        return (pos_x, pos_y)
    
    def displayTime(self):
        time_str = datetime.datetime.now().strftime(CLOCK_TIME_FORMAT)
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.TimeIcons.Clock, IconPos.Left)
        self.font.render_to(
            self.screen,
            self.centerText(time_str, TextPosRect.Right),
            time_str,
            Colors.White
        )
        pygame.display.flip()

    def displayWeather(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.WeatherIcons.Clear, IconPos.Right)
        # TODO
        self.font.render_to(
            self.screen,
            self.centerText(' 95 F', TextPosRect.Left),
            ' 95 F',
            Colors.White
        )
        pygame.display.flip()

    def displayPollen(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.PollenIcons.High, IconPos.Left)
        # TODO
        self.font.render_to(
            self.screen,
            self.centerText('6.8', TextPosRect.Right),
            '6.8',
            Colors.White
        )
        pygame.display.flip()

    def displaySunIntensity(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.SunIntensityIcons.Medium, IconPos.Right)
        # TODO
        self.font.render_to(
            self.screen,
            self.centerText('10', TextPosRect.Left),
            '10',
            Colors.White
        )
        pygame.display.flip()

    def route(self, event):
        if event.type == Events.Tick:
            self.checkTimeUpdate()
        elif event.type == Events.Switch:
            self.nextScreen()

    def checkTimeUpdate(self):
        current_time = datetime.datetime.now()
        display_function = self.display_functions[self.current_display]
        
        if display_function == self.displayTime and current_time >= self.next_minute:
            self.displayTime()
            self.next_minute = self.addMinute()

    def nextScreen(self):
        self.current_display = (self.current_display + 1) % len(self.display_functions)
        self.display_functions[self.current_display]()
