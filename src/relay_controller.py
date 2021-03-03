import board
import digitalio

from enum import Enum

class RelayController:
    def __init__(self):
        self.channel_one = digitalio.DigitalInOut(board.D18)
        self.channel_one.direction = digitalio.Direction.OUTPUT
        self.channel_one.value = True
        self.channel_two = digitalio.DigitalInOut(board.D19)
        self.channel_two.direction = digitalio.Direction.OUTPUT
        self.channel_two.value = True
        self.channel_three = digitalio.DigitalInOut(board.D20)
        self.channel_three.direction = digitalio.Direction.OUTPUT
        self.channel_three.value = True
        self.channel_four = digitalio.DigitalInOut(board.D21)
        self.channel_four.direction = digitalio.Direction.OUTPUT
        self.channel_four.value = True

    def all_channels_off(self):
        self.channel_one.value = True
        self.channel_two.value = True
        self.channel_three.value = True
        self.channel_four.value= True

    def heater_channels_on(self):
        self.channel_one.value = False
        self.channel_two.value = False
        self.channel_three.value = True
        self.channel_four.value= True
        
    def cooler_channels_on(self):
        self.channel_one.value = True
        self.channel_two.value = False
        self.channel_three.value = False
        self.channel_four.value = True
