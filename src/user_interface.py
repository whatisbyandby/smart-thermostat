from units import TemperatureUnits

class UserInterface:
    def __init__(self, temperature_units=TemperatureUnits.C):    
        self.temperature_units = temperature_units
        
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