from settings import Settings
from units import TemperatureUnits

class UserInterface:
    def __init__(self):    
        self.settings = Settings()
        self.temperature_units = TemperatureUnits.F
        

    @staticmethod
    def convert_C_to_F(temp_c):
        temp_f = temp_c * (9/5)
        temp_f = temp_f + 32
        return temp_f

    @staticmethod
    def convert_F_to_C(temp_f):
        temp_c = temp_f - 32
        temp_c = temp_c * (5/9)
        return temp_c

    def update_set_temperature(self, temperature_controller):
        pass