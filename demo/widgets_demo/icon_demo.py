import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget

from app_config.constant import Icons
from config import config
from widget import KitIcon, KitFramelessWindow, KitMovieIcon


class IconDemo(QWidget):
    def __init__(self):
        super().__init__()

        icon = KitIcon(Icons.md_add, self)
        icon.setText(Icons.md_home)
        icon.move(100, 100)

        move_icon = KitMovieIcon(parent=self)
        move_icon.move(10,10)


if __name__ == "__main__":

    # 适应分辨率
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = IconDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
