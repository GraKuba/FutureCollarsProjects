import sys

# CREATE A FILE PATH AND OPEN DOCUMENT 
filePath = '//Users/kubagrabarczyk/Desktop/python recap/Accountant 2/in.txt'
f = open(filePath, 'r')

# DOWNLOAD DATA FROM THE DOCUMENT AND SAVE IN THE VARIABLE, accountHistory
accountHistory = []
while True:
    action = f.readline().strip()
    if action == 'saldo':
        balance = ('saldo', f.readline().strip(), f.readline().strip())
        accountHistory.append(balance)
    elif action == 'sprzedaz':
        sale = ('sprzedaz', f.readline().strip(), f.readline().strip(), f.readline().strip())
        accountHistory.append(sale)
    elif action == 'zakup':
        purchase = ('zakup', f.readline().strip(), f.readline().strip(), f.readline().strip())
        accountHistory.append(purchase)
    elif action == 'stop' or False:
        break  
f.close() 

print(accountHistory)

    