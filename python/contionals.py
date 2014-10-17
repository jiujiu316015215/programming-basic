# conditionals

x = 5
y = 6
z = 6

print (x < y <= z)

print (x < y and y <= z)

age = 7
if age > 21:
	print ("Hace a pint!")
elif age == 13:
	print ("Welcome to teems!")
else:
	print ("Have a cookie!")

from random import randint
answer = randint(1,10)
print "Think of a number between 1 and 10."
guess = input("What is your gusee?")
if answer == guess:
	print "You win!"
else:
	print "You lose!"
