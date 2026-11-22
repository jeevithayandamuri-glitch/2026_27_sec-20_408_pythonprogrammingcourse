#2C_Centered_Pyramid_Stars.py
#Implement a Python program to print a centered pyramid pattern of stars
row=int(input("Enter no.of rows:"))
for i in range(row):
    for j in range(row-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()