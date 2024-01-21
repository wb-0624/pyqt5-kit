from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from .demo_card import DemoCard
from ...widgets_demo.badge_demo import DotBadgeDemo, NumberBadgeDemo, TextBadgeDemo


class StateWidgetList(QListWidget):

    def __init__(self, parent=None):
        super(StateWidgetList, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSpacing(20)

        dot_badge_card = DemoCard('点徽章', 'badge_demo.py', 'DotBadgeDemo')
        dot_badge_demo = DotBadgeDemo()
        dot_badge_card.setDemoWidget(dot_badge_demo)
        self.addDemoCard(dot_badge_card)

        number_badge_card = DemoCard('数字徽章', 'badge_demo.py', 'NumberBadgeDemo')
        number_badge_demo = NumberBadgeDemo()
        number_badge_card.setDemoWidget(number_badge_demo)
        self.addDemoCard(number_badge_card)

        text_badge_card = DemoCard('文本徽章', 'badge_demo.py', 'TextBadgeDemo')
        text_badge_demo = TextBadgeDemo()
        text_badge_card.setDemoWidget(text_badge_demo)
        self.addDemoCard(text_badge_card)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def addDemoCard(self, card: DemoCard):
        demo_item = QListWidgetItem(self)
        demo_item.setSizeHint(card.sizeHint())
        self.setItemWidget(demo_item, card)
