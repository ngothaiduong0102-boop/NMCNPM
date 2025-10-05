import os, hashlib
import mysql.connector
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()

DB_CFG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "123456"),
    "database": os.getenv("DB_NAME", "atm_demo"),
    "auth_plugin": 'mysql_native_password',
}

@contextmanager
def db_conn():
    conn = mysql.connector.connect(**DB_CFG)
    try:
        yield conn
    finally:
        conn.close()

def sha256(s): return hashlib.sha256(s.encode()).hexdigest()

def verify_pin(card_no, pin):
    sql = "SELECT pin_hash, is_active FROM cards WHERE card_no=%s"
    with db_conn() as conn:
        cur = conn.cursor()
        cur.execute(sql, (card_no,))
        row = cur.fetchone()
        cur.close()
    return bool(row and row[1] and row[0] == sha256(pin))

def get_account_for_update(conn, card_no):
    sql = """SELECT a.account_id, a.balance
             FROM accounts a JOIN cards c ON c.account_id=a.account_id
             WHERE c.card_no=%s FOR UPDATE"""
    cur = conn.cursor()
    cur.execute(sql, (card_no,))
    row = cur.fetchone()
    cur.close()
    if not row: raise ValueError("Card not found")
    return row[0], int(row[1])

def withdraw(card_no, amount, atm_id=1):
    if amount <= 0: raise ValueError("Amount must be > 0")
    with db_conn() as conn:
        try:
            conn.start_transaction()
            account_id, balance = get_account_for_update(conn, card_no)
            if balance < amount: raise ValueError("Insufficient funds")
            cur = conn.cursor()
            cur.execute("UPDATE accounts SET balance=balance-%s WHERE account_id=%s",
                        (amount, account_id))
            new_balance = balance - amount
            cur.execute("""INSERT INTO transactions(account_id,card_no,atm_id,tx_type,amount,balance_after)
                         VALUES(%s,%s,%s,'WITHDRAW',%s,%s)""",
                        (account_id, card_no, atm_id, amount, new_balance))
            conn.commit()
            cur.close()
            return new_balance
        except Exception as e:
            conn.rollback()
            raise
