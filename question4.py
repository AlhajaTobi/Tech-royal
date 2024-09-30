import random

number1 = random.randint(0, 1000)
number2= random.randint(0, 1000)
guess= int("what is the sum of the guessnumber:  ")

correct_guess= (number1 + number2== guess)

print(correct_guess)
	