import paho.mqtt.client as mqtt
import time
import json

class CommandSubscriber:
    def __init__(self, broker_address, handle_command):
        self.client = mqtt.Client('P1')
        self.broker_address = broker_address
        self.handle_command = handle_command

    def subscribe(self):
        self.client.connect(self.broker_address)
        self.client.subscribe("thermostat/command")
        self.client.on_message=self.handle_message

    def command_loop(self):
        self.client.loop_start()

    def handle_message(self, client, userdata, message):
        self.handle_command(json.loads(message.payload))