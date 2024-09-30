week_days = [ "sunday", "monday" , " tuesday" , "wednesday", "thursday", "friday",
"saturday"]


today = int(input(" Enter date of the day"))
number_days = int(input("Date for future date"))

to_get_future_day = (today + number_days) %7


print(f" today is {week_days[today]}")

	