#3D_4_Simple_Interest_Default_Args
#Implement a Python program that defines a function to calculate simple interest with parameters principal, time, and rate (default rate = 5); call it using the default rate and also with an explicit rate
def sim_interest(p,t,r=5):
    simple_interest=(p*r*t)/100
    return simple_interest
p=int(input("Enter principal amount:"))
t=int(input("Enter time per year:"))
simple_interest=sim_interest(p,t,r=5)
print("Simple Interst:",simple_interest)