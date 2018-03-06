import sys

def main():
	#opens new file
	newFile = 'shrink_'+str(sys.argv[1])

	h = open(newFile,'w')
	for line in  open(sys.argv[1]):
		if(valid(line)):
			h.write(line)
	h.close()

def valid(s):
	if "MPKI" in s:
		return True
	#if "IPC" in s:
	#	return True

	return False



if __name__ == '__main__':
	main()
