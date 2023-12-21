import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from config import config
from widget import KitCheckBox, KitFramelessWindow

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)

    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    window = KitFramelessWindow()
    main = QWidget()
    main.setLayout(QVBoxLayout())

    check1 = KitCheckBox()
    main.layout().addWidget(check1)
    check2 = KitCheckBox("12345")
    check2.setTristate(True)
    main.layout().addWidget(check2)

    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
