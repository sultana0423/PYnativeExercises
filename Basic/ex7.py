# Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer"
 
def emma(str_x):
    str_y = str_x.split()
    emma = str_y.count("Emma")
    print(f"Emma appeared {emma} times")

emma(str_x)
  
