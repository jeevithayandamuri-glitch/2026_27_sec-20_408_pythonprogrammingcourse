#2C__Diamond_Pattern_of_Stars.py
#Implement a Python program to print a diamond pattern of stars
row=int(input("Enter no.of rows:"))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

for i in range(row-1,0,-1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()