numbers = [4, 6, 25, 32, 49, 34, 50, 7, 45, 23]

numbers2 = list(range(1, 51, 5))

print(len(numbers))

def get_length(args):
	count = 0
	for _ in args:
		count += 1
	return count

print(get_length(numbers))

print(numbers[-1])

total = 0
for index in range(1, len(numbers), 2):
	total += numbers[index]

print("total of even positions is", total)	

totalz = 0
for index in range(0, len(numbers), 2):
	totalz += numbers[index]

print("total of odd positions is", totalz)

product = 1
for index in range(2, len(numbers), 3):
	product *= numbers[index]


print("the product is", product)

