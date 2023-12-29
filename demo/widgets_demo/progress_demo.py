from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from widget import KitFramelessWindow, KitProgressBar


class ProgressDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        progress_bar = KitProgressBar()
        progress_bar.setValue(40)
        layout.addWidget(progress_bar)


if __name__ == "__main__":

    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()



    window = KitFramelessWindow()
    # window = KitWindow()

    demo = ProgressDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
