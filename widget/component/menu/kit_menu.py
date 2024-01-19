from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu


class KitMenu(QMenu):

    def __init__(self, parent=None):
        super(KitMenu, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setWindowFlag(Qt.NoDropShadowWindowHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 透明背景 和 阴影效果 同时存在时， 会导致菜单项悬浮样式不生效
        # 所以这里暂时没有设置阴影效果
        self.setAttribute(Qt.WA_TranslucentBackground)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
