#!/bin/bash

#Creating 20 plots with manually inputted data from benchmark tests

#Latency Tests
python plotTest-Latency.py 

#IPC
python plotTest.py --title "Throughput Thread 1 IPC" -d 1.85,1.98,2.5,2.09,2.06 --ylabel "Instructions per cycle"
python plotTest.py --title "Throughput Thread 2 IPC" -d 1.26,1.56,2.3,1.96,2.03 --ylabel "Instructions per cycle"
python plotTest.py --title "Throuhgput Thread 4 IPC" -d 1.16,1.20,1.48,1.6,1.89 --ylabel "Instructions per cycle"
python plotTest.py --title "Throughput Thread 8 IPC" -d 1.1,1.12,1.5,1.68,1.8 --ylabel "Instructions per cycle"

#L1 MPKI
python plotTest.py --title "Throughput Thread 1 L1 MPKI" -d 1,2,3,4,5 --ylabel "L1 misses per kilo instructions"
python plotTest.py --title "Throughput Thread 2 L1 MPKI" -d 1,2,3,4,5 --ylabel "L1 misses per kilo instructions"
python plotTest.py --title "Throughput Thread 4 L1 MPKI" -d 1,2,3,4,5 --ylabel "L1 misses per kilo instructions"
python plotTest.py --title "Thread 8 L1 MPKI" -d 1,2,3,4,5 --ylabel "L1 misses per kilo instructions"

#L2 MPKI
python plotTest.py --title "Throughput Thread 1 L2 MPKI" -d 1,2,3,4,5 --ylabel "L2 misses per kilo instructions"
python plotTest.py --title "Throughput Thread 2 L2 MPKI" -d 1,2,3,4,5 --ylabel "L2 misses per kilo instructions"
python plotTest.py --title "Throughput Thread 4 L2 MPKI" -d 1,2,3,4,5 --ylabel "L2 misses per kilo instructions"
python plotTest.py --title "Throughput Thread 8 L2 MPKI" -d 1,2,3,4,5 --ylabel "L2 misses per kilo instructions"

#L3 MPKI
python plotTest.py --title "Throughput Thread 1 L3 MPKI" -d 1,2,3,4,5 --ylabel "L3 misses per kilo instructions"
python plotTest.py --title "Throughput Thread 2 L3 MPKI" -d 1,2,3,4,5 --ylabel "L3 misses per kilo instructions"
python plotTest.py --title "Throughput Thread 4 L3 MPKI" -d 1,2,3,4,5 --ylabel "L3 misses per kilo instructions"
python plotTest.py --title "Throughput Thread 8 L3 MPKI" -d 1,2,3,4,5 --ylabel "L3 misses per kilo instructions"

#Branch MPKI
python plotTest.py --title "Throughput Thread 1 Branch MPKI" -d 1,2,3,4,5 --ylabel "Branch misses per kilo instructions"
python plotTest.py --title "Throughput Thread 2 Branch MPKI" -d 1,2,3,4,5 --ylabel "Branch misses per kilo instructions"
python plotTest.py --title "Throughput Thread 4 Branch MPKI" -d 1,2,3,4,5 --ylabel "Branch misses per kilo instructions"
python plotTest.py --title "Throughput Thread 8 Branch MPKI" -d 1,2,3,4,5 --ylabel "Branch misses per kilo instructions"



