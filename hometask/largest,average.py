user_input = float(input("enter a number: "))
smallest_num = user_input
largest_num = user_input
for number in range (1,5):
	user_input = float(input("enter a number: "))

	sum+=user_input
	average = sum/user_input
	#product = number**2

	
	if user_input < smallest_num:
		smallest_num = user_input

	
	if user_input > largest_num:
		largest_num = user_input

	

print ("sum is: ", sum ,"average is: ", average, "product is: ", user_input**2)
print(smallest_num)
print(largest_num)