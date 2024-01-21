import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication

from config import config
from widget import KitSlider, KitFramelessWindow


class SliderDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.slider = KitSlider(Qt.Horizontal)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.slider)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    config.init()



    window = KitFramelessWindow()
    # window = KitWindow()

    demo = SliderDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
