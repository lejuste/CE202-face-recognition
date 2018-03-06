import matplotlib.pyplot as plt
import numpy as np

from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-t", "--title", dest="title",
                  help="Plot title", default='NO TITLE')
parser.add_option("-d", "--data", dest="data",
                  help="Input data as a string form of a list", default='1')

(options, args) = parser.parse_args()

title = str(options.title)
list_string = str(options.data)

print title
print list_string

list_list = list_string.split(",")
print list_list




x = np.array([3900000000,15625000000,62500000000,250000000000,1010000000000])
y = np.array([2.2,2.0,1.8,1.6,1.4])
my_xticks = ['~X/256','~X/64','~X/16','~X/4','~X']
plt.xticks(x, my_xticks,rotation='90',fontsize = 5)
plt.plot(x, y,'bo')
plt.xlabel('Input Size')
plt.ylabel('Instructions per cycle')
plt.title(str(title))#'Thread 1 IPC'
plt.margins(0.1)
plt.grid(True)
plt.show()
