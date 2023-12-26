import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from config import config
from app_config.constant import Position
from widget import KitFramelessWindow, KitLoading, KitButton, KitMessage, KitModal, KitWindow


class PopupDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        btn = KitButton('open loading')
        main_layout.addWidget(btn)
        btn.clicked.connect(lambda: KitLoading.run(self.window()))

        btn2 = KitButton("info msg")
        main_layout.addWidget(btn2)
        btn2.clicked.connect(lambda: KitMessage.info(self.window(), "info", Position.Top))

        btn3 = KitButton("success msg")
        main_layout.addWidget(btn3)
        btn3.clicked.connect(lambda: KitMessage.success(self.window(), "success", Position.Left))

        btn4 = KitButton("warning msg")
        main_layout.addWidget(btn4)
        btn4.clicked.connect(lambda: KitMessage.warning(self.window(), "warning", Position.Right))

        btn5 = KitButton("error msg")
        main_layout.addWidget(btn5)
        btn5.clicked.connect(lambda: KitMessage.error(self.window(), "error", Position.Bottom))

        modal_btn = KitButton('modal notice')
        modal_btn2 = KitButton('modal dialog')
        main_layout.addWidget(modal_btn)
        main_layout.addWidget(modal_btn2)

        content1 = QWidget()
        content1.setLayout(QVBoxLayout())
        content1.layout().addWidget(QLabel('123'))
        content1.layout().addWidget(QLabel('456'))
        content1.layout().addWidget(KitButton('789'))

        modal_btn.clicked.connect(lambda: KitModal.notice(self.window(), "title", content1))
        modal_btn2.clicked.connect(lambda: KitModal.dialog(self.window(), '123', '456', lambda: print('confirm')))


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = PopupDemo(window)
    window.setCentralWidget(demo)

    window.show()
    sys.exit(app.exec_())
