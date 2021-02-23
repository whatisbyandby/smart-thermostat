from temperature_controller import TemperatureController
from sensor_controller import SensorController
from data_controller import DataController
from display_controller import DisplayController
from relay_controller import RelayController
from settings import Settings
import time


class Thermostat():
    def __init__(self):
        self.temperature_controller = TemperatureController()
        self.sensor_controller = SensorController()
        self.data_controller = DataController()
        self.settings = Settings()
        self.relay_controller = RelayController()
        self.display_controller = DisplayController()

    def startup(self):
        pass

    def run(self):
        # print('Starting the thermostat')
        while True:
            current_temperature = self.sensor_controller.get_temperature()
            self.temperature_controller.handle_new_reading(current_temperature)
            current_humidity = self.sensor_controller.get_humidity()
            self.data_controller.publish_data({"temperature": self.display_controller.convert_C_to_F(current_temperature), "humidity": current_humidity})
            time.sleep(1)
    
    def shutdown(self):
        print('Shutting Down')
        self.temperature_controller.shutdown()
