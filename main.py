from random import randint
from PyQt5.QtGui import QBrush, QPainter, QColor, QPalette, QFont
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(10, 10, 381, 51))
        font = QFont()
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Построить окружность"))


class YellowCircle(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Окружность')

        palette = QPalette()
        brush = QBrush(QColor(100, 100, 100))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        self.setPalette(palette)

        self.r = randint(10, 100)
        self.color1 = randint(0, 255)
        self.color2 = randint(0, 255)
        self.color3 = randint(0, 255)

        self.show()

    def run(self):
        self.r = randint(10, 100)
        self.color1 = randint(0, 255)
        self.color2 = randint(0, 255)
        self.color3 = randint(0, 255)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        qp.setPen(QColor(self.color1, self.color2, self.color3))
        r = self.r
        qp.drawEllipse(200 - r / 2, 200 - r / 2, r, r)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec_())
