import tkinter as tk
from tkinter import messagebox

def nhap_phim(gia_tri):
    hien_tai = entry_hien_thi.get()
    entry_hien_thi.delete(0, tk.END)
    entry_hien_thi.insert(0, hien_tai + str(gia_tri))

def xoa_man_hinh():
    entry_hien_thi.delete(0, tk.END)

def tinh_ket_qua():
    bieu_thuc = entry_hien_thi.get()
    try:
        # Sử dụng eval để tính giá trị biểu thức toán học
        ket_qua = eval(bieu_thuc)
        entry_hien_thi.delete(0, tk.END)
        entry_hien_thi.insert(0, str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0.")
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le.")

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("300x400")
cua_so.resizable(False, False)

# Ô hiển thị biểu thức/kết quả
entry_hien_thi = tk.Entry(cua_so, font=("Arial", 18), justify="right", width=16)
entry_hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Danh sách các nút bấm bàn phím số và phép tính
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

for (text, row, col) in buttons:
    tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2,
              command=lambda t=text: nhap_phim(t)).grid(row=row, column=col, padx=5, pady=5)

# Nút C (Xóa) chiếm cột 2 hàng 4
tk.Button(cua_so, text="C", font=("Arial", 14), width=5, height=2,
          command=xoa_man_hinh).grid(row=4, column=2, padx=5, pady=5)

# Nút = (Tính kết quả) trải dài ở hàng 5
tk.Button(cua_so, text="=", font=("Arial", 14), width=22, height=2, bg="orange",
          command=tinh_ket_qua).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

if __name__ == "__main__":
    cua_so.mainloop()