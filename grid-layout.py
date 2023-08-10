from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Window Layout")
        self.setGeometry(200, 200, 400, 300)

        grid_layout = QGridLayout()
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(grid_layout)

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")

        grid_layout.addWidget(button1, 0, 0)
        grid_layout.addWidget(button2, 0, 1)
        grid_layout.addWidget(button3, 1, 0, 1, 2)

        self.setCentralWidget(self.central_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
