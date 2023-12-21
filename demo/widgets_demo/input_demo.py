from PyQt5.QtGui import QFontDatabase, QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from config import config
from widget import KitLineEdit, KitFramelessWindow

if __name__ == '__main__':
    app = QApplication([])
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
    window = KitFramelessWindow()
    main = QWidget()
    main.resize(800, 600)
    layout = QVBoxLayout()
    line1 = KitLineEdit()
    validator = QIntValidator(1, 10)
    line1.setValidator(validator)
    line1.setToolTip("请输入1-10的数字")
    main.setLayout(layout)
    layout.addWidget(line1)
    window.setCentralWidget(main)
    window.show()
    app.exec_()
