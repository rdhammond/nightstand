#!/usr/bin/python
import os
import pygame

def load_image(filename):
  return pygame.image.load(os.path.join('sprites/' + filename + '.png')).convert()

pygame.init()

class TimeIcons:
  Clock = load_image('clock')

class WeatherIcons:
  Cloudy = load_image('cloudy-day')
  CloudyNight = load_image('cloudy-night')
  ClearNight = load_image('night')
  Rainy = load_image('rainy')
  Snowy = load_image('snowy')
  Clear = load_image('sunny')

class PollenIcons:
  Low = load_image('low-pollen')
  Medium = load_image('medium-pollen')
  High = load_image('high-pollen')

class SunIntensityIcons:
  Low = load_image('low-sun');
  Medium = load_image('medium-sun')
  High = load_image('high-sun')

class ToolbarIcons:
  Time = load_image('toolbar-time')
  Weather = load_image('toolbar-weather')
  Pollen = load_image('toolbar-pollen')
  SunIntensity = load_image('toolbar-sunintensity')
