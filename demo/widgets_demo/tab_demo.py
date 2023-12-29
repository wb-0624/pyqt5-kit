from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget

from app_config.constant import Icons
from widget import KitTabBar, KitButton, KitFramelessWindow, KitWindow


class TabDemo(QWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent=parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        tab_bar = KitTabBar()
        tab_bar.addTab('Tab 1', Icons.md_home)
        tab_bar.addTab('Tab 2', Icons.md_home)
        tab_bar.addTab('Tab 312341235123', Icons.md_home)

        stacked = QStackedWidget()
        stacked.addWidget(KitButton('1'))
        stacked.addWidget(KitButton('2'))
        stacked.addWidget(KitButton('3'))

        tab_bar.connectStackedWidget(stacked)

        layout.addWidget(tab_bar)
        layout.addWidget(stacked)


if __name__ == "__main__":

    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()



    window = KitFramelessWindow()
    # window = KitWindow()

    demo = TabDemo()
    window.setCentralWidget(demo)
    window.show()

    sys.exit(app.exec_())
