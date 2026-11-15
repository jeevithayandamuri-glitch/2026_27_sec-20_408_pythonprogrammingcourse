#2B_sum_and_average_of_N_numbers
n=int(input("Enter number N:"))
sum=0
for i in range(1,n+1):
    sum+=i
average=sum/n
print(f"sum of 1 to {n} numbers is {sum}")
print(f"average of 1 to {n} numbers is {average}")