#!/usr/bin/python3

#Lab4
#Author: B.W. Israelsen
#Purpose:
#Introduce students to submitting files to the online grader
#https://web-cog.cs.colorado.edu/login.html

#Load the random library below:


#Create variable to store all of the random numbers generated
store = []

#get 5000 different random numbers by looping 5000 times
for i in range(1,5001):
  ###
  #insert the random function below:
  rand = #Insert your code here

  #add the random number into the "store" variable
  store.append(rand)

#calculate the average
avg = sum(store)/5000

#print the result, rounded to 2 decimal places
print("The average is: %.2f" %avg)