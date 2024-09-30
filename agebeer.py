name = input("Enter your name : ")
user_age = int(input("Enter user age : "))

if user_age < 18:
	print(name +"  you are underage")
elif user_age >= 18 and user_age <= 55:
	print(name + "  you are eligiable")

else:
	print(name + "  you are too old")