import pytest

class FakeCursor:
    def __init__(self, state):
        self.state = state
        self._fetchone = None
    def execute(self, sql, params=None):
        s = " ".join(sql.split()).lower()
        if "from cards" in s and "where card_no" in s:
            self._fetchone = (self.state["pin_hash"], self.state["is_active"])
        elif "for update" in s:
            self._fetchone = (self.state["account_id"], self.state["balance"])
        elif "update accounts set balance=balance-" in s:
            amount, account_id = params
            assert account_id == self.state["account_id"]
            self.state["balance"] -= amount
        elif "insert into transactions" in s:
            self.state["logs"].append(params)
    def fetchone(self): return self._fetchone
    def close(self): pass

class FakeConn:
    def __init__(self, state):
        self.state = state
        self.started = False
    def cursor(self): return FakeCursor(self.state)
    def start_transaction(self): self.started = True
    def commit(self): pass
    def rollback(self): pass
    def close(self): pass

class FakeCtx:
    def __init__(self, conn): self.conn = conn
    def __enter__(self): return self.conn
    def __exit__(self, *a): self.conn.close()

@pytest.fixture
def mock_app(monkeypatch):
    import importlib
    app = importlib.import_module("app")
    state = {
        "pin_hash": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
        "is_active": 1,
        "balance": 5_000_000,
        "account_id": 1,
        "card_no": "4000123412341234",
        "logs": []
    }
    def fake_db_conn():
        return FakeCtx(FakeConn(state))
    monkeypatch.setattr(app, "db_conn", fake_db_conn)
    return app, state
