from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from .demo_card import DemoCard
from ... import DrawerDemo, DropDemo
from ...widgets_demo.collapse_demo import CollapseDemo


class DataWidgetList(QListWidget):

    def __init__(self, parent=None):
        super(DataWidgetList, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSpacing(20)

        collapse_card = DemoCard('折叠面板', 'collapse_demo.py', 'CollapseDemo')
        collapse_demo = CollapseDemo()
        collapse_card.setDemoWidget(collapse_demo)
        collapse_card_item = self.addDemoCard(collapse_card)
        collapse_card_item.setSizeHint(QSize(collapse_card.sizeHint().width(), 280))

        drawer_card = DemoCard('抽屉', 'drawer_demo.py', 'DrawerDemo')
        drawer_demo = DrawerDemo(self)
        drawer_card.setDemoWidget(drawer_demo)
        self.addDemoCard(drawer_card)

        drop_card = DemoCard('拖拽文件(.png, .jpg, .jpeg)', 'drop_file_demo.py', 'DropDemo')
        drop_demo = DropDemo()
        drop_card.setDemoWidget(drop_demo)
        self.addDemoCard(drop_card)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def addDemoCard(self, card: DemoCard):
        demo_item = QListWidgetItem(self)
        demo_item.setSizeHint(card.sizeHint())
        self.setItemWidget(demo_item, card)
        return demo_item
