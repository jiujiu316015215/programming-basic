#File I/O

infile = open("data.txt","r")
"""
for line in infile:
	print(line[:-1])
	myvariable = line[:-1]
	print(myvariable)
print(myvariable)
"""
#calculate the average of numbers in file and print average
infile = open("data.txt","r")
summ = 0
count = 0
for line in infile:
	number = int(line[:-1])
	#print(number)
	summ = summ + number
	count = count + 1
print ("avg:",(summ/count))

outfile = open("output.txt","a")
outfile.write(str(summ/count))
outfile
outfile.close()
