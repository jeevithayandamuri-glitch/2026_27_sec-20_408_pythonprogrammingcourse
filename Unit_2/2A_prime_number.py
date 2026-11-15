#2A_prime_number
n=int(input("enter a number:"))
if n<=1:
    print(f"{n}not a prime number")
else:
    for i in range(2,n):
        if n % i==0:
            print(n,"not a prime number")
            break
    else:
            print(f"{n} is a prime number")