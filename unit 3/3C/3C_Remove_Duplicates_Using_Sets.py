#3C_Remove_Duplicates_Using_Sets
#Implement a Python program to remove duplicates from a list using sets
list_data=[1,2,2,3,4,5,6,6,4,2]
set_a=set(list_data)
unique_list=list(set_a)
print("Orginal:",list_data)
print("non-duplicate set:",set_a)
print("non-duplicte set:",unique_list)