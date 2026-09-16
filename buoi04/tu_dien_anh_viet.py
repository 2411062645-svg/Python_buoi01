# ==========================================
# HOẠT ĐỘNG 5: VẬN DỤNG - TỪ ĐIỂN ANH - VIỆT
# ==========================================

tu_dien_anh_viet = {
    "hello": "xin chao",
    "book": "quyen sach",
    "table": "cai ban"
}

# 1. Tra từ
print(tu_dien_anh_viet.get("hello", "Khong tim thay tu nay"))
print(tu_dien_anh_viet.get("computer", "Khong tim thay tu nay"))

# 2. Thêm từ mới
tu_dien_anh_viet["computer"] = "may tinh"

# 3. Xóa một từ
tu_dien_anh_viet.pop("table")

# 4. In danh sách từ điển hiện tại
print("\nTu dien hien tai:")
for tu_anh, tu_viet in tu_dien_anh_viet.items():
    print(f"{tu_anh} - {tu_viet}")