import pytest
from source.classes import account

class Testaccount:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.id = 1
        self.username = "João"
        self.balance = 0.0
    
    @pytest.mark.parametrize("amount", [100.0, 100])
    def test_deposit(self, amount):
        prev_balance = self.balance
        account.deposit(self, amount)
        assert self.balance == prev_balance + amount

    @pytest.mark.parametrize("amount", ["random string"])
    def test_fail_deposit(self,amount, capsys):
        account.deposit(self, amount)
        captured = capsys.readouterr().out
        expected_output = ("Invalid input! Please enter a numeric value.")
        assert expected_output in captured
    
    @pytest.mark.parametrize("balance, amount", [(100.0, 20.0), (20.0, 100.0)])
    def test_withdraw(self, balance, amount, capsys):
        self.balance = balance
        account.withdraw(self, amount)
        if (balance > amount):
            assert self.balance == balance - amount
        else:
            captured = capsys.readouterr().out
            expected_output = ('This account does not have sufficient funds!')
            assert expected_output in captured

    @pytest.mark.parametrize("amount", ["random string"])
    def test_error_withdraw(self, amount):
        with pytest.raises(ValueError): # Indicates an exception
            result = account.withdraw(self, amount)

    @pytest.mark.parametrize("amount", ["random string"])
    @pytest.mark.xfail(reason="A string cannot be inserted on the amount field")
    def test_error2_withdraw(self, amount):
        account.withdraw(self, amount)


    def test_extract(self, capsys):
        account.extract(self)
        captured = capsys.readouterr().out
        expected_output = (
            "----- Account Data -----\n"
            f"ID Number: {self.id}\n"
            f"Username: {self.username}\n"
            f"Balance: {self.balance}€\n"
        )
        assert expected_output in captured

# @pytest.fixture
# def test_account():
#     # Create an account with id=1 and username="Teste"
#     return account(1, "Teste")

# # Test to check that the username is correctly set
# def test_username(test_account):
#     assert test_account.username == "Teste"
