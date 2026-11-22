#2C__Right_Angled_Triangle_Pattern
row=int(input("Enter no.of rows:"))
symbole=input("Enter sylmbole:")
for i in range(1,row+1):
    for j in range(1,i+1):
        print(symbole,end=" ")
    print()
