from PyQt5.QtCore import Qt

from app_config.constant import ClosePolicy
from widget import KitButton, KitOverlay, KitFramelessWindow, KitWindow

if __name__ == "__main__":
    from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
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
    # window = KitWindow()
    main = QWidget()
    window.setCentralWidget(main)
    layout = QVBoxLayout()
    main.setLayout(layout)
    btn = KitButton('open overlay')
    overlay = KitOverlay(main.window())
    overlay.setClosePolicy(ClosePolicy.CloseOnClicked)
    layout.addWidget(btn)
    btn.clicked.connect(lambda: overlay.show())

    window.show()
    sys.exit(app.exec_())
