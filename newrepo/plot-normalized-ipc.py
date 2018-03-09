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
for r in rc:
    #print(r)
    num += 1
    if num == 1:
        for j in r[1:]:
            columns[j] = []
        continue
    timestamps.append(r[0])
    c = 1
    for j in columns:
        try:
            columns[j].append(float(r[c]))
        except ValueError:
            columns[j].append(float('nan'))
        c += 1

IPC = []
for x, y in zip(columns['cpu-cycles'],columns['instructions']):
    if(y==0):
	IPC.append(0)
	continue
    else:
        IPC.append(x/y)

plt.plot(timestamps,IPC,'bo-',label='IPC')
plt.xlabel('Time (seconds)')
plt.ylabel(args.ylabel)	#plt.ylabel('Instructions per cycle')
plt.title(str(args.title))	#'Thread 1 IPC'
plt.margins(0.1)
plt.grid(True)
leg = plt.legend()
leg.get_frame().set_alpha(0.5)
plt.savefig('dude.png')

if args.output:
    plt.savefig(args.output)
else:
    plt.show()
