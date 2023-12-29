import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from config import config
from widget import KitCheckBox, KitFramelessWindow

class CheckBoxDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        check1 = KitCheckBox()
        layout.addWidget(check1)
        check2 = KitCheckBox("12345")
        check2.setTristate(True)
        layout.addWidget(check2)

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()




    window = KitFramelessWindow()
    # window = KitWindow()

    demo = CheckBoxDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
