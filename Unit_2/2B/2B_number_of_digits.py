#2B_number_of_digits
n=int(input("enter number:"))
count=0
while n>0:
    count+=1
    n=n//10
    print("number of digits:",count)