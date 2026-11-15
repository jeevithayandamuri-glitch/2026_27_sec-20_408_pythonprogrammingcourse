#2B_sum_digits
n=int(input("Enter a number:"))
sum=0

while n > 0:
    digits = n % 10
    sum = sum + digits
    n = n // 10
print("sum of digits:",sum)