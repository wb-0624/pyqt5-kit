from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication



class KitWindow(QMainWindow):

    def __init__(self, parent=None):
        super(KitWindow, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        pass

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

if __name__ == "__main__":
    from PyQt5.QtGui import QFontDatabase
    from config import config
    import sys
    
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    window = KitWindow()

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    layout.addWidget(QLabel('hello'))

    window.setCentralWidget(main)
    window.show()

    sys.exit(app.exec_())