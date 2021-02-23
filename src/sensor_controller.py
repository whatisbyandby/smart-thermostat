from sensor import Sensor

class SensorController:
    def __init__(self):
        self.sensor = Sensor()
        
    def get_temperature(self):
        return self.sensor.get_temperature()

    def get_humidity(self):
        return self.sensor.get_humidity()