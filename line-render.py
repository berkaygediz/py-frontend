import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DrawingRenderer(QWidget):
    def __init__(self, text, parent=None):
        super(DrawingRenderer, self).__init__(parent)
        self.text = text

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen()
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, 0, self.width(), self.height())
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Line Render")
    renderer = DrawingRenderer("Berkay Gediz")
    renderer.show()
    sys.exit(app.exec_())
