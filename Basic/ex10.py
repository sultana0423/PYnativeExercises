# Merge two lists using the following condition
# Given two lists of numbers, write a Python code to create a new list such that 
# the latest list should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

for num in list1:
    if num % 2 == 1:
        list3.append(num)
for num in list2:
    if num % 2 == 0:
        list3.append(num)

print(f"result list: {list3}")
