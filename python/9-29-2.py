# 9-29
# swapfun

#def swapplaces(name1,name2):
	#name1,name2 = name2, name1
	#print ('First places goes to the awesome' + name1)

#def main():
	#firstplace = "Clair"
	#secondplace = "Liz"
	#swapplaces(firstplace,secondplace)
	#print ("First:", firstplace)
	#print ("Second:", secondplace)

#main()

## creat a funtion to read in from a file
import sys
def parsefile(fn):
	infile = open(fn,"r")
	for line in infile:
		line = line[:-1]
		tokens = line.split()
		print(tokens)
		#print(line)
	infile.close()
	
def main():
	dilename = sys.argv[1]
	parsefile(dilename)
main():
