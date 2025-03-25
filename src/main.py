from source.functions import menu

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