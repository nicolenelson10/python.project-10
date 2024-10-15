'''
author name:Nicole Nelson
program to obtain sum
'''
num=int(input("enter the number"))
sum=0
while(num>0):
    r=num%10
    num=num//10
    sum=sum+r
print("the sum of numbers:",sum)

