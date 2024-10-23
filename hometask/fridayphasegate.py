try:	
	row = int(input('Enter the number of rows'))
	column = int(input('Enter the number of columns'))
	digit = [[0] * column]*row

	
	for i  in range (row):
		for j in range(column):
			print(f'  {i * j:5}', end = " ")

		print()
except(Exception):
	print("not valid")
