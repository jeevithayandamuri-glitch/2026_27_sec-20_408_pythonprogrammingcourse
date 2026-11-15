#2A_largest_of_three_num
x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
z=float(input("Enter third number:"))
if x>y and x>z:
    print("the largest number is:",x)
if z>y and z>x:
    print("the largest number is:",z)
else:
    print("the largest number is:",y)



"""if x>y:
    if x>z:
        print("the largest number is:",x)
    else:
        print("the largest number is:",z)
else:
    if y>x:
        if y>z:
            print("the largest number is :",y)
        else:
            print("the largest number is:",z)"""