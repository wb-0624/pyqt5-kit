import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QGraphicsDropShadowEffect

from widget.component.window.title_bar import KitTitleBar
from config import config
from app_config.signal_center import signal_center


class KitWindowBody(QWidget):

    def __init__(self, parent=None):
        super(KitWindowBody, self).__init__(parent=parent)

        self.title_bar = KitTitleBar(self)
        self.main_content = QWidget(self)
        self.main_content.setMouseTracking(True)
        self.status_bar = QWidget(self)
        self.layout = QVBoxLayout()

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setMouseTracking(True)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.setLayout(self.layout)
        self.layout.addWidget(self.title_bar)
        self.layout.addWidget(self.main_content, 1)
        self.layout.addWidget(self.status_bar)

        self.setStatusBar(False)

    def setCentralWidget(self, widget: QWidget):
        self.layout.removeWidget(self.main_content)
        self.main_content.deleteLater()
        widget.setMouseTracking(True)
        self.layout.insertWidget(1, widget, stretch=1)
        self.main_content = widget

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 设置阴影
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(0, 0)
        shadow.setBlurRadius(10)
        shadow.setColor(Qt.gray)
        self.setGraphicsEffect(shadow)

    def resizeEvent(self, a0) -> None:
        if self.title_bar is not None:
            self.title_bar.resizeEvent(a0)
        signal_center.mainWindowResized.emit(self.size())
        super().resizeEvent(a0)

    def setTitleBar(self, bar):
        origin_bar = self.title_bar
        self.layout.removeWidget(origin_bar)
        origin_bar.deleteLater()
        if isinstance(bar, QWidget):
            bar.setMouseTracking(True)
            self.layout.insertWidget(0, bar)
        self.title_bar = bar
        self.update()

    def setStatusBar(self, show: bool):
        self.status_bar.setVisible(show)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    window = KitWindowBody()
    window.show()

    sys.exit(app.exec_())
