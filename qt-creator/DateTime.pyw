# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tarih.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("DateTime.ui", self)
        self.ui.dateTimeEdit.dateTimeChanged.connect(
            self.on_dateTimeEdit_dateTimeChanged)

    @pyqtSlot(QDateTime)
    def on_dateTimeEdit_dateTimeChanged(self, datetime):
        date = datetime.date()
        time = datetime.time()
        self.ui.label.setText("{}/{}/{} {}:{}" .format(date.day(),
                                                       date.month(), date.year(), time.hour(), time.minute()))


app = QApplication([])
app.setApplicationName("Date/Time Application")
window = MainWindow()
window.show()
app.exec_()