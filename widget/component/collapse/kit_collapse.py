from PyQt5.QtCore import Qt, pyqtSignal, QRect, QPropertyAnimation
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from animation.kit_animation import KitAnimationFactory
from app_config import Icons, Animation
from widget import KitIcon


class KitCollapse(QWidget):

    def __init__(self, title: str, icon: str = None, parent=None):
        super(KitCollapse, self).__init__(parent=parent)

        self.title = title
        self.icon = icon
        self._show_content = False

        self._ani_show = None
        self._ani_hide = None
        self._ani_start_value = None
        self._ani_end_value = None

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.collapse_item = KitCollapseItem(self.title, self.icon, self)
        self.collapse_content = KitCollapseContent()
        self.collapse_content.hide()

        self.layout.addWidget(self.collapse_item)
        self.layout.addWidget(self.collapse_content)

    def __init_slot(self):
        self.collapse_item.clicked.connect(self._change_show_content)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def _change_show_content(self):
        self._show_content = False if self._show_content else True
        self.collapse_item.setState(self._show_content)
        self.collapse_content.setVisible(self._show_content)

    def setTitle(self, title):
        self.collapse_item.setTitle(title)

    def setIcon(self, icon):
        self.collapse_item.setIcon(icon)

    def setContent(self, content: QWidget):
        self.collapse_content.setContent(content)
        self.collapse_content.adjustSize()


class KitCollapseItem(QWidget):
    clicked = pyqtSignal()

    def __init__(self, title: str, icon: str = None, parent=None):
        super(KitCollapseItem, self).__init__(parent=parent)
        self.icon = KitIcon(icon)
        self.title = QLabel(title)

        self.right_arrow = Icons.md_chevron_right
        self.down_arrow = Icons.md_expand_more

        self.indicator = KitIcon(self.right_arrow)
        self._state = False

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.setContentsMargins(4, 4, 4, 4)
        self.setFixedHeight(40)

        self.layout.addWidget(self.icon)
        self.layout.addWidget(self.title)
        self.layout.addStretch(1)
        self.layout.addWidget(self.indicator)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setTitle(self, title):
        self.title.setText(title)

    def setIcon(self, icon):
        self.icon.setIcon(icon)

    def mousePressEvent(self, a0) -> None:
        self.clicked.emit()
        return super().mousePressEvent(a0)

    def _change_state(self):
        self._state = False if self._state else True
        self.indicator.setIcon(self.down_arrow if self._state else self.right_arrow)

    def setState(self, state):
        self._state = state
        self.indicator.setIcon(self.down_arrow if self._state else self.right_arrow)

    def enterEvent(self, a0) -> None:
        self.setCursor(Qt.PointingHandCursor)
        return super().enterEvent(a0)

    def leaveEvent(self, a0) -> None:
        self.setCursor(Qt.ArrowCursor)
        return super().leaveEvent(a0)


class KitCollapseContent(QWidget):

    def __init__(self, parent=None):
        super(KitCollapseContent, self).__init__(parent=parent)

        self.content = None

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setContent(self, content: QWidget):
        self.content = content
        self.layout.addWidget(content)
