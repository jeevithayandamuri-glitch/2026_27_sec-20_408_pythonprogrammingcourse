#2C_3x3_grid 
#Write a python program to print numbers in a 3x3 grid (as shown in the hint) using for-for nested loop
num=0
for row in range(3):
    for column in range(3):
       num = num+1
       print(num,end=" ")
    print()