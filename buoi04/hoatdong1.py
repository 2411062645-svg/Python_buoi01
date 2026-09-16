# ==========================================
# BÀI TẬP 1.1: KHAI BÁO & TRUY XUẤT
# ==========================================
print("=== BÀI TẬP 1.1 ===")
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

# Truy xuất thông tin
print("Họ tên:", sinh_vien["ho_ten"])                # Truy xuất theo khóa
print("Điểm TB:", sinh_vien.get("diem_tb"))         # Truy xuất an toàn bằng get()
print("Lớp:", sinh_vien.get("lop", "Chua co"))       # get() với giá trị mặc định khi khóa không tồn tại


# ==========================================
# BÀI TẬP 1.2: THÊM / SỬA / XÓA
# ==========================================
print("\n=== BÀI TẬP 1.2 ===")

# 1. Thêm khóa mới & Sửa giá trị khóa đã có
sinh_vien["lop"] = "CNTT01"       # Thêm khóa "lop"
sinh_vien["diem_tb"] = 9.0        # Sửa "diem_tb" thành 9.0
print("Sau khi thêm lớp & sửa điểm:")
print(sinh_vien)

# 2. Xóa theo khóa bằng pop()
diem_cu = sinh_vien.pop("diem_tb")
print("\nSau khi xóa diem_tb:")
print(sinh_vien, "- điểm đã xóa:", diem_cu)

# 3. Cập nhật / Thêm nhiều khóa cùng lúc bằng update()
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"})
print("\nSau khi dùng update():")
print(sinh_vien)