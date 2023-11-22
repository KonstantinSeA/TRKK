import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic

import random

from UI import Ui_Circle_Factory


class CircleFactoryForm(QWidget, Ui_Circle_Factory):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ImButton.clicked.connect(self.run_imbutton)
        self.coords = []

    def run_imbutton(self):
        size = random.randint(10, 100)
        self.coords.append((random.randint(0, 500), random.randint(0, 500), size, size,
                            random.randint(0, 255), random.randint(0, 255),
                            random.randint(0, 255)))
        self.update()

    def paintEvent(self, event):
        for c in self.coords:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(c[4], c[5], c[6]))
            qp.drawEllipse(c[0], c[1], c[2], c[3])
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleFactoryForm()
    ex.show()
    exit(app.exec())
