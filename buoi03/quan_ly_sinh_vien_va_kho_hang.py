print("=== HOẠT ĐỘNG 6: Mini project 1 - Quản lý danh sách sinh viên ===")
danh_sach_sv = [(8.5, "An"), (7.0, "Bình"), (9.2, "Chi"), (6.5, "Dung")]

# Them sinh vien moi
danh_sach_sv.append((8.0, "Em"))

# Xoa mot sinh vien (biet chinh xac ca diem va ten)
danh_sach_sv.remove((7.0, "Bình"))

# Sua diem cho sinh vien o vi tri xac dinh (vi du vi tri 0)
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

# Kiem tra mot sinh vien co trong danh sach hay khong (dung toan tu in)
print("Chi co trong danh sach khong?", (9.2, "Chi") in danh_sach_sv)

# Sap xep theo diem tang dan (mac dinh so sanh phan tu dau tien cua tuple truoc)
danh_sach_sv.sort()
print("\nDanh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")

# Sap xep giam dan
danh_sach_sv.sort(reverse=True)
print("\nDanh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


print("\n=== HOẠT ĐỘNG 7: Mini project 2 - Quản lý kho hàng + Tổng kết ===")
kho_hang = [
    ("Bàn phím", 250000, 10),
    ("Chuột", 150000, 20),
    ("Màn hình", 2500000, 5)
]

# Them san pham moi
kho_hang.append(("Tai nghe", 300000, 15))

# Xoa mot san pham
kho_hang.remove(("Chuột", 150000, 20))

# Hien thi danh sach kho hang
print("\nDANH SÁCH KHO HÀNG:")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Giá: {gia:>10,} - Sl: {so_luong}")

# Tinh tong gia tri kho hang bang vong lap cong don
tong_gia_tri = 0
for ten, gia, so_luong in kho_hang:
    tong_gia_tri = tong_gia_tri + gia * so_luong

print(f"\nTổng giá trị kho hàng: {tong_gia_tri:,} VNĐ")