from settings import Settings
from units import TemperatureUnits

class UserInterface:
    def __init__(self, temperature_units=TemperatureUnits.C):    
        self.settings = Settings()
        self.temperature_units = temperature_units
        

    @staticmethod
    def convert_c_to_f(temp_c):
        temp_f = temp_c * (9/5)
        temp_f = temp_f + 32
        return temp_f

    @staticmethod
    def convert_f_to_c(temp_f):
        temp_c = temp_f - 32
        temp_c = temp_c * (5/9)
        return temp_c

    def update_set_temperature(self, set_temperature, temperature_controller):
        if self.temperature_units == TemperatureUnits.F:
            temp_c = self.convert_f_to_c(set_temperature)
            return temperature_controller.update_set_temperature(temp_c)
        return temperature_controller.update_set_temperature(set_temperature)

    def display_temperature(temperature):
        if self.temperature_units == TemperatureUnits.F:
            temp_f = self.convert_c_to_f(temperature)
            print(temp_f)
        print(temperature)