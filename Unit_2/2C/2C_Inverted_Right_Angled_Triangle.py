#2C_Inverted_Right_Angled_Triangle.py
#Implement a Python program to print an inverted right-angled triangle pattern
rows=int(input("Enter no.of rows:"))
for i in range(rows,0,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()