import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_kho_hang as db

DANH_SACH_DANH_MUC = ["Điện tử", "Gia dụng", "Thời trang", "Thực phẩm", "Văn phòng phẩm", "Khác"]

class UngDungQuanLyKho(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ứng dụng Quản lý Kho hàng Mini")
        self.geometry("620x520")
        self.resizable(False, False)

        db.tao_bang_nhu_cau_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        # Frame Nhập liệu
        khung_nhap = tk.LabelFrame(self, text="Thêm sản phẩm mới", padx=10, pady=10)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Tên sản phẩm:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten = tk.Entry(khung_nhap, width=25)
        self.o_nhap_ten.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(khung_nhap, text="Danh mục:").grid(row=0, column=2, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_DANH_MUC, width=18, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(khung_nhap, text="Số lượng ban đầu:").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_so_luong = tk.Entry(khung_nhap, width=25)
        self.o_nhap_so_luong.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(khung_nhap, text="Giá bán (VNĐ):").grid(row=1, column=2, sticky="w", pady=5)
        self.o_nhap_gia = tk.Entry(khung_nhap, width=20)
        self.o_nhap_gia.grid(row=1, column=3, padx=5, pady=5)

        tk.Button(khung_nhap, text="Thêm Sản Phẩm", bg="#4CAF50", fg="white", command=self.xu_ly_them_sp).grid(row=2, column=0, columnspan=4, pady=10)

        # Frame Danh sách
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_sp = tk.Listbox(khung_danh_sach, width=80, height=12)
        self.listbox_sp.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_sp.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sp.config(yscrollcommand=thanh_cuon.set)

        # Frame Thao tác Nhập / Xuất Kho
        khung_thao_tac = tk.Frame(self)
        khung_thao_tac.pack(pady=10)

        tk.Button(khung_thao_tac, text="+ Nhập Thêm (10 sp)", command=lambda: self.xu_ly_thay_doi_sl(10)).grid(row=0, column=0, padx=5)
        tk.Button(khung_thao_tac, text="- Xuất Kho (1 sp)", command=lambda: self.xu_ly_thay_doi_sl(-1)).grid(row=0, column=1, padx=5)
        tk.Button(khung_thao_tac, text="Xóa Sản Phẩm", bg="#f44336", fg="white", command=self.xu_ly_xoa_sp).grid(row=0, column=2, padx=5)
        tk.Button(khung_thao_tac, text="Biểu Đồ Tồn Kho", bg="#2196F3", fg="white", command=self.xu_ly_thong_ke).grid(row=0, column=3, padx=5)

    def tai_lai_danh_sach(self):
        self.listbox_sp.delete(0, tk.END)
        self.danh_sach_sp = db.lay_danh_sach_san_pham()

        for sp in self.danh_sach_sp:
            id_sp, ten_sp, danh_muc, so_luong, gia_ban = sp
            canh_bao = "[CẢNH BÁO HẾT]" if so_luong <= 2 else ""
            self.listbox_sp.insert(
                tk.END, 
                f"ID: {id_sp} | {ten_sp} - {danh_muc} | Tồn: {so_luong} | Giá: {gia_ban:,.0f} VNĐ {canh_bao}"
            )

    def xu_ly_them_sp(self):
        ten = self.o_nhap_ten.get().strip()
        danh_muc = self.chon_danh_muc.get()
        so_luong_str = self.o_nhap_so_luong.get().strip()
        gia_str = self.o_nhap_gia.get().strip()

        if not ten or not so_luong_str or not gia_str:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            so_luong = int(so_luong_str)
            gia_ban = float(gia_str)
            if so_luong < 0 or gia_ban < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng và giá phải là số dương hợp lệ!")
            return

        db.them_san_pham(ten, danh_muc, so_luong, gia_ban)
        self.o_nhap_ten.delete(0, tk.END)
        self.o_nhap_so_luong.delete(0, tk.END)
        self.o_nhap_gia.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", f"Đã thêm sản phẩm: {ten}")

    def xu_ly_thay_doi_sl(self, thay_doi):
        lua_chon = self.listbox_sp.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn 1 sản phẩm trong danh sách!")
            return

        id_sp = self.danh_sach_sp[lua_chon[0]][0]
        thanh_cong, thong_bao = db.cap_nhat_so_luong(id_sp, thay_doi)
        if thanh_cong:
            self.tai_lai_danh_sach()
        else:
            messagebox.showerror("Lỗi", thong_bao)

    def xu_ly_xoa_sp(self):
        lua_chon = self.listbox_sp.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn 1 sản phẩm để xóa!")
            return

        id_sp = self.danh_sach_sp[lua_chon[0]][0]
        db.xoa_san_pham(id_sp)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_ton_kho_theo_danh_muc()
        if not du_lieu:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu tồn kho để thống kê.")
            return

        danh_muc = [dong[0] for dong in du_lieu]
        tong_ton = [dong[1] for dong in du_lieu]

        plt.figure(figsize=(6, 4))
        plt.bar(danh_muc, tong_ton, color="#4CAF50")
        plt.title("TỔNG SỐ LƯỢNG HÀNG TỒN KHO THEO DANH MỤC")
        plt.xlabel("Danh mục")
        plt.ylabel("Số lượng tồn")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungQuanLyKho()
    app.mainloop()