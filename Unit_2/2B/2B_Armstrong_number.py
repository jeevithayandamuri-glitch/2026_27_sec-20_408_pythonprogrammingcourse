#2B_Armstrong_number
#Write a python program to check whether a number is an Armstrong number using while loop(assume the number has 3 digits)
N=int(input("Enter a number:"))
tem=N
sum=0
while tem>0:
    digit=tem%10
    sum=sum+digit**3
    tem=tem//10
if sum==N:
      print(f"{N} is a armstrong")
else:
       print(f"{N}is not a armstrong")
