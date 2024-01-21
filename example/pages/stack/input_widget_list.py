from PyQt5.QtCore import QSize, QEvent
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from .demo_card import DemoCard
from ... import DrawerDemo, DropDemo, InputDemo, ValidatorDemo, SpinBoxDemo, DoubleSpinBoxDemo, DateSpinBoxDemo, \
    DateTimeSpinBoxDemo, TimeSpinBoxDemo
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

        spin_card = DemoCard('不同步长的步进器', 'spinbox_demo.py', 'SpinBoxDemo')
        spin_demo = SpinBoxDemo()
        spin_card.setDemoWidget(spin_demo)
        self.addDemoCard(spin_card)

        double_spin_card = DemoCard('两位小数的步进器', 'spinbox_demo.py', 'DoubleSpinBoxDemo')
        double_spin_demo = DoubleSpinBoxDemo()
        double_spin_card.setDemoWidget(double_spin_demo)
        self.addDemoCard(double_spin_card)

        date_spin_card = DemoCard('日期步进器', 'spinbox_demo.py', 'DateSpinBoxDemo')
        date_spin_demo = DateSpinBoxDemo()
        date_spin_card.setDemoWidget(date_spin_demo)
        self.addDemoCard(date_spin_card)

        time_spin_card = DemoCard('时间步进器', 'spinbox_demo.py', 'TimeSpinBoxDemo')
        time_spin_demo = TimeSpinBoxDemo()
        time_spin_card.setDemoWidget(time_spin_demo)
        self.addDemoCard(time_spin_card)

        date_time_spin_card = DemoCard('日期时间步进器', 'spinbox_demo.py', 'DateTimeSpinBoxDemo')
        date_time_spin_demo = DateTimeSpinBoxDemo()
        date_time_spin_card.setDemoWidget(date_time_spin_demo)
        self.addDemoCard(date_time_spin_card)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def addDemoCard(self, card: DemoCard):
        demo_item = QListWidgetItem(self)
        demo_item.setSizeHint(card.sizeHint())
        self.setItemWidget(demo_item, card)
        return demo_item
