#Print characters from a string that are present at an even index number
#Write a program to accept a string from the user and display characters that are present at an even index number.

userInput = str(input("Enter String: "))
 
def even_index_char(str):
    print(f"Orginal String is {str}")
    print("Printing only even index chars")
    for char in str:
        index = str.index(char)
        if index % 2 == 0:
            print(char)
            
even_index_char(userInput)
