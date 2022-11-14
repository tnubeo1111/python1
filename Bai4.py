#Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
#Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

values=int(input("Nhap vào các giá trị: "))
l=values.split(",") #Hàm Split trả lại danh sách của chuỗi sau khi chia các chuỗi này dựa vào các dấu phân tách đã cho
t=tuple(1) #Tuple trong Python là một kiểu dữ liệu dùng để lưu trữ các đối tượng có thứ tự và bất biến
print(l)
print(t)