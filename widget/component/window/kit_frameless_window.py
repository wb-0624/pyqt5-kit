import sys

from PyQt5.QtCore import Qt, QSize, QEvent
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QGraphicsDropShadowEffect

from widget.component.button import KitButton
from config import config
from app_config.constant import Position, Window

from widget.component.window.status_bar import KitStatusBar
from widget.component.window.title_bar import KitTitleBar
from app_config.signal_center import signal_center


class KitWindowBody(QWidget):

    def __init__(self, parent=None):
        super(KitWindowBody, self).__init__(parent=parent)

        self.title_bar = KitTitleBar(self)
        self.main_content = QWidget(self)
        self.main_content.setMouseTracking(True)
        self.status_bar = KitStatusBar(self)
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

    def setStatusBar(self, status_bar):
        origin_bar = self.status_bar
        self.layout.removeWidget(origin_bar)
        origin_bar.deleteLater()
        if isinstance(status_bar, QWidget):
            self.layout.insertWidget(0, status_bar)
        self.status_bar = status_bar
        self.update()
class KitFramelessWindow(QMainWindow):

    def __init__(self):
        super(KitFramelessWindow, self).__init__()

        self.window_body = None
        self.title_bar = None
        self.window_status = Window.Normal
        self.resizeable = True
        self.draggable = True

        self.__drag_resize = None
        self.resize_margin = Window.resize_margin

        self.__init_widget()

    def __init_widget(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)
        self.setContentsMargins(self.resize_margin, self.resize_margin, self.resize_margin, self.resize_margin)

        self.window_body = KitWindowBody()
        self.title_bar = self.window_body.title_bar

        self.setWindowBody(self.window_body)

    def setCentralWidget(self, widget: QWidget):
        self.window_body.setCentralWidget(widget)

    def setTitle(self, title):
        self.title_bar.setTitle(title)

    def setTitleBar(self, title_bar):
        self.window_body.setTitleBar(title_bar)

    def setWindowBody(self, window_body):
        self.window_body = window_body
        super().setCentralWidget(window_body)

    def setResizeable(self, resizeable:bool):
        self.resizeable = resizeable

    def isResizeable(self):
        return self.resizeable

    def setDraggable(self, draggable:bool):
        self.draggable = draggable

    def isDraggable(self):
        return self.draggable

    def mouseMoveEvent(self, a0) -> None:
        mouse_pos = a0.pos()
        # 这里的 减2 非常微妙
        # 如果不减，和周围留空的边距刚好一样的话
        # 那么在临界的时候，由于鼠标就到了 body 的组件上，而不是在底层上
        # 就会导致临界值时，反而依然会导致拉伸功能生效。
        # 所以这里 减2 可以使得在底层上，就判断出临界。当然减几都行。
        mouse_resize_margin = self.resize_margin - 2
        if self.isMaximized() or self.isFullScreen() or self.resizeable is False:
            return

        if 0 < mouse_pos.x() < mouse_resize_margin:
            self.setCursor(Qt.SizeHorCursor)
            self.__drag_resize = Position.Left
        elif self.width() - mouse_resize_margin < mouse_pos.x() < self.width():
            self.setCursor(Qt.SizeHorCursor)
            self.__drag_resize = Position.Right
        elif 0 < mouse_pos.y() < mouse_resize_margin:
            self.setCursor(Qt.SizeVerCursor)
            self.__drag_resize = Position.Top
        elif self.height() - mouse_resize_margin < mouse_pos.y() < self.height():
            self.setCursor(Qt.SizeVerCursor)
            self.__drag_resize = Position.Bottom
        else:
            self.setCursor(Qt.ArrowCursor)
            self.__drag_resize = None
        a0.ignore()

    def mousePressEvent(self, a0) -> None:
        if a0.button() == Qt.LeftButton:
            if self.__drag_resize == Position.Left and self.cursor() == Qt.SizeHorCursor:
                self.window().windowHandle().startSystemResize(Qt.LeftEdge)
            elif self.__drag_resize == Position.Right and self.cursor() == Qt.SizeHorCursor:
                self.window().windowHandle().startSystemResize(Qt.RightEdge)
            elif self.__drag_resize == Position.Top and self.cursor() == Qt.SizeVerCursor:
                self.window().windowHandle().startSystemResize(Qt.TopEdge)
            elif self.__drag_resize == Position.Bottom and self.cursor() == Qt.SizeVerCursor:
                self.window().windowHandle().startSystemResize(Qt.BottomEdge)
        else:
            a0.ignore()

    def mouseReleaseEvent(self, a0) -> None:
        if self.__drag_resize is not None:
            self.__drag_resize = None
            self.setCursor(Qt.ArrowCursor)
            a0.accept()
        else:
            a0.ignore()

    def sizeHint(self):
        return QSize(800, 600)

    def showMinimized(self) -> None:
        self.window_status = Window.Minimized
        super().showMinimized()

    def showNormal(self) -> None:
        self.window_status = Window.Normal
        self.setContentsMargins(self.resize_margin, self.resize_margin, self.resize_margin, self.resize_margin)
        self.window_body.setProperty('type', 'normal')
        self.window_body.style().polish(self.window_body)
        super().showNormal()

    def showMaximized(self) -> None:
        self.window_status = Window.Maximized
        self.setContentsMargins(0, 0, 0, 0)
        self.window_body.setProperty('type', 'max')
        self.window_body.style().polish(self.window_body)
        super().showMaximized()

    def showFullScreen(self) -> None:
        self.window_status = Window.FullScreen
        self.setContentsMargins(0, 0, 0, 0)
        self.window_body.setProperty('type', 'max')
        self.window_body.style().polish(self.window_body)
        super().showFullScreen()


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    window = KitFramelessWindow()
    main = QWidget()
    main.setLayout(QVBoxLayout())
    btn = KitButton('full')
    btn.clicked.connect(window.showFullScreen)
    main.layout().addWidget(btn)
    window.setCentralWidget(main)
    window.show()


    sys.exit(app.exec_())
