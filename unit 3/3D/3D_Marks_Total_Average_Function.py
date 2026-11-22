#3D_Marks_Total_Average_Function
#Implement a Python program that defines a function taking marks of three subjects as parameters and returns the total and average
def total_and_average(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return total, average

m1=int(input("Enter marks1:"))
m2=int(input("Enter marks2:"))
m3=int(input("Enter marks3:"))
total, average = total_and_average(m1, m2, m3)
print("Total:", total)
print("Average:", average)