import sys

from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QRect, QEvent
from PyQt5.QtGui import QFontDatabase, QMouseEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QLabel

from widget.component.button.kit_button import KitIconButton
from app_config.constant import Button, Icons
from widget.component.icon.kit_icon import KitIcon
from config import config


class KitTitleBarButton(KitIconButton):

    def __init__(self, icon_str=None, parent=None):
        super(KitTitleBarButton, self).__init__(icon=icon_str, parent=parent)
        self.setObjectName("title_bar_button")
        self.setShape(Button.Round)
        self.setStyle(Button.Text)


class KitTitleBar(QWidget):
    """
    提供最小化，最大/正常，关闭三个默认按钮功能。
    """

    def __init__(self, parent):
        super(KitTitleBar, self).__init__(parent=parent)

        self.title_icon = KitIcon(Icons.star)
        self.title = QLabel('demo')

        self.min_button = KitTitleBarButton(Icons.minimize)
        self.change_size_button = KitTitleBarButton(Icons.crop_square)
        self.close_button = KitTitleBarButton(Icons.close)
        self.close_button.setObjectName("title_bar_close_button")

        self._handler_show = False

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(4, 0, 4, 0)
        self.setLayout(self.layout)

        self.layout.addWidget(self.title_icon)
        self.layout.addWidget(self.title)
        self.layout.addStretch(1)
        self.layout.addWidget(self.min_button)
        self.layout.addWidget(self.change_size_button)
        self.layout.addWidget(self.close_button)

        # 标题栏操作手柄
        self.handler = QWidget(self)
        self.handler_top_margin = 4
        self.handler.setObjectName('title_bar_handler')
        self.handler.setFixedSize(100, 4)
        self.handler.move((self.width() - self.handler.width()) // 2, -self.handler.height())

        self._animation = QPropertyAnimation(self.handler, b"geometry", self)
        self._animation.setStartValue(QRect(self.handler.x(), -self.handler.height(), self.handler.width(), self.handler.height()))
        self._animation.setEndValue(QRect(self.handler.x(), self.handler_top_margin, self.handler.width(), self.handler.height()))
        self._animation.setDuration(200)

    def __init_slot(self):
        self.min_button.clicked.connect(lambda: self.__show_min())
        self.change_size_button.clicked.connect(lambda: self.__change_size())
        self.close_button.clicked.connect(lambda: self.__show_close())

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIcon(self, icon_str):
        self.title_icon.setIcon(icon_str)

    def setTitle(self, title: str):
        self.title.setText(title)

    def __show_min(self):
        self.window().showMinimized()
        self.window().update()

    def __show_max(self):
        self.change_size_button.setIcon(Icons.filter_none)
        self.window().layout.setContentsMargins(0, 0, 0, 0)
        self.parent().setProperty('type', 'max')
        self.window().showMaximized()
        self.parent().style().polish(self.parent())
        self.window().update()

    def __show_normal(self):
        self.change_size_button.setIcon(Icons.crop_square)
        self.window().layout.setContentsMargins(self.window().resize_margin, self.window().resize_margin,
                                                self.window().resize_margin, self.window().resize_margin)
        self.parent().setProperty('type', 'normal')
        self.window().showNormal()
        self.parent().style().polish(self.parent())
        self.window().update()

    def __show_full(self):
        self.window().showFullScreen()
        self.window().update()

    def __change_size(self):
        if self.window().isMaximized():
            self.__show_normal()
        else:
            self.__show_max()

    def __show_close(self):
        self.window().close()

    def addButton(self, add_button: KitTitleBarButton, add_index=3):
        """
        默认添加在按钮布局的最前面
        :param add_button: 标题按钮类
        :param add_index: 添加的位置索引 前面是icon title stretch
        :return:
        """
        self.layout.insertWidget(add_index, add_button)
        self.update()

    def removeButton(self, icon_btn: KitTitleBarButton):
        self.layout.removeWidget(icon_btn)
        icon_btn.deleteLater()
        self.update()

    def sizeHint(self):
        return QSize(800, 40)

    def mouseDoubleClickEvent(self, a0) -> None:
        self.__change_size()

    def paintEvent(self, a0) -> None:
        self.handler.move((self.width() - self.handler.width()) // 2, self.handler.y())

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        # 脱离边缘，变成normal大小的功能是startSystemMove() 里自带的
        # 所以对标题栏的状态变化要这里单独变化一次
        if self.window().isMaximized():
            self.__show_normal()
        self.window().windowHandle().startSystemMove()
        a0.ignore()

    def enterEvent(self, a0):
        self.setCursor(Qt.ArrowCursor)
        if not self._handler_show:
            self._handler_show = True
            self._animation.setDirection(QPropertyAnimation.Forward)
            self._animation.start()
            a0.accept()
        else:
            a0.ignore()

    # 贴靠顶部最大化
    # 离开最小化，内置的 startSystemMove() 已经实现了。
    def mouseReleaseEvent(self, a0) -> None:
        if a0.globalPos().y() < 10 and not self.window().isMaximized() and not self.window().isFullScreen():
            self.__show_max()

    def leaveEvent(self, a0: QEvent) -> None:
        self._handler_show = False
        self._animation.setDirection(QPropertyAnimation.Backward)
        self._animation.start()


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)

    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    main = KitTitleBar(None)
    main.show()

    sys.exit(app.exec_())
