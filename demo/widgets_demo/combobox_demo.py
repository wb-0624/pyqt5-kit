from PyQt5.QtCore import Qt

from widget import KitComboBox, KitButton, KitFramelessWindow

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
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

    window = KitFramelessWindow()
    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)
    combo = KitComboBox()
    combo.setContentList([{'id': 1, 'name': 'test1213512351'}, {'id': 2, 'name': 'test2'}, {'id': 3, 'name': 'test3'}, {'id': 4, 'name': 'test4'}, {'id': 5, 'name': 'test5'}])

    btn1 = KitButton("set1")
    btn1.clicked.connect(lambda: combo.setCurrentId(1))
    btn2 = KitButton("set2")
    btn2.clicked.connect(lambda: combo.setCurrentId(2))

    layout.addWidget(combo)
    layout.addWidget(btn1)
    layout.addWidget(btn2)

    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
