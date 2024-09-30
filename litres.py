"""
prompt user budget
store as total_budget
propmt the gas station to enter price for litres
store as price_per_litre
multipy the total_budget*price_per_litres
display result

"""

total_budget = float(input("enter the user input"))
price_per_litre = 855
litre = total_budget / price_per_litre
print(f"the litres of fuel is {litre:.2f}litres")
