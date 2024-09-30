number1 = int(input("Enter first digit: "))
number2 = int(input("Enter second digit: "))
number3 = int(input("Enter third digit: "))


if number1 > number2:
    number1, number2 = number2, number1
if number1  > number3:
    number1, number3 = number3, number1
if number2 > number3:
    number2, number3 = number3, number2

print("This are the Digits in increasing order:", number1, number2, number3 )      