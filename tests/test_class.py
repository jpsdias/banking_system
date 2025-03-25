import pytest
from source.classes import account
from source.exceptions import InsufficientFundsException

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

    #Pytest to the error is raised
    @pytest.mark.parametrize("amount", ["random string", -100])
    def test_raised_error_deposit(self, amount):
        with pytest.raises(ValueError): # Indicates an exception
            result = account.deposit(self, amount)

    #Pytest to fail
    @pytest.mark.parametrize("amount", ["random string", -100])
    @pytest.mark.xfail(reason="A string cannot be inserted on the amount field or negative number")
    def test_fail_deposit(self, amount):
        account.deposit(self, amount)
    
    @pytest.mark.parametrize("balance, amount", [(100.0, 20.0), (20.0, 100.0)])
    def test_withdraw(self, balance, amount):
        self.balance = balance
        
        if (self.balance < amount):
            with pytest.raises(InsufficientFundsException): # Indicates an exception
                account.withdraw(self, amount)
        else:
            account.withdraw(self, amount)
            assert self.balance == balance - amount

    # @pytest.mark.parametrize("balance, amount", [(20.0, 100.0)])
    # def test_insufficient_funds_withdraw(self, balance, amount):
    #     self.balance = balance
    #     with pytest.raises(InsufficientFundsException): # Indicates an exception
    #         account.withdraw(self, amount)

    #Pytest to the error is raised
    @pytest.mark.parametrize("amount", ["random string", -100])
    def test_raised_error_withdraw(self, amount):
        with pytest.raises(ValueError): # Indicates an exception
            result = account.withdraw(self, amount)
    
    #Pytest to fail
    @pytest.mark.parametrize("amount", ["random string", -100])
    @pytest.mark.xfail(reason="A string cannot be inserted on the amount field or negative number")
    def test_fail_withdraw(self, amount):
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