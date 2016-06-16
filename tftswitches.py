#!/usr/bin/python
import pygame
import RPi.GPIO as GPIO
import events

from events import Events

ButtonEvents = {
    '21': Events.Button1,
    '22': Events.Button2,
    '23': Events.Button3,
    '24': Events.Button4
}

class TFTSwitches:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.initButtons()
        self.enableEvents()

    def initButtons(self):
        for channel in ButtonChannels:
            GPIO.setup(channel, GPIO.IN)
    
    def enableEvents(self):
        for channel in ButtonChannels:
            GPIO.add_event_detect(channel, GPIO.RISING)
            GPIO.add_event_callback(channel, self.sendEvent)

    def sendEvent(self, channel):
        event = pygame.event.Event(ButtonEvents[str(channel)])
        pygame.event.post(event)

    def cleanup(self):
        GPIO.cleanup()
