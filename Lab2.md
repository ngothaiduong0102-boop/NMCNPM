![USE CASE DIAGRAM](https://github.com/ngothaiduong0102-boop/NMCNPM/blob/main/usecase.png)

# Use Case Descriptions – Hotel Booking Management System

1) Book Room
Goal: Khách đặt phòng thành công và nhận xác nhận đặt chỗ.  
Primary Actor: Guest  
Supporting Actors: Payment Gateway, Email Service  
Preconditions:  
- Guest đã chọn ngày nhận/trả phòng hợp lệ.  
- Phòng còn trống.  

**Postconditions:  
- Đơn đặt phòng ở trạng thái *Confirmed*.  
- Biên lai thanh toán được lưu; email xác nhận được gửi.  

Main Flow:  
1. Guest tìm phòng theo ngày và tiêu chí.  
2. Hệ thống hiển thị danh sách phòng còn trống.  
3. Guest chọn phòng → nhấn *Book*.  
4. Hệ thống hiển thị thông tin đặt phòng và tổng tiền.  
5. Guest nhập thông tin thanh toán → xác nhận.  
6. Hệ thống chuyển đến Payment Gateway để xử lý.  
7. Payment Gateway phản hồi *thành công*.  
8. Hệ thống tạo đơn đặt phòng *Confirmed*.  
9. Hệ thống gửi email xác nhận cho Guest.  

Alternate Flows:  
- A1: Guest chưa đăng nhập → hệ thống yêu cầu *Register/Login* rồi quay lại bước 4.  
- A2: Phòng vừa hết chỗ ở bước 3 → thông báo và đề xuất phòng khác.  

Exceptions:  
- E1: Thanh toán thất bại ở bước 7 → hiển thị thông báo, cho phép thử lại hoặc chọn phương thức khác.  
- E2: Lỗi hệ thống/Email Service không gửi được → ghi log và hiển thị thông báo “Đã đặt thành công, email sẽ được gửi sau”.  

Business Rules:  
- BR1: Thời gian giữ phòng tạm thời tối đa 10 phút trong khi chờ thanh toán.  
- BR2: Giá phòng có thể thay đổi theo ngày lễ/cuối tuần.  

---

 2) Cancel Booking
Goal: Hủy đơn đặt phòng trước thời điểm check-in theo chính sách.  
Primary Actor: Guest  
Supporting Actors: Email Service, (tuỳ chọn) Payment Gateway cho hoàn tiền.  
Preconditions:  
- Đơn ở trạng thái *Confirmed* và chưa check-in.  
- Chính sách hủy cho phép (ví dụ: trước 24h).  

Postconditions: 
- Đơn ở trạng thái *Cancelled*.  
- (Nếu đủ điều kiện) Hoàn tiền được thực hiện.  
- Email thông báo hủy được gửi.  

Main Flow:
1. Guest mở *My Bookings* → chọn đơn cần hủy.  
2. Hệ thống kiểm tra chính sách hủy cho đơn đó.  
3. Guest xác nhận hủy.  
4. Hệ thống cập nhật trạng thái đơn thành *Cancelled*.  
5. (Nếu áp dụng) Hệ thống yêu cầu Payment Gateway hoàn tiền.  
6. Hệ thống gửi email thông báo hủy cho Guest.  

Alternate Flows:
- A1: Hủy ngoài thời hạn miễn phí → hiển thị phí phạt, Guest xác nhận tiếp tục trước khi hủy.  

Exceptions: 
- E1: Không đủ điều kiện hủy theo chính sách → hiển thị lý do và chặn thao tác.  
- E2: Lỗi hoàn tiền từ Payment Gateway → hiển thị thông báo và tạo ticket hỗ trợ.  

Business Rules:
- BR1: Phí hủy được tính dựa trên số giờ còn lại đến thời điểm check-in.  
- BR2: Hoàn tiền thực hiện theo cùng phương thức thanh toán đã dùng.
