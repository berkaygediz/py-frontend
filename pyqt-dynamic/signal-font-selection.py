from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class FontSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super(FontSelectionDialog, self).__init__(parent)
        grid = QGridLayout()
        grid.addWidget(QLabel("Font:"), 0, 0)
        self.font_combo = QComboBox()
        self.font_combo.addItems(("Arial", "Times New Roman", "Verdana"))
        grid.addWidget(self.font_combo, 0, 1)

        select_button = QPushButton("Select")
        cancel_button = QPushButton("Cancel")
        select_button.setDefault(True)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(select_button)
        buttons_layout.addWidget(cancel_button)
        grid.addLayout(buttons_layout, 1, 0, 1, 2)

        select_button.pressed.connect(self.font_selected)
        cancel_button.pressed.connect(self.reject)

        self.setLayout(grid)
        self.setWindowTitle("Font Selection")
        self.setWindowIcon(QIcon("icons/icon.png"))

    def font_selected(self):
        print(self.font_combo.currentText())
        self.accept()


app = QApplication(sys.argv)
font_dialog = FontSelectionDialog()
font_dialog.show()
app.exec_()
