# HOW TO RUN: python plotTest.py --title "Thread 1 IPC" -d 1,2,3,4,5 --ylabel "Instructions per cycle"
# Figure is saved into the current directory

import matplotlib.pyplot as plt
import numpy as np

title = str('Latency of all 1/2/4/8 threads')
print title + ' figure created'

x = np.array([3900000000,15625000000,62500000000,250000000000,1010000000000])
thread1 = np.array([2.47,2.69,11.86,54.43,223.57])
thread2 = np.array([4.09,3.92,12.96,59.67,226.91])
thread4 = np.array([4.48,5.13,14.54,75.87,263.42])
thread8 = np.array([5.01,7.90,20.66,137.03,282.2])



my_xticks = ['~X/256','~X/64','~X/16','~X/4','~X']
plt.xticks(x, my_xticks,rotation='90',fontsize = 5)
plt.plot(x, thread1,'o-')
plt.plot(x, thread2,'o-')
plt.plot(x, thread4,'o-')
plt.plot(x, thread8,'o-')


plt.legend(['1 Thread', '2 Threads', '4 Threads', '8 Threads'], loc='upper left')

plt.xlabel('Total Number of Instructions (X = ~1 Trillion)')
plt.ylabel('Time (seconds)')	#plt.ylabel('Instructions per cycle')
plt.title(str(title))	#'Thread 1 IPC'
plt.margins(0.1)
plt.grid(True)
plt.savefig('Latency of all 1.2.4.8 threads.png')

plt.show()

