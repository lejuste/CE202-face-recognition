#!/usr/bin/env python
# plot already normalized data
# first column is time stamp
#cloned from https://github.com/andikleen/pmu-tools/blob/master/plot-normalized.py
import csv
import matplotlib.pyplot as plt
import sys
import argparse

ap = argparse.ArgumentParser(usage='Plot already normalized CSV data')
ap.add_argument('--output', '-o', help='Output to file. Otherwise show.',
                nargs='?')
ap.add_argument('--title', '-t', help='title of plot',
                nargs='?')
ap.add_argument('--ylabel', '-y', help='ylabel for plot',
                nargs='?')
ap.add_argument('inf', nargs='?', default=sys.stdin, type=argparse.FileType('r'),
                help='input CSV file')

args = ap.parse_args()

inf = args.inf

rc = csv.reader(inf)

num = 0
timestamps = []
columns = dict()
listTracker = []
for r in rc:
    num += 1
    if num == 1:
        for j in r[1:]:
            columns[j] = []
            listTracker.append(str(j))
        continue
    timestamps.append(r[0])
    c = 1

    for j in listTracker:#used to be columns which would add to any random plot	
        try:
            columns[j].append(float(r[c]))
        except ValueError:
            columns[j].append(float('nan'))
        c += 1

IPC = []
for x, y in zip(columns['cpu-cycles'],columns['instructions']):
    if(y==0)or (x==0):
	if not IPC:
	    IPC.append(0)
	else:
	    IPC.append(IPC[-1])
    else:
	value = float(y)/float(x)
        IPC.append(value)

plt.plot(timestamps,IPC,'b-',label='IPC')
plt.xlabel('Time (seconds)')
plt.ylabel(args.ylabel)	#plt.ylabel('Instructions per cycle')
plt.title(str(args.title))	#'Thread 1 IPC'
plt.margins(0.1)
plt.grid(True)
leg = plt.legend()
leg.get_frame().set_alpha(0.5)

if args.output:
    plt.savefig(args.output)
    #plt.show()
else:
    plt.show()
