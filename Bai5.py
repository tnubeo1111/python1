#Định nghĩa một class có ít nhất 2 method:
#getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
#printString: in chuỗi vừa nhập sang chữ hoa.
#Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.
#Chuỗi nhập vào là lethanhtha thì đầu ra phải là: LE THANH THA

class InputOutString(object):
    def __init__(self): #__init__() là tên của hàm khởi tạo (constructor) self là tham số đầu tiên của hàm __init__(). Đây là một tham chiếu đến đối tượng hiện tại của lớp và được sử dụng để truy cập các biến thuộc về lớp đó.
        self.s = ""

    def getString(self):
        self.s = input("Nhập chuỗi: ")
    
    def printString(self):
        print(self.s.upper()) #Hàm upper() trong Python chuyển đổi các chữ thường trong chuỗi thành chữ hoa.

strobj = InputOutString()
strobj.getString()
strobj.printString()