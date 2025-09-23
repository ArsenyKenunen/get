import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
ledpin = 26
gpio.setup(ledpin, gpio.OUT)

state = 0
period = 1.0


while True:
    gpio.output(ledpin, state)
    state = not state
    time.sleep(period/2)
