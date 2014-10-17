def getMin(x, y):
	if x < y:
		min = x
	else:
		min = y
	return min

def main():
	minvalue = getMin( getMin(2,3), 5)
	print (minvalue)

main()
