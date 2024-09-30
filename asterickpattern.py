userinput = int(input("Enter user number"))
for rows in range (1, userinput+1):
	print(" ")
	for columns in range(rows, 0 , -1 ):
		print(" * ", end = " " )