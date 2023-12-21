from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from app_config.constant import Icons, Button
from widget import KitButton, KitIconButton, KitToolButton, KitFramelessWindow

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

    btn1 = KitButton("Button", Icons.home)
    btn1.setType(Button.Primary)
    btn2 = KitButton("Button", Icons.home)
    btn2.setType(Button.Success)
    btn4 = KitButton("Button", Icons.home)
    btn4.setType(Button.Warning)
    btn5 = KitButton("Button", Icons.home)
    btn5.setType(Button.Danger)
    btn8 = KitButton("Button", Icons.home)
    btn8.setType(Button.Danger)
    btn8.setDisabled(True)

    btn6 = KitButton("Button", Icons.home)
    btn6.setStyle(Button.Text)
    btn6.setType(Button.Primary)
    btn7 = KitButton("Button", Icons.home)
    btn7.setStyle(Button.Text)
    btn7.setType(Button.Success)

    icon_btn = KitIconButton(Icons.home)
    icon_btn.setShape(Button.Round)

    icon_btn2 = KitIconButton(Icons.home)
    icon_btn2.setShape(Button.Round)
    icon_btn2.setStyle(Button.Text)

    tool_btn = KitToolButton("", Icons.home)
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

    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
