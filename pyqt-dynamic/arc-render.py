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

        start_angle = 90 * 16
        span_angle = 60 * 16
        rect = QRectF(10, 10, 500, 520)
        painter.drawArc(rect, start_angle, span_angle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Arc Render")
    renderer = DrawingRenderer("Berkay Gediz")
    renderer.show()
    sys.exit(app.exec_())
