import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from config import config
from widget import KitSplashScreen, KitMovieIcon, KitProgressBar, KitButton

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    window = KitSplashScreen()
    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    icon = KitMovieIcon()
    layout.addWidget(icon, alignment=Qt.AlignHCenter)
    progress = KitProgressBar()
    progress.setValue(0)
    layout.addWidget(progress)
    btn = KitButton('progress add 1')
    btn.clicked.connect(lambda: progress.setValue(progress.value() + 5))
    layout.addWidget(btn)

    window.setCentralWidget(main)
    window.show()

    sys.exit(app.exec_())
