import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget

from config import config
from app_config.constant import ClosePolicy
from widget import KitButton, KitOverlay, KitFramelessWindow, KitWindow


class OverlayDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        btn = KitButton('open overlay')
        main_layout.addWidget(btn)
        btn.clicked.connect(lambda: overlay.show())
        overlay = KitOverlay(self.window())
        overlay.setClosePolicy(ClosePolicy.CloseOnClicked)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()



    window = KitFramelessWindow()
    # window = KitWindow()

    demo = OverlayDemo(window)
    window.setCentralWidget(demo)

    window.show()
    sys.exit(app.exec_())
