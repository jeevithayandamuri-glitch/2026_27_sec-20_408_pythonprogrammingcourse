#4B_Multiple_Except_Blocks
#Implement a Python program that reads a list index and handles ValueError and IndexError separately
# Example solution: try-except-else-finally (square of an integer)
try:
    text = input("Enter a number: ")
    number = int(text)
except ValueError:
    print("That is not a valid integer.")
else:
    print("Square:", number * number)
finally:
    print("Program finished.")