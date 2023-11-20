from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtSignal
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel

from widget.component.icon.kit_icon import KitIcon
from widget.component.window.kit_frameless_window import KitFramelessWindow
from app_config.constant import Icons


class KitSwitchIndicator(QWidget):
    """
    这里虽然显示的只是一个圆形，但是嵌套了两层。
    原因在于，只用一个的时候，在移动动画时，边缘的弧形会变成直角，不美观。
    故外面多套了一层透明的，防止变形。
    """

    def __init__(self, parent=None):
        super(KitSwitchIndicator, self).__init__(parent=parent)

        self.inner = QWidget(self)
        self.inner.setObjectName('indicator-inner')

        self.inner_icon = KitIcon()
        self.inner_icon.setObjectName('indicator-inner-icon')
        # self.inner_icon.setFixedSize(16, 16)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setMouseTracking(True)

        self.setFixedSize(32, 32)
        self.inner.setFixedSize(24, 24)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.inner, alignment=Qt.AlignHCenter)
        self.setLayout(self.layout)

        self.inner_layout = QVBoxLayout(self.inner)
        self.inner_layout.setContentsMargins(0, 0, 0, 0)
        self.inner_layout.addWidget(self.inner_icon, alignment=Qt.AlignHCenter)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setIcon(self, icon_str):
        self.inner_icon.setIcon(icon_str)


class KitSwitch(QWidget):

    checkedChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(KitSwitch, self).__init__(parent=parent)
        self.indicator = KitSwitchIndicator(self)
        self.checked = False
        self.checked_icon = Icons.check
        self.unchecked_icon = Icons.close

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setMouseTracking(True)
        self.setFixedSize(56, 32)

        self._animate = QPropertyAnimation(self.indicator, b"x", self)
        self._animate.setDuration(100)
        self._animate.setStartValue(0)
        self._animate.setEndValue(24)
        self._animate.valueChanged.connect(lambda value: self.indicator.move(value, self.indicator.y()))
        self.setChecked(self.checked)

    def __init_slot(self):
        self._animate.finished.connect(self.__animate_finished)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def __init_indicator_pos(self):
        self.indicator.move(24 if self.checked else 0, self.indicator.y())

    def setChecked(self, checked):
        self._animate.setDirection(QPropertyAnimation.Backward if self.checked else QPropertyAnimation.Forward)
        self.__init_indicator_pos()
        self.__fresh_qss()
        if self.checked != checked:
            self._animate.start()

    def __fresh_qss(self):
        if self.checked:
            self.setProperty('checked', 'true')
            self.indicator.setIcon(self.checked_icon)
        else:
            self.setProperty('checked', 'false')
            self.indicator.setIcon(self.unchecked_icon)
        self.style().polish(self)
        self.indicator.inner.style().polish(self.indicator.inner)
        self.indicator.inner_icon.style().polish(self.indicator.inner_icon)

    def __animate_finished(self):
        self.checked = not self.checked
        self.__fresh_qss()
        self.checkedChanged.emit(self.checked)

    def mouseReleaseEvent(self, a0) -> None:
        self.setChecked(not self.checked)

    def mouseMoveEvent(self, a0) -> None:
        if self.underMouse() and self.isEnabled():
            self.setCursor(Qt.PointingHandCursor)


if __name__ == "__main__":
    from config import config
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)

    QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")

    window = KitFramelessWindow()
    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)
    switch = KitSwitch()
    switch.setChecked(True)
    switch2 = KitSwitch()
    switch2.setChecked(True)
    switch2.setDisabled(True)
    layout.addWidget(switch)
    layout.addWidget(switch2)

    switch.checkedChanged.connect(lambda checked: switch2.setDisabled(checked))

    label = QLabel()
    switch.checkedChanged.connect(lambda checked: label.setText(str(checked)))
    layout.addWidget(label)

    layout.addStretch(1)
    # main.show()
    window.setContentWidget(main)
    window.show()
    sys.exit(app.exec_())
