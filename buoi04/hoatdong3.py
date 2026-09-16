# Bài tập 3.1 - Dictionary comprehension
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}

# Cộng thêm 0.5 điểm cho mỗi môn
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)

# Viết hoa tên các môn học
ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)


# Bài tập 3.2 - So sánh nhanh với Set
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

# Giao: môn học chung giữa 2 học kỳ (&)
print(mon_hoc_ky1 & mon_hoc_ky2)

# Hợp: tất cả môn học cả 2 học kỳ (|)
print(mon_hoc_ky1 | mon_hoc_ky2)
print(mon_hoc_ky1 - mon_hoc_ky2) # mon chi co o hoc ky 1