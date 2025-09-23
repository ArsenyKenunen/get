import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
up = 9
down = 10
gpio.setup(leds, gpio.OUT)
gpio.setup(up, gpio.IN)
gpio.setup(down, gpio.IN)
gpio.output(leds, 0)
sleep_time = 0.1

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleeptime = 0.2

while True:
    if gpio.input(up) and num < 255:
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        for i in range(8):
            gpio.output(leds[i], dec2bin(num)[i])
    if gpio.input(down) and num > 0:
        num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        for i in range(8):
            gpio.output(leds[i], dec2bin(num)[i])

