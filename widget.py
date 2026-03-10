import sys
from PySide6.QtWidgets import (
    QApplication, 
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QRadioButton
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

        label = QLabel("Teks yang ditampilkan")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 16px; color: blue;")

        layout.addWidget(label)

        tombol = QPushButton("Klik saya")
        # tombol.clicked.connect()
        tombol.setEnabled(True)

        layout.addWidget(tombol)

        input_text = QLineEdit()
        input_text.setPlaceholderText("Masukkan nama...")
        input_text.setText("Nilai Awal")

        nilai = input_text.text()
        input_text.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(input_text)

        combo = QComboBox()
        combo.addItems(["Pilihan 1", "Pilihan 2", "Pilihan 3"])
        text = combo.currentText()
        index = combo.currentIndex()
        combo.setCurrentIndex(0)

        layout.addWidget(combo)

        checkbox = QCheckBox("Saya setuju")

        if checkbox.isChecked():
            print("Checkbox dicentang")

        checkbox.setChecked(False)

        layout.addWidget(checkbox)

        radio1 = QRadioButton("Opsi A")
        radio2 = QRadioButton("Opsi B")
        radio3 = QRadioButton("Opsi C")

        if radio1.isChecked():
            print("Opsi A dipilih")

        layout.addWidget(radio1)
        layout.addWidget(radio2)
        layout.addWidget(radio3)

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