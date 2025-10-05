# Lab 07 – Phát triển Module Rút tiền (Prototype Python + MySQL)

## 🎯 Mục tiêu
Viết module code mô phỏng **Withdraw** trong ATM, dùng **Python + MySQL connector**, có transaction, kiểm tra số dư, ghi log.

## Cấu trúc
```
/labs/lab07-withdraw-module/
├─ README.md
├─ requirements.txt
├─ .env.example
├─ schema.sql
├─ seed.sql
├─ app.py
├─ cli.py
├─ test_plan.md
├─ run_demo.sh
└─ run_demo.bat
```

### Cài đặt & chạy
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env           # chỉnh thông số DB
mysql -u root -p < schema.sql
mysql -u root -p atm_demo < seed.sql

python cli.py --card 4000123412341234 --pin 123456 --amount 500000
```
