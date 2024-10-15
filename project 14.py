'''
author name:Nicole Nelson
to check the discount based on total purchase amount
'''
purchase_amount=int(input("enter the purchase amount:"))
if purchase_amount>500:
    discount=purchase_amount*20/100
    final_amount=purchase_amount-discount
    print("finalamount=",final_amount)
elif (purchase_amount>=200 and purchase_amount<500):
    discount=purchase_amount*10/100
    final_amount=purchase_amount-discount
    print("final amount:",final_amount)
else:
    print("final amount:",purchase_amount)