from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from .demo_card import DemoCard
from ... import TableDemo
from ...widgets_demo.badge_demo import DotBadgeDemo, NumberBadgeDemo, TextBadgeDemo


class TableWidgetList(QListWidget):

    def __init__(self, parent=None):
        super(TableWidgetList, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSpacing(20)

        table_card = DemoCard('表格', 'table_demo.py', 'TableDemo')
        table_demo = TableDemo()
        table_card.setDemoWidget(table_demo)
        self.addDemoCard(table_card)


    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def addDemoCard(self, card: DemoCard):
        demo_item = QListWidgetItem(self)
        demo_item.setSizeHint(card.sizeHint())
        self.setItemWidget(demo_item, card)
