import sys
from PySide6.QtWidgets import (
    QApplication, 
    QWidget,
    QVBoxLayout,
    QLabel
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