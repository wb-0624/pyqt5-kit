from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from app_config.constant import Icons, Button
from widget import KitButton, KitIconButton, KitToolButton, KitFramelessWindow


class ButtonDemo(QWidget):
    def __init__(self, parent=None):
        super(ButtonDemo, self).__init__(parent=parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        btn1 = KitButton("Button", Icons.md_home)
        btn1.setType(Button.Primary)
        btn2 = KitButton("Button", Icons.md_home)
        btn2.setType(Button.Success)
        btn4 = KitButton("Button", Icons.md_home)
        btn4.setType(Button.Warning)
        btn5 = KitButton("Button", Icons.md_home)
        btn5.setType(Button.Danger)
        btn8 = KitButton("Button", Icons.md_home)
        btn8.setType(Button.Danger)
        btn8.setDisabled(True)

        btn6 = KitButton("Button", Icons.md_home)
        btn6.setStyle(Button.Text)
        btn6.setType(Button.Primary)
        btn7 = KitButton("Button", Icons.md_home)
        btn7.setStyle(Button.Text)
        btn7.setType(Button.Success)

        icon_btn = KitIconButton(Icons.md_home)
        icon_btn.setShape(Button.Round)

        icon_btn2 = KitIconButton(Icons.md_home)
        icon_btn2.setShape(Button.Round)
        icon_btn2.setStyle(Button.Text)

        tool_btn = KitToolButton("", Icons.md_home)
        tool_btn.setShape(Button.Round)
        tool_btn.setStyle(Button.Text)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        layout.addWidget(btn8)
        layout.addWidget(btn6)
        layout.addWidget(btn7)

        layout.addWidget(icon_btn)
        layout.addWidget(icon_btn2)

        layout.addWidget(tool_btn)


if __name__ == "__main__":

    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()



    window = KitFramelessWindow()
    # window = KitWindow()

    demo = ButtonDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
