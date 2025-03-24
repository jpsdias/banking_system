from classes import account

def create_account(accounts_db):
    username = input("Enter a username for your account:\n")
    id = len(accounts_db) + 1
    new_account = account(id, username)
    accounts_db.append(new_account)
    account.extract(accounts_db[id-1])

def transfer(accounts_db):
    id = input('Insert the ID from the beneficiary: ')
    try:
        id = int(id)
        for i in range (len(accounts_db)):
            if accounts_db[i].id == id:
                dest = i
                continue
    except ValueError:
        print('No id found! Choose another beneficiary.')
    
    trans_amount = input("Amount to transfer:")
    try:
        account.withdraw(accounts_db[0], trans_amount)
        account.deposit(accounts_db[dest], trans_amount)
    except ValueError:
        print('Such amount is not available!')

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
            continue
            # raise ValueError("Invalid input. Please enter a number.")

        match ivalue:
            case 1:
                create_account(accounts_db)
            case 2:
                amount = input('Introduce an amount: ')
                try:
                    account.deposit(accounts_db[0], amount)
                except ValueError as e:
                    # Captura o ValueError lançado e exibe a mensagem
                    print(f"Erro: {e}")
            case 3:
                amount = input('Introduce an amount: ')
                try:
                    account.withdraw(accounts_db[0], amount)
                except ValueError as e:
                    # Captura o ValueError lançado e exibe a mensagem
                    print(f"Erro: {e}")
            case 4:
                transfer(accounts_db)
            case 5:
                account.extract(accounts_db[0])
            case 6:
                return 0
            case _:
                raise ValueError("Deposit amount must be numeric.")
                # print("Invalid input. Please enter a number.")

def main():
    accounts_db = []
    print("---- Welcome to John's Bank ----")
    while (True):
        try:
            exit_code = menu(accounts_db)

            if exit_code == 0:
                break
        
        except ValueError as e:
            # Captura o ValueError lançado e exibe a mensagem
            print(f"Erro: {e}")
        
        

    

    # accounts_db = create_account(accounts_db)

    # accounts_db = deposit(accounts_db)

    # withdraw(accounts_db)


if __name__ == "__main__":
    main()