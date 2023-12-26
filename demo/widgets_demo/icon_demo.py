import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget

from app_config.constant import Icons
from config import config
from widget import KitIcon, KitFramelessWindow, KitMovieIcon

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
    main = QWidget()

    icon = KitIcon(Icons.md_add, main)
    icon.setText(Icons.md_home)

    icon_movie = KitMovieIcon(parent=main)
    icon_movie.move(100, 100)

    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
