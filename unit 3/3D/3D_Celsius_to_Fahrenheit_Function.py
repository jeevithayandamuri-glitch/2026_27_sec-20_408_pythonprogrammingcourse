#3D_Celsius_to_Fahrenheit_Function
#Implement a Python program that defines a function to convert temperature from Celsius to Fahrenheit (Celsius as parameter) and returns the result
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

celsius = int(input("Enter celsius value:"))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Fahrenheit:", fahrenheit)