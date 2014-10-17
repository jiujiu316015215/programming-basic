# 9-22

grades = [99,87,96,57,91]
print (len(grades))
print (grades[:2])

something = grades[:0]
print(something)

print (57 in grades)
print (9999 in grades)
print ("57" in grades)

if 57 in grades:
	grades[3] = 100  # print ("Un-oh")
	
print (grades)

for gr in grades:
	print (gr + 2)
	
# testing split
words = "Hi ho off to work we go   4455"
word_list = words.split()
print (word_list)
for token in word_list:
	print(token)
	
# Date Example!
myDate = "12/04/2014"
print (myDate)
date = myDate.split("/")
print (date)

month = date[0]
day = date[1]
year = date[2[
print (day + "." + month + "." + year)
