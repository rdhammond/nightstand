#!/usr/bin/python
import pygame
import RPi.GPIO as GPIO
import events

from events import Events

FIRST_BUTTON_PIN = 21
BUTTON_COUNT = 4
LAST_BUTTON_PIN = FIRST_BUTTON_PIN + BUTTON_COUNT

class TFTSwitches:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.initButtons()

    def initButtons(self):
        for channel in xrange(FIRST_BUTTON_PIN, LAST_BUTTON_PIN+1):
            GPIO.setup(channel, GPIO.IN)
            GPIO.add_event_detect(channel, GPIO.RISING)
            GPIO.add_event_callback(channel, self.sendEvent)
    
    def sendEvent(self, channel):
        buttonNumber = channel - FIRST_BUTTON_PIN
        event = pygame.event.Event(Events.Button, {'buttonNumber': buttonNumber})
        pygame.event.post(event)

    def cleanup(self):
        GPIO.cleanup()
