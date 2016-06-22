#!/usr/bin/python
import pygame

class Events:
    Click = pygame.MOUSEBUTTONDOWN
    Tick = pygame.USEREVENT
    Switch = pygame.USEREVENT + 1
    UpdateWeatherFeed = pygame.USEREVENT + 2
    UpdatePollenFeed = pygame.USEREVENT + 3
    UpdateSunIntensityFeed = pygame.USEREVENT + 4
    Button = pygame.USEREVENT + 5
    Quit = pygame.QUIT
