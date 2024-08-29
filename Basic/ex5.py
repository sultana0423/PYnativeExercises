# Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

def start_and_end(array):
    arrayL = len(array)
    result = False
    if array[0] == array[arrayL - 1]:
        result = True
    print(f"Given list: {array}")
    print(f"result is {result}") 
