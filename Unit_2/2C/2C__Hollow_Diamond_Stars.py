#2C__Hollow_Diamond_Stars.py
#Implement a Python program to print a hollow diamond pattern of stars
row=int(input("Enter no.of rows:"))
for i in range(row):
    for j in range(row-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        if k==0 or k==2*i:
            print("*",end=" ")
        else:
          print(" ",end=" ")
    print()


for i in range(row-2,-1,-1):
    for j in range(row-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        if k==0 or k==2*i:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
