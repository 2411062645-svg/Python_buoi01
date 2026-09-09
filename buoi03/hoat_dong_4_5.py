import math

print("=== HOẠT ĐỘNG 4: Tuple - khai báo, bất biến, unpacking ===")
# Bài tập 4.1 - Khai báo & tính bất biến:
toa_do = (3, 5)
print(toa_do, type(toa_do))
# Thu gan lai: toa_do[0] = 10 -> quan sat loi TypeError (tuple bat bien)

# Bài tập 4.2 - Unpacking tuple:
x, y = toa_do
print("x =", x, "- y =", y)

# Doi gia tri 2 bien bang unpacking (khong can bien tam)
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

# Bài tập 4.3 - Trả về nhiều giá trị từ một biểu thức:
c, d = 17, 5
thuong_du = divmod(c, d)     # divmod tra ve mot tuple (thuong, du)
thuong, du = thuong_du       # unpacking ket qua
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")


print("\n=== HOẠT ĐỘNG 5: Vận dụng Tuple - Tọa độ điểm & khoảng cách ===")
diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

# --- YÊU CẦU TÔ VÀNG HOẠT ĐỘNG 5 ---
# Tạo thêm danh_sach_cac_diem = [(0,0), (3,4), (6,8)], dùng for để in ra khoảng cách của từng điểm so với gốc tọa độ (0,0)
danh_sach_cac_diem = [(0, 0), (3, 4), (6, 8)]
print("\nTính khoảng cách đến gốc tọa độ (0,0):")
for diem in danh_sach_cac_diem:
    x_i, y_i = diem
    kc = math.sqrt(x_i**2 + y_i**2)
    print(f"Khoảng cách từ điểm {diem} đến gốc tọa độ (0,0) là: {round(kc, 2)}")