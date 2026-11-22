#2C_Floyds_Triangle_Number_Pattern.py
#Implement a Python program to print a number pattern (e.g., Floyd's triangle)
row=int(input("Enter a number:"))
num=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()