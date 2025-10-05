Ghi chú Lab06 – Thiết kế lớp & kiến trúc ATM
1. Class Diagram
- Gồm 4 lớp chính ATM, Card, Account, Transaction
- ATM quản lý các thao tác authenticate, withdraw, deposit, transfer
- Card liên kết Account, Account liên kết Transaction
2. Package Diagram
- UI giao diện ATM
- Controller xử lý nghiệp vụ
- BankService cung cấp dịch vụ kiểm tra tài khoản và giao dịch
- Hardware mô phỏng phần cứng (CardReader, CashDispenser, ReceiptPrinter)
3. Lý do thiết kế
- Phân tách rõ trách nhiệm từng lớp
- Dễ mở rộng và bảo trì hệ thống
