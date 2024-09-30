import random


number1 = random.randint(1, 100)
number2 = random.randint(1, 100)

guess = int(input("What is the sum of the generated number: "))


correct_guess = (number1 + number2 == guess)
print(correct_guess)