import pytest

def test_verify_pin_ok(mock_app):
    app, state = mock_app
    assert app.verify_pin(state["card_no"], "123456") is True

def test_verify_pin_wrong(mock_app):
    app, state = mock_app
    assert app.verify_pin(state["card_no"], "000000") is False

def test_withdraw_ok(mock_app):
    app, state = mock_app
    old = state["balance"]
    nb = app.withdraw(state["card_no"], 500000)
    assert nb == old - 500000
    assert state["balance"] == old - 500000
    assert len(state["logs"]) >= 1

def test_withdraw_insufficient(mock_app):
    app, state = mock_app
    with pytest.raises(ValueError, match="Insufficient funds"):
        app.withdraw(state["card_no"], 99999999)
