#4A_Create_Access_Update_Dictionary
#Implement a Python program that creates a student dictionary (name, age, course), updates age, and adds city
# Example solution: create, access and update a dictionary
student = {
    "name": "Anu",
    "age": 20,
    "course": "Python",
}
print("Student:", student)
print("Name:", student["name"])

student["age"] = 21
student["city"] = "Guntur"
print("Updated:", student)