from temperature_controller import TemperatureController, Mode
from sensor_controller import SensorController
from data_controller import DataController
from display_controller import DisplayController
from relay_controller import RelayController
from user_interface import UserInterface
from unit_controller import UnitController
from command_subscriber import CommandSubscriber
import time
import json

class Thermostat():
    def __init__(self, update_server):
        self.temperature_controller = TemperatureController(set_temperature=20, mode=Mode.COOLER)
        self.sensor_controller = SensorController()
        self.mqtt_controller = DataController()
        self.user_interface = UserInterface()
        self.unit_controller = UnitController()
        self.update_server = update_server
        self.command_subscriber = CommandSubscriber("192.168.3.2", self.handle_command)
        self.current_display_data = None

    def startup(self):
        pass

    def run(self):
        self.command_subscriber.subscribe()
        while True:
            current_temperature = self.sensor_controller.get_temperature()
            current_state = self.temperature_controller.handle_new_reading(current_temperature)
            current_humidity = self.sensor_controller.get_humidity()
            converted_data = self.unit_controller.convert(
                {"temperature": current_temperature, 
                "set_temperature": self.temperature_controller.get_set_temperature(), 
                "humidity": current_humidity, "mode": self.temperature_controller.get_mode(), 
                "state": current_state})
            self.mqtt_controller.publish_data(converted_data)
            self.update_server(converted_data)
            self.command_subscriber.command_loop()
            self.current_display_data = converted_data
            time.sleep(1)

    def handle_command(self, command):
        command_type = command.get('command')
        if command_type == "SET_TEMPERATURE":
            self.temperature_controller.update_set_temperature(self.unit_controller.convert_incomming(command['data']['temperature']))
        elif command_type == "SET_MODE":
            self.temperature_controller.set_mode(Mode(command['data']['mode']))

    def update_set_temperature(self, set_temperature):
        converted_temp = UnitController.convert_f_to_c(set_temperature)
        self.temperature_controller.update_set_temperature(converted_temp)
        self.update_server({"temperature": self.current_display_data.get('temperature'), 
                "set_temperature": set_temperature, 
                "humidity": self.current_display_data.get('humidity'), 
                "mode": self.temperature_controller.get_mode(), 
                "state": self.current_display_data.get('state')})
        
    
    def shutdown(self):
        print('Shutting Down')
        self.temperature_controller.shutdown()
