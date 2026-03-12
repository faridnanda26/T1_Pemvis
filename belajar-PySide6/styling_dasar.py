import sys
from PySide6.QtWidgets import (
    QApplication, 
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_connection()

    def init_ui(self):
        self.setWindowTitle("Aplikasi Lengkap")
        self.resize(600, 450)
        self.setMinimumSize(400, 300)

        layout = QVBoxLayout()

        label = QLabel("Teks Berwarna")
        label.setStyleSheet("color: blue; font-size: 18px")

        tombol = QPushButton("Tombol cantik")
        tombol.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 14px;         
            }
            QPushButton:hover {
                background-color: #2980b9;        
            }
            QPushButton:pressed {
                background-color: #1f618d;        
            }
        """)

        layout.addWidget(label)
        layout.addWidget(tombol)

        self.setLayout(layout)

        self.center_on_screen()

    def setup_connection(self):
        pass

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