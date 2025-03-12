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
    return accounts_db

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
    

def main():
    accounts_db = []
    print ('Banking App')

    accounts_db = create_account(accounts_db)

    deposit(accounts_db)


if __name__ == "__main__":
    main()