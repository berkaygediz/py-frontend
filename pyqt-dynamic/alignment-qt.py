from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Item Alignment")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(layout)

        left_button = QPushButton("Left", self)
        center_button = QPushButton("Center", self)
        right_button = QPushButton("Right", self)

        layout.addWidget(left_button)
        layout.addWidget(center_button)
        layout.addWidget(right_button)

        layout.setAlignment(left_button, Qt.AlignLeft)
        layout.setAlignment(center_button, Qt.AlignHCenter)
        layout.setAlignment(right_button, Qt.AlignRight)

        self.setCentralWidget(self.central_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
