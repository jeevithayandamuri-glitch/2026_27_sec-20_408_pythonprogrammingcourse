#3C_Set_Membership_and_Methods
#Implement a Python program to demonstrate set membership testing and methods (add, remove, discard)
set_data={1,2,3,4,5}
print("set:",set_data)
print("2 in set?",2 in set_data)
print("1 not in set?", 1 not in set_data)
set_data.add(6)
print("add:",set_data)
set_data.remove(1)
print("remove:",set_data)
set_data.discard(2)
print("discard:",set_data)
print(type(set_data))