from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget

from app_config.constant import Icons
from widget import KitTabBar, KitButton

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

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    tab_bar = KitTabBar()
    tab_bar.addTab('Tab 1', Icons.home)
    tab_bar.addTab('Tab 2', Icons.home)
    tab_bar.addTab('Tab 312341235123', Icons.home)

    stacked = QStackedWidget()
    stacked.addWidget(KitButton('1'))
    stacked.addWidget(KitButton('2'))
    stacked.addWidget(KitButton('3'))

    tab_bar.connectStackedWidget(stacked)

    layout.addWidget(tab_bar)
    layout.addWidget(stacked)

    main.show()
    sys.exit(app.exec_())
