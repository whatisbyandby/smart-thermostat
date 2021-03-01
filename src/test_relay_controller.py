import pytest
import time
from relay_controller import RelayController

def test_heater_on():
    relay_controller = RelayController()
    relay_controller.heater_channels_on()
    time.sleep(5)

def test_cooler_on():
    relay_controller = RelayController()
    relay_controller.cooler_channels_on()
    time.sleep(5)

def test_all_off():
    relay_controller = RelayController()
    relay_controller.all_channels_off()
    time.sleep(5)
