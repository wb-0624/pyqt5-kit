from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

from app_config.constant import Button
from app_config.md_icons import Icons
from widget import KitButton, KitIconButton, KitToolButton, KitFramelessWindow


class ButtonDemo(QWidget):
    def __init__(self, parent=None):
        super(ButtonDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        btn = KitButton("Button")
        layout.addWidget(btn)

        btn_round = KitButton("圆角", Icons.md_home)
        btn_round.setShape(Button.Round)
        layout.addWidget(btn_round)

        btn_square = KitButton("方形")
        btn_square.setShape(Button.Square)
        layout.addWidget(btn_square)


class ThemeButtonDemo(QWidget):
    def __init__(self, parent=None):
        super(ThemeButtonDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        primary_button = KitButton("Primary", Icons.md_settings)
        primary_button.setType(Button.Primary)

        success_button = KitButton("Success")
        success_button.setType(Button.Success)

        warning_button = KitButton("Warning")
        warning_button.setType(Button.Warning)

        danger_button = KitButton("Danger")
        danger_button.setType(Button.Danger)

        layout.addWidget(primary_button)
        layout.addWidget(success_button)
        layout.addWidget(warning_button)
        layout.addWidget(danger_button)


class TextButtonDemo(QWidget):
    def __init__(self, parent=None):
        super(TextButtonDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        btn = KitButton("文字按钮")
        btn.setStyle(Button.Text)
        layout.addWidget(btn)

        primary_text_btn = KitButton("文字按钮带主题色", Icons.md_set_meal)
        primary_text_btn.setStyle(Button.Text)
        primary_text_btn.setType(Button.Primary)
        layout.addWidget(primary_text_btn)


class IconButtonDemo(QWidget):
    def __init__(self, parent=None):
        super(IconButtonDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        btn = KitIconButton(Icons.md_home)
        layout.addWidget(btn)

        btn_square = KitIconButton(Icons.md_square)
        btn_square.setShape(Button.Square)
        layout.addWidget(btn_square)

        btn_round = KitIconButton(Icons.md_rounded_corner)
        btn_round.setShape(Button.Round)
        layout.addWidget(btn_round)

        primary_icon_btn = KitIconButton(Icons.md_settings)
        primary_icon_btn.setType(Button.Primary)
        layout.addWidget(primary_icon_btn)

        success_icon_btn = KitIconButton(Icons.md_check_circle)
        success_icon_btn.setType(Button.Success)
        layout.addWidget(success_icon_btn)

        text_icon_btn = KitIconButton(Icons.md_text_fields)
        text_icon_btn.setStyle(Button.Text)
        layout.addWidget(text_icon_btn)


class ToolButtonDemo(QWidget):
    def __init__(self, parent=None):
        super(ToolButtonDemo, self).__init__(parent=parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        tool_btn = KitToolButton('工具按钮', Icons.md_home)
        layout.addWidget(tool_btn)

        tool_icon_btn = KitToolButton(None, Icons.md_home)
        tool_icon_btn.setType(Button.Success)
        layout.addWidget(tool_icon_btn)



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
