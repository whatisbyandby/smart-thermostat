from enum import Enum

class TemperatureUnits(Enum):
    C = 1
    F = 2

class DisplayController:
    def __init__(self):
        self.units = TemperatureUnits.C

    def convert_C_to_F(self, temp_C):
        temp_F = temp_C * (9/5)
        temp_F = temp_F + 32
        return temp_F

    def convert_F_to_C(self, temp_F):
        pass