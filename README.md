# overthewrite
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
+ Bắt đầu chúng ta tập trung vào các điều kiện để viết script
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/a5d2ce26-a7fa-4911-beab-17f6734fec0d)
+ ta thấy điều kiện của biến v9 phải nhập đủ 4 byte "0x13371337" vì max của biến buf là 80 byte nên ta phải nhập đủ 76 byte trước đó và 0x13371337 để next được Stage1
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/81e779fb-e74f-458e-b1e2-7c0b99ef542b)
+ Vậy chúng ta đã next được Stage 1
+ Tiếp theo chúng ta kiểm tra lại các offset trên gdb hồi nãy chúng ta vừa kiểm tra
+ Điều kiện của v8 == 0xDEADBEEFCAFEBABE(8 byte) để next đc Stage 2 và với khoảng cách từ biến đầu tiên tới v8 là 64 byte 
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/41748fc4-4d9e-4c20-84db-a76b96ca9ef1)
+ Vậy điều kì lạ là để tới được v9 thì cần 76 byte, còn tới được v8 là 64 byte + 8 byte của v8 là 72 byte vậy ta cần 4 byte rác để tới được v9
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/910f2700-481c-42cc-887c-ca7dc9a79bcc)
+ Vậy chúng ta đã next được Stage2
+ Tiếp tục với điều kiện của v7== 0x215241104735F10F và khoảng cách từ biến đầu tiên tới v7 là 56 byte
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/f32acabb-1b9a-4a34-b982-ce1fbd72e159)
+ Với biến v7 tới v8 thì ta thấy 56 byte + 8 byte 0x215241104735F10F là 64 byte vậy ở đây không có byte rác nào
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/c08495be-fe19-4ab0-8743-3b45dda7ceb7)
+ Vậy là chúng ta đã next đc Stage 3
+ Điều kiện tiếp theo là check s1 == "Welcome to KCSC" với off set từ đầu đến char là 32 byte
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/fc58a443-b748-414e-afaa-36a77673c4d2)
+ Như đã nói ở trên từ biến s1 tới v7 là 56-32 = 24 byte trong đó chúng ta đã tính cả v6 nên chỗ này chúng ta ghi đè lên v6 với chuỗi kí tự Welcome to KCSC hoặc là byte rác
+ Quay lại script : Với chuỗi kí tự "Welcome to KCSC\0" là 16 byte vậy chúng ta cần 8 byte để lấp đủ s1 để tới v7
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/31a868ca-ff70-4af2-a060-edfb4d2a3b4e)
+ Vậy chúng ta đã hoàn thành được bài # overthewrite
+ Đây là script của bài
+ ![image](https://github.com/hieubmt1112004/overthewrite/assets/125638408/88428895-1583-4c21-8089-51ad82c857d4)












