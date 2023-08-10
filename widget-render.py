from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Classes")
        self.setGeometry(200, 200, 300, 200)

        self.label = QLabel("Hello", self)
        self.label.move(100, 50)

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
app.exec_()
