#2D_String_Palindrome
#Implement a Python program to check whether a string is a palindrome
s=input("enter any string:")
if s==s[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")