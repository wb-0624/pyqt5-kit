from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QAbstractAnimation, Qt, QRect
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsDropShadowEffect

from widget.component.overlay.kit_overlay import KitOverlay
from app_config.constant import ClosePolicy, Position


class KitDrawer(QWidget):
    """
    侧边栏抽屉
    """

    def __init__(self, orientation: [Position.Left, Position.Top, Position.Right, Position.Bottom] = Position.Left):
        super(KitDrawer, self).__init__()

        # 内部使用的变量
        self._parent = None
        self._width = 300
        self._height = 300
        self._orientation = orientation
        self.close_policy = ClosePolicy.CloseOnClicked
        self.overlay = KitOverlay()

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
        self.close_policy = policy
        self.overlay.setClosePolicy(policy)

    def __init_widget(self):
        self.hide()
        self.overlay.setClosePolicy(ClosePolicy.CloseOnClicked)


    def __init_slot(self):
        self.overlay.clicked.connect(lambda: self.close() if self.close_policy == ClosePolicy.CloseOnClicked else None)
        self.overlay.resized.connect(lambda: self.__init_size())
        self.overlay.resized.connect(lambda: self.__fresh_position())

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
            self.setFixedSize(self._width, self._parent.height())
        elif self._orientation == Position.Top or self._orientation == Position.Bottom:
            self.setFixedSize(self._parent.width(), self._height)

    def __init_parent(self):
        """
        初始化父类
        """
        window = QApplication.activeWindow()
        if window is not None:
            self._parent = window
            self.setParent(self._parent)
        else:
            self._parent = None

    def __init_position(self):
        """
        初始化位置
        """
        if self._orientation == Position.Left:
            self.move(0 - self._width, 0)
        elif self._orientation == Position.Top:
            self.move(0, 0 - self._height)
        elif self._orientation == Position.Right:
            self.move(self._parent.width(), 0)
        elif self._orientation == Position.Bottom:
            self.move(0, self._parent.height())

    def __fresh_position(self):
        if self.isHidden():
            return
        if self._orientation == Position.Left:
            self.move(0, 0)
        elif self._orientation == Position.Top:
            self.move(0, 0)
        elif self._orientation == Position.Right:
            self.move(self._parent.width() - self._width, 0)
        elif self._orientation == Position.Bottom:
            self.move(0, self._parent.height() - self._height)

    def __init_animation(self):
        """
        初始化动画
        """
        # 滑出动画
        self.__sizeAnimation = None
        if self._orientation == Position.Left:
            self.__sizeAnimation = QPropertyAnimation(self, b"geometry")
            self.__sizeAnimation.setStartValue(QRect(0-self.width(), self.y(), self.width(), self.height()))
            self.__sizeAnimation.setEndValue(QRect(0, self.y(), self.width(), self.height()))
        elif self._orientation == Position.Top:
            self.__sizeAnimation = QPropertyAnimation(self, b"geometry")
            self.__sizeAnimation.setStartValue(QRect(0, 0-self.height(), self.width(), self.height()))
            self.__sizeAnimation.setEndValue(QRect(0, 0, self.width(), self.height()))
        elif self._orientation == Position.Right:
            self.__sizeAnimation = QPropertyAnimation(self, b"geometry")
            self.__sizeAnimation.setStartValue(QRect(self._parent.width(), self.y(), self.width(), self.height()))
            self.__sizeAnimation.setEndValue(QRect(self._parent.width()-self._width, self.y(), self.width(), self.height()))
        elif self._orientation == Position.Bottom:
            self.__sizeAnimation = QPropertyAnimation(self, b"geometry")
            self.__sizeAnimation.setStartValue(QRect(self.x(), self._parent.height(), self.width(), self.height()))
            self.__sizeAnimation.setEndValue(QRect(self.x(), self._parent.height()-self._height, self.width(), self.height()))

        # 动画合集
        self.__animation_group = QParallelAnimationGroup()
        self.__animation_group.addAnimation(self.__sizeAnimation)

    def open(self):
        """
        打开抽屉
        """
        self.__init_parent()
        self.__init_animation()
        self.__animation_group.setDirection(QAbstractAnimation.Forward)
        self.overlay.show()
        self.setHidden(False)
        self.raise_()
        self.__animation_group.start()

    def close(self):
        """
        关闭抽屉
        """
        self.overlay.close()
        self.__animation_group.setDirection(QAbstractAnimation.Backward)
        self.__animation_group.start()
        self.__animation_group.finished.connect(self.hide)


