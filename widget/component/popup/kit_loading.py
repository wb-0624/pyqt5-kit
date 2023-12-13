from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication

from ..button import KitButton, KitIconButton
from ..icon import KitIcon
from ..overlay import KitOverlay
from app_config.constant import ClosePolicy, Icons, Button


class KitLoading(KitOverlay):

    def __init__(self, loading_gif: str = 'assets/gif/loading_annular.gif', parent=None):
        super(KitLoading, self).__init__(parent=parent)

        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.loading = QMovie(loading_gif)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setClosePolicy(ClosePolicy.CloseOnClicked)

        self.loading_icon = KitIcon()
        self.loading_icon.setMovie(self.loading)
        self.loading_icon.setFixedSize(60, 60)
        self.loading.setScaledSize(self.loading_icon.size())

        self.close_btn = KitIconButton(Icons.close)
        self.close_btn.setStyle(Button.Text)
        self.close_btn.setShape(Button.Round)
        self.close_btn.setVisible(False)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(16)
        self.layout.addStretch(1)
        self.layout.addWidget(self.loading_icon, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.close_btn, alignment=Qt.AlignHCenter)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def __init_slot(self):
        self.close_btn.clicked.connect(self.close)
        self.timer.timeout.connect(lambda: self.close_btn.setVisible(True))

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def show(self):
        self.loading_icon.raise_()
        self.loading_icon.movie().start()
        self.loading_icon.movie().setSpeed(200)
        self.timer.start()
        super().show()

    def close(self):
        self.loading_icon.movie().stop()
        self.timer.stop()
        super().close()

    @classmethod
    def run(cls, movie_url: str = 'assets/gif/loading_annular.gif'):
        loading = cls(movie_url)
        loading.show()
        return loading


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

    loading = KitLoading()
    btn = KitButton('open loading')
    layout.addWidget(btn)
    btn.clicked.connect(lambda: KitLoading.run())

    main.show()
    sys.exit(app.exec_())
