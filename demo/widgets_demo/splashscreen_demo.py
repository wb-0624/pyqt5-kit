import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from config import config
from widget import KitSplashScreen, KitMovieIcon, KitProgressBar, KitButton


class SplashScreenDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        icon = KitMovieIcon()
        layout.addWidget(icon, alignment=Qt.AlignHCenter)
        progress = KitProgressBar()
        progress.setValue(0)
        layout.addWidget(progress)
        btn = KitButton('progress add 5')
        btn.clicked.connect(lambda: progress.setValue(progress.value() + 5))
        layout.addWidget(btn)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()



    window = KitSplashScreen()

    demo = SplashScreenDemo()
    window.setCentralWidget(demo)

    window.show()

    sys.exit(app.exec_())
