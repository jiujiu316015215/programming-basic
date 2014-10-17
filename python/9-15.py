#9-15
#strings
fun =  "biking"
print (fun[0])
print (len(fun))
print (fun[-1])
print (fun[-3])

print (fun[2:4])

for i in range(1,10):
	print(i)
	
print ("HREH I AM")
print (fun[2:])
print (fun[:2])

print ("The meaning of the universe has been found and the answer is:")
print ("42")

print ("The meaning of the universe has been found and the answer is:"
	+"42"
	+" And the class applauded...")
	
print ("A" > 'a')
print ('A' < 'a')
print (ord('A'))



sum = 0
for i in range(1,100, 2):
	sum = sum + i
print (sum)


sum = 0
for i in range(1,100):
	if i % 2 ==1:
		sum = sum + i
print (sum)

print (13%7)

grade = 85
if grade >= 70:
	print ("1")
	if grade < 80:
		print ("2")
		if grade > 83:
			print ("3")
		else:
			print ("9")
	elif grade > 95:
		print ("4")
if grade < 50:
	print ("5")
else:
	print ("6")
	
x = 3
if 2 > x:
	print ("1")
else :
	print ("2")
	if 2 > x:
		print ("3")
	print ("4")
print ("5")
	
print (3**2)

str1 = "Hello"
str2 = 'spam'
str3 = '''Hello
	fine
	people'''
print(str1,str2,str3)
