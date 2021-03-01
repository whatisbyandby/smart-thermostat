import pytest
from user_interface import UserInterface
from units import TemperatureUnits
from temperature_controller import TemperatureController


def test_update_set_temperature():
    temp_controller = TemperatureController()
    interface = UserInterface(TemperatureUnits.C)
    interface.update_set_temperature(70, temp_controller)