from temperature_controller import TemperatureController, Mode
from sensor_controller import SensorController
from data_controller import DataController
from display_controller import DisplayController
from relay_controller import RelayController
from user_interface import UserInterface
from unit_controller import UnitController
from settings import Settings
import time


class Thermostat():
    def __init__(self):
        self.temperature_controller = TemperatureController(set_temperature=20, mode=Mode.COOLER)
        self.sensor_controller = SensorController()
        self.mqtt_controller = DataController()
        self.settings = Settings()
        self.user_interface = UserInterface()
        self.unit_controller = UnitController()

    def startup(self):
        pass

    def run(self):
        while True:
            current_temperature = self.sensor_controller.get_temperature()
            current_state = self.temperature_controller.handle_new_reading(current_temperature)
            current_humidity = self.sensor_controller.get_humidity()
            converted_data = self.unit_controller.convert({"temperature": current_temperature, "humidity": current_humidity, "mode": self.temperature_controller.get_mode(), "state": current_state})
            self.mqtt_controller.publish_data(converted_data)
            time.sleep(1)
    
    def shutdown(self):
        print('Shutting Down')
        self.temperature_controller.shutdown()
