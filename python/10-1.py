# 10-1
# function ex

def isEven(num):
	even = False
	if num % 2 == 0:
		even = True
	else:
		even = False
	return even
	
#def is EvenVersion2(num):
#	return num % 2 ==0
		
def main():
	mynum = 5
	print(isEven(mynum))

main()


