import paho.mqtt.client as mqtt
import json

class DataController:
    def __init__(self):
        self.client = mqtt.Client('thermostat')

    def publish_data(self, data):
        self.client.connect('192.168.3.2')
        self.client.publish("thermostat/data", json.dumps(data))
