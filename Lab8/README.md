# Lab 08 – Kiểm thử ATM (Unit test & Integration test)

## 🎯 Mục tiêu
- Unit Test: `verify_pin`, `withdraw` (Lab 07) bằng pytest (mock DB).
- Integration Test: Form Login (Lab 04) bằng Selenium.
- Báo cáo pass/fail (ảnh hoặc HTML report).

## Cấu trúc
```
/labs/lab08-testing/
├─ README.md
├─ requirements.txt
├─ conftest.py
├─ test_withdraw.py
├─ selenium_test_login.py
├─ run_pytest.sh / .bat
└─ run_selenium.sh / .bat
```

## Cài đặt
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Chạy Unit Test
```bash
pytest -q --maxfail=1 --disable-warnings --html=report_unit.html --self-contained-html
```

## Chạy Selenium (Integration)
- Dùng GitHub Pages của Lab 04: 
  ```bash
  export BASE_URL="https://<username>.github.io/Lab04_LoginForm/"
  python selenium_test_login.py
  ```
- Hoặc dùng file local:
  ```bash
  python selenium_test_login.py --local /path/to/Lab04_Login/index.html
  ```

## Rubric
- Unit test đủ case (4)
- Integration test form login (4)
- Báo cáo (2)
