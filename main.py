from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QBrush, QPainter, QColor, QPalette
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QWidget, QApplication


class YellowCircle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Окружность')

        palette = QPalette()
        brush = QBrush(QColor(100, 100, 100))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        self.setPalette(palette)

        self.r = randint(10, 100)

        self.show()

    def run(self):
        self.r = randint(10, 200)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        qp.setPen(QColor(255, 255, 0))
        r = self.r
        qp.drawEllipse(200 - r / 2, 200 - r / 2, r, r)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec_())
