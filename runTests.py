#new python program to just test environmental variables when running a docker container

import os
import time
#getting the environment variables
threads = os.environ.get('threadCount')      #.get() is a safe way to get values from a dictionary if their key might not exist
size = os.environ.get('SIZE')

print 'threads: '+str(threads)
print 'size: '+str(size)

programString = 'python runThreads.py -t '+str(threads)+' --program \"python throughPutRun.py -s '+str(size)+'\"'
print programString
os.system(programString)
