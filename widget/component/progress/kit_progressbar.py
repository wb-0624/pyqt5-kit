from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt


class KitProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTextVisible(False)

    def setColor(self, color: str):
        self.setStyleSheet(self.styleSheet() + f'KitProgressBar::chunk {{background-color: {color};}}')


if __name__ == "__main__":
    from PyQt5.QtGui import QFontDatabase
    from config import config
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    progress_bar = KitProgressBar(main)
    progress_bar.setValue(40)
    layout.addWidget(progress_bar)

    main.show()
    sys.exit(app.exec_())
