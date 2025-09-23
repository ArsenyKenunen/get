import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

button = 13
ledpin = 26
gpio.setup(button, gpio.IN)
gpio.setup(ledpin, gpio.OUT)
state = 0

while True:
    if gpio.input(button):
        state = not state
        gpio.output(ledpin, state)
        time.sleep(0.2)