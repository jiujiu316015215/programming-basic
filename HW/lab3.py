import math
peritemcost = input ("What is the cost per item?")
numberofitem = input ("How many were purchased?")
tax = .0735

if ((peritemcost * 100) % 10 != 0):
	cost = peritemcost * (1 + tax) * numberofitem
else:
	cost = peritemcost * numberofitem
	
print ("The price is $%.2f" % cost)
