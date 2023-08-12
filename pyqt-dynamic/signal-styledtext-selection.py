from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class FontSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super(FontSelectionDialog, self).__init__(parent)
        self.font = QFont("Arial", 10)
        self.text = "<font color='red' size='5'>Hello</font> <font color='blue' size='5'>World</font>"
        self.label = QLabel(self.text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        font_button = QPushButton("Select Font")
        font_button.pressed.connect(self.select_font)
        layout.addWidget(font_button)
        self.setLayout(layout)
        self.setWindowTitle("Styled Text Dialog")
        self.setWindowIcon(QIcon("icons/icon.png"))

    def select_font(self):
        font, ok = QFontDialog.getFont(self.font, self, "Select Font")
        if ok:
            self.font = font
            self.label.setFont(self.font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_dialog = FontSelectionDialog()
    main_dialog.show()
    sys.exit(app.exec_())
