import pygame

class Events:
    Tick = pygame.USEREVENT
    Switch = pygame.USEREVENT + 1
    UpdateWeatherFeed = pygame.USEREVENT + 2
    UpdatePollenFeed = pygame.USEREVENT + 3
    UpdateSunIntensityFeed = pygame.USEREVENT + 4
    Button1 = pygame.USEREVENT + 5
    Button2 = pygame.USEREVENT + 6
    Button3 = pygame.USEREVENT + 7
    Button4 = pygame.USEREVENT + 8
    Quit = pygame.QUIT
