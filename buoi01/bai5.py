# ==========================================
# Bài tập 5.1 – Toán tử số học
# ==========================================
print("--- Bài tập 5.1 ---")
a = 17
b = 5

print("a + b =", a + b)      # 22
print("a - b =", a - b)      # 12
print("a * b =", a * b)      # 85
print("a / b =", a / b)      # 3.4
print("a // b =", a // b)    # 3
print("a % b =", a % b)      # 2
print("a ** b =", a ** b)    # 1419857

# ==========================================
# Bài tập 5.2 – Toán tử so sánh & logic
# ==========================================
print("\n--- Bài tập 5.2 ---")
diem = 6.5
tuoi = 20

# 1. Kiểm tra điểm đạt loại Khá (từ 6.5 đến dưới 8.0)
kt_khac = (diem >= 6.5) and (diem < 8.0)
print("Điểm đạt loại Khá?:", kt_khac)

# 2. Kiểm tra tuổi chưa đủ 18 hoặc trên 60
kt_tuoi = (tuoi < 18) or (tuoi > 60)
print("Tuổi < 18 hoặc > 60?:", kt_tuoi)

# 3. Phủ định lại các điều kiện trên bằng 'not'
print("Phủ định điều kiện điểm Khá:", not kt_khac)
print("Phủ định điều kiện tuổi:", not kt_tuoi)

# ==========================================
# Bài tập 5.3 – Toán tử gán & toán tử đặc biệt
# ==========================================
print("\n--- Bài tập 5.3 ---")
x = 10

x += 5
print("x sau khi += 5 là:", x)

x -= 3
print("x sau khi -= 3 là:", x)

x *= 2
print("x sau khi *= 2 là:", x)

x /= 4
print("x sau khi /= 4 là:", x)


print("x sau khi //= 2 là:", x)


print("x sau khi **= 3 là:", x)


danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không?:", 3 in danh_sach)

list1 = [1, 2, 3]
list2 = list1  
print("list1 is list2?:", list1 is list2)

print("\n--- Bài tập 5.4 ---")
print("Kết quả 1:", 2 + 3 * 4 ** 2)
print("Kết quả 2:", (2 + 3) * 4 ** 2)
print("Kết quả 3:", 10 > 5 and 3 < 1 or not False)