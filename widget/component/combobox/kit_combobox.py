from PyQt5.QtCore import Qt, QSize, QVariant, QRect
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QComboBox, QListView, QStyle, QStyleOptionComboBox

from app_config.md_icons import MdIcons
from utils.kit_property import KitNotifyProperty
from ..icon import KitIcon


class KitComboBox(QComboBox):

    currentId = KitNotifyProperty(QVariant)
    """
    [{'id': 1, 'name': 'test1'}, {'id': 2, 'name': 'test2'}}]
    """

    def __init__(self, parent=None):
        super(KitComboBox, self).__init__(parent=parent)
        self.content_list = []
        self.indicator_size = 16

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setView(QListView(self))
        self.view().setTextElideMode(Qt.ElideRight)
        self.view().parent().setWindowFlag(Qt.NoDropShadowWindowHint)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setContentList(self, content_list):
        self.content_list = content_list
        self.clear()
        for content in content_list:
            self.addItem(content['name'], content)

    def setCurrentId(self, id):
        self.currentId = id
        if self.content_list is None or len(self.content_list) == 0:
            self.setCurrentIndex(-1)
            return
        for i in self.content_list:
            try:
                if i.get('id') == self.currentId():
                    self.setCurrentText(i.get('name'))
                    return
            except Exception as e:
                print(e)

        self.setCurrentIndex(-1)

    def setIndicatorSize(self, size):
        self.indicator_size = size
        self.update()

    def sizeHint(self):
        return QSize(80, 32)

    def paintEvent(self, e) -> None:
        super().paintEvent(e)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        opt = QStyleOptionComboBox()
        opt.initFrom(self)
        arrow_rect = self.style().subControlRect(QStyle.CC_ComboBox, opt, QStyle.SC_ComboBoxArrow, self)

        rect = QRect(arrow_rect.center().x() - self.indicator_size // 2, arrow_rect.center().y() - self.indicator_size // 2, self.indicator_size, self.indicator_size)
        opt.rect = rect

        if self.view().isVisible():
            icon = KitIcon(MdIcons.md_expand_more)
            icon.setObjectName('combobox_icon')
            painter.drawPixmap(rect, icon.toPixmap())
        else:
            icon = KitIcon(MdIcons.md_chevron_right)
            icon.setObjectName('combobox_icon')
            painter.drawPixmap(rect, icon.toPixmap())


