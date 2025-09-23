import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

photores = 6
ledpin = 26
gpio.setup(photores, gpio.IN)
gpio.setup(ledpin, gpio.OUT)
state = 0

while True:
    gpio.output( ledpin, not gpio.input(photores))