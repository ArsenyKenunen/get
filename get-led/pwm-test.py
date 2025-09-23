import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
pwmpin = 13
gpio.setup(pwmpin, gpio.OUT)

pwm = gpio.PWM(pwmpin, 200)
pwm.start(50)
duty = 0.0
while True:
    duty += 10
    pwm.ChangeDutyCycle(duty % 100)
    time.sleep(1)