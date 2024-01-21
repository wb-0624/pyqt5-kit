from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from .demo_card import DemoCard
from ... import MessageDemo, LoadingDemo, DialogDemo, NoticeDemo


class DialogWidgetList(QListWidget):

    def __init__(self, parent=None):
        super(DialogWidgetList, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSpacing(20)

        message_card = DemoCard('消息提示', 'popup_demo.py', 'MessageDemo')
        message_demo = MessageDemo(self)
        message_card.setDemoWidget(message_demo)
        self.addDemoCard(message_card)

        loading_card = DemoCard('加载提示', 'popup_demo.py', 'LoadingDemo')
        loading_demo = LoadingDemo(self)
        loading_card.setDemoWidget(loading_demo)
        self.addDemoCard(loading_card)

        notice_card = DemoCard('模态通知', 'popup_demo.py', 'NoticeDemo')
        notice_demo = NoticeDemo(self)
        notice_card.setDemoWidget(notice_demo)
        self.addDemoCard(notice_card)

        dialog_card = DemoCard('模态对话框', 'popup_demo.py', 'DialogDemo')
        dialog_demo = DialogDemo(self)
        dialog_card.setDemoWidget(dialog_demo)
        self.addDemoCard(dialog_card)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def addDemoCard(self, card: DemoCard):
        demo_item = QListWidgetItem(self)
        demo_item.setSizeHint(card.sizeHint())
        self.setItemWidget(demo_item, card)
