#3B_Tuple_Operations
#Implement a Python program to demonstrate tuple operations (concatenation, slicing, unpacking)
tuple_data=(1,2,3,4)
tuple_extract=(5,6)
joined=tuple_data+tuple_extract
print("concadination:",joined)
print("slicing:",tuple_data[:2])
a,b,c,d=tuple_data
print("unpacked:", a,b,c,d)