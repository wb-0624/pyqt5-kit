from PyQt5.QtCore import QSize, QEvent
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from .demo_card import DemoCard
from ... import DrawerDemo, DropDemo, InputDemo, ValidatorDemo
from ...widgets_demo.checkbox_demo import *
from ...widgets_demo.collapse_demo import CollapseDemo


class InputWidgetList(QListWidget):

    def __init__(self, parent=None):
        super(InputWidgetList, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSpacing(20)

        input_card = DemoCard('简单输入框', 'input_demo.py', 'InputDemo')
        input_demo = InputDemo()
        input_card.setDemoWidget(input_demo)
        self.addDemoCard(input_card)

        validator_card = DemoCard('输入框验证(1-10)', 'input_demo.py', 'ValidatorDemo')
        validator_demo = ValidatorDemo()
        validator_card.setDemoWidget(validator_demo)
        self.addDemoCard(validator_card)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def addDemoCard(self, card: DemoCard):
        demo_item = QListWidgetItem(self)
        demo_item.setSizeHint(card.sizeHint())
        self.setItemWidget(demo_item, card)
        return demo_item
