
"""
prompt the user to enter principal amount
store as principal
collect annual interest rate
store as annual_interest_rate
collect the duration of the loan
store as duration_years
calculate the monthly rate using the formular.
Display result  as monthly return


"""





principal = int(input("Enter the loan amount: "))
annual_interest_rate = int(input("Enter the annual interest rate: "))
duration_in_years = int(input("enter the duration of the loan in years: "))

monthly_rate = (annual_interest_rate / 100) / 12
duration_of_year = duration_years * 12
loan_rate  = 1 + monthly_payment

loan_rate2 = loan_rate ** duration_of_loan
monthly_payment = (principal * monthly_payment * loan_rate2) / (loan_rate2 -1)
print("monthly payment is: $", (round(monthly_payment_rate,2)))
