"""
Nama: Farid Nanda Syauqi
NIM: F1D02310050
Kelas: C
"""

import sys
from PySide6.QtWidgets import (
    QApplication, 
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox
)
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(400, 600)
        self.setStyleSheet("""
            QWidget {
                color: black;
                background-color: white;
                border: none;               
            }
            QLineEdit {
                background-color: #ebebeb;   
                border: 1px solid black;
                border-radius: 5px;
                padding: 8px;
            }
            QComboBox {
                background-color: #ebebeb;   
                border: 1px solid black;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton {
                background-color: #ebebeb;   
                border: 1px solid black;
                border-radius: 5px;
                padding: 10px;   
            }
        """)

        layout = QVBoxLayout()

        # INPUT DATA
        label_nama = QLabel("Nama Lengkap:")
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan Nama")

        label_nim = QLabel("NIM:")
        label_nim.setStyleSheet("margin-top: 5px;")
        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")

        label_kelas = QLabel("Kelas:")
        label_kelas.setStyleSheet("margin-top: 5px;")
        self.input_kelas = QLineEdit()
        self.input_kelas.setPlaceholderText("Contoh: TI-2A")

        label_kelamin = QLabel("Jenis Kelamin:")
        label_kelamin.setStyleSheet("margin-top: 5px;")
        self.input_kelamin = QComboBox()
        self.input_kelamin.addItems(["Laki-laki", "Perempuan"])

        layout.addWidget(label_nama)
        layout.addWidget(self.input_nama)
        layout.addWidget(label_nim)
        layout.addWidget(self.input_nim)
        layout.addWidget(label_kelas)
        layout.addWidget(self.input_kelas)
        layout.addWidget(label_kelamin)
        layout.addWidget(self.input_kelamin)

        # BUTTON
        widget_btn = QWidget()
        layout_btn = QHBoxLayout()

        btn_tampilkan = QPushButton("Tampilkan")
        btn_tampilkan.setStyleSheet("width: 70px; color: white; background-color: #43a4fe; border: none")
        btn_reset = QPushButton("Reset")
        btn_reset.setStyleSheet("width: 50px; color: white; background-color: #b0b0b0; border: none")

        btn_tampilkan.clicked.connect(self.tampilkan_data)
        btn_reset.clicked.connect(self.reset_data)

        layout_btn.addWidget(btn_tampilkan)
        layout_btn.addWidget(btn_reset)

        layout_btn.addStretch()
        widget_btn.setLayout(layout_btn)

        layout.addWidget(widget_btn)

        # TAMPILKAN DATA
        self.widget_data = QWidget()
        self.widget_data.setStyleSheet("border-left: 4px solid #8f8f8f; border-radius: 5px; background-color: #ebebeb")
        layout_data = QVBoxLayout()

        self.data_nama = QLabel()
        self.data_nama.setStyleSheet("border: none;")

        self.data_nim = QLabel()
        self.data_nim.setStyleSheet("border: none;")

        self.data_kelas = QLabel()
        self.data_kelas.setStyleSheet("border: none;")

        self.data_kelamin = QLabel()
        self.data_kelamin.setStyleSheet("border: none;")

        layout_data.addWidget(self.data_nama)
        layout_data.addWidget(self.data_nim)
        layout_data.addWidget(self.data_kelas)
        layout_data.addWidget(self.data_kelamin)

        layout_data.addStretch()
        self.widget_data.setLayout(layout_data)

        layout.addWidget(self.widget_data)

        layout.addStretch()
        self.setLayout(layout)
        self.center_on_screen()

    def tampilkan_data(self):
        self.widget_data.setStyleSheet("border-left: 4px solid #0a8f00; border-radius: 5px; background-color: #cbffc7")

        nama = self.input_nama.text()
        nim = self.input_nim.text()
        kelas = self.input_kelas.text()
        kelamin = self.input_kelamin.currentText()

        self.data_nama.setText(f"Nama: {nama}")
        self.data_nim.setText(f"NIM: {nim}")
        self.data_kelas.setText(f"Kelas: {kelas}")
        self.data_kelamin.setText(f"Kelamin: {kelamin}")

    def reset_data(self):
        self.widget_data.setStyleSheet("border-left: 4px solid #8f8f8f; border-radius: 5px; background-color: #ebebeb")
        
        self.data_nama.setText("")
        self.data_nim.setText("")
        self.data_kelas.setText("")
        self.data_kelamin.setText("")

        self.input_nama.clear()
        self.input_nim.clear()
        self.input_kelas.clear()
        self.input_kelamin.setCurrentIndex(0)

    def update_style(self):
        self.setStyleSheet

    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()