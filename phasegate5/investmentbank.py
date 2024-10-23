user_investment = int(input("Enter your investment: "))
number_of_years = int(input("Enter the years: "))
interest_percentage = int(input("Enter the percentage :"))
interest_rate = user_investment * interest_percentage/100
total_investment = user_investment + interest_rate
yearly_investment = interest_rate + user_investment
for number in range(1, number_of_years+1):
	rate = user_investment * (interest_percentage/100)
	investment = user_investment + rate
	user_investment = investment
	print(rate, investment)
				