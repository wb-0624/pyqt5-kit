from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from widget import KitFramelessWindow, KitFileDropArea, KitModal


class DropDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        file_drop = KitFileDropArea([".png", ".jpg", ".jpeg"])
        layout.addWidget(file_drop)
        file_drop.dropped.connect(lambda l1, l2: KitModal.notice(self.window(), 'info', '接受文件' + ','.join(l1)+'\n拒绝文件' + '.'.join(l2)))


if __name__ == "__main__":

    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)



    config.init()

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = DropDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
