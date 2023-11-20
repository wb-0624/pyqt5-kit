from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QAbstractAnimation, Qt, QRect
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QGraphicsDropShadowEffect

from widget.component.button import KitButton
from widget.component.overlay.kit_overlay import KitOverlay
from config import config
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


if __name__ == '__main__':
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    top_main = QWidget()
    top_main.setObjectName('top_main')
    top_main.resize(800, 800)
    top_main_layout = QVBoxLayout()
    top_main.setLayout(top_main_layout)

    main = QWidget()
    main.setObjectName('main')
    main.resize(400, 400)
    main_layout = QVBoxLayout()
    main.setLayout(main_layout)

    top_main_layout.addWidget(main)

    drawer_left = KitDrawer(orientation=Position.Left)
    drawer_left.setWidth(600)
    drawer_left.setClosePolicy(ClosePolicy.CloseOnEscape)
    btn = KitButton('left')
    btn.clicked.connect(lambda: drawer_left.open())
    drawer_left.setLayout(QVBoxLayout())
    close_left = KitButton('close')
    close_left.clicked.connect(lambda: drawer_left.close())
    drawer_left.layout().addWidget(close_left)

    drawer_right = KitDrawer(orientation=Position.Right)
    btn2 = KitButton('right')
    btn2.clicked.connect(lambda: drawer_right.open())
    drawer_right.setLayout(QVBoxLayout())
    close_right = KitButton('close')
    close_right.clicked.connect(lambda: drawer_right.close())
    drawer_right.layout().addWidget(close_right)

    drawer_top = KitDrawer(orientation=Position.Top)
    btn3 = KitButton('top')
    btn3.clicked.connect(lambda: drawer_top.open())
    drawer_top.setLayout(QVBoxLayout())
    close_top = KitButton('close')
    close_top.clicked.connect(lambda: drawer_top.close())
    drawer_top.layout().addWidget(close_top)

    drawer_bottom = KitDrawer(orientation=Position.Bottom)
    btn4 = KitButton('bottom')
    btn4.clicked.connect(lambda: drawer_bottom.open())
    drawer_bottom.setLayout(QVBoxLayout())
    close_bottom = KitButton('close')
    close_bottom.clicked.connect(lambda: drawer_bottom.close())
    drawer_bottom.layout().addWidget(close_bottom)

    main_layout.addWidget(btn)
    main_layout.addWidget(btn2)
    main_layout.addWidget(btn3)
    main_layout.addWidget(btn4)

    top_main.show()
    sys.exit(app.exec_())
