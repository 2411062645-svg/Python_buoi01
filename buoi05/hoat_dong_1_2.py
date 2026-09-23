# ==========================================
# HOẠT ĐỘNG 1: IF, IF-ELSE, IF-ELIF-ELSE & ĐIỀU KIỆN RÚT GỌN
# ==========================================

# Bài tập 1.1 - if đơn và if-else
tuoi = 20

if tuoi >= 18:
    print("Đã đủ tuổi trưởng thành")

if tuoi >= 18:
    print("Được phép đăng ký xe máy")
else:
    print("Chưa đủ tuổi")

# Bài tập 1.2 - if-elif-else
diem = 7.2

if diem >= 8.0:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")

# Bài tập 1.3 - Điều kiện lồng nhau
tuoi = 17
co_giay_phep = False

if tuoi >= 18:
    if co_giay_phep:
        print("Được phép lái xe")
    else:
        print("Đủ tuổi nhưng chưa có giấy phép")
else:
    print("Chưa đủ tuổi lái xe")

# Bài tập 1.4 - Biểu thức điều kiện rút gọn (Conditional Expression)
diem = 4.5
ket_qua = "Đạt" if diem >= 5.0 else "Không đạt"
print(ket_qua)

so = -7
tri_tuyet_doi = so if so >= 0 else -so
print(tri_tuyet_doi)


# ==========================================
# HOẠT ĐỘNG 2: VẬN DỤNG IF - XẾP LOẠI HỌC LỰC, TÌM SỐ LỚN NHẤT
# ==========================================

# Bài tập 2.1 - Xếp loại học lực đầy đủ
ho_ten = "Nguyễn Văn A"
diem_toan, diem_ly, diem_hoa = 8.0, 7.5, 9.0

dtb = round((diem_toan + diem_ly + diem_hoa) / 3, 2)

if dtb >= 8.0:
    xep_loai = "Giỏi"
elif dtb >= 6.5:
    xep_loai = "Khá"
elif dtb >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print(f"{ho_ten} - ĐTB: {dtb} - Xếp loại: {xep_loai}")

# Bài tập 2.2 - Tìm số lớn nhất trong 3 số nhập vào
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if a >= b and a >= c:
    lon_nhat = a
elif b >= a and b >= c:
    lon_nhat = b
else:
    lon_nhat = c

print("Số lớn nhất là:", lon_nhat)
