import pygame
import pygame.freetype
import weathericons
import time

from weathericons import *

WHITE = pygame.Color(255,255,255,255)

FONT_PATH = 'fonts/DejaVuSans.ttf'
FONT_SIZE = 28

LEFT_ICON = (15,15)
RIGHT_ICON = (155,15)

LEFT_TEXT_RECT = pygame.Rect(0,0,160,180)
RIGHT_TEXT_RECT = pygame.Rect(160,0,160,180)

LINE_POS = (0,180,320,5)

class IconPos:
    Time = (20,195)
    Weather = (100,195)
    Pollen = (180,195)
    SunIntensity = (260,195)

class Screen:
    def __init__(self, screen_surface):
        self.screen = screen_surface
        self.background = self.create_background()
        self.text = pygame.freetype.Font(FONT_PATH, FONT_SIZE)

    def create_background(self):
        background_size = self.screen.get_size()
        background = pygame.Surface(background_size).convert()
        background.blit(ToolbarIcons.Time, IconPos.Time)
        background.blit(ToolbarIcons.Weather, IconPos.Weather)
        background.blit(ToolbarIcons.Pollen, IconPos.Pollen)
        background.blit(ToolbarIcons.SunIntensity, IconPos.SunIntensity)
        background.fill(WHITE, LINE_POS)
        return background

    def center_text(self, text, bounds_rect):
        size_rect = self.text.get_rect(text)
        pos_x = bounds_rect.left + float(bounds_rect.width - size_rect.width) / 2
        pos_y = bounds_rect.top + float(bounds_rect.height - size_rect.height) / 2
        print pos_x, pos_y
        return (pos_x, pos_y)
    
    def display_time(self):
        now = time.localtime(time.time())
        time_str = time.strftime("%I:%M %p", now)
        self.screen.blit(self.background, (0,0))
        self.screen.blit(TimeIcons.Clock, LEFT_ICON)
        self.text.render_to(
            self.screen,
            self.center_text(time_str, RIGHT_TEXT_RECT),
            time_str,
            WHITE
        )
        pygame.display.flip()

    def display_weather(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(WeatherIcons.Clear, RIGHT_ICON)
        self.text.render_to(
            self.screen,
            self.center_text(' 95 F', LEFT_TEXT_RECT),
            ' 95 F',
            WHITE
        )
        pygame.display.flip()

    def display_pollen(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(PollenIcons.High, LEFT_ICON)
        self.text.render_to(
            self.screen,
            self.center_text('6.8', RIGHT_TEXT_RECT),
            '6.8',
            WHITE
        )
        pygame.display.flip()

    def display_sunintensity(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(SunIntensityIcons.Medium, RIGHT_ICON)
        self.text.render_to(
            self.screen,
            self.center_text('10', LEFT_TEXT_RECT),
            '10',
            WHITE
        )
        pygame.display.flip()

pygame.init()
