from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key SIGNALS and SLOTS")
        self.setGeometry(200, 200, 300, 200)

        self.label = QLabel("Text", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.label.setText("SPACE key pressed!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
