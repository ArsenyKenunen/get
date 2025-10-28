from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage, duration):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.xlabel("time, s")
    plt.ylabel("voltage, V")
    plt.title("V(t)")
    #plt.ylim(max_voltage)
    #plt.xlim(duration)
    plt.grid()
    plt.show()