import pytest
from source.classes import account
from source.functions import transfer

def setup_method(self, method):
    print(f"Setting up {method}")
    self.id = 1
    self.username = "João"
    self.balance = 0.0

@pytest.mark.parametrize("amount", ["random string"])
def test_string_amount_transfer(self, amount, capsys):
    transfer(self)
    captured = capsys.readouterr().out
    expected_output = ("Error:"    )
    assert expected_output in captured
