from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-t", "--test", dest="test",
                  help="Which benchmark settings you want to run", default=-1)
parser.add_option("-p", "--program", dest="prog",
                  help="programCall example: \"python throughPutRun.py -s 64\"", default=1)

(options, args) = parser.parse_args()

tests = int(options.test)


#Running on Size x/256
os.system('sudo perf stat -D 20 -I 10 -e L1-dcache-load-misses,l2_rqsts.miss,branch-misses,branch-instructions,instructions,mem_load_uops_retired.l3_miss,cpu-cycles,LLC-load-misses -x, -o output.csv sudo docker run -e threadCount=4 -e SIZE=64 jusclee/ce-202:firstTry')
  489  python interval-normalize.py output.csv --output mpki.csv
  490  python plot-normalized-ipc.py mpki.csv --title "Thread 4 Size x/64 MPKI" --ylabel "Misses per 1000 Instructions"

os.system('toplev.py --all --quiet --output thread_1_size_256.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 256"')
os.system('toplev.py --all --quiet --output thread_2_size_256.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 256"')
os.system('toplev.py --all --quiet --output thread_4_size_256.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 256"')
os.system('toplev.py --all --quiet --output thread_8_size_256.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 256"')


#Running on size x/64
os.system('toplev.py --all --quiet --output thread_1_size_64.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 64"')
os.system('toplev.py --all --quiet --output thread_2_size_64.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 64"')
os.system('toplev.py --all --quiet --output thread_4_size_64.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 64"')
os.system('toplev.py --all --quiet --output thread_8_size_64.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 64"')


#Running on size x/16
os.system('toplev.py --all --quiet --output thread_1_size_16.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 16"')
os.system('toplev.py --all --quiet --output thread_2_size_16.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 1 -s 16"')
os.system('toplev.py --all --quiet --output thread_4_size_16.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 1 -s 16"')
os.system('toplev.py --all --quiet --output thread_8_size_16.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 1 -s 16"')

#Running on size x/4
os.system('toplev.py --all --quiet --output thread_1_size_4.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 4"')
os.system('toplev.py --all --quiet --output thread_2_size_4.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 4"')
os.system('toplev.py --all --quiet --output thread_4_size_4.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 4"')
os.system('toplev.py --all --quiet --output thread_8_size_4.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 4"')

#Running on size x
os.system('toplev.py --all --quiet --output thread_1_size_1.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 1"')
os.system('toplev.py --all --quiet --output thread_2_size_1.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 1"')
os.system('toplev.py --all --quiet --output thread_4_size_1.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 1"')
os.system('toplev.py --all --quiet --output thread_8_size_1.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 1"')

'''
#1 Thread
print('RUNNING 1 THREAD ON X')
#os.system('toplev.py --all --quiet --output thread_1_size_1.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 1"')
#print('CHECKING STATS ON IPC')
os.system('3>thread_1_size_1_IPC.txt perf stat --log-fd 3 python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 1"')


print('RUNNING 1 THREAD ON X/4')
#os.system('toplev.py --all --quiet --output thread_1_size_4.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 4"')
os.system('3>thread_1_size_4_IPC.txt perf stat --log-fd 3 python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 4"')

print('RUNNING 1 THREAD ON X/16')
#os.system('toplev.py --all --quiet --output thread_1_size_16.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 16"')
os.system('3>thread_1_size_16_IPC.txt perf stat --log-fd 3 python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 16"')

print('RUNNING 1 THREAD ON X/64')
#os.system('toplev.py --all --quiet --output thread_1_size_64.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 64"')
os.system('3>thread_1_size_64_IPC.txt perf stat --log-fd 3 python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 64"')

print('RUNNING 1 THREAD ON X/256')
#os.system('toplev.py --all --quiet --output thread_1_size_256.txt python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 256"')
os.system('3>thread_1_size_256_IPC.txt perf stat --log-fd 3 python runThreads.py -t 1 --program "python throughPutRun.py -t 1 -s 256"')
 

#2 Threads
print('RUNNING 2 THREAD ON X')
#os.system('toplev.py --all --quiet --output thread_2_size_1.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 1"')
os.system('3>thread_2_size_1_IPC.txt perf stat --log-fd 3 python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 1"')

print('RUNNING 2 THREAD ON X/4')
#os.system('toplev.py --all --quiet --output thread_2_size_4.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 4"')
os.system('3>thread_2_size_4_IPC.txt perf stat --log-fd 3 python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 4"')

print('RUNNING 2 THREAD ON X/16')
#os.system('toplev.py --all --quiet --output thread_2_size_16.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 16"')
os.system('3>thread_2_size_16_IPC.txt perf stat --log-fd 3 python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 16"')

print('RUNNING 2 THREAD ON X/64')
#os.system('toplev.py --all --quiet --output thread_2_size_64.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 64"')
os.system('3>thread_2_size_64_IPC.txt perf stat --log-fd 3 python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 64"')

print('RUNNING 2 THREAD ON X/256')
#os.system('toplev.py --all --quiet --output thread_2_size_256.txt python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 256"')
os.system('3>thread_2_size_256_IPC.txt perf stat --log-fd 3 python runThreads.py -t 2 --program "python throughPutRun.py -t 2 -s 256"')

#4 Threads

print('RUNNING 4 THREAD ON X')
#os.system('toplev.py --all --quiet --output thread_4_size_1.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 1"')
os.system('3>thread_4_size_1_IPC.txt perf stat --log-fd 3 python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 1"')

print('RUNNING 4 THREAD ON X/4')
#os.system('toplev.py --all --quiet --output thread_4_size_4.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 4"')
os.system('3>thread_4_size_4_IPC.txt perf stat --log-fd 3 python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 4"')

print('RUNNING 4 THREAD ON X/16')
#os.system('toplev.py --all --quiet --output thread_4_size_16.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 16"')
os.system('3>thread_4_size_16_IPC.txt perf stat --log-fd 3 python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 16"')

print('RUNNING 4 THREAD ON X/64')
#os.system('toplev.py --all --quiet --output thread_4_size_64.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 64"')
os.system('3>thread_4_size_64_IPC.txt perf stat --log-fd 3 python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 64"')

print('RUNNING 4 THREAD ON X/256')
#os.system('toplev.py --all --quiet --output thread_4_size_256.txt python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 256"')
os.system('3>thread_4_size_256_IPC.txt perf stat --log-fd 3 python runThreads.py -t 4 --program "python throughPutRun.py -t 4 -s 256"')

#8 Threads
print('RUNNING 8 THREAD ON X')
#os.system('toplev.py --all --quiet --output thread_8_size_1.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 1"')
os.system('3>thread_8_size_1_IPC.txt perf stat --log-fd 3 python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 1"')

print('RUNNING 8 THREAD ON X/4')
#os.system('toplev.py --all --quiet --output thread_8_size_4.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 4"')
os.system('3>thread_8_size_4_IPC.txt perf stat --log-fd 3 python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 4"')

print('RUNNING 8 THREAD ON X/16')
#os.system('toplev.py --all --quiet --output thread_8_size_16.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 16"')
os.system('3>thread_8_size_16_IPC.txt perf stat --log-fd 3 python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 16"')

print('RUNNING 8 THREAD ON X/64')
#os.system('toplev.py --all --quiet --output thread_8_size_64.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 64"')
os.system('3>thread_8_size_64_IPC.txt perf stat --log-fd 3 python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 64"')

print('RUNNING 8 THREAD ON X/256')
#os.system('toplev.py --all --quiet --output thread_8_size_256.txt python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 256"')
os.system('3>thread_8_size_256_IPC.txt perf stat --log-fd 3 python runThreads.py -t 8 --program "python throughPutRun.py -t 8 -s 256"')

'''

'''
#Shrink all output files
print('Shrinking all output files')
os.system('python file_shrink.py thread_1_size_1.txt')
os.system('python file_shrink.py thread_1_size_4.txt')
os.system('python file_shrink.py thread_1_size_16.txt')
os.system('python file_shrink.py thread_1_size_64.txt')
os.system('python file_shrink.py thread_1_size_256.txt')

os.system('python file_shrink.py thread_2_size_1.txt')
os.system('python file_shrink.py thread_2_size_4.txt')
os.system('python file_shrink.py thread_2_size_16.txt')
os.system('python file_shrink.py thread_2_size_64.txt')
os.system('python file_shrink.py thread_2_size_256.txt')

os.system('python file_shrink.py thread_4_size_1.txt')
os.system('python file_shrink.py thread_4_size_4.txt')
os.system('python file_shrink.py thread_4_size_16.txt')
os.system('python file_shrink.py thread_4_size_64.txt')
os.system('python file_shrink.py thread_4_size_256.txt')

os.system('python file_shrink.py thread_8_size_1.txt')
os.system('python file_shrink.py thread_8_size_4.txt')
os.system('python file_shrink.py thread_8_size_16.txt')
os.system('python file_shrink.py thread_8_size_64.txt')
os.system('python file_shrink.py thread_8_size_256.txt')

'''



