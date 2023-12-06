import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from widget.component.window.window_body import KitWindowBody
from config import config
from app_config.constant import Position, Window


class KitFramelessWindow(QWidget):

    def __init__(self):
        super(KitFramelessWindow, self).__init__()

        self.window_body = None
        self.title_bar = None
        self.resizeable = True

        self.__drag_resize = None
        self.resize_margin = Window.resize_margin

        self.__init_widget()
        self.__init_slot()

    def __init_widget(self):
        self.setMouseTracking(True)
        self.setContentsMargins(0, 0, 0, 0)

        self.window_body = KitWindowBody()
        self.title_bar = self.window_body.title_bar

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(self.resize_margin, self.resize_margin, self.resize_margin, self.resize_margin)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self.layout.addWidget(self.window_body, stretch=1)

    def __init_slot(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def setContentWidget(self, widget: QWidget):
        self.window_body.setContentWidget(widget)

    def setTitle(self, title):
        self.title_bar.setTitle(title)

    def setTitleBar(self, title_bar):
        self.window_body.setTitleBar(title_bar)

    def setResizeable(self, resizeable:bool):
        self.resizeable = resizeable

    def mouseMoveEvent(self, a0) -> None:
        mouse_pos = a0.pos()
        # 这里的 减2 非常微妙
        # 如果不减，和周围留空的边距刚好一样的话
        # 那么在临界的时候，由于鼠标就到了 body 的组件上，而不是在底层上
        # 就会导致临界值时，反而依然会导致拉伸功能生效。
        # 所以这里 减2 可以使得在底层上，就判断出临界。当然减几都行。
        mouse_resize_margin = self.resize_margin - 2
        if self.isMaximized() or self.isFullScreen():
            return

        if 0 < mouse_pos.x() < mouse_resize_margin and self.resizeable:
            self.setCursor(Qt.SizeHorCursor)
            self.__drag_resize = Position.Left
        elif self.width() - mouse_resize_margin < mouse_pos.x() < self.width() and self.resizeable:
            self.setCursor(Qt.SizeHorCursor)
            self.__drag_resize = Position.Right
        elif 0 < mouse_pos.y() < mouse_resize_margin and self.resizeable:
            self.setCursor(Qt.SizeVerCursor)
            self.__drag_resize = Position.Top
        elif self.height() - mouse_resize_margin < mouse_pos.y() < self.height() and self.resizeable:
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


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    window = KitFramelessWindow()
    window.show()

    sys.exit(app.exec_())
