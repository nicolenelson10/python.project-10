'''
author name:Nicole Nelson
a program to generate odd numbers up to limit
'''
limit=int(input("enter the limit:"))
odd_number=1
count=0
while count<limit:
            print(odd_number,"\t",end="")
            count+=1
            odd_number+=2