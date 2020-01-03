# importing matplotlib module
from matplotlib import pyplot as plt

# x-axis values
time = [14.16,7.46,5.15,4.13,3.64,3.34,3.23,3.21,2.99,2.85]

# Y-axis values
cpu = [17,26,35,40,49,58,63,73,83,90]

workers = [1,2,3,4,5,6,7,8,9,10]

# Function to plot
#plt.plot(time,cpu)

#plt.plot(time,workers)

plt.plot(workers,cpu)

# function to show the plot
plt.show()
