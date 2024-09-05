# Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

userInput1 = int(input("Base: "))
userInput2 = int(input("Power: "))
def exponent(base, exp): 
    value = base ** exp
    print(f"{base} raised to the power of {exp} is: {value}")

exponent(userInput1, userInput2)
