import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication

from config import config
from widget import KitSlider, KitFramelessWindow


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 150)
        self.setStyleSheet("Demo{background: rgb(184, 106, 106)}")

        self.slider = KitSlider(Qt.Horizontal)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.slider)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)

    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
    window = KitFramelessWindow()
    demo = Demo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
