import sqlite3

TEN_FILE_CSDL = "kho_hang.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_nhu_cau_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    # Bảng sản phẩm
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS san_pham (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_sp TEXT NOT NULL,
            danh_muc TEXT NOT NULL,
            so_luong INTEGER NOT NULL DEFAULT 0,
            gia_ban REAL NOT NULL DEFAULT 0
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_san_pham(ten_sp, danh_muc, so_luong, gia_ban):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO san_pham (ten_sp, danh_muc, so_luong, gia_ban) VALUES (?, ?, ?, ?)",
        (ten_sp, danh_muc, so_luong, gia_ban)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_danh_sach_san_pham():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ten_sp, danh_muc, so_luong, gia_ban FROM san_pham ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def cap_nhat_so_luong(id_sp, so_luong_thay_doi):
    """Thay đổi số lượng (dương là nhập thêm, âm là xuất hàng)"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    
    # Kiểm tra số lượng hiện tại
    con_tro.execute("SELECT so_luong FROM san_pham WHERE id = ?", (id_sp,))
    ket_qua = con_tro.fetchone()
    if ket_qua:
        so_luong_moi = ket_qua[0] + so_luong_thay_doi
        if so_luong_moi < 0:
            ket_noi.close()
            return False, "Số lượng tồn kho không đủ để xuất!"
        
        con_tro.execute("UPDATE san_pham SET so_luong = ? WHERE id = ?", (so_luong_moi, id_sp))
        ket_noi.commit()
        ket_noi.close()
        return True, "Cập nhật thành công!"
    
    ket_noi.close()
    return False, "Không tìm thấy sản phẩm!"

def xoa_san_pham(id_sp):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM san_pham WHERE id = ?", (id_sp,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_ton_kho_theo_danh_muc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT danh_muc, SUM(so_luong) FROM san_pham GROUP BY danh_muc")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua