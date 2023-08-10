import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])

QMessageBox.information(None, "Information", "This is an information message.")
QMessageBox.warning(None, "Warning", "This is a warning message.")
QMessageBox.critical(None, "Error", "This is an error message.")
text, ok = QInputDialog.getText(None, "Text Input", "Enter some text:")

if ok:
    print("Entered text:", text)

number, ok = QInputDialog.getInt(None, "Number Input", "Enter a number:")

if ok:
    print("Entered number:", number)

error_dialog = QErrorMessage()

try:
    result = 10 / 0
except Exception as e:
    error_dialog.showMessage("Error: " + str(e))

color = QColorDialog.getColor()

if color.isValid():
    print("Selected color:", color.name())

app.exec_()
