import pytest
from bank_app import Account, User

def test_add_funds_via_transfer():
    acc = Account(1, 100)
    assert acc.add_funds_via_transfer(50) == 150
    assert acc.add_funds_via_transfer(1) == 151
    with pytest.raises(ValueError):
        acc.add_funds_via_transfer(0)
    with pytest.raises(ValueError):
        acc.add_funds_via_transfer(-10)

def test_schedule_payment():
    acc = Account(1, 100)
    assert acc.schedule_payment(50) == 50
    assert acc.schedule_payment(10) == 40
    with pytest.raises(ValueError):
        acc.schedule_payment(0)
    with pytest.raises(ValueError):
        acc.schedule_payment(100)

def test_transfer():
    acc1 = Account(1, 200)
    acc2 = Account(2, 50)
    assert acc1.transfer(acc2, 50) == 150
    assert acc2.get_balance() == 100
    with pytest.raises(ValueError):
        acc1.transfer(acc2, 300)
    with pytest.raises(ValueError):
        acc1.transfer(acc2, -5)

def test_get_balance():
    acc = Account(1, 123.45)
    assert acc.get_balance() == 123.45
    acc.add_funds_via_transfer(10)
    assert acc.get_balance() == 133.45
    acc.schedule_payment(3.45)
    assert acc.get_balance() == 130.0

def test_get_transaction_history():
    acc = Account(1)
    acc.add_funds_via_transfer(100)
    acc.schedule_payment(30)
    history = acc.get_transaction_history()
    assert "Incoming transfer: 100" in history
    assert "Scheduled payment: 30" in history
    assert len(history) == 2

def test_login():
    user = User("john", "1234")
    assert user.login("john", "1234") is True
    assert user.logged_in is True
    assert user.login("john", "wrong") is False
    assert user.login("wrong", "1234") is False
    assert user.login("", "") is False
