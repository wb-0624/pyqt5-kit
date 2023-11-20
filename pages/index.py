from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from widget.component.button import KitButton
from widget.component.popup.kit_modal import KitModal


class Index(QWidget):

    def __init__(self, parent=None):
        super(Index, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        btn = KitButton('test')
        self.layout.addWidget(btn)

        btn.clicked.connect(lambda: KitModal.notice('提示', '这是一个提示信息'))

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)