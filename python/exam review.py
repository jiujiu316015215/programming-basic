# exam review

#review 10
def printBackAndForth(msg1,msg2):
	print(msg1 + " " + msg2)
	print(msg2,msg1)
def main():
	printBackAndForth("Money","Python")
main()

# review 17
def foo():
	x=3
	print ("foo has been called")
	
x=10
print ("x=",x)
foo()
print ("x=",x)

#review 28
myArray = [5,7,8,5,3,3,5,5,2]
for i in range( 3 ):
	print (myArray(i))
	
#review 35
def swapEnds(mylist):
	temp=mylist[0]
	mylist[0]=mylist[-1]
	mylist[-1]=temp	
print(myArray)
awapEnds(myArray)
print(myArray)

#review 66
scores = {}
scores['exam'] = 100
scores['quiz'] = 99
print(scores.get("exam"))
print(scores['exam'])

# 71
def printsum(num1,num2):
	print(num1+num2)
