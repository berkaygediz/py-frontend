from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Update")
        self.setGeometry(200, 200, 300, 200)

        self.label = QLabel("Hello", self)
        self.label.move(100, 50)

        self.button = QPushButton("Update", self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.update_label)

    def update_label(self):
        self.label.setText("Text Updated!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
