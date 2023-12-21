import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from config import config
from widget import KitFramelessWindow, KitImage

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    w = KitFramelessWindow()
    main = QWidget()
    main.setLayout(QVBoxLayout())
    window = KitImage()
    window.setImage("assets/img/radio_button_checked.svg", KitImage.Fit)
    main.layout().addWidget(window)
    window2 = KitImage()
    window2.setImage("assets/img/radio_button_checked.svg", KitImage.Fit)
    window2.setFixedHeight(100)
    main.layout().addWidget(window2)
    window3 = KitImage()
    window3.setImage("assets/img/radio_button_checked.svg", KitImage.Fill)
    main.layout().addWidget(window3)
    w.setCentralWidget(main)
    w.show()
    sys.exit(app.exec_())
