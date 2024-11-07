import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

## YOUR CODE HERE ##
data = np.loadtxt(signal_filepath, delimiter=',', skiprows=2)

signal=data[:,2]

plt.title('Raw signal loaded from file')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.plot(signal)
plt.ylim(-1.5,.2)
plt.xlim(0,8000)
plt.show()

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##
diff = np.diff(signal)

plt.title('Signal after differentiation')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.plot(diff)
plt.ylim(-.2 , .2)
plt.xlim(0,8000)
plt.show()

"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
sqr = np.square(diff)

plt.title('Signal after squaring')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.plot(sqr)
plt.ylim(0, 0.04)
plt.xlim(0,8000)
plt.show()

"""
Step 5: Pass a moving filter over your data
"""

## YOUR CODE HERE
size = 30 ##reduce noise
g= np.ones(size) / size
moving_average = np.convolve(sqr,g)

plt.title('Signal after moving after filter')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.plot(moving_average)
plt.ylim(0, .01)
plt.xlim(0,8000)
plt.show()

# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
#plt.title('Process Signal for ' + database_name)
#plt.plot(signal)
#plt.show()