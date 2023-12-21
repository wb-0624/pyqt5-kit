from PyQt5.QtCore import Qt, QSize

from ..window import KitFramelessWindow


class KitSplashScreen(KitFramelessWindow):

    def __init__(self):
        super(KitSplashScreen, self).__init__()

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setTitleBar(None)
        self.setStatusBar(None)
        self.setResizeable(False)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def sizeHint(self):
        return QSize(500, 300)
