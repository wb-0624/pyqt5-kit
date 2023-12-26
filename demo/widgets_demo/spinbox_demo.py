import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase

from config import config
from widget import KitSpinBox, KitDoubleSpinBox, KitFramelessWindow, KitWindow


class SpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        spin = KitSpinBox()
        layout.addWidget(spin)
        double_spin = KitDoubleSpinBox()
        layout.addWidget(double_spin)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = SpinBoxDemo()
    window.setCentralWidget(demo)

    window.show()
    sys.exit(app.exec_())
