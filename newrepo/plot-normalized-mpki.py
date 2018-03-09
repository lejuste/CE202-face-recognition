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


l1 = []
for x, y in zip(columns['L1-dcache-load-misses'],columns['instructions']):
    if(y==0)or(x==0):
	l1.append(float('NaN'))
    else:
	value = float(x)/float(y)/float(1000)
        l1.append(value)

l2 = []
for x, y in zip(columns['l2_rqsts.miss'],columns['instructions']):
    if(y==0)or(x==0):
	l2.append(float('NaN'))
    else:
	value = float(x)/float(y)/float(1000)
        l2.append(value)

l3 = []
for x, y in zip(columns['mem_load_uops_retired.l3_miss'],columns['instructions']):
    if(y==0)or(x==0):
	l3.append(float('NaN'))
    else:
	value = float(x)/float(y)/float(1000)
        l3.append(value)

branchMisses = []
for x, y in zip(columns['branch-misses'],columns['branch-instructions']):
    if(y==0)or(x==0):
	branchMisses.append(float('nan'))
    else:
	value = float(x)/float(y)/float(1000)
        branchMisses.append(value)
print l1
print l2
print l3
print branchMisses

plt.plot(timestamps,l1,'o-',label='L1')
plt.plot(timestamps,l2,'o-',label='L2')
plt.plot(timestamps,l3,'o-',label='L3')
plt.plot(timestamps,branchMisses,'o-',label='Branch')

plt.xlabel('Time (seconds)')
plt.ylabel(args.ylabel)
plt.title(str(args.title))
plt.margins(0.1)
plt.grid(True)
leg = plt.legend()
leg.get_frame().set_alpha(0.5)
plt.tight_layout()
if args.output:
    plt.savefig(args.output)
else:
    plt.show()
