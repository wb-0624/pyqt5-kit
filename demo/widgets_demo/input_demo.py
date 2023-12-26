from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from config import config
from widget import KitLineEdit, KitFramelessWindow


class InputDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        line1 = KitLineEdit()
        validator = QIntValidator(1, 10)
        line1.setValidator(validator)
        line1.setToolTip("请输入1-10的数字")
        layout.addWidget(line1)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication([])
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = InputDemo()
    window.setCentralWidget(demo)

    window.show()
    app.exec_()
