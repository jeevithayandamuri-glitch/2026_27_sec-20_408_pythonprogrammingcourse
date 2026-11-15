#2B_palindrome
#Write a python program to check whether a number is a palindrome using while loop
n=int(input("Enter a number:"))
ori_num=n
rev_num=0
while ori_num > 0:
    digit = ori_num%10
    rev_num = rev_num*10+digit
    ori_num = ori_num//10
if rev_num == n:
     print("it is a palindrome")
else:
     print("it is not a palindrome")