#2C__Number_Right_Angled_Triangle.py
#Implement a Python program to print a number right-angled triangle pattern
row=int(input("Enter no.of rows:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()