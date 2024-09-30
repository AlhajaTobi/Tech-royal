def get_transaction
balance=0
	user_input = input("Enter option 1 if you want to deposit or  2 to withdraw or 0 to end : ")
	if user_input == '1' :
		amount=float(input("Enter amount:  "))
		balance += amount
	elif user_input == '2' :
		amount= float(input("Enter amount:  "))
		if balance < amount:
			print ("Insufficient fund")
		else:
			balance -= amount 
	elif user_input == '0':
		print("your balance is ", balance)
		break


