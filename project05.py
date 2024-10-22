"""
Author: Kouame Alexandre Paul
Last updated: 17/10/2024 11:55 PM UTC

Program: Add, View, Remove item in shopping cart

Creativity: 
    - Allow user to enter the quantity of items, 
    - Allow user to remove items based on their quantity
    - Format the display of items, prices and quantities
"""
print('Welcome to the Shopping Cart Program!\n')

cart = []
prices = []
quantities = []

action = -1

while action != 5:
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')

    action = int(input('Please enter an action:'  ))
    
    if action == 1:

        #Add item to carts
        item = ''
        while item.lower() != 'quit' :
            #request item
            item = input('What item would you like to add (type: "quit" to stop add item)? ')
        
            if item.lower() != 'quit':
                #request item's price
                price = float(input(f"What is the price of '{item}'? "))

                #request item's quantity
                quantity = int(input(f"How many of '{item}' do you want? "))

                #Add item, price and quantity to required list
                cart.append(item)
                prices.append(price)
                quantities.append(quantity)
            
            print(f"'{item}' has been added to the cart.")

        print()

    elif action == 2:

        #Display item in cart
        print('The contents of the shopping cart are:')
        print(f'{"#":<2} {"Item":<10} {"Quantity":<15} {"Price"}')
        for i in range(len(cart)):
            print(f'{i+1:<2} {cart[i]:<13} {quantities[i]:<10} ${prices[i]:.2f}')

        print()

    elif action == 3:

        #Display item in cart
        print('The contents of the shopping cart are:')
        print(f'{"#":<2} {"Item":<10} {"Quantity":<15} {"Price"}')
        for i in range(len(cart)):
            print(f'{i+1:<2} {cart[i]:<13} {quantities[i]:<10} ${prices[i]:.2f}')

        #Remove item
        #request item's index from cart list
        index = int(input('Which item would you like to remove? '))
        count_cart = len(cart)

        if index <= count_cart:

            #request quantity of item to remove
            quantity = int(input(f"How many of '{cart[index - 1]}' do you want to remove? "))

            #request only a max of item's quantity
            while quantity > quantities[index - 1] or quantity < 0:
                print(f'you can delete a maximum of {quantities[index - 1]} {cart[index - 1]}.')
                quantity = int(input(f"How many of '{cart[index - 1]}' do you want to remove? "))

            #If the user requests to remove a specific item and the requested quantity equals the item's quantity, 
            # remove the item entirely from the cart.Otherwise decrease item'quantity
            if quantity == quantities[index - 1]:
                cart.pop(index - 1)
                prices.pop(index - 1)
                quantities.pop(index - 1)
            else:
                old_quantity = quantities[index - 1]
                new_quantity = old_quantity - quantity
                quantities[index - 1] = new_quantity

            print('Item removed.')

        else:
            print('Sorry, that is not a valid item number.')
        
        print()

    elif action == 4:

        #Compute total
        sum = 0
        for i in range(len(prices)):
            sum += (quantities[i] * prices[i])
        print(f'The total price of the items in the shopping cart is ${sum:.2f}')

        print()
    
    else:
        print('Thank you. Goodbye.')