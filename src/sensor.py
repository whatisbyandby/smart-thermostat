import board
import busio
import adafruit_bme280

class Sensor:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(self.i2c)

    def get_temperature(self):
        return self.bme280.temperature

    def get_humidity(self):
        return self.bme280.humidity

    def get_pressure(self):
        return self.bme280.pressure

if __name__ == '__main__':
    sensor = Sensor()
    print(sensor.get_temperature())