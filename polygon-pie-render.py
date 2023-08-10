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

        point1 = QPointF(0, 0)
        point2 = QPointF(100, 100)
        point3 = QPointF(200, 10)
        point4 = QPointF(300, 100)
        point5 = QPointF(400, 0)
        point6 = QPointF(500, 100)

        polygon = QPolygonF([point1, point2, point3, point4, point5, point6])
        painter.drawPolygon(polygon)

        pie_rect = QRectF(250, 250, 300, 300)
        start_angle = 30 * 16
        span_angle = 90 * 16

        painter.drawPie(pie_rect, start_angle, span_angle)

        image = QImage("icons/my_icon.png")
        scaled_image = image.scaled(150, 150, Qt.KeepAspectRatio)
        painter.drawImage(0, 200, scaled_image)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Polygon and Pie Render")
    renderer = DrawingRenderer("Berkay Gediz")
    renderer.show()
    sys.exit(app.exec_())
