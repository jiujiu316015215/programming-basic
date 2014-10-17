# search

values = [ 1, 100, 2, 66, 55, 44, 88, 77, 12, 23, 45, 9 ]
key = 88

found = False
numElements = len(value)
index = 0

#for value in values:
while not found and index <numElements:
	value = values[index]
   if value == key:
      print (key, "found in list")
      found = True
      index = index + 1

if not found:
   print (key, "not found in list.")
