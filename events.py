import pygame

class Events:
    Tick = pygame.USEREVENT
    Switch = pygame.USEREVENT + 1
    UpdateWeatherFeed = pygame.USEREVENT + 2
    UpdatePollenFeed = pygame.USEREVENT + 3
    UpdateSunIntensityFeed = pygame.USEREVENT + 4
    Quit = pygame.QUIT
