from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractButton, QApplication, QWidget, QVBoxLayout


class KitTab(QAbstractButton):

    def __init__(self, parent=None):
        super(KitTab, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setCheckable(True)
        self.setAutoExclusive(True)
        palette = self.palette()
        print(palette.color(self.backgroundRole()))

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)



if __name__ == "__main__":
    from PyQt5.QtGui import QFontDatabase
    from kit_config import config
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    tab = KitTab()
    layout.addWidget(tab)

    main.show()
    sys.exit(app.exec_())