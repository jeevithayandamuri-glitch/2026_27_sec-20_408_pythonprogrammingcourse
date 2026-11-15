#compound interst
A=int(input("Enter principal amount="))
R=int(input("Enter rate="))
T=int(input("Enter time="))
total_amount=A*(1+R/100)**T
compound_interst=total_amount - A
print("compound_interst:",compound_interst)