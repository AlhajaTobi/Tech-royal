numbers = list(range(1,16))

print(numbers)

numbers = list(range(1,16))
duplicated_list = [item for item in numbers for _ in range(2)]
print(duplicated_list)

max_num = 0
for large in numbers:
	if large > max_num:
		max_num = large
print(max_num)

"""min_num = 0
for smallest in numbers:
	if smallest < min_num:
		min_num = smallest
print(min_num)
"""

smallest_element = min(numbers)
print(smallest_element)

