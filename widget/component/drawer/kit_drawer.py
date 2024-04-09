from typing import Union
from PyQt5.QtCore import QPropertyAnimation, Qt, QRect
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect

from app_config.constant import ClosePolicy, Position

from ..window import KitFramelessWindow, KitWindow
from ..overlay import KitOverlay


class KitDrawer(QWidget):
    """
    侧边栏抽屉
    """

    def __init__(self, window: Union[KitFramelessWindow, KitWindow], orientation: Position = Position.Left):
        if isinstance(window, KitFramelessWindow):
            super(KitDrawer, self).__init__(parent=window.windowBody())
        elif isinstance(window, KitWindow):
            super(KitDrawer, self).__init__(parent=window)
        else:
            raise TypeError("window must be KitFramelessWindow or KitWindow")

        # 内部使用的变量
        self._width = 300
        self._height = 300
        self._orientation = orientation
        self._close_policy = ClosePolicy.CloseOnClicked

        self._show_window = window
        self.__show_animation = QPropertyAnimation(self, b"geometry", self)
        self.__close_animation = QPropertyAnimation(self, b"geometry", self)
        self.__close_animation.finished.connect(lambda: self.hide())

        self.overlay = KitOverlay(window)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def setWidth(self, width):
        if self._orientation == Position.Left or self._orientation == Position.Right:
            self._width = width

    def setHeight(self, height):
        if self._orientation == Position.Top or self._orientation == Position.Bottom:
            self._height = height

    def setClosePolicy(self, policy: int):
        self._close_policy = policy
        self.overlay.setClosePolicy(policy)

    def closePolicy(self):
        return self._close_policy

    def __init_widget(self):
        self.hide()
        self.overlay.setClosePolicy(ClosePolicy.CloseOnClicked)

    def __init_slot(self):
        self.overlay.clicked.connect(lambda: self.close() if self._close_policy == ClosePolicy.CloseOnClicked else None)
        self._show_window.windowSizeChanged.connect(lambda: self.__init_size())
        self._show_window.windowSizeChanged.connect(lambda: self.__fresh_position())

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 0)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 200))
        self.setGraphicsEffect(shadow)

    def __init_size(self):
        """
        初始化大小
        """
        if self._orientation == Position.Left or self._orientation == Position.Right:
            self.setFixedSize(self._width, self.parent().height())
        elif self._orientation == Position.Top or self._orientation == Position.Bottom:
            self.setFixedSize(self.parent().width(), self._height)

    def __init_position(self):
        """
        初始化位置
        """
        if self._orientation == Position.Left:
            self.move(0 - self._width, 0)
        elif self._orientation == Position.Top:
            self.move(0, 0 - self._height)
        elif self._orientation == Position.Right:
            self.move(self.parent().width(), 0)
        elif self._orientation == Position.Bottom:
            self.move(0, self.parent().height())

    def __fresh_position(self):
        if self.isHidden():
            return
        if self._orientation == Position.Left:
            self.move(0, 0)
        elif self._orientation == Position.Top:
            self.move(0, 0)
        elif self._orientation == Position.Right:
            self.move(self.parent().width() - self._width, 0)
        elif self._orientation == Position.Bottom:
            self.move(0, self.parent().height() - self._height)

    def __init_animation(self):
        """
        初始化动画
        """
        # 滑出动画

        start_value = None
        end_value = None

        if self._orientation == Position.Left:
            start_value = QRect(0 - self._width, 0, self._width, self._height)
            end_value = QRect(0, 0, self._width, self._height)
        elif self._orientation == Position.Top:
            start_value = QRect(0, 0 - self._height, self._width, self._height)
            end_value = QRect(0, 0, self._width, self._height)
        elif self._orientation == Position.Right:
            start_value = QRect(self.parent().width(), 0, self._width, self._height)
            end_value = QRect(self.parent().width() - self._width, 0, self._width, self._height)
        elif self._orientation == Position.Bottom:
            start_value = QRect(0, self.parent().height(), self._width, self._height)
            end_value = QRect(0, self.parent().height() - self._height, self._width, self._height)
        self.__show_animation.setStartValue(start_value)
        self.__show_animation.setEndValue(end_value)
        self.__show_animation.setDuration(200)
        self.__close_animation.setStartValue(end_value)
        self.__close_animation.setEndValue(start_value)
        self.__close_animation.setDuration(200)

    def open(self):
        """
        打开抽屉
        """
        self.__init_size()
        self.__init_position()
        self.__init_animation()
        self.overlay.show()
        self.setHidden(False)
        self.__show_animation.start()
        self.raise_()

    def close(self):
        """
        关闭抽屉
        """
        self.overlay.close()
        self.__close_animation.start()


