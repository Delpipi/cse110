"""
    Author: Kouame Alexandre Paul
    Last updated: 09/24/2024 5:36 PM UTC

    Program: Calcule the price of a meal

    For creativity we will ask user's currency(e.g., USD, EUR, XOF)
"""
currency = input('What is your currency (e.g., USD, EUR, XOF)? ')

price_per_child = float(input("What is the price of a child's meal? "))
price_per_adult = float(input("What is the price of an adult's meal? "))

childrens = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))

#compute subtotal
subtotal = (childrens * price_per_child) + (adults * price_per_adult)
print(f'\nSubtotal: {subtotal:.2f} {currency.upper()}')

#compute Sales Tax 
rate = float(input('What is the sales tax rate? '))
sale_tax = subtotal * (rate / 100)
print(f'Sales Tax: {sale_tax:.2f} {currency.upper()}')

#compute Total
total = subtotal + sale_tax
print(f'Total: {total:.2f} {currency.upper()}')

print()
#compute Change
pay_amout = int(input('What is the payment amount? '))
change = pay_amout - total
print(f'Change: {change:.2f} {currency.upper()}')


