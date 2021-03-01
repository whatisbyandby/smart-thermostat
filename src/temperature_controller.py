from enum import Enum
from relay_controller import RelayController
from settings import Settings


class Mode(str, Enum):
    HEATER = 'HEATER'
    COOLER = 'COOLER'
    OFF = 'OFF'

class TemperatureCondition(Enum):
    UNDER_TEMP = 1
    OVER_TEMP = 2
    IN_RANGE_UNDER_TEMP = 3
    IN_RANGE_OVER_TEMP = 4

class State(str, Enum):
    HEATER_ON = 'HEATER_ON'
    COOLER_ON = 'COOLER_ON'
    ALL_OFF = 'ALL_OFF'

class TemperatureController:
    def __init__(self, set_temperature=20, temp_range=1, mode=Mode.OFF, relay_controller=RelayController()):
        self.mode = mode
        self.current_state = None
        self.set_temperature = set_temperature
        self.temp_range = temp_range
        self.relay_controller = relay_controller
        self.settings = Settings()

    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode

    def get_set_temperature(self):
        return self.set_temperature

    def update_set_temperature(self, new_set_temp):
        self.set_temperature = new_set_temp
        return self.set_temperature

    def shutdown(self):
        self._all_off()

    def handle_new_reading(self, current_temperature):
        print(current_temperature)
        temperature_state = self._compare_temperature(current_temperature)
        self.current_state = self._adjust_temperature(temperature_state)
        return self.current_state

    def _compare_temperature(self, current_temperature):
        if current_temperature is None:
            raise Exception("No Temperature Reading")
        elif current_temperature >= self.set_temperature + self.temp_range:
            return TemperatureCondition.OVER_TEMP
        elif current_temperature <= self.set_temperature - self.temp_range:
            return TemperatureCondition.UNDER_TEMP
        elif current_temperature <= self.set_temperature:
            return TemperatureCondition.IN_RANGE_UNDER_TEMP
        elif current_temperature >= self.set_temperature:
            return TemperatureCondition.IN_RANGE_OVER_TEMP
        elif current_temperature > 100 or current_temperature < 0:
            raise Exception("Temperature reading out of range")
        else:
            raise Exception("Unable to compare temps")


    def _adjust_temperature(self, temperature_state):
        if self.mode == Mode.OFF:
            return self._all_off()
        elif temperature_state == TemperatureCondition.UNDER_TEMP:
            return self._heater_on()
        elif temperature_state == TemperatureCondition.IN_RANGE_UNDER_TEMP and self.current_state == State.HEATER_ON:
            return self._heater_on()
        elif temperature_state == TemperatureCondition.OVER_TEMP:
            return self._cooler_on()
        elif temperature_state == TemperatureCondition.IN_RANGE_OVER_TEMP and self.current_state == State.COOLER_ON:
            return self._cooler_on()
        else:
            return self._all_off()

    def _heater_on(self):
        if self.mode != Mode.HEATER:
            self.relay_controller.all_channels_off()
            return State.ALL_OFF
        self.relay_controller.heater_channels_on()
        return State.HEATER_ON

    def _cooler_on(self):
        if self.mode != Mode.COOLER:
            self.relay_controller.all_channels_off()
            return State.ALL_OFF
        self.relay_controller.cooler_channels_on()
        return State.COOLER_ON

    def _all_off(self):
        self.relay_controller.all_channels_off()
        return State.ALL_OFF
        