#swap of two numbers
number1=10
number2=20
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
#after_swap
print(number1)
print(number2)

#swap of two numbers
number1=10
number2=20
number1,number2=number2,number1
#after_swap
print(number1)
print(number2)