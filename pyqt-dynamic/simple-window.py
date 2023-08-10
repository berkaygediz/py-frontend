from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Dimensions and Layout")
        self.setGeometry(400, 400, 400, 200)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
