number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))
number3 = int(input("Enter third number"))

minimum = number1

 if number2 < minimum :
 	minimum = number2

 if number3 < minimum :
 	minimum = number3

print('The minimum value :' minimum)