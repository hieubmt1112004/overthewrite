![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/5cf03dc4-7251-4d25-a18c-87708ef54891)# overthewrite
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/dcd5ff75-e96f-45be-952a-d8053a92e8e6)
+ Đầu tiên ta bật IDA để dịch ngược và đọc code đề bài cho thấy đầu tiên biến buf gồm 4 phần tử , chuỗi kí tự s1 , v6,v7,v8,v9
+ Biến buf cho phép nhập 80 byte
+ Với điều kiện v9 =0x13371337 thì ta next được "Stage 1"
+ Tương tự v8 = 0xDEADBEEFCAFEBABE next được "Stage 2" và v9 = 0x215241104735F10F thì next được "Stage 3"
+ Và s1 phải là chuỗi kí tự "Welcome to KCSC"
+ GDB và dùng lệnh disas main
+ Sau đó đặt break point ở sau hàm read
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/6076c668-803e-4ec9-843b-4132d117e16c)
+ Sau đó ta qua 1 tab terminal mới
+ GDB và ni cho tới hàm read
+ Sau đó tạo 1 chuỗi bằng pattern create và nhập vào hàm read cỡ 50 byte
+ Tiếp tục kiểm tra offset của các biến
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/7c4606f1-b20b-4110-a6d9-da12d183fe47)
+ Ta có thể thấy rõ offset của các biến có trên gdb




