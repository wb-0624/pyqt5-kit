import sys
from PyQt5.QtCore import Qt

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
        btn3.clicked.connect(lambda: KitMessage.success(self.window(), "超长success success success\n换行文本\n自适应大小", Position.Left))

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
        layout = QVBoxLayout()
        layout.addWidget(QLabel('123'))
        layout.addWidget(QLabel('456'))
        layout.addWidget(KitButton('789'))
        content1.setLayout(layout)

        modal_btn.clicked.connect(lambda: KitModal.notice(self.window(), "title", content1))
        modal_btn2.clicked.connect(lambda: KitModal.dialog(self.window(), '123', '45612\n74021\n231\n41\n234\n12341', lambda: print('confirm')))


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()



    window = KitFramelessWindow()
    # window = KitWindow()

    demo = PopupDemo(window)
    window.setCentralWidget(demo)

    window.show()
    sys.exit(app.exec_())
