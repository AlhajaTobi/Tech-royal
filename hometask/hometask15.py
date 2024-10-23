numbers = [ 2,4,5,7,8]

product = 1

for index in range (2 , len(numbers), 5):
	product *= numbers[index]
print(product)