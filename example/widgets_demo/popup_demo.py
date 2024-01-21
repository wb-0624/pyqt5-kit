import sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout

from config import config
from app_config.constant import Position, Button
from widget import KitFramelessWindow, KitLoading, KitButton, KitMessage, KitModal, KitWindow


class MessageDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        btn2 = KitButton("info msg")
        self.layout.addWidget(btn2)
        btn2.clicked.connect(lambda: KitMessage.info(self.window(), "info", Position.Top))

        btn3 = KitButton("success msg")
        btn3.setType(Button.Success)
        self.layout.addWidget(btn3)
        btn3.clicked.connect(
            lambda: KitMessage.success(self.window(), "超长success success success\n换行文本\n自适应大小",
                                       Position.Left))

        btn4 = KitButton("warning msg")
        btn4.setType(Button.Warning)
        self.layout.addWidget(btn4)
        btn4.clicked.connect(lambda: KitMessage.warning(self.window(), "warning", Position.Right))

        btn5 = KitButton("danger msg")
        btn5.setType(Button.Danger)
        self.layout.addWidget(btn5)
        btn5.clicked.connect(lambda: KitMessage.error(self.window(), "danger", Position.Bottom))


class LoadingDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        btn = KitButton("open loading")
        self.layout.addWidget(btn)
        btn.clicked.connect(lambda: KitLoading.run(self.window()))


class NoticeDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        btn = KitButton("notice")
        self.layout.addWidget(btn)
        content1 = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('123'))
        layout.addWidget(QLabel('456'))
        layout.addWidget(KitButton('789'))
        content1.setLayout(layout)
        btn.clicked.connect(lambda: KitModal.notice(self.window(), "title", content1))


class DialogDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        btn = KitButton("dialog")
        self.layout.addWidget(btn)
        btn.clicked.connect(lambda: KitModal.dialog(self.window(), "123", "45612\n74021\n231\n41\n234\n12341",
                                                    lambda: print('confirm')))


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = MessageDemo(window)
    window.setCentralWidget(demo)

    window.show()
    sys.exit(app.exec_())
