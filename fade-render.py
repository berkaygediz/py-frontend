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

        font = QFont("Verdana", 40)
        painter.setFont(font)
        font_metrics = painter.fontMetrics()
        text_width = font_metrics.width(self.text)
        text_height = font_metrics.height()

        self.resize(text_width + 20, text_height + 20)

        gradient = QLinearGradient(0, 0, text_width, 0)
        gradient.setColorAt(0, Qt.white)
        gradient.setColorAt(1, Qt.black)
        brush = QBrush(gradient)

        pen = QPen()
        pen.setBrush(brush)
        painter.setPen(pen)

        painter.drawText(QRect(0, 0, text_width + 20, text_height + 20),
                         Qt.AlignRight | Qt.AlignVCenter, self.text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Fade Render")
    renderer = DrawingRenderer("Berkay Gediz")
    renderer.show()
    sys.exit(app.exec_())
