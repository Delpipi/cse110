clients = []
#clients = ["Emily", "John", "Mary"]'

new_client = ''
while new_client != 'quiert':
    new_client = input('what is the name of a client? ')
    clients.append(new_client)

clients.append("Emily")
clients.append("John")
clients.append("Mary")

for client in clients:
    print(client)


