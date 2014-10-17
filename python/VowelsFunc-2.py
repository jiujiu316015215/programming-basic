'''
Exercise: We could count the vowels in a sentence:
'''
'''
sentence = "The quick brown fox jumped over the lazy dog"
vowels = 0
for letter in sentence:
	if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
		vowels = vowels + 1

print("The sentence has ", vowels, "vowels")
'''

'''
In this example, the sentence was fixed, and the code could calculate
the number of vowels in that sentence only. But, what if you wanted this
to work for any sentence. We could make the sentence an input from the 
user and then put the calculation in a loop. But, there's an additional
issue, the code is kinda messy. The thing we really care about is 
counting the number of vowels, and our code will be more readable if
we can put the code we've written into a function, and then call that
function. That will perform the task that we're interested in, which is
counting vowels, and it will also make our code more readable.
'''
def countVowels(sentence):
	vowels = 0
	for letter in sentence:
		if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
			vowels = vowels + 1
	return vowels
'''
A few things changed when we put the code in a function. The sentence is
now an argument that will be set outside the function. This will be
the string that the function uses for counting. The other change is that
we removed the print, and the function will now return a number.
'''
'''
Once we have the function, we can call it. We will pass it the sentence
that we've declared.
'''

sentence = "The quick brown fox jumped over the lazy dog"
vowels = countVowels(sentence)
print("The sentence has ", vowels, "vowels")

'''
By having a countVowels function, we've hidden the actual calculation,
or put it in a box so that we don't really have to look at it. The name
of our function tells us what it's doing.
In this example, I wrote the function to return a number, and depending
on what you wanted to do with the function once it's written, you could
return a number, or have it print the result of the calculation right
in the function. Here's an example of a problem where you would need it
to return a number.

Exercise: ask the user for two sentences, use the countVowels function
to count the number of vowels in each sentence, and then tell the user
which sentence has more vowels.
'''
