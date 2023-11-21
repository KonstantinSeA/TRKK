import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import Qt
from PyQt5 import uic
import os


class Fortepiano(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.DoButton.clicked.connect(self.play_do)
        self.ReButton.clicked.connect(self.play_re)
        self.MiButton.clicked.connect(self.play_mi)
        self.FaButton.clicked.connect(self.play_fa)
        self.SolButton.clicked.connect(self.play_sol)
        self.LjaButton.clicked.connect(self.play_lja)
        self.SiButton.clicked.connect(self.play_si)

    def play_do(self):
        os.path.abspath(' file.txt')
        media = QtCore.QUrl.fromLocalFile(os.path.abspath('do.mp3'))
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def play_re(self):
        media = QtCore.QUrl.fromLocalFile(os.path.abspath('re.mp3'))
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def play_mi(self):
        media = QtCore.QUrl.fromLocalFile(os.path.abspath('mi.mp3'))
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def play_fa(self):
        media = QtCore.QUrl.fromLocalFile(os.path.abspath('fa.mp3'))
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def play_sol(self):
        media = QtCore.QUrl.fromLocalFile(os.path.abspath('sol.mp3'))
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def play_lja(self):
        media = QtCore.QUrl.fromLocalFile(os.path.abspath('lja.mp3'))
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def play_si(self):
        media = QtCore.QUrl.fromLocalFile(os.path.abspath('si.mp3'))
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q or event.key() == Qt.Key_1:
            self.play_do()
        if event.key() == Qt.Key_W or event.key() == Qt.Key_2:
            self.play_re()
        if event.key() == Qt.Key_E or event.key() == Qt.Key_3:
            self.play_mi()
        if event.key() == Qt.Key_R or event.key() == Qt.Key_4:
            self.play_fa()
        if event.key() == Qt.Key_T or event.key() == Qt.Key_5:
            self.play_sol()
        if event.key() == Qt.Key_Y or event.key() == Qt.Key_6:
            self.play_lja()
        if event.key() == Qt.Key_U or event.key() == Qt.Key_7:
            self.play_si()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Fortepiano()
    ex.show()
    sys.exit(app.exec())
