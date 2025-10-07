import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
dac = [16, 20, 21, 25, 26, 17, 27, 22]
gpio.setup(dac, gpio.OUT)

dynamic_range = 3.15

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"voltage exceeds the DAC dynamic range (0.0 - {dynamic_range:.2}V)")
        print("voltage set to 0V")
        return 0
    return int(voltage / dynamic_range * 255)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def number_to_dac(number):
    for i in range(8):
            gpio.output(dac[i], dec2bin(number)[i])


try:
    while True:
        try:
            voltage = float(input("input voltage in Volts: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        
        except ValueError:
            print("no input number, try again\n")

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
