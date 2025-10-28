import r2r_adc as radc
import time
from adc_plot import plot_voltage_vs_time

dynamic_range = 3.18

adc = radc.R2R_ADC(dynamic_range, 0.0001)

voltage_values = []
time_values = []
duration = 10.0

if __name__ == "__main__":
    try:
        start_time = time.time()

        while time.time() - start_time < duration:
            time_values.append(time.time() - start_time)
            print(time.time())
            voltage_values.append(adc.get_sc_voltage())
            print(adc.get_sc_voltage())
        plot_voltage_vs_time(time_values, voltage_values, dynamic_range, duration)
    finally:
        adc.deinit()
