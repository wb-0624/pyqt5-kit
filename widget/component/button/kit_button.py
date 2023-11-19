from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QVBoxLayout, QGraphicsDropShadowEffect

from widget.component.icon.kit_icon import KitIcon
from utils.constant import Button, Icons


class KitButton(QPushButton):

    def __init__(self, text: str = "", icon: str = None, parent=None):
        super(KitButton, self).__init__(parent=parent)

        self._type = None
        self._shape = None
        self._style = None

        self.icon = None
        self.setText(text)
        if icon is not None:
            self.icon = KitIcon(icon)
            self.setIcon(self.icon.toIcon())

        self.setShadow(True)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setMouseTracking(True)
        self.setContentsMargins(4, 0, 4, 0)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setShadow(self, if_shadow: bool = True):
        # creating a QGraphicsDropShadowEffect object
        if if_shadow:
            shadow = QGraphicsDropShadowEffect()
            shadow.setXOffset(0)
            shadow.setYOffset(1)
            # setting blur radius
            shadow.setBlurRadius(1)
            shadow.setColor(QColor(0, 0, 0, 100))
            # adding shadow to the button
            self.setGraphicsEffect(shadow)
        else:
            self.setGraphicsEffect(None)

    def setType(self, button_type: str):
        self._type = button_type
        self._freshButton()
        self.setProperty('type', button_type)
        self.style().polish(self)

    def setShape(self, button_shape: str):
        self._shape = button_shape
        self.setProperty('shape', button_shape)
        self.style().polish(self)

    def setStyle(self, button_style: str):
        self._style = button_style
        self._freshButton()
        self.setProperty('style', button_style)
        self.style().polish(self)

    def _freshButton(self):
        if self._style != Button.Text:
            self.setShadow(True)
            return
        else:
            self.setShadow(False)

        if self.icon is None:
            return

        if self._type == Button.Primary:
            self.icon.setProperty('type', 'primary')
        elif self._type == Button.Success:
            self.icon.setProperty('type', 'success')
        elif self._type == Button.Warning:
            self.icon.setProperty('type', 'warning')
        elif self._type == Button.Danger:
            self.icon.setProperty('type', 'danger')
        self.icon.style().polish(self.icon)
        self.setIcon(self.icon.toIcon())

    def mouseMoveEvent(self, e) -> None:
        if self.underMouse():
            self.setCursor(Qt.PointingHandCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

    def setIcon(self, icon: [QIcon, str]):
        if icon is None:
            return
        if type(icon) is QIcon:
            new_icon = icon
        elif type(icon) is str:
            new_icon = KitIcon(icon).toIcon()
        else:
            raise TypeError("Icon must be a QIcon or a str")
        super().setIcon(new_icon)

    def sizeHint(self):
        return QSize(52, 32)


class KitIconButton(KitButton):

    def __init__(self, icon: str = None, parent=None):
        super(KitIconButton, self).__init__(icon=icon, parent=parent)

        self.setText("")

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setFixedSize(32, 32)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)


class KitToolButton(KitButton):

    def __init__(self, text: str = "", icon: str = None, parent=None):
        super(KitToolButton, self).__init__(text, icon, parent)

        self.state = Button.UnChecked

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        pass

    def __init_slot(self):
        self.clicked.connect(self.toggledCheck)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setCheckState(self, state: [Button.UnChecked, Button.Checked]):
        self.state = state
        self.setProperty('state', state)
        self.style().polish(self)

    def toggledCheck(self):
        if self.state == Button.UnChecked:
            self.setCheckState(Button.Checked)
        elif self.state == Button.Checked:
            self.setCheckState(Button.UnChecked)


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


    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    btn1 = KitButton("Button", Icons.home)
    btn1.setType(Button.Primary)
    btn1.clicked.connect(lambda: print(QApplication.activeWindow().width(), QApplication.activeWindow().height()))
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

    main.show()
    sys.exit(app.exec_())
