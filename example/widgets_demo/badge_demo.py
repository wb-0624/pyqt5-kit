from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout

from app_config.constant import Button, Badge
from app_config.md_icons import Icons
from widget import KitButton, KitFramelessWindow, KitBadge, KitDotBadge, KitIconButton


class BadgeDemo(QWidget):
    def __init__(self, parent=None):
        super(BadgeDemo, self).__init__(parent=parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        btn1 = KitButton("Button", Icons.md_home)
        btn1.setStyle(Button.Text)
        badge1 = KitBadge(btn1)
        badge1.setType(Badge.Danger)
        badge1.setNum(10)

        btn2 = KitButton("Button", Icons.md_home)
        btn2.setShape(Button.Round)
        badge2 = KitBadge(btn2)
        badge2.setType(Badge.Primary)
        badge2.setNum(100)

        btn4 = KitButton("Button", Icons.md_home)
        badge4 = KitBadge(btn4)
        badge4.setType(Badge.Success)
        badge4.setNum(1000)

        btn5 = KitIconButton(Icons.md_home)
        btn5.setStyle(Button.Text)
        badge5 = KitDotBadge(btn5)
        badge5.setType(Badge.Danger)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn4)
        layout.addWidget(btn5)


class DotBadgeDemo(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        button = KitButton('多种主题色')
        label_dot_badge = KitDotBadge(button)
        label_dot_badge.setType(Badge.Primary)
        self.layout.addWidget(button)

        button2 = KitIconButton(Icons.md_person)
        label2_dot_badge = KitDotBadge(button2)
        label2_dot_badge.setType(Badge.Success)
        self.layout.addWidget(button2)

        self.layout.addStretch(1)


class NumberBadgeDemo(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        button = KitButton('小于99')
        button_badge = KitBadge(button)
        button_badge.setType(Badge.Primary)
        button_badge.setNum(23)
        self.layout.addWidget(button)

        button2 = KitButton('大于99')
        button2_badge = KitBadge(button2)
        button2_badge.setNum(123)
        button2_badge.setType(Badge.Success)
        self.layout.addWidget(button2)

        button3 = KitButton('大于999')
        button3_badge = KitBadge(button3)
        button3_badge.setNum(1234)
        button3_badge.setType(Badge.Danger)
        self.layout.addWidget(button3)

class TextBadgeDemo(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        button = KitButton('文本')
        button_badge = KitBadge(button)
        button_badge.setType(Badge.Primary)
        button_badge.setText('NEW')
        self.layout.addWidget(button)

        button2 = KitButton('文本')
        button2_badge = KitBadge(button2)
        button2_badge.setText('!!')
        button2_badge.setType(Badge.Warning)
        self.layout.addWidget(button2)

        button3 = KitButton('文本')
        button3_badge = KitBadge(button3)
        button3_badge.setText('HOT')
        button3_badge.setType(Badge.Danger)
        self.layout.addWidget(button3)


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
