# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

def num_curr_prev():
    print("Printing current and previous number sum in a range(10)")
    for i in range(10):
        curr = i
        prev = i - 1 if i - 1 != -1 else 0
        thierSum = curr + prev
        print(f"Current number {curr} Previous number {prev} Sum: {thierSum}")

num_curr_prev()
