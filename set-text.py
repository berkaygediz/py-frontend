from PyQt5.QtWidgets import *
import sys


def changeText():
    global label
    if label.text() != oldLabel:
        label.setText(oldLabel)
    else:
        label.setText("<h1>Text changed</h1>")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Sample Area")

label = QLabel()
label.setText("<h1>Berkay Gediz</h1> <p>Software Developer</p>")
oldLabel = label.text()
button = QPushButton("Click")
button.clicked.connect(changeText)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()
