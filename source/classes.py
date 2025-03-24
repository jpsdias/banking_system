
class account():
    def __init__(self, id:int, user:str):
        self.id = id
        self.username = user
        self.balance = 0.0

    def deposit(self, amount:float):
        try:
            # Convert the input to a float
            famount = float(amount)
            # Round the number to 2 decimal places
            famount = round(famount, 2)

            self.balance = self.balance + famount
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            raise ValueError
        

    def withdraw(self, amount:float):
        try:
            # Convert the input to a float
            famount = float(amount)
            # Round the number to 2 decimal places
            famount = round(famount, 2)

            if (self.balance < famount):
                print ('This account does not have sufficient funds!')
            else:
                self.balance = self.balance - famount
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            raise ValueError
    
    def extract(self):
        print(f'----- Account Data -----\n'
            f'ID Number: {self.id}\n'
            f'Username: {self.username}\n'
            f'Balance: {self.balance}€\n')
