#!/usr/bin/python
import datetime
import pygame
import pygame.freetype
import events
import weathericons
import weatherfeed
import pollenfeed
import sunintensityfeed

from events import Events
from weathericons import *
from weatherfeed import WeatherFeed
from pollenfeed import PollenFeed
from sunintensityfeed import SunIntensityFeed


# TODO
STATION_ID = '102'
LONGITUDE = -85.7594
LATITUDE = 38.2541


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
        self.initFeeds()

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

        self.display_function = self.display_functions[self.current_display]

    def initTimeUpdates(self):
        self.next_minute = self.addMinute()

    def initIcons(self):
        self.TimeIcons = weathericons.TimeIcons()
        self.WeatherIcons = weathericons.WeatherIcons()
        self.PollenIcons = weathericons.PollenIcons()
        self.SunIntensityIcons = weathericons.SunIntensityIcons()
        self.ToolbarIcons = weathericons.ToolbarIcons()

    def initFeeds(self):
        self.weatherFeed = WeatherFeed(LONGITUDE, LATITUDE)
        self.pollenFeed = PollenFeed(STATION_ID)
        self.sunIntensityFeed = SunIntensityFeed(LONGITUDE, LATITUDE)

        self.updateWeather()
        self.updatePollen()
        self.updateSunIntensity()

    def updateWeather(self):
        response = self.weatherFeed.get()
        self.temperature = response['temp']
        self.weather = response['weather']

        if self.display_function == self.displayWeather:
            self.displayWeather()

    def updatePollen(self):
        self.pollen_count = self.pollenFeed.get()

        if self.display_function == self.displayPollen:
            self.displayPollen()

    def updateSunIntensity(self):
        self.sun_intensity = self.sunIntensityFeed.get()

        if self.display_function == self.displaySunIntensity:
            self.displaySunIntensity()

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
        temp_str = str(self.temperature) + ' F'
        icon = self.getWeatherIcon()

        self.screen.blit(self.background, (0,0))
        self.screen.blit(icon, IconPos.Right)
        self.font.render_to(
            self.screen,
            self.centerText(temp_str, TextPosRect.Left),
            temp_str,
            Colors.White
        )
        pygame.display.flip()

    def getWeatherIcon(self):
        is_night = (datetime.datetime.now().hour >= 18)

        if self.weather == 'cloudy':
            if is_night:
                return self.WeatherIcons.CloudyNight

            return self.WeatherIcons.Cloudy
        
        if self.weather == 'rainy':
            return self.WeatherIcons.Rainy
        
        if self.weather == 'snowy':
            return self.WeatherIcons.Snowy
        
        if is_night:
            return self.WeatherIcons.ClearNight

        return self.WeatherIcons.Clear

    def displayPollen(self):
        if self.pollen_count >= 6:
            icon = self.PollenIcons.High
        elif 3 <= self.pollen_count < 6:
            icon = self.PollenIcons.Medium
        else:
            icon = self.PollenIcons.Low

        pollen_str = str(self.pollen_count)

        self.screen.blit(self.background, (0,0))
        self.screen.blit(icon, IconPos.Left)
        self.font.render_to(
            self.screen,
            self.centerText(pollen_str, TextPosRect.Right),
            pollen_str,
            Colors.White
        )
        pygame.display.flip()

    def displaySunIntensity(self):
        if self.sun_intensity >= 8:
            icon = self.SunIntensityIcons.High
        elif 4 <= self.sun_intensity < 8:
            icon = self.SunIntensityIcons.Medium
        else:
            icon = self.SunIntensityIcons.Low

        sun_intensity_str = str(self.sun_intensity)
        
        self.screen.blit(self.background, (0,0))
        self.screen.blit(icon, IconPos.Right)
        self.font.render_to(
            self.screen,
            self.centerText(sun_intensity_str, TextPosRect.Left),
            sun_intensity_str,
            Colors.White
        )
        pygame.display.flip()

    def route(self, event):
        if event.type == Events.Tick:
            self.checkTimeUpdate()
        elif event.type == Events.Switch:
            self.nextScreen()
        elif event.type == Events.UpdateWeatherFeed:
            self.updateWeather()
        elif event.type == Events.UpdatePollenFeed:
            self.updatePollen()
        elif event.type == Events.UpdateSunIntensityFeed:
            self.updateSunIntensity()

    def checkTimeUpdate(self):
        current_time = datetime.datetime.now()
        display_function = self.display_functions[self.current_display]
        
        if self.display_function == self.displayTime and current_time >= self.next_minute:
            self.displayTime()
            self.next_minute = self.addMinute()

    def nextScreen(self):
        self.current_display = (self.current_display + 1) % len(self.display_functions)
        self.display_function = self.display_functions[self.current_display]
        self.display_function()
