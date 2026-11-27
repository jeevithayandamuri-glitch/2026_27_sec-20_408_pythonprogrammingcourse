#4B_Try_Except_Block
#Implement a Python program that catches ZeroDivisionError when dividing 10 by 0
try:
   a=int(input("Enter 1st number:"))
   b=int(input("Enter 2nd number:"))
   result=a/b
   print("Result:",result)
except ZeroDivisionError:
    print("Dnominator did not < 0 ")