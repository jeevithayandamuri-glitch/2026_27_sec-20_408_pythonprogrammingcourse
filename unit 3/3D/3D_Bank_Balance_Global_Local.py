#3D_Bank_Balance_Global_Local
#(Optional) Implement a Python program for a simple bank balance: a global balance, a function to deposit (uses global), and a function that uses a local balance to show it does not update the account
balance = 1000
def deposit(amount):
    global balance
    balance = balance + amount
    print("After deposit, balance =", balance)

def show_local_balance():
    balance = 0  # local only
    print("Inside local function, balance =", balance)

print("Start:", balance)
deposit(500)
print("Account balance:", balance)
show_local_balance()
print("Account balance still:", balance)