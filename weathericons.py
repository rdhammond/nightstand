#!/usr/bin/python
import os
import pygame

def load_image(filename):
  return pygame.image.load(os.path.join('sprites/' + filename + '.png')).convert()

class TimeIcons:
  def __init__(self):
    self.Clock = load_image('clock')

class WeatherIcons:
  def __init__(self):
    self.Cloudy = load_image('cloudy-day')
    self.CloudyNight = load_image('cloudy-night')
    self.ClearNight = load_image('night')
    self.Rainy = load_image('rainy')
    self.Snowy = load_image('snowy')
    self.Clear = load_image('sunny')

class PollenIcons:
  def __init__(self):
    self.Low = load_image('low-pollen')
    self.Medium = load_image('medium-pollen')
    self.High = load_image('high-pollen')

class SunIntensityIcons:
  def __init__(self):
    self.Low = load_image('low-sun');
    self.Medium = load_image('medium-sun')
    self.High = load_image('high-sun')

class ToolbarIcons:
  def __init__(self):
    self.Time = load_image('toolbar-time')
    self.Weather = load_image('toolbar-weather')
    self.Pollen = load_image('toolbar-pollen')
    self.SunIntensity = load_image('toolbar-sunintensity')
