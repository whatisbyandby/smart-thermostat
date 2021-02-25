import pytest
from user_interface import UserInterface
from units import TemperatureUnits
from temperature_controller import TemperatureController

def test_convert_f_to_c():
    assert UserInterface.convert_f_to_c(212) == 100
    assert UserInterface.convert_f_to_c(32) == 0
    assert UserInterface.convert_f_to_c(-40) == -40

def test_convert_c_to_f():
    assert UserInterface.convert_c_to_f(100) == 212
    assert UserInterface.convert_c_to_f(0) == 32
    assert UserInterface.convert_c_to_f(-40) == -40

def test_update_set_temperature():
    temp_controller = TemperatureController()
    interface = UserInterface(TemperatureUnits.C)
    interface.update_set_temperature(70, temp_controller)