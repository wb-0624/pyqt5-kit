from PyQt5.QtCore import Qt, QSize, QTimer, QPropertyAnimation
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QLabel, QVBoxLayout, QHBoxLayout, QApplication, QWidget

from ..button.kit_button import KitButton
from ..icon.kit_icon import KitIcon
from ..popup.kit_popup import KitPopup
from app_config.constant import Position, Icons


class KitMessage(KitPopup):
    """
    消息提示框
    @param position: 位置
    @param close_time: 自动关闭时间毫秒, -1 为不关闭
    """

    def __init__(self, position=Position.BottomRight, close_time=3000):
        super(KitMessage, self).__init__()

        self.offset = 20
        self.position = position
        self.close_timer = QTimer(self)
        self.close_time = close_time

        self._animation = None

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.__init_animation()

    def __init_slot(self):
        self.close_timer.timeout.connect(lambda: self.close())

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def __init_close_timer(self):
        if self.close_time > 0:
            self.close_timer.start(self.close_time)

    def __init_animation(self):
        self._animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self._animation.setDuration(300)
        self._animation.setStartValue(0)
        self._animation.setEndValue(1)

    def __init_parent(self):
        self.focusWidget()
        # 用于获取当前应用的最上层的组件，可以理解为主窗口
        widget = QApplication.activeWindow()
        if widget is None:
            widget = self.window()
        if self._parent == widget:
            return
        self._parent = widget
        self.setParent(self._parent)

    def sizeHint(self):
        return QSize(100, 40)

    def setOffset(self, offset: int):
        self.offset = offset

    def show(self):
        self.__init_parent()
        self.__init_close_timer()
        self._animation.setDirection(QPropertyAnimation.Forward)
        self._animation.start()
        super().show()

    def close(self):
        self.close_timer.stop()
        self._animation.setDirection(QPropertyAnimation.Backward)
        self._animation.finished.connect(super().close)
        self._animation.start()

    @classmethod
    def make(cls, icon, title, position=Position.BottomRight, close_time=3000, style_type="info"):
        msg = cls(position, close_time)
        msg.icon = icon
        msg.title = title

        msg_icon = KitIcon(icon)
        msg_icon.setObjectName("message_icon")
        msg_icon.setFixedSize(QSize(24, 24))
        msg_title = QLabel(title)
        msg_title.setFixedHeight(msg_icon.height())
        msg_title.setAlignment(Qt.AlignVCenter)
        msg_title.setObjectName("message_title")

        msg_layout = QVBoxLayout()
        msg_layout.setContentsMargins(8, 8, 8, 8)
        msg.setLayout(msg_layout)

        msg_header_layout = QHBoxLayout()
        msg_header_layout.setSpacing(4)
        msg_header_layout.addWidget(msg_icon)
        msg_header_layout.addWidget(msg_title)

        msg_layout.addLayout(msg_header_layout)

        msg.setProperty("type", style_type)
        msg.style().polish(msg)
        msg.adjustSize()
        msg.show()
        return msg

    @classmethod
    def info(cls, title, position=Position.BottomRight, close_time=3000):
        msg_info = cls.make(Icons.info, title, position, close_time, "info")
        return msg_info

    @classmethod
    def success(cls, title, position=Position.BottomRight, close_time=3000):
        msg_success = cls.make(Icons.check_circle, title, position, close_time, "success")
        return msg_success

    @classmethod
    def warning(cls, title, position=Position.BottomRight, close_time=3000):
        msg_warning = cls.make(Icons.error, title, position, close_time, "warning")
        return msg_warning

    @classmethod
    def error(cls, title, position=Position.BottomRight, close_time=3000):
        msg_error = cls.make(Icons.cancel, title, position, close_time, "danger")
        return msg_error


if __name__ == "__main__":
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

    btn2 = KitButton("showInfo")
    layout.addWidget(btn2)
    btn2.clicked.connect(lambda: KitMessage.info("info", Position.Top))

    btn3 = KitButton("showSuccess")
    layout.addWidget(btn3)
    btn3.clicked.connect(lambda: KitMessage.success("success", Position.Left))

    btn4 = KitButton("showWarning")
    layout.addWidget(btn4)
    btn4.clicked.connect(lambda: KitMessage.warning("warning", Position.Right))

    btn5 = KitButton("showError")
    layout.addWidget(btn5)
    btn5.clicked.connect(lambda: KitMessage.error("error"))

    main.show()
    sys.exit(app.exec_())
