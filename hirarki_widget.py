import sys
from PySide6.QtWidgets import (
    QApplication, 
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Contoh Hirarki")
        self.resize(400, 300)

        layout = QVBoxLayout()

        label = QLabel("Ini adalah label")
        tombol = QPushButton("Ini adalah tombol")

        layout.addWidget(label)
        layout.addWidget(tombol)

        self.setLayout(layout)

        self.center_on_screen()

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