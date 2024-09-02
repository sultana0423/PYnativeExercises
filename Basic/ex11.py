# Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = 7536
num_str = str(number)
num_rev = ""
i = len(num_str) - 1
while i >= 0:
    num_rev += " " + num_str[i] + " "
    i -= 1
print(num_rev)
