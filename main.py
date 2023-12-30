import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication

from config import config
from demo.pages.index import Index
from widget import KitFramelessWindow


def main():
    # 适应分辨率
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()

    window = KitFramelessWindow()
    window.resize(800, 600)
    window.setCentralWidget(Index())

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

