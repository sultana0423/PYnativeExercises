# Calculate income tax

income = 45000
tax_payable = 0
print(f"Income: {income}")

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    a = income - 10000
    tax_payable = x * 10 / 100
else:
    tax_payable = 0
    tax_payable = 10000 * 10 / 100
    tax_payable += (income - 20000) * 20 / 100

print(f"Total tax to pay is: {tax_payable}")
