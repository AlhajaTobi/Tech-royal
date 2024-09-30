def get_total(first_number , second_number , third_number):
		return first_number + second_number + third_number
get_total = (50 +12 +20)
print(get_total)
	
def get_sum(*numbers):
	print(numbers)
	total=0
	for number in numbers:
		total += number
	return total


print(get_sum(40, 50, 100, 20, 60))
print(get_sum(1, 3, 6, 7, 4, 9, 40, 56, 67))


