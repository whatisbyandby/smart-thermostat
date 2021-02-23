import time
import board
import digitalio

print("hello blinky!")
 
led1 = digitalio.DigitalInOut(board.D18)
led2 = digitalio.DigitalInOut(board.D19)
led3 = digitalio.DigitalInOut(board.D20)
led4 = digitalio.DigitalInOut(board.D21)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT
led4.direction = digitalio.Direction.OUTPUT

try:
    while True:
        led1.value = True
        time.sleep(0.25)
        led2.value = True
        time.sleep(0.25)
        led1.value = False
        time.sleep(0.25)
        led2.value = False
        time.sleep(0.25)
        led3.value = True
        time.sleep(0.25)
        led4.value = True
        time.sleep(0.25)
        led3.value = False
        time.sleep(0.25)
        led4.value = False
        time.sleep(0.25)
except KeyboardInterrupt as e:
    print('\nKeyboard Interupt')
finally:
    led1.value = True
    led2.value = True
    led3.value = True
    led4.value = True


