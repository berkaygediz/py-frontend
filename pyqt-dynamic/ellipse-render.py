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
        pen.setColor(Qt.black)
        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(QColor("#343538"))
        pen.setBrush(brush)
        painter.setPen(pen)
        painter.drawEllipse(20, 20, 420, 420)
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Ellipse Renderer")
    renderer = DrawingRenderer("Berkay Gediz")
    renderer.show()
    sys.exit(app.exec_())
