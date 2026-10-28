import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        
        # Tự động lấy đường dẫn tuyệt đối tới thư mục chứa file py hiện tại
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "form_dang_nhap.ui")
        
        # Nạp giao diện từ file .ui
        uic.loadUi(ui_path, self)

        # Kết nối sự kiện nút bấm (đã khớp với tên nut_dang_nhap_2 trong giao diện của bạn)
        if hasattr(self, 'nut_dang_nhap_2'):
            self.nut_dang_nhap_2.clicked.connect(self.xu_ly_dang_nhap)
        elif hasattr(self, 'nut_dang_nhap'):
            self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        # Kiểm tra xem tên object của ô nhập là gì để lấy text chính xác
        tai_khoan = ""
        mat_khau = ""
        
        if hasattr(self, 'o_nhap_tai_khoan_2'):
            tai_khoan = self.o_nhap_tai_khoan_2.text()
        elif hasattr(self, 'o_nhap_tai_khoan'):
            tai_khoan = self.o_nhap_tai_khoan.text()
            
        if hasattr(self, 'o_nhap_mat_khau_2'):
            mat_khau = self.o_nhap_mat_khau_2.text()
        elif hasattr(self, 'o_nhap_mat_khau'):
            mat_khau = self.o_nhap_mat_khau.text()

        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Loi", "Vui long nhap du du lieu tai khoan va mat khau.")
            return

        QMessageBox.information(self, "Thanh cong", f"Xin chao {tai_khoan}, dang nhap thanh cong!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec_())