"""
Author: Kouame Alexandre Paul
Last updated: 09/29/2024 7:29 PM GMT

Program: Qualifying for a loan
"""
print("What is your rating from 1-10 on the following : \n")

rate_load = int(input("How large is the loan (1-10)? "))
rate_credit = int(input("How good is your credit history (1-10)? "))
rate_income = int(input("How high is your income (1-10)? "))
rate_payment = int(input("How large is your down payment (1-10)? "))

can_load = False

if rate_load >= 5 :
    if rate_credit >= 7 and rate_income >= 7 :
        can_load = True
    elif rate_credit >= 7 or rate_income >= 7 :
        if rate_payment >= 5 :
            can_load = True
        else:
            can_load = False
    else:
        can_load = False
elif rate_load > 4 :
    can_load = False
else:
    if rate_load > 4 :
        can_load = False
    else:
      if rate_income >= 7 or rate_payment >= 7 :
        can_load = True
      elif rate_income >= 4 and rate_payment >= 4 :
        can_load = True
      else:
        can_load = False

print()
if can_load:
    print("Loan the money")
else:
    print("Sorry, money cannot be loaded")