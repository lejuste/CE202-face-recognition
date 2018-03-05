import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,3900000000,15625000000,62500000000,250000000000,1010000000000])
y = np.array([2.4,2.2,2.0,1.8,1.6,1.4])
my_xticks = ['0','~X/256','~X/64','~X/16','~X/4','~X']
plt.xticks(x, my_xticks)
plt.plot(x, y,'bo')
plt.xlabel('Input Size')
plt.ylabel('Instructions per cycle')
plt.title('Thread 1 IPC')
plt.show()

