from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-t", "--threads", dest="threads",
                  help="select number of threads to run the program on: 1,2,4,8", default=1)
parser.add_option("-p", "--program", dest="prog",
                  help="programCall example: \"python throughPutRun.py -s 64\"", default=1)

(options, args) = parser.parse_args()

threads = int(options.threads)
prog = ' \"'+ str(options.prog)+'\"'

#print 'threads: ' +str(threads)
#print 'programCall: '+str(prog)

#programCall = ' \"python throughPutRun.py -s 64\"'
programString = ''

for i in range(0,threads):
	programString = programString + prog


#print 'parallel --no-notice :::'+programString

os.system('parallel --no-notice :::'+programString)



print ('Running threads: '+str(threads))
