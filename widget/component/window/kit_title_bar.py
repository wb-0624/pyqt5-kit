import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QLabel

from ..button import KitIconButton
from ..icon import KitIcon
from app_config.constant import Button
from app_config.md_icons import MdIcons
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

        self.title_icon = KitIcon(MdIcons.md_star)
        self.title = QLabel('demo')

        self.min_button = KitTitleBarButton(MdIcons.md_minimize)
        self.change_size_button = KitTitleBarButton(MdIcons.md_crop_square)
        self.close_button = KitTitleBarButton(MdIcons.md_close)
        self.close_button.setObjectName("title_bar_close_button")

        self._pos = None

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setFixedHeight(40)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(4, 0, 4, 0)
        self.setLayout(self.layout)

        self.layout.addWidget(self.title_icon)
        self.layout.addWidget(self.title)
        self.layout.addStretch(1)
        self.layout.addWidget(self.min_button)
        self.layout.addWidget(self.change_size_button)
        self.layout.addWidget(self.close_button)

    def __init_slot(self):
        self.min_button.clicked.connect(lambda: self.window().showMinimized())
        self.change_size_button.clicked.connect(lambda: self.__change_size())
        self.close_button.clicked.connect(lambda: self.window().close())

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIcon(self, icon_str):
        self.title_icon.setIcon(icon_str)

    def setTitle(self, title: str):
        self.title.setText(title)

    def __change_size(self):
        if self.window().isMaximized() or self.window().isFullScreen():
            self.window().showNormal()
        else:
            self.window().showMaximized()

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

    def resizeEvent(self, a0) -> None:
        if self.window().isMaximized() or self.window().isFullScreen():
            self.change_size_button.setIcon(MdIcons.md_filter_none)
        else:
            self.change_size_button.setIcon(MdIcons.md_crop_square)
        super().resizeEvent(a0)

    def mouseDoubleClickEvent(self, a0) -> None:
        self.__change_size()

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self.window().isFullScreen() or not self.window().isDraggable():
            return
        if self.window().isMaximized():
            pos_x_radio = self._pos.x()/self.window().window().width()
            self.window().showNormal()
            self.window().move(a0.globalPos().x()-pos_x_radio*self.window().width(), 0)
        if self._pos:
            self.window().move(self.window().pos() + a0.globalPos() - self._pos)
            self._pos = a0.globalPos()
        a0.ignore()

    def enterEvent(self, a0):
        self.setCursor(Qt.ArrowCursor)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self._pos = a0.globalPos()
        super().mousePressEvent(a0)

    # 离开时，如果是最大化状态，就变成normal
    def mouseReleaseEvent(self, a0) -> None:
        if a0.globalPos().y() < 10 and not self.window().isMaximized() and not self.window().isFullScreen():
            self.window().showMaximized()
        self._pos = None
        super().mouseReleaseEvent(a0)



if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    config.init()




    main = KitTitleBar(None)
    main.show()

    sys.exit(app.exec_())
