# Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

numbers = [10, 20, 33, 46, 55]
def div_by_5(array):
    print(f"Given list is {array}")
    print("Divsible by 5")
    for num in array:
        if num % 5 == 0:
            print(num)
div_by_5(numbers)
