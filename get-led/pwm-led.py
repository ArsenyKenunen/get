import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
ledpin = 26
gpio.setup(ledpin, gpio.OUT)

pwm = gpio.PWM(ledpin, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.01)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0
