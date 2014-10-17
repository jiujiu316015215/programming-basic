# 9-29
# swapfun

def swapplaces(name1,name2):
	temp = name1
	name = name2
	name2 = temp
	print ('First places goes to the awesome' + name1)

def main():
	firstplace = "Clair"
	secondplace = "Liz"
	swapplaces(firstplace,secondplace)
	print ("First:", firstplace)
	print ("Second:", secondplace)

main()
