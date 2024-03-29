from PyQt5.QtCore import pyqtSignal, Qt, QEvent, QSize, QPropertyAnimation
from PyQt5.QtWidgets import QWidget, QGraphicsOpacityEffect

from app_config.constant import ClosePolicy
from ..window import KitFramelessWindow, KitWindow


class KitOverlay(QWidget):
    """
    遮罩层
    show() 打开遮罩层，同时置于顶层，如果需要其他组件在最上面，记得调用该组件的raise_()函数
    close() 关闭遮罩层
    setClosePolicy() 设置关闭策略
    """

    clicked = pyqtSignal()
    resized = pyqtSignal(QSize)

    def __init__(self, window: KitWindow):

        if isinstance(window, KitFramelessWindow):
            super(KitOverlay, self).__init__(parent=window.windowBody())
        elif isinstance(window, KitWindow):
            super(KitOverlay, self).__init__(parent=window)
        else:
            raise TypeError("window must be KitFramelessWindow or KitWindow")

        self._show_window = window
        self._show_animation = None
        self._close_animation = None
        self.close_policy = ClosePolicy.CloseOnEscape

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.installEventFilter(self)
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.opacity_effect.setOpacity(0)
        # todo 这里使用透明度变化动画时，会导致遮罩位置发生偏移，似乎是和 KitWindowBody 的阴影有关.
        # self.setGraphicsEffect(self.opacity_effect)
        self.hide()

        self.__init_animation()

    def __init_slot(self):
        self.clicked.connect(lambda: self.close() if self.close_policy == ClosePolicy.CloseOnClicked else None)
        self._show_window.windowSizeChanged.connect(lambda: self.__fresh_overlay())

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground)

    def __init_animation(self):
        self._show_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self._show_animation.setDuration(200)
        self._show_animation.setStartValue(0)
        self._show_animation.setEndValue(1)

        self._close_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self._close_animation.setDuration(200)
        self._close_animation.setStartValue(1)
        self._close_animation.setEndValue(0)
        self._close_animation.finished.connect(lambda: self.hide())

    def setClosePolicy(self, policy: [ClosePolicy.CloseOnClicked, ClosePolicy.CloseOnEscape]):
        self.close_policy = policy

    def __fresh_overlay(self):
        window = self.parent()
        self.resize(window.width(), window.height())

    def resizeEvent(self, a0) -> None:
        self.resized.emit(self.size())
        super().resizeEvent(a0)

    def eventFilter(self, obj, e):
        if e.type() == QEvent.MouseButtonPress:
            self.clicked.emit()
        elif e.type() == QEvent.MouseButtonDblClick:
            return True
        elif e.type() == QEvent.MouseMove and e.buttons() == Qt.LeftButton:
            return True
        return super().eventFilter(obj, e)

    def show(self):
        self.__fresh_overlay()
        self.raise_()
        super().show()
        self._show_animation.start()

    def close(self):
        self._close_animation.start()
        super().close()
