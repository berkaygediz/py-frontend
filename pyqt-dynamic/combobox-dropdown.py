from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rotating Box and Combo Box")
        self.setGeometry(200, 200, 300, 200)

        combo_box = QComboBox(self)
        combo_box.addItem("Option 1")
        combo_box.addItem("Option 2")
        combo_box.addItem("Option 3")
        combo_box.move(100, 50)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
