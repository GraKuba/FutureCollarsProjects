import sys
# global variables
accountHistory = []

# Saving inputs from in.txt to accountHistory 
while True:
    action = input()
    if action == 'saldo':
        balance = ('saldo', input(), input())
        accountHistory.append(balance)
    elif action == 'sprzedaz':
        sale = ('sprzedaz', input(), input(), input())
        accountHistory.append(sale)
    elif action == 'zakup':
        purchase = ('zakup', input(), input(), input())
        accountHistory.append(purchase)
    elif action == 'stop' or False:
        break   

# Calculating currentBalance, as well as warehouse changes
currentBalance = 0
for idx in accountHistory:
    if idx[0] == 'saldo':
        currentBalance += int(idx[1])
    elif idx[0] == 'sprzedaz':
        currentBalance += int(idx[2]) * int(idx[3])
    elif idx[0] == 'zakup':
        currentBalance -= int(idx[2]) * int(idx[3])

warehouse = []
for i in accountHistory:
    if i[0] == 'zakup':
        warehouse.append({i[1]: i[3]})
    elif i[0] == 'sprzedaz':
        for idx in warehouse:
            for item in idx:
                if i[1] == item:
                    idx[item] = int(idx[item]) - int(i[3])

# Adding new entries to account history - saldo, sprzedaz, zakup. Also actions such as magazyn, konto, przeglad. 
if len(sys.argv) > 1: 
    if sys.argv[1] == 'saldo':
        balance = ('saldo', sys.argv[2], sys.argv[3])
        accountHistory.append(balance)
    elif sys.argv[1] == 'sprzedaz':
        for idx in warehouse:
            for item in idx:
                if int(sys.argv[4]) > int(idx[item]):
                    print('Niewystarczajaca ilosc w magazynie!')
                else:
                    sale = ('sprzedaz', sys.argv[2], sys.argv[3], sys.argv[4])
                    accountHistory.append(sale)
    elif sys.argv[1] == 'zakup':
        if int(sys.argv[3]) * int(sys.argv[4]) > currentBalance:
            print('Niewystarczajace srodki!')
        else:
            purchase = ('zakup', sys.argv[2], sys.argv[3], sys.argv[4])  
            accountHistory.append(purchase) 
    elif sys.argv[1] == 'magazyn':
        print(warehouse)
    elif sys.argv[1] == 'konto':
        print(currentBalance)
    elif sys.argv[1] == 'przeglad':
        for entry in range(int(sys.argv[2]), int(sys.argv[3]) + 1):
            print(accountHistory[entry])