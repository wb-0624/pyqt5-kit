from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication


class KitWindow(QMainWindow):
    windowSizeChanged = pyqtSignal(QSize)

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

    def resizeEvent(self, a0) -> None:
        self.windowSizeChanged.emit(self.size())
        super().resizeEvent(a0)

if __name__ == "__main__":

    from config import config
    import sys
    
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()



    window = KitWindow()

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    layout.addWidget(QLabel('hello'))

    window.setCentralWidget(main)
    window.show()

    sys.exit(app.exec_())