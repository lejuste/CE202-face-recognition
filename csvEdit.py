import sys

def main():
	#opens new file
	print 'starting!!!'
	h = open('newCSV.csv','w')
	for line in  open(sys.argv[1]):
    		print line
		if(valid(line)):
			h.write(line)
	print 'ending...'
	#f.close()
	h.close()

def valid(s):
	if "Backend" in s:
		return False
	else:
		return True 



if __name__ == '__main__':
	main()
