'''
author name:Nicole Nelson
date:29-10-2024
'''
limit=int(input("enter limit"))
for limit in range(2,limit+1):
    isprime=True
    for i in range(2,(limit//2)+1):
        if limit%i==0:
            isprime=False
    if isprime:
        print(limit,end=" ")
