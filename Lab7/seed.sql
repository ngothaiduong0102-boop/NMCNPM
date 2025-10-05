USE atm_demo;
INSERT INTO accounts(customer_name, balance) VALUES
('Nguyen Van A', 5000000),
('Le Thi B', 2000000);
-- pin 123456 -> sha256
INSERT INTO cards(card_no, account_id, pin_hash) VALUES
('4000123412341234', 1, '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('4999123411112222', 2, '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92');