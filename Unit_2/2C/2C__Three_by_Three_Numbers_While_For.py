#2C__Three_by_Three_Numbers_While_For
#Write a python program to print numbers in a 3x3 grid (as shown in the hint) using while-for nested loop
num = 1
row = 1
while row <= 3:
  for i in range(1, 4):
    print(num, end=" ")
    num = num + 1
  print()
  row = row + 1