from PyQt5.QtCore import Qt, QSize, QTimer, QPropertyAnimation
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QLabel, QVBoxLayout, QHBoxLayout

from ..icon.kit_icon import KitIcon
from ..popup.kit_popup import KitPopup
from app_config.constant import Position
from app_config.md_icons import MdIcons


class KitMessage(KitPopup):
    """
    消息提示框
    @param position: 位置
    @param close_time: 自动关闭时间毫秒, -1 为不关闭
    """

    def __init__(self, window, position: Position = Position.BottomRight, close_time=3000):
        super(KitMessage, self).__init__(window=window)

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
        # todo 透明度动画 和 KitOverlay 一样，会导致位置发生偏移
        # self.setGraphicsEffect(self.opacity_effect)
        self.__init_animation()

    def __init_slot(self):
        self.close_timer.timeout.connect(lambda: self.close())

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def __init_close_timer(self):
        if self.close_time > 0:
            self.close_timer.start(self.close_time)

    def __init_animation(self):
        self._animation = QPropertyAnimation(self.opacity_effect, b'opacity')
        self._animation.setDuration(300)
        self._animation.setStartValue(0)
        self._animation.setEndValue(1)

    def setOffset(self, offset: int):
        self.offset = offset

    def showEvent(self, a0) -> None:
        self.__init_close_timer()
        self._animation.setDirection(QPropertyAnimation.Forward)
        self._animation.start()
        super().showEvent(a0)

    def close(self):
        self.close_timer.stop()
        self._animation.setDirection(QPropertyAnimation.Backward)
        self._animation.finished.connect(super().close)
        self._animation.start()

    def sizeHint(self):
        return QSize(-1, -1)

    @classmethod
    def make(cls, window, icon, title, position=Position.BottomRight, close_time=3000, style_type="info"):
        msg = cls(window, position, close_time)
        msg.icon = icon
        msg.title = title

        msg_icon = KitIcon(icon)
        msg_icon.setObjectName("message_icon")
        msg_icon.setFixedSize(QSize(24, 24))
        msg_title = QLabel(title)
        msg_title.setAlignment(Qt.AlignVCenter)
        msg_title.setObjectName("message_title")
        msg_title.adjustSize()

        msg_layout = QVBoxLayout()
        msg_layout.setContentsMargins(8, 8, 8, 8)
        msg.setLayout(msg_layout)

        msg_header_layout = QHBoxLayout()
        msg_header_layout.setSpacing(4)
        msg_header_layout.addWidget(msg_icon, alignment=Qt.AlignTop)
        msg_header_layout.addWidget(msg_title)

        msg_layout.addLayout(msg_header_layout)

        msg.setProperty("type", style_type)
        msg.style().polish(msg)
        msg.resize(msg_layout.sizeHint())
        msg.show()
        return msg

    @classmethod
    def info(cls, window, title, position=Position.BottomRight, close_time=3000):
        msg_info = cls.make(window, MdIcons.md_info, title, position, close_time, "info")
        return msg_info

    @classmethod
    def success(cls, window, title, position=Position.BottomRight, close_time=3000):
        msg_success = cls.make(window, MdIcons.md_check_circle, title, position, close_time, "success")
        return msg_success

    @classmethod
    def warning(cls, window, title, position=Position.BottomRight, close_time=3000):
        msg_warning = cls.make(window, MdIcons.md_error, title, position, close_time, "warning")
        return msg_warning

    @classmethod
    def error(cls, window, title, position=Position.BottomRight, close_time=3000):
        msg_error = cls.make(window, MdIcons.md_cancel, title, position, close_time, "danger")
        return msg_error
