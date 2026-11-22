#3D_Student_Details_Kwargs
#Implement a Python program that defines a function using **kwargs to display a student's name and subject marks
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_details(name="Anu", maths=85, science=90)