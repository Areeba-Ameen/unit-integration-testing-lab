import pytest
from bank_app import calculate_interest, transfer

#transfer test case

def test_transfer_success():
    from_balance, to_balance = transfer(10000, 2000, 3000)

    assert from_balance == 7000
    assert to_balance == 5000

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(2000, 1000, 3000)

def test_transfer_negative_amount():
    with pytest.raises(ValueError):
        transfer(5000, 2000, -100)

#transfer followed by interest

def test_transfer_then_interest():
    from_balance, to_balance = transfer(10000, 2000, 3000)

    updated_balance = calculate_interest(to_balance, 10, 1)

    assert round(updated_balance, 2) == 5500.00

