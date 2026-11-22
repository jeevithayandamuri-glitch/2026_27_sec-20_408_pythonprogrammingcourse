#2C__Centered_Number_Pyramid.py
#Implement a Python program to print a centered pyramid pattern of numbers
rows=int(input("enter no.of number:"))
for i in range(1,rows+1):
    for j in range(1,rows-i+1):
        print(" ",end=" ")
    for k in range(1,2*i):
        print(k,end=" ")
    print()
