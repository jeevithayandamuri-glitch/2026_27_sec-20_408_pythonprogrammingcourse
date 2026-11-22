#2D_Count_Vowels_Consonants_Digits_Spaces
#Implement a Python program to count vowels, consonants, digits and spaces in a string
s=input("Enter any string:")
vowels=0
consonants=0
digits=0
spaces=0
for ch in s:
 if ch.lower() in "aeiou":
    vowels=vowels+1
 elif ch.isalpha():
    consonants=consonants+1
 elif ch.isdigit():
   digits=digits+1
 elif ch==" ":
     spaces=spaces+1

print("vowel:",vowels)
print("consonents:",consonants)
print("digits:",digits)
print("space:",spaces)