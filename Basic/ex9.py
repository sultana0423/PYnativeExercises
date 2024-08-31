# Check Palindrome Number
# Write a Python code to check if the given number is palindrome. 
# A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.

number = str(input("Enter a number: "))

def num_pali(num):
    print(f"original number {num}")
    numRList = []
    length = len(num)
    i = len(num) - 1
    while i >= 0:
        numRList.append(num[i])
        i -= 1
    numR = ""
    for n in numRList:
        numR += n
    if numR == num:
        print("Yes. given number is palindrome number")
    else: 
        print("No. given number is not palindrome number")

num_pali(number)
