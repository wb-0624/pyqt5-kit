from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

from widget import KitFramelessWindow, KitProgressBar, KitSpinBox


class ProgressDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        progress_bar = KitProgressBar()
        progress_bar.setValue(40)
        layout.addWidget(progress_bar)

        spin_box = KitSpinBox()
        spin_box.setRange(0, 100)
        spin_box.setValue(40)
        layout.addWidget(spin_box)

        spin_box.textChanged.connect(lambda value: progress_bar.setValue(int(value)))


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
