# 1. Hàm không có tham số
# Đây là loại hàm cơ bản nhất, không nhận bất kỳ giá trị đầu vào nào.
def chao_mung():
    print("Chào mừng bạn đến với thế giới Python!")

# Gọi hàm để thực thi
chao_mung() 
# Kết quả: Chào mừng bạn đến với thế giới Python!
# --------------------------------------------------



# 2. Hàm có tham số
# Hàm có thể nhận các giá trị đầu vào, gọi là tham số (parameters), để thực hiện các tác vụ linh hoạt hơn.
def chao_ten(ten):
    print(f"Xin chào, {ten}!")

# Gọi hàm với tham số
chao_ten("An") 
# Kết quả: Xin chào, An!

chao_ten("Bình")
# Kết quả: Xin chào, Bình!

# 3. Hàm có giá trị trả về (return)
# Hàm không chỉ thực thi một tác vụ mà còn có thể trả về một giá trị nào đó sau khi kết thúc. Bạn sử dụng từ khóa return để làm điều này.
def tinh_tong(a, b):
    tong = a + b
    return tong  # <= trả về giá trị cho hàm

# Gọi hàm và gán giá trị trả về vào một biến
ket_qua = tinh_tong(5, 6)
print(f"Tổng là: {ket_qua}") 
# Kết quả: Tổng là: 11


ket_qua = tinh_tong(8, 6)
print(f"Tổng là: {ket_qua}") 
# Kết quả: Tổng là: 14