#3A_Remove_Duplicates_from_List
#Implement a Python program to remove duplicate elements from a list
list_data=[1,2,3,4,5,5,6,6,77,75,2,3,3]
unique=[]
for i in list_data:
    if i not in unique:
        unique.append(i)
print("without duplicate:",unique)