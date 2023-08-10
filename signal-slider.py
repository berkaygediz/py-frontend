from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class SliderProperties(QDialog):
    def __init__(self, parent=None):
        super(SliderProperties, self).__init__(parent)

        grid = QGridLayout()
        scrollbar = QScrollBar()
        scrollbar.setRange(0, 25)
        scrollbar.setOrientation(Qt.Horizontal)
        grid.addWidget(scrollbar, 0, 0)

        value_box = QSpinBox()
        value_box.setRange(0, 25)
        grid.addWidget(value_box, 1, 0)

        scrollbar.valueChanged.connect(value_box.setValue)
        value_box.valueChanged.connect(scrollbar.setValue)

        self.setLayout(grid)
        self.setWindowTitle("Slider Properties")
        self.setGeometry(300, 300, 300, 150)


app = QApplication(sys.argv)
window = SliderProperties()
window.show()
app.exec_()
