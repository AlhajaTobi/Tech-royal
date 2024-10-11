"""
prompt user to enter yearof birth
save as year_of_birth
save current year as current_year
substract current_year from YOB
Save as user_age

"""
year_of_birth = int(input("Enter the year of birth"))
current_year = 2024
user_age = current_year - year_of_birth
if user_age < 18:
	print (" not Eligiable to vote")
else:
	print("Eligiable to vote")


