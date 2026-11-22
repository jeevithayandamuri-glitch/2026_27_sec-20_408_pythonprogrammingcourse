#2C_5x5_grid
#Write a python program to print a 5x5 grid of stars (*); generalize the program so the grid size is based on user input
row=0
for row in range(5):
    for column in range(5):
        row=row+1
        print("*",end=" ")
    print()