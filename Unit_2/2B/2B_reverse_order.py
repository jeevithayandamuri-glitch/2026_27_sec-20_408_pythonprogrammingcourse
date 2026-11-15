#2B_reverse_order
# Write a python program to reverse a given number using while loop
n=int(input("Enter a number:"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
    print("The reverse order is ",reverse)
