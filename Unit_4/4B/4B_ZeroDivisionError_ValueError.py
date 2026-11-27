#4B_ZeroDivisionError_ValueError
#Implement a Python program that reads numerator and denominator and handles ZeroDivisionError and ValueError
try:
    num = float(input("Enter numerator: "))
    den = float(input("Enter denominator: "))
    print("Quotient:", num / den)
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except ValueError:
    print("Please enter valid numbers.")