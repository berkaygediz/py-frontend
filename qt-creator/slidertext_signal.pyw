import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from slidertext_signal import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.changeLabel)
        self.horizontalSlider.valueChanged.connect(self.label.setNum)

    def changeLabel(self):
        self.label.setText("Merhaba Dünyam!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
