# Given two integer numbers, return their product only if the product is
# equal to or lower than 1000. Otherwise, return their sum.

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

if number1 * number2 <= 1000:
    result = number1 * number2
    print(f"The result is {result}")
else: 
    result = number1 + number2
    print(f"The result is {result}")
