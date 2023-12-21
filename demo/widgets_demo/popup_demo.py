from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from app_config.constant import Position
from widget import KitFramelessWindow, KitLoading, KitButton, KitMessage, KitModal

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

    window = KitFramelessWindow()
    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    loading = KitLoading()
    btn = KitButton('open loading')
    layout.addWidget(btn)
    btn.clicked.connect(lambda: KitLoading.run())

    btn2 = KitButton("info msg")
    layout.addWidget(btn2)
    btn2.clicked.connect(lambda: KitMessage.info("info", Position.Top))

    btn3 = KitButton("success msg")
    layout.addWidget(btn3)
    btn3.clicked.connect(lambda: KitMessage.success("success", Position.Left))

    btn4 = KitButton("warning msg")
    layout.addWidget(btn4)
    btn4.clicked.connect(lambda: KitMessage.warning("warning", Position.Right))

    btn5 = KitButton("error msg")
    layout.addWidget(btn5)
    btn5.clicked.connect(lambda: KitMessage.error("error"))

    modal_btn = KitButton('modal notice')
    modal_btn2 = KitButton('modal dialog')
    layout.addWidget(modal_btn)
    layout.addWidget(modal_btn2)

    content1 = QWidget()
    content1.setLayout(QVBoxLayout())
    content1.layout().addWidget(QLabel('123'))
    content1.layout().addWidget(QLabel('456'))
    content1.layout().addWidget(KitButton('789'))

    modal_btn.clicked.connect(lambda: KitModal.notice("title", content1))
    modal_btn2.clicked.connect(lambda: KitModal.dialog('123', '456', lambda: print('confirm')))

    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
