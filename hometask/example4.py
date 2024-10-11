"""
ask user to enter 3 integers or numbers
store first number as number1
store second number as number2
store third number as number3

then compare the three and the output should be in increasing number
"""
number1 = int(input("Enter firstnumber"))
number2 = int(input("Enter secondnumber"))
number3 = int(input("Enter thirdnumber"))

if number1 > number2:
   number1, number2 = number2,number1
if number1 > number3:
   number1,number3 = number3,number1
if number2 > number3 :
   number2,number3 = number3,number2
print("the numbers in increasing order :",number1,number2,number3)
   


