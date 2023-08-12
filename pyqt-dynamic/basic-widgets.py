from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

app = QApplication([])

window = QWidget()
window.setWindowTitle("Sample Area")

label = QLabel()
label.setText("<h1>Berkay Gediz</h1> <p>Software Developer</p>")
button = QPushButton("Click")

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()
