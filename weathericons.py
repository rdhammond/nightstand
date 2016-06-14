#!/usr/bin/python
import os
import pygame

def load_image(filename):
  return pygame.image
    .load(os.path.join('sprites/' + filename + '.png'))
    .convert()

class timeIcons:
  Clock = load_image('clock')

class weatherIcons:
  Cloudy = load_image('cloudy-day')
  CloudyNight = load_image('cloudy-night')
  ClearNight = load_image('night')
  Rainy = load_image('rainy')
  Snowy = load_image('snowy')
  Clear = load_image('sunny')

class pollenIcons:
  Low = load_image('low-pollen')
  Medium = load_image('medium-pollen')
  High = load_image('high-pollen')

class sunIntensityIcons:
  Low = load_image('low-sun');
  Medium = load_image('medium-sun')
  High = load_image('high-sun')

class toolbarIcons:
  Time = load_image('toolbar-time')
  Weather = load_image('toolbar-weather')
  Pollen = load_image('toolbar-pollen')
  SunIntensity = load_image('toolbar-sun-intensity')


TimeIcons = timeIcons()
WeatherIcons = weatherIcons()
PollenIcons = pollenIcons()
SunIntensityIcons = sunIntensityIcons()
ToolbarIcons = toolbarIcons()
