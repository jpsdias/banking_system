import random

class account():
    def __init__(self, id:int, user:str):
        self.id = id
        self.username = user
        self.balance = 0.0

    def deposit(self, amount:float):
        self.balance = self.balance + amount

    def withdraw(self, amount:float):
        if (self.balance < amount):
            print (f'This account does not have enough money, only {self.balance}€')
        else:
            self.balance = self.balance - amount
    
    def extract(self):
        print(f'----- Account Data -----\n'
            f'ID Number: {self.id}\n'
            f'Username: {self.username}\n'
            f'Balance: {self.balance}€\n')

def create_account(accounts_db):
    username = input("Enter a username for your account:\n")
    id = len(accounts_db) + 1
    new_account = account(id, username)
    accounts_db.append(new_account)
    account.extract(accounts_db[id-1])

def deposit(accounts_db):
    amount = input('Introduce an amount: ')

    try:
        # Convert the input to a float
        famount = float(amount)
        # Round the number to 2 decimal places
        famount = round(famount, 2)
        account.deposit(accounts_db[0], famount)
        account.extract(accounts_db[0])
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

    return accounts_db

def withdraw(accounts_db):
    amount = input('Introduce an amount: ')

    try:
        # Convert the input to a float
        famount = float(amount)
        # Round the number to 2 decimal places
        famount = round(famount, 2)

        account.withdraw(accounts_db[0], famount)
        account.extract(accounts_db[0])
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def menu(accounts_db):
    while True:
        print ("""Select an operation:
1 - Create an account
2 - Deposit
3 - Withdraw
4 - Transfer
5 - Consultation
6 - Exit\n""")
        
        value = input("Choose an operation: ")
        try:
            ivalue = int(value)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match ivalue:
            case 1:
                create_account(accounts_db)
            case 2:
                deposit(accounts_db)
            case 3:
                return 'Option three'
            case 4:
                return 'Option four'
            case 5:
                return 'Option five'
            case 6:
                return 0
            case _:
                print("Invalid input. Please enter a number.")

def main():
    accounts_db = []
    print("---- Welcome to John's Bank ----")
    while (True):
        exit_code = menu(accounts_db)
        if exit_code == 0:
            break

    

    # accounts_db = create_account(accounts_db)

    # accounts_db = deposit(accounts_db)

    # withdraw(accounts_db)


if __name__ == "__main__":
    main()