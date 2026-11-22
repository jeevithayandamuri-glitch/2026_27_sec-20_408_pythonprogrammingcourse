#3D_4a_Divide_Keyword_Positional_Args
#Implement a Python program that defines a function divide(a, b) returning a / b; call it with keyword arguments divide(b=10, a=20) and with positional arguments divide(10, 20), and print both results

def divide(a, b):
    return a / b

result = divide(b=10, a=20)
print(result)

result = divide(10, 20) 
print(result)