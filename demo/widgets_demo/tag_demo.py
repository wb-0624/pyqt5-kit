from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from widget import KitTag, KitFramelessWindow, KitWindow


class TagDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        tag1 = KitTag("Tag1")
        tag2 = KitTag("Tag223151", "#6e6e6e")
        tag3 = KitTag("Tag3", "#ff11ff")

        layout.addWidget(tag1)
        layout.addWidget(tag2)
        layout.addWidget(tag3)

if __name__ == "__main__":

    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()



    window = KitFramelessWindow()
    # window = KitWindow()

    demo = TagDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
