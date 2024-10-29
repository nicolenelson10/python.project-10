'''
author name:Nicole Nelson
date:29-10-2024
'''
number=int(input("enter a number"))
isprime=True
for i in range(2,(number//2)+1):
    if number%i==0:
        isprime=False
        break
if isprime:
    print(f"the given {number}is prime")
else:
    print(f"the given {number}is not prime")
