from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

from app_config.md_icons import MdIcons
from ..icon import KitIcon


class KitCollapse(QWidget):

    def __init__(self, title: str, content: QWidget, parent=None):
        super(KitCollapse, self).__init__(parent=parent)

        self._item = KitCollapseItem(title, self)
        self._content = KitCollapseContent(content, self)
        self._show_content = False

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self._item)
        self.layout.addWidget(self._content)
        self.setLayout(self.layout)
        self._fresh_content()

    def __init_slot(self):
        self._item.clicked.connect(self._change_state)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def _change_state(self):
        self._show_content = not self._show_content
        self._fresh_content()

    def _fresh_content(self):
        self._item.setState(self._show_content)
        self._content.setVisible(self._show_content)

    def setTitle(self, title: str):
        self._item.setTitle(title)

    def setTitleIndicatorIcon(self, content_hide, content_show):
        self._item.setIndicatorIcon(content_hide, content_show)

    def setTitleAlignment(self, alignment: Qt.Alignment):
        self._item.setAlignment(alignment)

    def setIcon(self, icon):
        self._item.setIcon(icon)

    def setContent(self, widget: QWidget):
        self._content.setContent(widget)


class KitCollapseItem(QWidget):
    clicked = pyqtSignal()

    def __init__(self, title: str, parent=None):
        super(KitCollapseItem, self).__init__(parent=parent)
        self._title = QLabel(title, self)
        self._icon = KitIcon(None)
        self._state = False
        self._indicator_icon_show = MdIcons.md_expand_more
        self._indicator_icon_hide = MdIcons.md_chevron_right
        self._indicator_icon = KitIcon(self._indicator_icon_hide)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.layout.addWidget(self._icon)
        self.layout.addWidget(self._title, stretch=1)
        self.layout.addWidget(self._indicator_icon)

    def __init_slot(self):
        self.clicked.connect(lambda: self._change_show_content())

    def setState(self, state: bool):
        self._state = state
        self._fresh_indicator_icon()

    def _change_show_content(self):
        self._state = not self._state
        self._fresh_indicator_icon()

    def _fresh_indicator_icon(self):
        if self._state:
            self._indicator_icon.setIcon(self._indicator_icon_show)
        else:
            self._indicator_icon.setIcon(self._indicator_icon_hide)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setTitle(self, title: str):
        self._title.setText(title)

    def setIcon(self, icon):
        self._icon.setIcon(icon)

    def setAlignment(self, alignment: Qt.Alignment):
        self._title.setAlignment(alignment)

    def setIndicatorIcon(self, content_hide, content_show):
        self._indicator_icon_hide = content_hide
        self._indicator_icon_show = content_show
        self._fresh_indicator_icon()

    def mousePressEvent(self, ev) -> None:
        self.clicked.emit()


class KitCollapseContent(QWidget):

    def __init__(self, content: QWidget, parent=None):
        super(KitCollapseContent, self).__init__(parent=parent)
        self._content = content

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self._content)
        self.setLayout(self.layout)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setContent(self, widget: QWidget):
        self.layout.removeWidget(self._content)
        self._content.deleteLater()
        self._content = widget
        self.layout.addWidget(self._content)
