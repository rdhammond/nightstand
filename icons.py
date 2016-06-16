#!/usr/bin/python
import nightstandicon

from nightstandicon import NightstandIcon

class Icons:
    def __init__(self):
        self.Clock = NightstandIcon('clock')

        self.Cloudy = NightstandIcon('cloudy-day')
        self.Clear = NightstandIcon('sunny')
        self.ClearNight = NightstandIcon('night')
        self.Cloudy = NightstandIcon('cloudy-day')
        self.CloudyNight = NightstandIcon('cloudy-night')
        self.Rainy = NightstandIcon('rainy')
        self.Snowy = NightstandIcon('snowy')

        self.LowPollen = NightstandIcon('low-pollen')
        self.MediumPollen = NightstandIcon('medium-pollen')
        self.HighPollen = NightstandIcon('high-pollen')

        self.LowSunIntensity = NightstandIcon('low-sun')
        self.MediumSunIntensity = NightstandIcon('medium-sun')
        self.HighSunIntensity = NightstandIcon('high-sun')

        self.ToolbarTime = NightstandIcon('toolbar-time')
        self.ToolbarWeather = NightstandIcon('toolbar-weather')
        self.ToolbarPollen = NightstandIcon('toolbar-pollen')
        self.ToolbarSunIntensity = NightstandIcon('toolbar-sunintensity')
