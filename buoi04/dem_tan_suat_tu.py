# =======================================================
# HOẠT ĐỘNG 6: VẬN DỤNG - ĐẾM TẦN SUẤT TỪ TRONG VĂN BẢN
# =======================================================

doan_van = "python la ngon ngu lap trinh python de hoc python de dung"

# 1. Tách chuỗi thành danh sách các từ
danh_sach_tu = doan_van.split()
tan_suat = {}

# 2. Duyệt qua từng từ và đếm số lần xuất hiện
for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

# 3. In kết quả tần suất xuất hiện
print("Tan suat xuat hien cac tu:")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")
    