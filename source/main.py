from classes import account
from exceptions import InsufficientFundsException, NoIdException

def create_account(accounts_db):
    username = input("Enter a username for your account:\n")
    id = len(accounts_db) + 1
    new_account = account(id, username)
    accounts_db.append(new_account)
    account.extract(accounts_db[id-1])

def id_verification(accounts_db):
    dest_id = input('Insert beneficiary ID: ')

    try:
        dest_id = int(dest_id)
    except ValueError:
        raise ValueError("ID must be an Integer!")
    
    if dest_id <= 0:
        raise ValueError("ID must be a positive number.")
    
    for i in range (len(accounts_db)):
        if accounts_db[i].id == dest_id:
                return i
    
    raise NoIdException("No User found in the DB.")
        
def transfer(src, dest):
    amount = input('Insert the amount to transfer: ')
    try:
        account.withdraw(src, amount)
    except ValueError as e:
        # Captura o ValueError lançado e exibe a mensagem
        print(f"Error: {e}")
    except InsufficientFundsException as e:
        print(f"Error: {e}")

    else:
        try:
            account.deposit(dest, amount)
        except ValueError as e:
            # Captura o ValueError lançado e exibe a mensagem
            print(f"Error: {e}")
        
        account.extract(src)
        account.extract(dest)

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
            raise ValueError("Invalid input. Please enter a number.")

        match ivalue:
            case 1:
                create_account(accounts_db)
            case 2:
                amount = input('Introduce an amount: ')
                try:
                    account.deposit(accounts_db[0], amount)
                except ValueError as e:
                    # Captura o ValueError lançado e exibe a mensagem
                    print(f"Error: {e}")
            case 3:
                amount = input('Introduce an amount: ')
                try:
                    account.withdraw(accounts_db[0], amount)
                except (ValueError, InsufficientFundsException) as e:
                    # Captura o ValueError lançado e exibe a mensagem
                    print(f"Error: {e}")
            case 4:
                try:
                    dest = id_verification(accounts_db)
                except NoIdException as e:
                    # Captura o ValueError lançado e exibe a mensagem
                    print(f"Error: {e}")
                else:
                    transfer(accounts_db[0], accounts_db[dest])
            case 5:
                account.extract(accounts_db[0])
            case 6:
                return 0
            case _:
                continue

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
            print(f"Error: {e}")

if __name__ == "__main__":
    main()