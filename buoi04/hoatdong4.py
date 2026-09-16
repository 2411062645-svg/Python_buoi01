# ==========================================
# BÀI TẬP 4.1: ÉP KIỂU TƯỜNG MINH
# ==========================================
print("=== BÀI TẬP 4.1 ===")
chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))

so_thuc = float("3.14")
print(so_thuc, type(so_thuc))

danh_sach = list((1, 2, 3))                       # tuple -> list
bo_ba = tuple([4, 5, 6])                           # list -> tuple
tap_hop = set([1, 2, 2, 3, 3, 3])                 # list -> set (tự loại bỏ trùng lặp)
tu_dien = dict([("a", 1), ("b", 2)])              # list các tuple -> dict

print(danh_sach, bo_ba, tap_hop, tu_dien)


# ==========================================
# BÀI TẬP 4.2: TRƯỜNG HỢP GÂY LỖI KHI ÉP KIỂU
# ==========================================
print("\n=== BÀI TẬP 4.2 ===")

# Cách làm đúng: ép qua float trước rồi mới ép về int
so_hop_le = int(float("3.14"))
print("so_hop_le:", so_hop_le)


# ==========================================
# BÀI TẬP 4.3: CHUYỂN ĐỔI NGẦM ĐỊNH
# ==========================================
print("\n=== BÀI TẬP 4.3 ===")
ket_qua = 5 + 2.5                                 # int + float -> Python tự động chuyển thành float
print(ket_qua, type(ket_qua))

ket_qua_2 = "Diem: " + str(8.5)                   # Phải ép str() tường minh, Python KHÔNG tự động nối str với số
print(ket_qua_2)
