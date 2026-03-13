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
    QLineEdit,
    QCheckBox, 
    QPushButton
)
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login")
        self.resize(350, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                color: black;
                border: none;        
            }
            QLineEdit {
                border: 1px solid #b8b8b8;
                border-radius: 5px;
                padding: 8px; 
                margin-bottom: 15px;    
            }
            QCheckBox {
                margin-bottom: 15px;              
            }
            QCheckBox::indicator {
                border: 1px solid #b8b8b8; 
                border-radius: 5px;              
            }
            QCheckBox::indicator:checked {
                background-color: #b41daf;
                border: 1px solid #b41daf;
            }
        """)

        layout = QVBoxLayout()

        # LABEL LOGIN
        label = QLabel("LOGIN")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("background-color: #b41daf; color: white; font-size: 20px; padding: 15px; font-weight: bold; border-radius: 8px; margin-bottom: 15px;")
        layout.addWidget(label)

        # INPUT DATA
        label_username = QLabel("Username:")
        self.input_username = QLineEdit()
        label_password = QLabel("Password:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)

        # CHECKBOX
        self.password_visible = QCheckBox("Tampilkan Password")
        self.password_visible.stateChanged.connect(self.checked)
        layout.addWidget(self.password_visible)

        # BUTTON
        container_btn = QWidget()
        layout_container = QHBoxLayout()

        self.login = QPushButton("Login")
        self.login.setStyleSheet("border: none; border-radius: 5px; background-color: #07b61b; color: white; padding: 10px; font-weight: bold;")
        self.login.clicked.connect(self.login_process)

        self.reset = QPushButton("Reset")
        self.reset.setStyleSheet("border: none; border-radius: 5px; background-color: #919191; color: white; padding: 10px; font-weight: bold;")
        self.reset.clicked.connect(self.reset_process)

        layout_container.addWidget(self.login)
        layout_container.addWidget(self.reset)

        container_btn.setLayout(layout_container)

        layout.addWidget(container_btn)

        # KETERANGAN
        self.label_keterangan = QLabel("")
        layout.addWidget(self.label_keterangan)

        layout.addStretch()
        self.setLayout(layout)
        self.center_on_screen()

    def login_process(self):
        username = self.input_username.text()
        password = self.input_password.text()

        if username == "admin" and password == "12345":
            self.label_keterangan.setText("Login berhasil! Selamat datang, admin.")
            self.label_keterangan.setStyleSheet("border-left: 4px solid rgb(10,189,64); border-radius: 5px; background-color: rgb(155,255,153); padding: 15px;")
        else:
            self.label_keterangan.setText("Login gagal! Username atau password salah.")
            self.label_keterangan.setStyleSheet("border-left: 4px solid rgb(255,0,0); border-radius: 5px; background-color: rgb(255,153,153); padding: 15px;")

    def reset_process(self):
        self.input_username.clear()
        self.input_password.clear()
        self.label_keterangan.setText("")
        self.label_keterangan.setStyleSheet("")

    def checked(self):
        if self.password_visible.isChecked():
            self.input_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

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