Lap-03
UML Thiết kế (Use case-UC, Sequence Diagram-SQ)
Use Case: Rút tiền
Tên Use Case: Rút tiền
Tác nhân chính: Khách hàng (ATM User)
Mục tiêu: Khách hàng rút tiền mặt từ tài khoản ngân hàng qua máy ATM.
Phạm vi: ATM Mini Project
Tiền điều kiện:
Khách hàng có thẻ ATM và tài khoản hợp lệ.
ATM có đủ tiền mặt.
Luồng sự kiện chính:
Khách hàng đưa thẻ vào máy ATM.
Hệ thống yêu cầu nhập mã PIN.
Khách hàng nhập PIN.
Hệ thống xác thực PIN với Ngân hàng.
Hệ thống hiển thị menu, khách hàng chọn “Rút tiền”.
Khách hàng nhập số tiền muốn rút.
Hệ thống kiểm tra số dư tài khoản và số tiền khả dụng.
Nếu hợp lệ → ATM nhả tiền mặt.
Hệ thống cập nhật số dư và in biên lai.
Luồng thay thế:
3a. Nhập sai PIN 3 lần → Thẻ bị khóa.
7a. Số dư không đủ → Thông báo lỗi, hủy giao dịch.
8a. ATM hết tiền → Thông báo lỗi.
Hậu điều kiện:
Giao dịch hoàn tất, số dư tài khoản được cập nhật.
