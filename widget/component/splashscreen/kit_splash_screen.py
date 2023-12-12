from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication

from widget.component.button import KitButton
from widget.component.icon.kit_movie_icon import KitMovieIcon
from widget.component.progress.kit_progressbar import KitProgressBar
from widget.component.window.kit_frameless_window import KitFramelessWindow


class KitSplashScreen(KitFramelessWindow):

    def __init__(self):
        super(KitSplashScreen, self).__init__()

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setTitleBar(None)
        self.setStatusBar(None)
        self.setResizeable(False)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def sizeHint(self):
        return QSize(500, 300)


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

    window = KitSplashScreen()
    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    icon = KitMovieIcon()
    layout.addWidget(icon, alignment=Qt.AlignHCenter)
    progress = KitProgressBar()
    progress.setValue(0)
    layout.addWidget(progress)
    btn = KitButton('progress add 1')
    btn.clicked.connect(lambda: progress.setValue(progress.value()+5))
    layout.addWidget(btn)

    window.setCentralWidget(main)
    window.show()

    sys.exit(app.exec_())