from PyQt5.QtCore import pyqtSignal, Qt, QEvent, QSize, QPropertyAnimation
from PyQt5.QtGui import QPalette, QPainter, QBrush, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsOpacityEffect

from widget.component.button import KitButton
from utils.constant import ClosePolicy


class KitOverlay(QWidget):
    """
    遮罩层
    show() 打开遮罩层，同时置于顶层，如果需要其他组件在最上面，记得调用该组件的raise_()函数
    close() 关闭遮罩层
    setClosePolicy() 设置关闭策略
    """

    clicked = pyqtSignal()
    resized = pyqtSignal(QSize)

    def __init__(self, parent=None):
        super(KitOverlay, self).__init__(parent)

        self._parent = parent
        self._show_animation = None
        self._close_animation = None
        self.close_policy = ClosePolicy.CloseOnEscape

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setMouseTracking(False)
        self.installEventFilter(self)
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.opacity_effect.setOpacity(0)
        self.setGraphicsEffect(self.opacity_effect)
        self.hide()

        self.__init_animation()

    def __init_slot(self):
        self.clicked.connect(lambda: self.close() if self.close_policy == ClosePolicy.CloseOnClicked else None)

    def __init_qss(self):
        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)
        self.setPalette(palette)

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

    def __init_parent(self):
        self.focusWidget()
        # 用于获取当前应用的最上层的组件，可以理解为主窗口
        widget = None
        try:
            widget = QApplication.activeWindow()
        except Exception as e:
            print(e)

        if widget is None:
            widget = self.window()
        if self._parent == widget:
            return
        self._parent = widget
        self.setParent(self._parent)

    def setClosePolicy(self, policy: [ClosePolicy.CloseOnClicked, ClosePolicy.CloseOnEscape]):
        self.close_policy = policy

    def paintEvent(self, event):
        if self._parent is not None:
            self.resize(self._parent.size())
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(0, 0, 0, 127)))
        painter.setPen(QPen(Qt.NoPen))
        painter.end()

    def eventFilter(self, obj, e):
        if e.type() == QEvent.MouseButtonPress:
            self.clicked.emit()
        elif e.type() == QEvent.MouseButtonDblClick:
            return True
        elif e.type() == QEvent.MouseMove and e.buttons() == Qt.LeftButton:
            return True
        return super().eventFilter(obj, e)

    def show(self):
        self.__init_parent()
        self.raise_()
        super().show()
        self._show_animation.start()

    def close(self):
        self._close_animation.start()

    def resizeEvent(self, a0) -> None:
        super().resizeEvent(a0)
        self.resized.emit(self.size())


if __name__ == "__main__":
    from PyQt5.QtWidgets import QWidget, QVBoxLayout
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
    btn = KitButton('open overlay')
    overlay = KitOverlay()
    overlay.setClosePolicy(ClosePolicy.CloseOnClicked)
    layout.addWidget(btn)
    btn.clicked.connect(lambda: [overlay.show(), btn.raise_()])

    main.show()
    sys.exit(app.exec_())