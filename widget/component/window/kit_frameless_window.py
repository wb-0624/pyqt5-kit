import sys

from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import QFontDatabase, QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QGraphicsDropShadowEffect

from config import config
from app_config.constant import Position, Window
from app_config.signal_center import signal_center

from ..button import KitButton
from .kit_title_bar import KitTitleBar
from .kit_status_bar import KitStatusBar


class KitWindowBody(QWidget):

    def __init__(self, parent=None):
        super(KitWindowBody, self).__init__(parent=parent)

        self.title_bar = KitTitleBar(self)
        self.main_content = QWidget(self)
        self.status_bar = KitStatusBar(self)
        self.layout = QVBoxLayout()

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
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

    def enterEvent(self, a0) -> None:
        self.parent().leaveEvent(a0)

    def leaveEvent(self, a0) -> None:
        self.parent().enterEvent(a0)


class KitFramelessWindow(QMainWindow):

    def __init__(self):
        super(KitFramelessWindow, self).__init__()

        self.window_body = None
        self.title_bar = None

        self.window_status = Window.Normal
        self.resizable = True
        self.draggable = True

        self.__drag_position = None
        self.__resize = None
        self.resize_margin = Window.resize_margin

        self.__init_widget()

    def __init_widget(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
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

    def setStatusBar(self, status_bar) -> None:
        self.window_body.setStatusBar(status_bar)

    def setWindowBody(self, window_body):
        self.window_body = window_body
        super().setCentralWidget(window_body)

    def setResizeable(self, resizeable:bool):
        self.resizable = resizeable

    def isResizable(self):
        return self.resizable

    def windowStatus(self):
        return self.window_status

    def setDraggable(self, draggable: bool):
        self.draggable = draggable

    def isDraggable(self):
        return self.draggable

    # 鼠标边界判断
    def __fresh_mouse_edge(self, pos: QPoint):
        # 这里 +8 实际上是增加了拉伸的判定范围。
        # 否则在边界处难以判定，得稍微离开一点才能判定为拉伸，这里是为了视觉效果体验做出的让步
        mouse_resize_margin = self.resize_margin + 8
        edge = 0
        if not self.isResizable():
            self.__drag_position = None
            return
        if 0 <= pos.x() <= mouse_resize_margin:
            edge |= Position.Left
        elif self.width() - mouse_resize_margin <= pos.x() <= self.width():
            edge |= Position.Right
        if 0 <= pos.y() <= mouse_resize_margin:
            edge |= Position.Top
        elif self.height() - mouse_resize_margin <= pos.y() <= self.height():
            edge |= Position.Bottom
        self.__drag_position = None if edge == 0 else edge

    # 根据边界判断鼠标样式
    def __fresh_mouse_cursor(self):

        if self.__drag_position in (Position.Top, Position.Bottom):
            cursor = Qt.SizeVerCursor
        elif self.__drag_position in (Position.Left, Position.Right):
            cursor = Qt.SizeHorCursor
        elif self.__drag_position in (Position.TopLeft, Position.BottomRight):
            cursor = Qt.SizeFDiagCursor
        elif self.__drag_position in (Position.TopRight, Position.BottomLeft):
            cursor = Qt.SizeBDiagCursor
        else:
            cursor = Qt.ArrowCursor

        self.setCursor(cursor)

    def mouseMoveEvent(self, a0) -> None:
        if self.isMaximized() or self.isFullScreen() or self.resizable is False:
            return

        if self.__drag_position is not None and self.__resize is not None:
            dw = a0.globalPos().x() - self.__resize.x()
            dh = a0.globalPos().y() - self.__resize.y()
            width = self.width()
            height = self.height()
            x = self.x()
            y = self.y()
            if self.__drag_position & Position.Right == Position.Right:
                width += dw
            elif self.__drag_position & Position.Left == Position.Left:
                width -= dw
                x += dw
            if self.__drag_position & Position.Bottom == Position.Bottom:
                height += dh
            elif self.__drag_position & Position.Top == Position.Top:
                height -= dh
                y += dh

            minw = self.minimumWidth()
            minh = self.minimumHeight()
            maxw = self.maximumWidth()
            maxh = self.maximumHeight()

            if width < minw or width > maxw or height < minh or height > maxh:
                return

            self.setGeometry(x, y, width, height)
            self.__resize = a0.globalPos()
        a0.ignore()

    def mousePressEvent(self, a0) -> None:
        if a0.button() == Qt.LeftButton \
                and self.__drag_position is not None \
                and self.__resize is None:
            self.__resize = a0.globalPos()
        else:
            a0.ignore()

    def mouseReleaseEvent(self, a0) -> None:
        self.__resize = None
        self.__drag_position = None
        self.setCursor(Qt.ArrowCursor)

    def enterEvent(self, a0) -> None:
        self.__fresh_mouse_edge(self.mapFromGlobal(QCursor.pos()))
        self.__fresh_mouse_cursor()

    def leaveEvent(self, a0) -> None:
        self.__resize = None
        self.__drag_position = None
        self.setCursor(Qt.ArrowCursor)

    def sizeHint(self):
        return QSize(800, 600)

    def showMinimized(self) -> None:
        self.window_status = Window.Minimized
        super().showMinimized()

    def showNormal(self) -> None:
        self.setContentsMargins(self.resize_margin, self.resize_margin, self.resize_margin, self.resize_margin)
        self.window_status = Window.Normal
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
