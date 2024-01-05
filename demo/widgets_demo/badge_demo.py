from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from app_config.constant import Icons, Button, Badge
from widget import KitButton, KitIconButton, KitToolButton, KitFramelessWindow, KitBadge, KitDotBadge


class BadgeDemo(QWidget):
    def __init__(self, parent=None):
        super(BadgeDemo, self).__init__(parent=parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        btn1 = KitButton("Button", Icons.md_home)
        btn1.setType(Button.Primary)
        badge1 = KitBadge(btn1)
        badge1.setType(Badge.Danger)
        badge1.setNum(10)

        btn2 = KitButton("Button", Icons.md_home)
        btn2.setType(Button.Success)
        badge2 = KitBadge(btn2)
        badge2.setType(Badge.Primary)
        badge2.setNum(100)

        btn4 = KitButton("Button", Icons.md_home)
        btn4.setType(Button.Warning)
        badge4 = KitBadge(btn4)
        badge4.setType(Badge.Success)
        badge4.setNum(1000)

        btn5 = KitButton("Button", Icons.md_home)
        btn5.setType(Button.Danger)
        badge5 = KitDotBadge(btn5)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn4)
        layout.addWidget(btn5)

if __name__ == "__main__":

    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()

    window = KitFramelessWindow()
    # window = KitWindow()

    demo = BadgeDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())