numbers = []
import random
for _ in range(1, 20):
	numbers.append(random.randrange(1,20))
print(numbers)

for index in range(1,len(numbers), 2):
	    numbers[index] = numbers[index]**2
print(numbers)