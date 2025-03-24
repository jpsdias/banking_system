
class account():
    def __init__(self, id:int, user:str):
        self.id = id
        self.username = user
        self.balance = 0.0
    
    def deposit(self, amount: float):
        try:
            # Convert the input to a float
            famount = float(amount)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            raise ValueError("Deposit amount must be numeric.")

        # Check if the deposit amount is positive
        if famount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        
        # Round the number to 2 decimal places and update the balance
        famount = round(famount, 2)
        self.balance += famount


    def withdraw(self, amount:float):
        try:
            # Convert the input to a float
            famount = float(amount)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            raise ValueError("Deposit amount must be numeric.")
        
        # Check if the deposit amount is positive
        if famount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        
        if (self.balance < famount):
            print ('This account does not have sufficient funds!')
        else:
            # Round the number to 2 decimal places and update the balance
            famount = round(famount, 2)
            self.balance = self.balance - famount
    
    def extract(self):
        print(f'----- Account Data -----\n'
            f'ID Number: {self.id}\n'
            f'Username: {self.username}\n'
            f'Balance: {self.balance}€\n')
