import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"data: {data}, upper byte:{upper_data_byte:x}, lower byte: {lower_data_byte:x}, number: {number}")
        return number
    def get_voltage(self):
        return float(self.get_number())*self.dynamic_range/1024 

if __name__ == "__main__":
    adc = MCP3021(5, verbose = True)
    try:


        while True:
            print(adc.get_voltage())
            time.sleep(0.1)
    finally:
        adc.deinit()
