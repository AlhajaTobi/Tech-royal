def subtraction_number(*numbers):
	total = 0
	for number in numbers:
		total -= number
	return total

print(substraction_number(10, 20, 50))
help(print)
