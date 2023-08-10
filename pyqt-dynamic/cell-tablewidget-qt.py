from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget & Cells")
        self.setGeometry(200, 200, 400, 300)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(50, 50, 300, 200)

        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(5)

        self.table_widget.setItem(0, 0, QTableWidgetItem("A1"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("B1"))
        self.table_widget.setItem(0, 2, QTableWidgetItem("C1"))

        self.table_widget.setItem(1, 0, QTableWidgetItem("A2"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("B2"))
        self.table_widget.setItem(1, 2, QTableWidgetItem("C2"))

        self.table_widget.setHorizontalHeaderLabels(
            ["Column 1", "Column 2", "Column 3"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
