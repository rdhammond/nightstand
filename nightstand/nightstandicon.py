#!/usr/bin/python
import os
import pygame

ICON_PATH = 'sprites'

class NightstandIcon:
    def __init__(self, name):
        self.path = os.path.join(ICON_PATH, name + '.png')
        self.image = pygame.image.load(self.path).convert()
        self.rect = self.image.get_rect()

    def setPos(self, pos):
        self.rect.left, self.rect.top = pos

    def blitTo(self, surface):
        surface.blit(self.image, self.rect)

    def contains(self, point):
        right = self.rect.left + self.rect.width
        bottom = self.rect.top + self.rect.height
        return (self.rect.left <= point[0] <= right) and (self.rect.top <= point[1] <= bottom)
