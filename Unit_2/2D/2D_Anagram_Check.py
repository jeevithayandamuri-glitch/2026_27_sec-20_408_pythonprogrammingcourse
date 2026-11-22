#2D_Anagram_Check
#Implement a Python program to check whether two strings are anagrams
s1=input("Enter a first string:")
s2=input("Enter a second string:")
if sorted(s1)==sorted(s2):
    print("it is a Anagram")
else:
    print("it is not a Anagram")