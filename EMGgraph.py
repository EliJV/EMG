import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import Adafruit_ADS1x15

# Parameters
x_len = 200         # Number of points to display
y_range = [10, 40]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 200))
ys = [0] * x_len
ax.set_ylim(y_range)

# Create instance of ADS1115 ADC
adc = Adafruit_ADS1x15.ADS1115()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('Millivolts over Time')
plt.xlabel('Samples')
plt.ylabel('Milivolts')

# This function is called periodically from FuncAnimation
def animate(i, ys):

    # Read voltage from ADC ADS1115
    voltage = adc.read_adc(1, gain=GAIN)

    # Add y voltage to list
    ys.append(voltage)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=50,
    blit=True)
plt.show()
