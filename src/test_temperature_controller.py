import pytest
import time
from temperature_controller import TemperatureController, Mode, State

def test_handle_new_reading_heater():
    temp_controller = TemperatureController(20, 1, Mode.HEATER)
    assert temp_controller.handle_new_reading(15) == State.HEATER_ON
    assert temp_controller.handle_new_reading(19) == State.HEATER_ON
    assert temp_controller.handle_new_reading(19.9) == State.HEATER_ON
    assert temp_controller.handle_new_reading(20.1) == State.ALL_OFF
    assert temp_controller.handle_new_reading(21) == State.ALL_OFF
    assert temp_controller.handle_new_reading(19.9) == State.ALL_OFF
    assert temp_controller.handle_new_reading(19.1) == State.ALL_OFF
    assert temp_controller.handle_new_reading(19.0) == State.HEATER_ON
    temp_controller.shutdown()

def test_handle_new_reading_cooler():
    temp_controller = TemperatureController(20, 1, Mode.COOLER)
    assert temp_controller.handle_new_reading(25) == State.COOLER_ON
    assert temp_controller.handle_new_reading(22) == State.COOLER_ON
    assert temp_controller.handle_new_reading(20.1) == State.COOLER_ON
    assert temp_controller.handle_new_reading(20) == State.ALL_OFF
    assert temp_controller.handle_new_reading(20.1) == State.ALL_OFF
    assert temp_controller.handle_new_reading(20.9) == State.ALL_OFF
    assert temp_controller.handle_new_reading(21) == State.COOLER_ON
    temp_controller.shutdown()

def test_handle_new_reading_off():
    temp_controller = TemperatureController(20, 1, Mode.OFF)
    assert temp_controller.handle_new_reading(25) == State.ALL_OFF
    assert temp_controller.handle_new_reading(22) == State.ALL_OFF
    assert temp_controller.handle_new_reading(20.1) == State.ALL_OFF
    assert temp_controller.handle_new_reading(20) == State.ALL_OFF
    assert temp_controller.handle_new_reading(20.1) == State.ALL_OFF
    assert temp_controller.handle_new_reading(20.9) == State.ALL_OFF
    assert temp_controller.handle_new_reading(21) == State.ALL_OFF
    temp_controller.shutdown()

def test_update_set_temperature():
    temp_controller = TemperatureController(20, 1, Mode.OFF)
    assert temp_controller.update_set_temperature(25) == 25

def test_get_mode_set_mode():
    temp_controller = TemperatureController(20, 1, Mode.OFF)
    assert temp_controller.get_mode() == Mode.OFF
    temp_controller.set_mode(Mode.HEATER)
    assert temp_controller.get_mode() == Mode.HEATER
    temp_controller.set_mode(Mode.COOLER)
    assert temp_controller.get_mode() == Mode.COOLER

def test_get_set_temperature():
    temp_controller = TemperatureController(20, 1, Mode.OFF)
    assert temp_controller.get_set_temperature() == 20


