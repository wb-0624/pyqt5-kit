from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPaintEngine
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout

from app_config.constant import Button
from widget import KitButton, KitModal
from .stack_card import StackCard


class BasicStack(QScrollArea):

    def __init__(self, parent=None):
        super(BasicStack, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.content = QWidget()
        self.content.resize(self.width(), 1000)
        self.setWidget(self.content)
        self.layout = QVBoxLayout()
        self.content.setLayout(self.layout)

        card1 = StackCard()
        self.layout.addWidget(card1)

        btn = KitButton('default')
        btn.setToolTip('default')
        btn.clicked.connect(lambda: KitModal.notice('default', 'default'))
        self.layout.addWidget(btn)

        btn2 = KitButton('primary')
        btn2.setToolTip('primary')
        btn2.setType(Button.Primary)
        self.layout.addWidget(btn2)

        self.layout.addStretch(1)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def eventFilter(self, a0, a1) -> bool:
        if a1.type() == QEvent.DynamicPropertyChange:
            self.update()
        elif a1.type() == QEvent.Wheel:
            self.update()
        return super().eventFilter(a0, a1)


