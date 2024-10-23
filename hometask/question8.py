user_number = [12,14,20,50,30,28,19]
print(len(user_number))

max_num = 0
for i in user_number:
	if i > max_num:
		max_num = i
print("large number:", max_num)

smallest_element =min(user_number)
print("smallest element :", smallest_element)

duplicated_list = [item for item in user_number for _ in range(5)]
print(duplicated_list)
duplicated_list = user_number *4
print(duplicated_list)

letters = "my name is loba"
capital = letters.title()

print(capital)

average = sum(numbers)/get_length(numbers)
print(average)