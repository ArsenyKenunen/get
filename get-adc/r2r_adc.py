import RPi.GPIO as gpio
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

class R2R_DAC:
    def __init__(self, bits, dynamic_range, verbose = False):
        self.bits = bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        gpio.setmode(gpio.BCM)
        gpio.setup(self.bits, gpio.OUT, initial = 0)
    def deinit(self):
        gpio.output(self.bits, 0)
        gpio.cleanup()
    def setnumber(self, number):
        for i in range(8):
            gpio.output(self.bits[i], dec2bin(number)[i])
    def setvoltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"voltage exceeds the DAC dynamic range (0.0 - {dynamic_range:.2}V)")
            print("voltage set to 0V")
            return 0
        self.setnumber( int(round(voltage / self.dynamic_range * 255)))


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25,11]
        self.comp_gpio = 21
        self.dac = R2R_DAC(self.bits_gpio, self.dynamic_range, True)

        gpio.setmode(gpio.BCM)
        gpio.setup(self.bits_gpio, gpio.OUT, initial = 0)
        gpio.setup(self.comp_gpio, gpio.IN)
        
    def deinit(self):
        self.dac.deinit()
    
    def number_to_dac(self, number):
        self.dac.setnumber(number)
    
    def sequential_counting_adc(self):
        self.number_to_dac(0)
        for cnt in range(0, 255):
            comp = gpio.input(self.comp_gpio)
            self.number_to_dac(cnt)
            time.sleep(self.compare_time)
            if(comp == 1):
                return cnt
        return cnt

    def successive_approximation_adc(self):
        cnt = 0
        self.number_to_dac(cnt)
        for i in range(1,9):
            self.number_to_dac(cnt)
            comp = gpio.input(self.comp_gpio)
            time.sleep(self.compare_time)
            if(comp == 0):
                cnt += int(256/(2**i))
            else:
                cnt -= int(256/(2**i))
        return cnt

    def get_sc_voltage(self):
        return self.sequential_counting_adc()/256*self.dynamic_range

    def get_sar_voltage(self):
        return self.successive_approximation_adc()/256*self.dynamic_range

if __name__ == "__main__":
    adc = R2R_ADC(3.18, 0.001)
    try:


        while True:
            #print(adc.get_sc_voltage())
            print(adc.get_sar_voltage())
    finally:
        adc.deinit()
