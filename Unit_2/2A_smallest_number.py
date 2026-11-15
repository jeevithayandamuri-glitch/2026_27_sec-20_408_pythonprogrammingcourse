#2A_smallest_number
x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
z=float(input("Enter third number:"))
if x<y:
    if x<z:
        print("the smallest number is :",x)
    else:
        print("the smallest is :",z)
else:
    if y<x:
        if y<z:
            print("the smallest number is:",y)
        else:
            print("the smallest number is:",z)