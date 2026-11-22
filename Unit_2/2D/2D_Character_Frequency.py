#2D_Character_Frequency
#Implement a Python program to count the frequency of each character in a string
s=input("enter string:")
frequency={}
for i in s:
    if i in frequency:
        frequency[i]=frequency[i]+1
    else:
        frequency[i]=1

for i,count in frequency.items():
    print(i,":",count)