import pytest
from source.classes import account
from source.functions import transfer, id_verification
from source.exceptions import InsufficientFundsException, NoIdException

@pytest.fixture
def src():
    account_obj = account(1, "T1")
    account_obj.balance = 100.0
    return account_obj

@pytest.fixture
def dest():
    account_obj = account(2, "T2")
    account_obj.balance = 20.0
    return account_obj

@pytest.fixture
def accounts_db(src, dest):
    return [src, dest]

@pytest.mark.parametrize("amount", ["random string"])
def test_string_amount_transfer(monkeypatch, src, dest, amount, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: amount)
    
    transfer(src, dest)
    
    captured = capsys.readouterr().out
    expected_output = ("Error:"    )
    assert expected_output in captured

@pytest.mark.parametrize("amount", ["200"])
def test_Inssuf_funds_transfer(monkeypatch, src, dest, amount, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: amount)
    
    transfer(src, dest)
    
    captured = capsys.readouterr().out
    expected_output = ("Error:"    )
    assert expected_output in captured


@pytest.mark.parametrize("amount", ["50"])
def test_transfer(monkeypatch, src, dest, amount, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: amount)
    
    transfer(src, dest)
    
    captured = capsys.readouterr().out
    expected_output = ("----- Account Data -----")
    assert expected_output in captured

@pytest.mark.parametrize("ids", ["teste", -3])
def test_string_verification(monkeypatch, accounts_db, ids):
    monkeypatch.setattr("builtins.input", lambda prompt: ids)
    with pytest.raises(ValueError):
        id_verification(accounts_db)

@pytest.mark.parametrize("ids", [3])
def test_no_id_verification(monkeypatch, accounts_db, ids):
    monkeypatch.setattr("builtins.input", lambda prompt: ids)
    with pytest.raises(NoIdException):
        id_verification(accounts_db)

@pytest.mark.parametrize("ids", [1, 2])
def test_no_id_verification(monkeypatch, accounts_db, ids):
    monkeypatch.setattr("builtins.input", lambda prompt: ids)
    assert id_verification(accounts_db) == ids-1