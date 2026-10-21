import tkinter as tk
from tkinter import ttk

# Khởi tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Vi du Listbox va Combobox")
cua_so.geometry("300x450")

# --- PHẦN BÀI TẬP 3.1: Listbox ---
listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single", height=5)
for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)
listbox_mon_hoc.pack(pady=10)

def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()
    if lua_chon:
        nhan_ket_qua_listbox.config(text=f"Mon da chon: {listbox_mon_hoc.get(lua_chon[0])}")

tk.Button(cua_so, text="Xem mon da chon", command=xem_mon_da_chon).pack(pady=5)
nhan_ket_qua_listbox = tk.Label(cua_so, text="")
nhan_ket_qua_listbox.pack(pady=5)

# Thêm đường kẻ phân cách giao diện
ttk.Separator(cua_so, orient="horizontal").pack(fill="x", padx=10, pady=10)

# --- PHẦN BÀI TẬP 3.2: Combobox ---
tk.Label(cua_so, text="Chon thanh pho:").pack(pady=5)

combobox_thanh_pho = ttk.Combobox(cua_so, values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"])
combobox_thanh_pho.current(0)  # chọn giá trị đầu tiên làm mặc định
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    nhan_ket_qua_combobox.config(text=f"Ban chon: {combobox_thanh_pho.get()}")

tk.Button(cua_so, text="Xac nhan", command=xem_thanh_pho).pack(pady=5)
nhan_ket_qua_combobox = tk.Label(cua_so, text="")
nhan_ket_qua_combobox.pack(pady=5)

# Chạy vòng lặp giao diện
cua_so.mainloop()