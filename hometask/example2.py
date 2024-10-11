"""
prompt the user to enter the year
save age as voter_age
compare the voter_age with the validage,
if lower,voter_age is not valid.
if voter_age is valid ,then voter_age is valid.
"""

voter_age = int(input("Enter your age"))
if voter_age < 18:
	print("You are too young to vote")
elif voter_age >= 18 and voter_age < 65:
	print ("You can vote")
elif voter_age >= 65:
	print("You are eligible to vote ,we will mail it to you")


	 